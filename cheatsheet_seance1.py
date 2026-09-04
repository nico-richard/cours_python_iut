from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import XPreformatted
from reportlab.platypus import (
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


PAGE_W, PAGE_H = A4
OUTPUT = Path("output/pdf/cheatsheet_seance1_a4.pdf")

NAVY = colors.HexColor("#17324D")
BLUE = colors.HexColor("#2A6F9E")
PALE_BLUE = colors.HexColor("#EEF5FB")
PALE_YELLOW = colors.HexColor("#FFF7D6")
PALE_RED = colors.HexColor("#FFF0ED")
INK = colors.HexColor("#17212B")
MUTED = colors.HexColor("#536271")
LINE = colors.HexColor("#C8D5DF")


font_path = Path('C:/Windows/Fonts/consola.ttf')
if font_path.exists():
    pdfmetrics.registerFont(TTFont('Courier', str(font_path)))
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
    fontSize=7.8,
    leading=9.5,
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
    fontSize=7.8,
    leading=9.5,
)


def P(text, style=BODY):
    return Paragraph(text, style)


def code(text):
    pattern = r'#[^\n]*|"[^"\n]*"|\b(?:if|elif|else|and|or|not|True|False)\b|\b(?:input|print|float|int|str|type|abs)\b|\b\d+(?:\.\d+)?\b'
    pieces, last = [], 0
    for match in re.finditer(pattern, text):
        pieces.append(escape(text[last:match.start()]))
        token = match.group()
        color = '#66717C' if token.startswith('#') else '#226C52' if token.startswith('"') else '#77551E' if token[0].isdigit() else '#69468E' if token in ('if', 'elif', 'else', 'and', 'or', 'not', 'True', 'False') else '#245D82'
        pieces.append(f'<font color="{color}">{escape(token)}</font>')
        last = match.end()
    pieces.append(escape(text[last:]))
    return XPreformatted(''.join(pieces), CODE)


def box(title, content, background=colors.white):
    return {"title": title, "content": content}


def mini_table(rows, widths, header=True):
    prepared = []
    for row_index, row in enumerate(rows):
        prepared.append(
            [
                P(str(value), TABLE_HEAD if header and row_index == 0 else TABLE_CELL)
                for value in row
            ]
        )
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
        commands.extend(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor('#EDF1F4')),
            ]
        )
    table.setStyle(TableStyle(commands))
    return table


