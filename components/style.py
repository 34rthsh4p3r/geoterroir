import streamlit as st


def apply_styles() -> None:
    st.html("""
        <style>
        .st-key-geoterroir-evaluation, .st-key-geoterroir-login {
            max-width: 48rem; margin-inline: auto;
        }
        .st-key-geoterroir-admin { max-width: 76rem; margin-inline: auto; }
        .dg-admin-brand {
            display: block;
            padding: 0;
            color: #9f1916;
            font-size: 1.15rem;
            font-weight: 700;
            text-decoration: none;
        }
        .st-key-dg-admin-header {
            padding-bottom: .5rem;
            border-bottom: 1px solid #e4dadc;
        }
        .st-key-geoterroir-admin h1 {
            padding: 0;
            font-size: clamp(1.65rem, 3vw, 2.3rem);
        }
        .st-key-geoterroir-admin [class*="st-key-dg-card-"] {
            background: #fffdfa;
            border-radius: .75rem;
        }
        .st-key-dg-lot-buttons button { min-height: 44px; }
        .st-key-dg-card-active, .st-key-dg-card-total { text-align: center; }
        .st-key-dg-card-active label, .st-key-dg-card-total label { display: flex; justify-content: center; }
        .st-key-geoterroir-evaluation [class*="st-key-question-"] {
            background: #fffdfa;
            border-radius: .65rem;
            box-shadow: 0 2px 9px #39212908;
        }
        .st-key-geoterroir-evaluation img {
            border-radius: .8rem;
            border: 1px solid #e6ddd6;
            box-shadow: 0 5px 20px #3921290d;
        }
        .st-key-geoterroir-evaluation [role="radiogroup"] label,
        .st-key-geoterroir-evaluation [role="combobox"],
        .st-key-geoterroir-evaluation button,
        .st-key-dg-admin-navigation button,
        .st-key-geoterroir-login button {
            min-height: 44px;
        }
        .st-key-geoterroir-evaluation [role="radiogroup"] label { margin-bottom: 0; }
        .st-key-geoterroir-evaluation button[data-variant="segmented_control"][role="radio"][aria-checked="true"]:not(:disabled),
        .st-key-dg-admin-navigation button[data-variant="segmented_control"][role="radio"][aria-checked="true"]:not(:disabled) {
            background-color: #9f1916;
            border-color: #9f1916;
            color: #fff;
        }
        @media (max-width: 640px) {
            .st-key-question-score [role="radiogroup"] {
                display: grid;
                grid-template-columns: repeat(5, minmax(0, 1fr));
                row-gap: .4rem;
            }
            .st-key-question-score button[role="radio"] {
                width: 100%;
                min-width: 0;
                margin-inline: 0;
                padding-inline: .25rem;
            }
            .st-key-question-score button[role="radio"]:nth-child(5) {
                border-start-end-radius: .65rem;
                border-end-end-radius: .65rem;
            }
            .st-key-question-score button[role="radio"]:nth-child(6) {
                border-start-start-radius: .65rem;
                border-end-start-radius: .65rem;
            }
        }
        [role="option"], [role="option"] * {
            white-space: normal;
            overflow-wrap: anywhere;
        }
        [role="option"] { min-height: 44px; }
        .st-key-admin_archive button:not(:disabled) { border-color: #9f1916; color: #9f1916; }
        h3.geoterroir-chart-title {
            margin: 0;
            padding: 0;
            font-size: 1.06rem;
            line-height: 1.25;
        }
        .dg-chart-empty {
            margin: .7rem 0 0;
            color: #635760;
            font-size: .79rem;
        }
        .st-key-geoterroir-admin ul.dg-ranking {
            list-style: none;
            display: grid;
            gap: .4rem;
            padding: 0;
            padding-inline: 0;
            margin: .65rem 0 0;
            text-align: left;
        }
        .st-key-geoterroir-admin .dg-ranking li {
            display: grid;
            grid-template-columns: minmax(0, 1fr) minmax(2rem, 1fr) auto;
            align-items: center;
            gap: .45rem;
            margin: 0;
            padding: 0;
            text-align: left;
            font-size: .83rem;
            line-height: 1.25;
        }
        .dg-rank-label { overflow-wrap: anywhere; }
        .dg-ranking strong { min-width: 1.6em; text-align: right; font-variant-numeric: tabular-nums; }
        .dg-rank-track, .dg-rank-track i { display: block; height: .5rem; border-radius: 1rem; }
        .dg-rank-track { background: #eee8eb; }
        .dg-sensory-charts {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(min(100%, 11rem), 1fr));
            gap: .5rem;
        }
        .dg-sensory-card {
            background: #fffdfa;
            border: 1px solid #e4dadc;
            border-radius: .75rem;
            padding: .85rem;
        }
        .dg-sensory-card .dg-ranking li {
            grid-template-columns: 4.1rem minmax(0, 1fr) auto;
        }
        .geoterroir-split-track {
            display: flex;
            height: .9rem;
            overflow: hidden;
            border-radius: 1rem;
            background: #eee8eb;
            margin-block: .45rem .8rem;
        }
        .geoterroir-split-segment { flex-shrink: 0; box-sizing: border-box; }
        .geoterroir-split-segment + .geoterroir-split-segment { border-inline-start: 2px solid #fffdfa; }
        .geoterroir-split ul { list-style: none; margin: .15rem 0 0; padding: 0; }
        .geoterroir-split li {
            display: grid;
            grid-template-columns: .55rem minmax(0, 1fr) auto;
            align-items: center;
            gap: .45rem;
            padding: .15rem 0;
            font-size: .83rem;
        }
        .geoterroir-split li strong { white-space: nowrap; }
        .geoterroir-split li small { color: #635760; font-weight: 400; }
        .geoterroir-swatch { width: .52rem; height: .52rem; border-radius: 50%; }
        .geoterroir-score {
            border-left: .2rem solid #9f1916;
            border-radius: .32rem;
            background: #f5e8e8;
            padding: .7rem .9rem;
            margin-block: .35rem;
        }
        </style>
        <script>
        (() => {
            if (window.geoterroirDropdownObserver) return;
            const selector = '.st-key-geoterroir-evaluation input[role="combobox"][inputmode="none"]';
            const lockDropdowns = () => {
                for (const input of document.querySelectorAll(selector)) {
                    if (!input.readOnly) input.readOnly = true;
                }
            };
            // Streamlit's non-searchable menus still use inputs, so block paste and IME edits as well.
            window.geoterroirDropdownObserver = new MutationObserver(lockDropdowns);
            window.geoterroirDropdownObserver.observe(document.body, {
                childList: true, subtree: true, attributes: true, attributeFilter: ['readonly'],
            });
            lockDropdowns();
        })();
        </script>
    """, unsafe_allow_javascript=True)
