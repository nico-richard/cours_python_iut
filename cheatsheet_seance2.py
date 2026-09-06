from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import Paragraph, Table, TableStyle, XPreformatted


PAGE_W, PAGE_H = A4
OUTPUT = Path("output/pdf/cheatsheet_seance2_a4.pdf")

NAVY = colors.HexColor("#17324D")
PALE_BLUE = colors.HexColor("#EEF5FB")
PALE_YELLOW = colors.HexColor("#FFF7D6")
PALE_RED = colors.HexColor("#FFF0ED")
INK = colors.HexColor("#17212B")
MUTED = colors.HexColor("#536271")
LINE = colors.HexColor("#C8D5DF")


font_path = Path("C:/Windows/Fonts/consola.ttf")
if font_path.exists():
    pdfmetrics.registerFont(TTFont("Courier", str(font_path)))

styles = getSampleStyleSheet()
BODY = ParagraphStyle(
    "Body",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=7.75,
    leading=9.35,
    textColor=INK,
    spaceAfter=2,
)
SMALL = ParagraphStyle(
    "Small",
    parent=BODY,
    fontSize=8.2,
    leading=10.5,
)
CODE = ParagraphStyle(
    "Code",
    parent=styles["Code"],
    fontName="Courier",
    fontSize=7.65,
    leading=9.25,
    leftIndent=0,
    rightIndent=0,
    spaceBefore=2,
    spaceAfter=3,
    textColor=INK,
)
TABLE_HEAD = ParagraphStyle(
    "TableHead",
    parent=BODY,
    fontName="Helvetica-Bold",
    fontSize=7.1,
    leading=8.2,
    textColor=INK,
)
TABLE_CELL = ParagraphStyle(
    "TableCell",
    parent=BODY,
    fontSize=7.7,
    leading=9.2,
)


def paragraph(text, style=BODY):
    return Paragraph(text, style)


def code(text):
    pattern = (
        r'#[^\n]*|"[^"\n]*"|'
        r"\b(?:def|return|for|in|while|if|elif|else|break|continue|and|or|not|True|False|None)\b|"
        r"\b(?:print|type|dir|help|len|sum|min|max|sorted|range|float|int|str|list|tuple)\b|"
        r"\b\d+(?:\.\d+)?\b"
    )
    pieces, last = [], 0
    for match in re.finditer(pattern, text):
        pieces.append(escape(text[last:match.start()]))
        token = match.group()
        if token.startswith("#"):
            color = "#66717C"
        elif token.startswith('"'):
            color = "#226C52"
        elif token[0].isdigit():
            color = "#77551E"
        elif token in {
            "def", "return", "for", "in", "while", "if", "elif", "else",
            "break", "continue", "and", "or", "not", "True", "False", "None",
        }:
            color = "#69468E"
        else:
            color = "#245D82"
        pieces.append(f'<font color="{color}">{escape(token)}</font>')
        last = match.end()
    pieces.append(escape(text[last:]))
    return XPreformatted("".join(pieces), CODE)


def panel(title, content):
    return {"title": title, "content": content}


