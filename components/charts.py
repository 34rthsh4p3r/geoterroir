from html import escape

import plotly.graph_objects as go
import streamlit as st

from utils.aggregates import answer_counts, aroma_counts, decimal_label
from utils.constants import BALANCES, LOTS, RED_VARIETIES, SCORES, TECHNIQUES, WHITE_VARIETIES, sensory_questions


BURGUNDY = "#9F1916"
GRAY = "#A6A0A4"


def leading_colors(values) -> list[str]:
    highest = max((value for value in values if value is not None), default=0)
    return [BURGUNDY if highest > 0 and value == highest else GRAY for value in values]


def chart_title(title: str) -> str:
    return f'<h3 class="geoterroir-chart-title">{escape(title)}</h3>'


def percent_label(share: float) -> str:
    return f"{share:.1f}".removesuffix(".0").replace(".", ",") + "%"


def plot(figure: go.Figure, key: str) -> None:
    figure.update_layout(
        height=155,
        margin=dict(t=12, b=27, l=32, r=8),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Source Sans 3, Segoe UI, sans-serif", color="#30232B", size=12),
        hoverlabel=dict(bgcolor="#FFFFFF", font_color="#30232B"),
    )
    figure.update_xaxes(automargin=True, showgrid=False, zeroline=False)
    figure.update_yaxes(
        automargin=True,
        gridcolor="#E8DBD9",
        zeroline=False,
        showticklabels=True,
        tickformat="d",
    )
    st.plotly_chart(
        figure, key=key, theme=None, width="stretch",
        config={"displayModeBar": False, "responsive": True},
    )


def ranking_chart(title: str, counts: dict, *, respondent_count: int = 0, sort_by_count: bool = True) -> str:
    items = list(counts.items())
    if sort_by_count:
        items.sort(key=lambda item: -item[1])
    maximum = max(counts.values(), default=0)
    heading = chart_title(title)
    if not maximum:
        return f'{heading}<p class="dg-chart-empty">Még nincs válasz.</p>'

    entries = []
    for (name, count), color in zip(items, leading_colors([count for _, count in items])):
        label = escape(name)
        detail = f"{label} · {count} válasz"
        if respondent_count:
            detail += f" · a kitöltők {percent_label(100 * count / respondent_count)}-a"
        entries.append(
            f'<li title="{detail}"><span class="dg-rank-label">{label}</span>'
            f'<span class="dg-rank-track" aria-hidden="true">'
            f'<i style="width:{100 * count / maximum:.3f}%;background:{color}"></i></span>'
            f'<strong>{count}</strong></li>'
        )

    return f'{heading}<ul class="dg-ranking">{"".join(entries)}</ul>'


def sensory_charts(records: list[dict], wine_type: str) -> None:
    cards = []
    for field, label, options in sensory_questions(wine_type):
        counts = answer_counts(records, field)
        chart = ranking_chart(label, {option: counts[option] for option in options}, sort_by_count=False)
        cards.append(f'<section class="dg-sensory-card">{chart}</section>')
    st.html(f'<div class="dg-sensory-charts">{"".join(cards)}</div>')


def split_bar(description: str, records: list[dict], field: str, options) -> None:
    counts = answer_counts(records, field)
    values = [counts[label] for label in options]
    total = sum(values)
    segments, legend, summaries = [], [], []
    for label, value, color in zip(options, values, leading_colors(values)):
        label = escape(label)
        share = value / total * 100 if total else 0
        summary = f"{label} · {value} válasz · {percent_label(share)}"
        summaries.append(summary)
        if value:
            segments.append(
                f'<span class="geoterroir-split-segment" title="{summary}" '
                f'style="width:{share:.6f}%;background:{color}"></span>'
            )
        legend.append(
            f'<li><span class="geoterroir-swatch" style="background:{color}"></span>'
            f'<span>{label}</span><strong>{percent_label(share)} <small>({value})</small></strong></li>'
        )

    empty = '<p class="dg-chart-empty">Még nincs válasz.</p>' if not total else ""
    st.html(
        f'<section class="geoterroir-split">'
        f'<div class="geoterroir-split-track" role="img" '
        f'aria-label="{escape(description)}. {". ".join(summaries)}">{"".join(segments)}</div>'
        f'{empty}<ul>{"".join(legend)}</ul></section>'
    )