def build():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    gauche = [
        box(
            "1. Exécuter un programme",
            [
                P("<b>Console</b> : essayer une instruction.", SMALL),
                code(">>> temperature = 20.5\n>>> temperature + 273.15\n293.65"),
                P("<b>Script</b> : enregistrer dans bonjour.py.", SMALL),
                code('print("Bonjour !")\n# Terminal : python bonjour.py\n# Affichage : Bonjour !'),
                P("CPU : exécute · RAM : temporaire · Stockage : durable.", SMALL),
            ],
            PALE_BLUE,
        ),
        Spacer(1, 6),
        box(
            "2. Variables, affectation et types",
            [
                code("temperature = 20.5   # affectation\nnombre = 12\nnombre += 1          # nombre vaut 13"),
                mini_table(
                    [
                        ["Type", "Exemple", "Rôle"],
                        ["int", "12", "entier"],
                        ["float", "20.5", "décimal"],
                        ["str", '"COM3"', "texte"],
                        ["bool", "True / False", "logique"],
                    ],
                    [18 * mm, 23 * mm, 43 * mm],
                ),
                Spacer(1, 3),
                code('type(20.5)       # float\ntype("20.5")     # str\ntype(20 > 10)    # bool'),
            ],
        ),
        Spacer(1, 6),
        box(
            "3. Saisie, conversion, affichage",
            [
                P("<b>input()</b> renvoie du texte : convertir pour calculer.", SMALL),
                code('saisie = input("Température : ")\n# Saisie au clavier : 20.456\nt = float(saisie)\nprint(f"Température : {t:.1f} °C")\n# Affichage : Température : 20.5 °C'),
                code('float("20.5")    # 20.5\nint("12")        # 12\nstr(20.5)        # "20.5"\nf"{3.14159:.2f}" # "3.14"'),
                P("Point décimal : 20.5. Le format .2f change l'affichage.", SMALL),
            ],
            PALE_BLUE,
        ),
    ]

    droite = [
        box(
            "4. Calculer",
            [
                code('7 + 2       # 9     addition\n7 - 2       # 5     soustraction\n7 * 2       # 14    multiplication\n7 / 2       # 3.5   division\n7 // 2      # 3     quotient arrondi en bas\n7 % 2       # 1     reste\n7 ** 2      # 49    puissance'),
                code('(2 + 3) * 4 # 20\n2 + 3 * 4   # 14\n8 % 2 == 0  # True : 8 est pair'),
            ],
        ),
        Spacer(1, 6),
        box(
            "5. Comparer et prendre une décision",
            [
                code('t = 20              # affecter\nt == 20             # True : comparer\nt != 20             # False\n0 <= t < 30         # True'),
                code('if t < 0:\n    print("Gel")\nelif t < 30:\n    print("Plage prévue")\nelse:\n    print("Seuil dépassé")\n# Avec t = 20 : Plage prévue'),
                code('t > 0 and t < 30    # True : les deux\nt < 0 or t > 30     # False : au moins un\nnot (t < 0)         # True : inverse'),
                P("Une seule branche. Ne pas oublier : et l'indentation.", SMALL),
            ],
            PALE_YELLOW,
        ),
        Spacer(1, 6),
        box(
            "6. Erreurs : lire avant de corriger",
            [
                P("<b>Syntaxe</b> : instruction mal écrite.", SMALL),
                code('if t < 0           # manque :\nif t < 0:          # corrigé'),
                P("<b>Exécution</b> : opération impossible.", SMALL),
                code('float("vingt")     # ValueError\nfloat("20.5")      # 20.5'),
                P("<b>Logique</b> : résultat incorrect.", SMALL),
                code('moyenne = 10 + 14 / 2    # 17 : faux\nmoyenne = (10 + 14) / 2  # 12 : correct'),
                P("Traceback : lire d'abord la dernière ligne.", SMALL),
            ],
            PALE_RED,
        ),
        Spacer(1, 6),
        box(
            "Exemple complet - Convertir une température",
            [
                code('t = float(input("Température en °C : "))\nkelvin = t + 273.15\nif t < 0:\n    print("Risque de gel")\nelse:\n    print("Pas de gel")\nprint(f"{kelvin:.2f} K")'),
                code('# Exemple de saisie et affichage\nTempérature en °C : -5\nRisque de gel\n268.15 K\n\n# Autre saisie : 20\n# Affiche : Pas de gel puis 293.15 K'),
            ],
            PALE_BLUE,
        ),
    ]

    render_sheet([item for item in gauche if isinstance(item, dict)],
                 [item for item in droite if isinstance(item, dict)])
    print(OUTPUT.resolve())