def mini_table(rows, widths, header=True):
    prepared = []
    for row_index, row in enumerate(rows):
        style = TABLE_HEAD if header and row_index == 0 else TABLE_CELL
        prepared.append([paragraph(str(value), style) for value in row])
    table = Table(prepared, colWidths=widths, hAlign="LEFT")
    commands = [
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]
    if header:
        commands.append(("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EDF1F4")))
    table.setStyle(TableStyle(commands))
    return table


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    left = [
        panel(
            "1. Écrire et appeler une fonction",
            [
                paragraph("Une fonction reçoit des <b>arguments</b> et peut renvoyer un résultat.", SMALL),
                code(
                    "def convertir_c_en_k(temperature_c):\n"
                    "    return temperature_c + 273.15\n\n"
                    "temperature_k = convertir_c_en_k(20.0)\n"
                    "# temperature_k vaut 293.15"
                ),
                code(
                    'def convertir(valeur, unite="m"):\n'
                    '    if unite == "cm":\n'
                    '        return valeur * 100\n'
                    '    return valeur'
                ),
                paragraph(
                    "<b>return</b> transmet une valeur ; <b>print()</b> l'affiche seulement. "
                    "Placer les paramètres obligatoires avant ceux par défaut.",
                    SMALL,
                ),
            ],
        ),
        panel(
            "2. Utiliser un objet",
            [
                code(
                    'capteur = CapteurTemperature("Salle A", 20.5)\n'
                    "capteur.valeur          # attribut\n"
                    "capteur.actualiser(21)  # méthode"
                ),
                mini_table(
                    [
                        ["Notion", "Rôle"],
                        ["classe", "modèle commun"],
                        ["instance", "objet créé"],
                        ["attribut", "donnée de l'objet"],
                        ["méthode", "action de l'objet"],
                    ],
                    [24 * mm, 60 * mm],
                ),
                code("type(capteur)\ndir(capteur)\nhelp(capteur.actualiser)"),
            ],
        ),
        panel(
            "3. Listes et tuples",
            [
                code(
                    "mesures = [18.2, 19.1, 20.0]\n"
                    "mesures[0] = 18.4\n"
                    "mesures.append(20.2)"
                ),
                code(
                    "position = (48.85, 2.35)\n"
                    "latitude, longitude = position"
                ),
                mini_table(
                    [
                        ["Liste [ ]", "Tuple ( )"],
                        ["modifiable", "non modifiable"],
                        ["série évolutive", "valeurs associées"],
                    ],
                    [42 * mm, 42 * mm],
                ),
            ],
        ),
    ]

    right = [
        panel(
            "4. Indexer et découper",
            [
                code(
                    "valeurs = [10, 20, 30, 40, 50]\n"
                    "valeurs[0]     # 10\n"
                    "valeurs[-1]    # 50\n"
                    "valeurs[1:4]   # [20, 30, 40]\n"
                    "valeurs[:2]    # [10, 20]\n"
                    "valeurs[::2]   # [10, 30, 50]"
                ),
                paragraph("Dans <b>[début:fin:pas]</b>, la borne de fin est exclue.", SMALL),
                code(
                    "len(valeurs)       # 5\n"
                    "sum(valeurs)       # 150\n"
                    "min(valeurs), max(valeurs)\n"
                    "sorted(valeurs)    # nouvelle liste\n"
                    "20 in valeurs      # True"
                ),
            ],
        ),
        panel(
            "5. Nettoyer une chaîne",
            [
                code(
                    'ligne = "  temperature;20,5  "\n'
                    "ligne = ligne.strip()\n"
                    'ligne = ligne.replace(",", ".")\n'
                    'morceaux = ligne.split(";")\n'
                    "# ['temperature', '20.5']"
                ),
                mini_table(
                    [
                        ["Méthode", "Résultat"],
                        ["strip()", "retire les bords"],
                        ["split(';')", "chaîne vers liste"],
                        ["';'.join(liste)", "liste vers chaîne"],
                        ["find('mot')", "index ou -1"],
                    ],
                    [31 * mm, 53 * mm],
                ),
                paragraph("Une chaîne est une séquence non modifiable.", SMALL),
            ],
        ),
        panel(
            "6. Répéter avec des boucles",
            [
                code(
                    "total = 0\n"
                    "for mesure in mesures:\n"
                    "    total += mesure\n"
                    "moyenne = total / len(mesures)"
                ),
                code(
                    "charge = 20\n"
                    "while charge < 80:\n"
                    "    charge += 15"
                ),
                code(
                    "for mesure in mesures:\n"
                    "    if mesure < 0:\n"
                    "        continue\n"
                    "    if mesure > 30:\n"
                    "        break"
                ),
                paragraph("<b>range(début, fin, pas)</b> produit des entiers ; fin est exclue.", SMALL),
                paragraph("<b>for</b> parcourt ; <b>while</b> répète tant qu'une condition est vraie.", SMALL),
            ],
        ),
    ]

    final_panel = panel(
        "Le patron à retenir - Traiter une série de mesures",
        [
            code(
                "def premiere_mesure_superieure(mesures, seuil):\n"
                "    for indice in range(len(mesures)):\n"
                "        mesure = mesures[indice]\n"
                "        if mesure < 0:\n"
                "            continue\n"
                "        if mesure > seuil:\n"
                "            return indice\n"
                "    return -1"
            ),
            paragraph(
                "Entrées par les paramètres, résultat avec <b>return</b>. "
                "Choisir des noms clairs, traiter les cas limites et éviter de modifier "
                "les données reçues sans nécessité.",
                SMALL,
            ),
        ],
    )

    render_sheet(left, right, final_panel)
    print(OUTPUT.resolve())