def scores_chart(records: list[dict]) -> None:
    st.html(chart_title("Pontszámok"))
    counts = answer_counts(records, "score")
    values = [counts[score] for score in SCORES]
    maximum = max(values)
    figure = go.Figure(go.Bar(
        x=list(SCORES),
        y=values,
        marker=dict(color=leading_colors(values), cornerradius=5),
        width=0.34,
        text=[value or "" for value in values],
        textposition="outside",
        cliponaxis=False,
        customdata=[label for label, _ in SCORES.values()],
        hovertemplate="%{x} pont · %{customdata}<br>%{y} értékelés<extra></extra>",
    ))
    figure.update_xaxes(tickmode="array", tickvals=list(SCORES))
    figure.update_yaxes(
        range=[0, max(1, maximum) * 1.18],
        tick0=0,
        dtick=max(1, (maximum + 3) // 4),
    )
    plot(figure, "chart-scores")


def comparison_chart(averages: dict[int, tuple[float, int]]) -> None:
    st.html(chart_title("Átlagpontszám tételenként"))
    scores = [averages.get(number, (None, 0)) for number in LOTS]
    values = [average for average, _ in scores]
    formatted = [decimal_label(average) for average in values]
    categories = [str(number) for number in LOTS]
    figure = go.Figure(go.Bar(
        x=categories,
        y=values,
        customdata=[
            [lot.name, label, count]
            for lot, label, (_, count) in zip(LOTS.values(), formatted, scores)
        ],
        marker=dict(color=leading_colors(values), cornerradius=5),
        width=0.30,
        text=[label if value is not None else "" for label, value in zip(formatted, values)],
        textposition="outside",
        cliponaxis=False,
        hovertemplate="%{customdata[0]}<br>Átlag %{customdata[1]}/10<br>%{customdata[2]} értékelés<extra></extra>",
    ))
    figure.update_xaxes(
        type="category",
        tickmode="array",
        tickvals=categories,
        ticktext=[lot.name for lot in LOTS.values()],
    )
    figure.update_yaxes(range=[0, 10.7], tick0=0, dtick=2)
    plot(figure, "chart-lot-comparison")


def render_charts(records: list[dict], lot: int, averages: dict[int, tuple[float, int]]) -> None:
    wine_type = LOTS[lot].wine_type
    sensory_charts(records, wine_type)
    first, second, third = st.columns(3, gap="small")
    with first, st.container(border=True, key="dg-card-technique"):
        split_bar("Borkészítési technológia", records, "technique", TECHNIQUES)
    with second, st.container(border=True, key="dg-card-balance"):
        split_bar("Egyensúly", records, "balance", BALANCES)
    with third, st.container(border=True, key="dg-card-branch"):
        if wine_type == "Fehérbor":
            split_bar("Illatosság · fehérborok", records, "fragrance", WHITE_VARIETIES)
        else:
            split_bar("Fajtacsoport · vörösborok", records, "variety_group", RED_VARIETIES)

    scores, comparison = st.columns(2, gap="small")
    with scores, st.container(border=True, key="dg-card-scores"):
        scores_chart(records)
    with comparison, st.container(border=True, key="dg-card-comparison"):
        comparison_chart(averages)

    aromas, grapes, regions = st.columns(3, gap="small")
    with aromas, st.container(border=True, key="dg-card-aromas"):
        st.html(ranking_chart("Aromacsoportok", aroma_counts(records), respondent_count=len(records)))
    with grapes, st.container(border=True, key="dg-card-grapes"):
        st.html(ranking_chart("Szőlőfajták", answer_counts(records, "grape")))
    with regions, st.container(border=True, key="dg-card-regions"):
        st.html(ranking_chart("Borvidékek", answer_counts(records, "region")))