def render_sheet(left, right):
    c = pdfcanvas.Canvas(str(OUTPUT), pagesize=A4)
    c.setTitle('Python - Séance 1 - Fiche mémo A4')
    c.setAuthor('Cours Python IUT')
    margin, gap = 10 * mm, 4 * mm
    width = (PAGE_W - 2 * margin - gap) / 2
    palette = ['#245D82', '#226C52', '#69468E', '#95501F']
    c.setFillColor(NAVY)
    c.setFont('Helvetica-Bold', 21)
    c.drawString(margin, PAGE_H - 17 * mm, 'Python | Séance 1')
    c.setFont('Helvetica', 10)
    c.drawRightString(PAGE_W - margin, PAGE_H - 16 * mm, 'PREMIERS PROGRAMMES')
    c.setFont('Helvetica', 8)
    c.setFillColor(MUTED)
    c.drawString(margin, PAGE_H - 23 * mm, 'Saisir  >  Convertir  >  Calculer  >  Décider  >  Afficher')
    for i, (label, color) in enumerate(zip(['Bases', 'Entrées-sorties', 'Calculs et décisions', 'Erreurs'], palette)):
        x = margin + i * 48 * mm
        c.setFillColor(colors.HexColor(color))
        c.roundRect(x, PAGE_H - 31 * mm, 2 * mm, 2 * mm, 1, fill=1, stroke=0)
        c.setFont('Helvetica', 7.5)
        c.drawString(x + 3.5 * mm, PAGE_H - 31 * mm, label)

    def measure(panel, w):
        total = 0
        for item in panel['content']:
            total += item.getSpaceBefore() + item.wrap(w - 16, PAGE_H)[1] + item.getSpaceAfter()
        return total + 34

    def draw_frame(x, top, w, h, color):
        radius = 5
        c.setStrokeColor(colors.HexColor(color))
        c.setLineWidth(0.55)
        c.setFillColor(colors.white)
        c.roundRect(x, top - h, w, h, radius, fill=1, stroke=0)
        c.setFillColor(colors.HexColor(color))
        c.roundRect(x, top - 22, w, 22, radius, fill=1, stroke=0)
        # Seuls les coins supérieurs du bandeau suivent le contour arrondi.
        c.rect(x, top - 22, w, 11, fill=1, stroke=0)
        c.roundRect(x, top - h, w, h, radius, fill=0, stroke=1)
        c.setFillColor(colors.white)

    def draw(panel, x, top, w, h, color):
        draw_frame(x, top, w, h, color)
        c.setFont('Helvetica-Bold', 9.3)
        c.drawString(x + 8, top - 14.5, panel['title'])
        y = top - 28
        for item in panel['content']:
            y -= item.getSpaceBefore()
            _, ih = item.wrap(w - 16, PAGE_H)
            item.drawOn(c, x + 8, y - ih)
            y -= ih + item.getSpaceAfter()

    rows = [(left[0], right[0], palette[0], palette[2]),
            (left[1], right[1], palette[0], palette[2]),
            (left[2], right[2], palette[1], palette[3])]
    y = PAGE_H - 36 * mm
    heights = [max(measure(a, width), measure(b, width)) for a, b, _, _ in rows]
    # Le dernier encadré réunit l'exemple et les réflexes sur toute la largeur.
    bottom_height = 111
    available = y - 16 * mm - bottom_height - 3 * gap
    if sum(heights) > available:
        raise ValueError(f'Contenu trop haut : {sum(heights):.1f} > {available:.1f}')
    extra = (available - sum(heights)) / 3
    for (a, b, ca, cb), h in zip(rows, heights):
        h += extra
        draw(a, margin, y, width, h, ca)
        draw(b, margin + width + gap, y, width, h, cb)
        y -= h + gap
    panel = right[3]
    full_width = PAGE_W - 2 * margin
    draw_frame(margin, y, full_width, bottom_height, palette[1])
    c.setFont('Helvetica-Bold', 9.3)
    c.drawString(margin + 8, y - 14.5, panel['title'])
    snippet = panel['content'][0]
    _, sh = snippet.wrap(width - 16, PAGE_H)
    snippet.drawOn(c, margin + 8, y - 29 - sh)
    note = panel['content'][1]
    _, nh = note.wrap(width - 20, PAGE_H)
    note.drawOn(c, margin + width + gap + 8, y - 33 - nh)
    c.setFillColor(MUTED)
    c.setFont('Helvetica', 7)
    c.drawString(margin, 9 * mm, 'PYTHON IUT  /  Fiche mémo - Séance 1')
    c.drawRightString(PAGE_W - margin, 9 * mm, 'A4  /  1 page')
    c.showPage()
    c.save()


if __name__ == "__main__":
    build()