def render_sheet(left, right, final_panel):
    canvas = pdfcanvas.Canvas(str(OUTPUT), pagesize=A4)
    canvas.setTitle("Python - Séance 2 - Fiche mémo A4")
    canvas.setAuthor("Cours Python IUT")

    margin, gap = 10 * mm, 4 * mm
    width = (PAGE_W - 2 * margin - gap) / 2
    palette = ["#245D82", "#226C52", "#69468E", "#95501F"]

    canvas.setFillColor(NAVY)
    canvas.setFont("Helvetica-Bold", 21)
    canvas.drawString(margin, PAGE_H - 17 * mm, "Python | Séance 2")
    canvas.setFont("Helvetica", 10)
    canvas.drawRightString(PAGE_W - margin, PAGE_H - 16 * mm, "ORGANISER ET RÉPÉTER")
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(MUTED)
    canvas.drawString(
        margin,
        PAGE_H - 23 * mm,
        "Structurer  >  Regrouper  >  Découper  >  Parcourir  >  Renvoyer",
    )

    legend = ["Fonctions", "Objets", "Séquences et textes", "Boucles"]
    for index, (label, color) in enumerate(zip(legend, palette)):
        x = margin + index * 48 * mm
        canvas.setFillColor(colors.HexColor(color))
        canvas.roundRect(x, PAGE_H - 31 * mm, 2 * mm, 2 * mm, 1, fill=1, stroke=0)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawString(x + 3.5 * mm, PAGE_H - 31 * mm, label)

    def measure(current_panel, panel_width):
        total = 0
        for item in current_panel["content"]:
            total += item.getSpaceBefore() + item.wrap(panel_width - 16, PAGE_H)[1] + item.getSpaceAfter()
        return total + 34

    def draw_frame(x, top, panel_width, height, color):
        radius = 5
        canvas.setStrokeColor(colors.HexColor(color))
        canvas.setLineWidth(0.55)
        canvas.setFillColor(colors.white)
        canvas.roundRect(x, top - height, panel_width, height, radius, fill=1, stroke=0)
        canvas.setFillColor(colors.HexColor(color))
        canvas.roundRect(x, top - 22, panel_width, 22, radius, fill=1, stroke=0)
        canvas.rect(x, top - 22, panel_width, 11, fill=1, stroke=0)
        canvas.roundRect(x, top - height, panel_width, height, radius, fill=0, stroke=1)
        canvas.setFillColor(colors.white)

    def draw(current_panel, x, top, panel_width, height, color):
        draw_frame(x, top, panel_width, height, color)
        canvas.setFont("Helvetica-Bold", 9.3)
        canvas.drawString(x + 8, top - 14.5, current_panel["title"])
        y = top - 28
        for item in current_panel["content"]:
            y -= item.getSpaceBefore()
            _, item_height = item.wrap(panel_width - 16, PAGE_H)
            item.drawOn(canvas, x + 8, y - item_height)
            y -= item_height + item.getSpaceAfter()

    rows = [
        (left[0], right[0], palette[0], palette[2]),
        (left[1], right[1], palette[1], palette[2]),
        (left[2], right[2], palette[2], palette[3]),
    ]
    y = PAGE_H - 36 * mm
    heights = [max(measure(a, width), measure(b, width)) for a, b, _, _ in rows]
    bottom_height = 105
    available = y - 16 * mm - bottom_height - 3 * gap
    if sum(heights) > available:
        raise ValueError(f"Contenu trop haut : {sum(heights):.1f} > {available:.1f}")
    extra = (available - sum(heights)) / 3
    for (left_panel, right_panel, left_color, right_color), height in zip(rows, heights):
        height += extra
        draw(left_panel, margin, y, width, height, left_color)
        draw(right_panel, margin + width + gap, y, width, height, right_color)
        y -= height + gap

    full_width = PAGE_W - 2 * margin
    draw_frame(margin, y, full_width, bottom_height, palette[1])
    canvas.setFont("Helvetica-Bold", 9.3)
    canvas.drawString(margin + 8, y - 14.5, final_panel["title"])
    snippet = final_panel["content"][0]
    _, snippet_height = snippet.wrap(width - 16, PAGE_H)
    snippet.drawOn(canvas, margin + 8, y - 29 - snippet_height)
    note = final_panel["content"][1]
    _, note_height = note.wrap(width - 20, PAGE_H)
    note.drawOn(canvas, margin + width + gap + 8, y - 33 - note_height)

    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7)
    canvas.drawString(margin, 9 * mm, "PYTHON IUT  /  Fiche mémo - Séance 2")
    canvas.drawRightString(PAGE_W - margin, 9 * mm, "A4  /  1 page")
    canvas.showPage()
    canvas.save()


if __name__ == "__main__":
    build()
