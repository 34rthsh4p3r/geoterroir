from dataclasses import dataclass
from zoneinfo import ZoneInfo


BUDAPEST = ZoneInfo("Europe/Budapest")


@dataclass(frozen=True)
class WineLot:
    name: str
    wine_type: str


LOTS = {
    number: WineLot(f"{number}. tétel", "Fehérbor" if number <= 3 else "Vörösbor")
    for number in range(1, 6)
}

LOT_QUESTION = "Válaszd ki az értékelni kívánt tételt!"
AROMA_QUESTION = "Jellemző aromacsoportok"
TECHNIQUE_QUESTION = "Reduktív vagy oxidatív volt a borkészítés?"
FRAGRANCE_QUESTION = "Illatos vagy nem illatos?"
GROUP_QUESTION = "Világfajta vagy Kárpát-medencei?"
REGION_QUESTION = "Melyik borvidékről származhat?"
BALANCE_QUESTION = "Egyensúlyos vagy nem egyensúlyos?"
SCORE_QUESTION = "Értékelje a bort az ízlése szerint:"

INTENSITIES = ("alacsony", "közepes", "magas")
SENSORY_QUESTIONS = (
    ("sweetness", "Édesség", ("száraz", "félszáraz", "félédes", "édes")),
    ("acidity", "Savasság", INTENSITIES),
    ("alcohol", "Alkohol", INTENSITIES),
    ("tannin", "Tannin", INTENSITIES),
    ("finish", "Lecsengés", ("rövid", "közepes", "hosszú")),
)

AROMAS = {
    "Florális": "akác, kamilla, bodza, rózsa, ibolya, virág",
    "Zöld gyümölcs": "zöldalma, egres, körte, szőlő",
    "Citrusféle": "citrom, lime, narancs, grapefruit",
    "Csonthéjas": "őszibarack, sárgabarack, nektarin",
    "Trópusi": "banán, licsi, mangó, dinnye, ananász, maracuja",
    "Piros bogyós": "ribizli, vörösáfonya, málna, eper, meggy, cseresznye",
    "Fekete bogyós": "feketeribizli, szeder, kékáfonya, kései meggy, szilva",
    "Fűszeres": "fűszer, fekete bors, fehér bors, édesgyökér",
    "Füves": "zöldpaprika, fű, paradicsomlevél, spárga, borsó",
    "Gyógynövényes": "eukaliptusz, menta, édeskömény, kapor",
    "Hordós": "pirítós, vaj, vanília, karamella, fa, füst stb.",
}
TECHNIQUES = ("Reduktív", "Oxidatív")
BALANCES = ("Egyensúlyos", "Nem egyensúlyos")

WHITE_VARIETIES = {
    "Illatos": (
        "Melyik illatos fajta lehet?",
        ("Cserszegi Fűszeres", "Irsai Olivér", "Sauvignon Blanc", "Sárgamuskotály", "Tramini"),
    ),
    "Nem illatos": (
        "Melyik nem illatos fajta lehet?",
        ("Chardonnay", "Furmint", "Hárslevelű", "Olaszrizling", "Rajnai Rizling"),
    ),
}
RED_VARIETIES = {
    "Világfajta": (
        "Melyik világfajta lehet?",
        ("Cabernet Franc", "Cabernet Sauvignon", "Merlot", "Pinot Noir", "Syrah / Shiraz"),
    ),
    "Kárpát-medencei": (
        "Melyik Kárpát-medencei fajta lehet?",
        ("Bikavér", "Feketeleányka", "Kékfrankos", "Kadarka", "Portugieser"),
    ),
}
REGIONS = (
    "Badacsonyi borvidék",
    "Balatonboglári borvidék",
    "Balaton-felvidéki borvidék",
    "Balatonfüred–Csopaki borvidék",
    "Bükki borvidék",
    "Csongrádi borvidék",
    "Egri borvidék",
    "Etyek–Budai borvidék",
    "Hajós–Bajai borvidék",
    "Kunsági borvidék",
    "Mátrai borvidék",
    "Móri borvidék",
    "Neszmélyi borvidék",
    "Pannonhalmi borvidék",
    "Pécsi borvidék",
    "Somlói borvidék",
    "Soproni borvidék",
    "Szekszárdi borvidék",
    "Tokaji borvidék",
    "Tolnai borvidék",
    "Villányi borvidék",
    "Zalai borvidék",
)
SCORES = {
    1: ("Ihatatlan", "súlyosan és menthetetlenül hibás tétel"),
    2: ("Súlyosan hibás", "dugós, oxidált vagy technológiailag elrontott bor"),
    3: ("Élvezhetetlen", "ihatatlanul savas, keserű vagy maróan alkoholos"),
    4: ("Átlag alatti", "unalmas, teljesen jellegtelen, „vékony” bor"),
    5: ("Korrekt alapbor", "tiszta, hibátlan, de teljesen egyszerű tétel"),
    6: ("Jó", "jó ivású, kellemes mindennapi bor, hozza a fajtajellegeket"),
    7: ("Nagyon jó", "komolyabb szerkezetű bor, szép egyensúllyal"),
    8: ("Kiváló", "kiemelkedő minőség, remek egyensúly és egyedi karakter"),
    9: ("Kivételes", "izgalmas és emlékezetes bor, tökéletes harmónia"),
    10: ("Tökéletes", "hibátlan, felejthetetlen élményt nyújtó ikonikus bor"),
}


def lot_label(lot: int | None, lots: dict[int, WineLot]) -> str:
    if lot is None:
        return "Összes tétel"
    entry = lots[lot]
    return f"{entry.name} ({entry.wine_type.lower()})"


def variety_branch(wine_type: str):
    if wine_type == "Fehérbor":
        return "fragrance", FRAGRANCE_QUESTION, WHITE_VARIETIES
    return "variety_group", GROUP_QUESTION, RED_VARIETIES


def sensory_questions(wine_type: str):
    return tuple(question for question in SENSORY_QUESTIONS
                 if question[0] != "tannin" or wine_type == "Vörösbor")
