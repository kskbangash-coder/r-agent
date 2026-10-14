"""Build the NSP KPK Part III presentation (initial slides: Improving What Is In Place,
the nine aspects, and Afghanistan).

Sources (NSP KPK folder on Google Drive):
  - 140419 Oct - NSP KPK Part III - Conclusions Only (struck items excluded)
  - 131958 Oct - NSP KPK Part III - Abridged (data notes 3 and 4 only)

Run: python build_deck.py  (requires python-pptx)
"""

from pathlib import Path

from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls
from pptx.util import Inches, Pt

OUT = Path(__file__).with_name("NSP_KPK_Part_III_Afghanistan_Draft.pptx")

# ---- Design tokens (placeholder until the master .pptx is applied) ----
FONT = "Calibri"
NAVY = RGBColor(0x1B, 0x36, 0x5D)
TEAL = RGBColor(0x00, 0x85, 0x7C)
TEXT = RGBColor(0x1D, 0x29, 0x39)
GREY_TXT = RGBColor(0x66, 0x70, 0x85)
LIGHT = RGBColor(0xF2, 0xF4, 0xF7)
MID = RGBColor(0xD0, 0xD5, 0xDD)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

BODY = 15       # body text (pt)
HEAD = 18       # slide headings, maximum (pt)
STAT = 28       # data call-outs only (pt)
FOOT = 11       # source lines (pt)

ASPECTS = [
    ("Afghanistan", "The border can be a gauge instead of a switch"),
    ("Political", "The merger can be a contract instead of an event"),
    ("People", "Youth can be a workforce instead of a risk"),
    ("Civil Administration", "Posts can move forward before new ones are built"),
    ("Narrative and Information", "Pashto content can be a craft instead of a defence"),
    ("Technology, Intelligence and Information",
     "A connected population can be a channel instead of a target"),
    ("Economy", "Provincial resources can be a local stake instead of a dispute"),
    ("Military and LEAs", "Operations can end in convictions instead of clearances"),
    ("Articles 232 and 234", "The emergency can be a ladder instead of a pause"),
]
SHORT_NAMES = ["Afghanistan", "Political", "People", "Civil Admin", "Narrative",
               "Technology", "Economy", "Military and LEAs", "Articles 232 and 234"]

SRC_CONCL = "Source: NSP KPK Part III Conclusions"

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]


# ---------------- helpers ----------------
def _style_run(run, size, bold=False, color=TEXT):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color


def _fill_text(tf, paras, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE):
    """paras: list of (text, size, bold, color) tuples."""
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for i, (text, size, bold, color) in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_after = Pt(4)
        r = p.add_run()
        r.text = text
        _style_run(r, size, bold, color)


def box(slide, x, y, w, h, paras, fill=LIGHT, line=None, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
        align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.MIDDLE, margin=0.12):
    """Shape with its text inside the shape (no overlaid text boxes)."""
    s = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        s.adjustments[0] = 0.08
    s.shadow.inherit = False
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    if line is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = line
        s.line.width = Pt(1)
    tf = s.text_frame
    tf.margin_left = tf.margin_right = Inches(margin)
    tf.margin_top = tf.margin_bottom = Inches(0.06)
    _fill_text(tf, paras, align=align, anchor=anchor)
    return s


def arrow(slide, x, y, w=0.4, h=0.32, fill=MID):
    s = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, Inches(x), Inches(y), Inches(w), Inches(h))
    s.shadow.inherit = False
    s.fill.solid()
    s.fill.fore_color.rgb = fill
    s.line.fill.background()
    return s


def text(slide, x, y, w, h, paras, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.margin_left = tf.margin_right = Inches(0.02)
    _fill_text(tf, paras, align=align, anchor=anchor)
    return tb


def header(slide, label, title):
    text(slide, 0.6, 0.38, 12.1, 0.35, [(label, BODY, True, TEAL)])
    text(slide, 0.6, 0.72, 12.1, 0.6, [(title, HEAD, True, NAVY)])


def footer(slide, source=SRC_CONCL):
    text(slide, 0.6, 6.95, 12.1, 0.3, [(source, FOOT, False, GREY_TXT)])


def notes(slide, body):
    slide.notes_slide.notes_text_frame.text = body


def aspect_strip(slide, active=0, y=1.55, h=0.8):
    """Nine aspect tiles across the top, with the active aspect highlighted."""
    gap = 0.1
    w = (12.1 - gap * 8) / 9
    tiles = []
    for i, name in enumerate(SHORT_NAMES):
        on = i == active
        tiles.append(box(slide, 0.6 + i * (w + gap), y, w, h,
                         [(name, BODY, on, WHITE if on else GREY_TXT)],
                         fill=TEAL if on else LIGHT, align=PP_ALIGN.CENTER, margin=0.05))
    return tiles


def add_click_steps(slide, steps):
    """Fade entrance, one On Click step per list element; shapes in a step appear together."""
    counter = [2]

    def nid():
        counter[0] += 1
        return counter[0]

    pars, bld = [], []
    for step in steps:
        outer, inner = nid(), nid()
        effects = []
        for k, shp in enumerate(step):
            sid = shp.shape_id
            node = "clickEffect" if k == 0 else "withEffect"
            e, s, a = nid(), nid(), nid()
            effects.append(
                f'<p:par><p:cTn id="{e}" presetID="10" presetClass="entr" presetSubtype="0" '
                f'fill="hold" grpId="0" nodeType="{node}"><p:stCondLst><p:cond delay="0"/>'
                f'</p:stCondLst><p:childTnLst><p:set><p:cBhvr><p:cTn id="{s}" dur="1" fill="hold">'
                f'<p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="{sid}"/>'
                f'</p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>'
                f'</p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>'
                f'<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{a}" dur="400"/>'
                f'<p:tgtEl><p:spTgt spid="{sid}"/></p:tgtEl></p:cBhvr></p:animEffect>'
                f'</p:childTnLst></p:cTn></p:par>')
            if shp.has_chart:
                bld.append(f'<p:bldGraphic spid="{sid}" grpId="0"><p:bldAsOne/></p:bldGraphic>')
            else:
                bld.append(f'<p:bldP spid="{sid}" grpId="0" animBg="1"/>')
        pars.append(
            f'<p:par><p:cTn id="{outer}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/>'
            f'</p:stCondLst><p:childTnLst><p:par><p:cTn id="{inner}" fill="hold"><p:stCondLst>'
            f'<p:cond delay="0"/></p:stCondLst><p:childTnLst>{"".join(effects)}</p:childTnLst>'
            f'</p:cTn></p:par></p:childTnLst></p:cTn></p:par>')

    xml = (
        f'<p:timing {nsdecls("p")}><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" '
        f'nodeType="tmRoot"><p:childTnLst><p:seq concurrent="1" nextAc="seek"><p:cTn id="2" '
        f'dur="indefinite" nodeType="mainSeq"><p:childTnLst>{"".join(pars)}</p:childTnLst></p:cTn>'
        f'<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond>'
        f'</p:prevCondLst><p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/>'
        f'</p:tgtEl></p:cond></p:nextCondLst></p:seq></p:childTnLst></p:cTn></p:par></p:tnLst>'
        f'<p:bldLst>{"".join(bld)}</p:bldLst></p:timing>')
    slide._element.append(parse_xml(xml))


# ---------------- slide 1: title ----------------
s = prs.slides.add_slide(BLANK)
band = box(s, 0, 0, 0.35, 7.5, [("", BODY, False, WHITE)], fill=NAVY, shape=MSO_SHAPE.RECTANGLE)
text(s, 1.0, 2.1, 11.0, 0.4, [("PART III | NORMALISING THE SECURITY SITUATION OF KPK", BODY, True, TEAL)])
text(s, 1.0, 2.6, 11.0, 0.9, [("Transmutation: Challenges into Opportunities", HEAD, True, NAVY)])
text(s, 1.0, 3.2, 11.0, 0.9, [("From the way things are, to a change of direction", BODY, False, GREY_TXT)])
notes(s, "Cover. Part III of the NSP KPK paper. Initial slides cover the framing, the nine aspects, "
         "and the Afghanistan aspect.")

# ---------------- slide 2: improving what is in place ----------------
s = prs.slides.add_slide(BLANK)
header(s, "PART III | IMPROVING WHAT IS IN PLACE",
       "Same effort, more yield, with a change of direction")
statement = text(s, 0.6, 1.55, 12.1, 0.9, [
    ("Most required actions are already in place.", BODY, True, TEXT),
    ("The position remains that a whole of nation effort is the most workable answer.", BODY, False, TEXT),
])
verbs = [("Flip", "Turn a threat's energy into an input"),
         ("Direct", "Steer existing activity towards a lawful channel"),
         ("Activate", "Use structures that exist on paper"),
         ("Learn", "Take a lesson from each result")]
vw, vg = 2.65, 0.5
verb_shapes = []
for i, (name, desc) in enumerate(verbs):
    x = 0.6 + i * (vw + vg)
    verb_shapes.append(box(s, x, 2.75, vw, 1.9,
                           [(name, HEAD, True, WHITE if i == 0 else NAVY),
                            (desc, BODY, False, WHITE if i == 0 else TEXT)],
                           fill=TEAL if i == 0 else LIGHT, align=PP_ALIGN.LEFT))
    if i < 3:
        arrow(s, x + vw + 0.1, 3.5, w=0.3, h=0.32)
fw_label = text(s, 0.6, 5.0, 12.1, 0.4, [("The Framework: each point follows one construct", BODY, True, TEAL)])
fw_boxes = []
fw = [("Challenge", "What was treated as a problem"), ("What it can be", "The reframed possibility"),
      ("Opportunity", "The gain, with a fact or lesson")]
fw_w, fw_g = 3.4, 0.95
for i, (name, desc) in enumerate(fw):
    x = 0.6 + i * (fw_w + fw_g)
    fw_boxes.append(box(s, x, 5.45, fw_w, 1.1, [(name, BODY, True, NAVY), (desc, BODY, False, TEXT)],
                        fill=LIGHT))
    if i < 2:
        arrow(s, x + fw_w + 0.3, 5.87, w=0.35, h=0.32)
footer(s)
add_click_steps(s, [[statement], [verb_shapes[0]], [verb_shapes[1]], [verb_shapes[2]],
                    [verb_shapes[3]], [fw_label] + fw_boxes])
notes(s, "Improving what is in place. Four verbs steer the change: Flip, Direct, Activate, Learn. "
         "The Framework is applied to every field: challenge, what it can be, opportunity.")

# ---------------- slide 3: nine aspects ----------------
s = prs.slides.add_slide(BLANK)
header(s, "PART III | NINE ASPECTS IN FOCUS",
       "Nine aspects, from Afghanistan to Articles 232 and 234")
cw, ch, cg = 3.9, 1.4, 0.2
rows = []
card_by_row = [[], [], []]
for i, (name, desc) in enumerate(ASPECTS):
    r, c = divmod(i, 3)
    x = 0.6 + c * (cw + cg)
    y = 1.65 + r * (ch + 0.2)
    on = i == 0
    shp = box(s, x, y, cw, ch,
              [(f"{i + 1}  {name}", BODY, True, WHITE if on else NAVY),
               (desc, BODY, False, WHITE if on else TEXT)],
              fill=TEAL if on else LIGHT)
    card_by_row[r].append(shp)
footer(s)
add_click_steps(s, [card_by_row[0], card_by_row[1], card_by_row[2]])
notes(s, "Nine aspects are the focus. Afghanistan is the first and is discussed in the next slides. "
         "Each card's sub-line is the headline of that aspect in the Conclusions document.")

# ---------------- slide 4: Afghanistan overview ----------------
s = prs.slides.add_slide(BLANK)
header(s, "PART III | AFGHANISTAN, 4 MAJOR TAKEAWAYS",
       "Afghanistan: the border can be a gauge instead of a switch")
strip = aspect_strip(s, active=0)
takeaways = [
    ("Takeaway 1", "Border Trade Gauge",
     "Quota, conduct, surety, conditions, venue and rule can turn the border into a gauge "
     "that answers to measured conduct."),
    ("Takeaway 2", "People and Access",
     "Kin and patients have been seen as a risk or a burden. A managed channel keeps kinship "
     "and care inside lawful, checked paths and earns goodwill."),
    ("Takeaway 3", "Dialogue and Verification",
     "Talks have rested on assurances. Custom, an independent verifier and area language give "
     "dialogue a structure that Pakistan can stand behind."),
    ("Takeaway 4", "Connectivity and Shared Risk",
     "Connectivity has been a reward after stability. Humanitarian data and a first segment "
     "inside Pakistan make it a shared interest that starts now."),
]
tw, tg = 2.85, 0.233
t_cards = []
for i, (lab, name, body) in enumerate(takeaways):
    x = 0.6 + i * (tw + tg)
    t_cards.append(box(s, x, 2.7, tw, 3.9,
                       [(lab, BODY, True, TEAL), (name, HEAD, True, NAVY), (body, BODY, False, TEXT)],
                       fill=LIGHT, anchor=MSO_ANCHOR.TOP, margin=0.18))
footer(s)
add_click_steps(s, [strip] + [[c] for c in t_cards])
notes(s, "Afghanistan is the first of nine aspects. Four major takeaways are discussed one per slide. "
         "Takeaway 1 is supported by figures; takeaways 2 to 4 are framed as shifts in how the issue is treated.")

# ---------------- slide 5: takeaway 1, border trade gauge ----------------
s = prs.slides.add_slide(BLANK)
header(s, "PART III | AFGHANISTAN, TAKEAWAY 1 OF 4",
       "Border trade gauge: the border has been run as a switch")
aspect_strip(s, active=0)

chart_title = text(s, 0.6, 2.7, 5.6, 0.4, [("Exports to Afghanistan, USD billion", BODY, True, NAVY)])
cd = CategoryChartData()
cd.categories = ["FY2015", "FY2024-25"]
cd.add_series("Exports to Afghanistan", (1.699, 0.774))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(0.6), Inches(3.1),
                        Inches(5.6), Inches(3.5), cd)
ch_ = gf.chart
ch_.has_legend = False
ch_.font.name = FONT
ch_.font.size = Pt(BODY)
ch_.value_axis.visible = False
ch_.value_axis.has_major_gridlines = False
ch_.category_axis.format.line.color.rgb = MID
plot = ch_.plots[0]
plot.gap_width = 90
plot.has_data_labels = True
dl = plot.data_labels
dl.number_format = '"$"0.00"bn"'
dl.number_format_is_linked = False
dl.position = XL_LABEL_POSITION.OUTSIDE_END
dl.font.size = Pt(BODY)
dl.font.bold = True
ser = plot.series[0]
ser.format.fill.solid()
ser.format.fill.fore_color.rgb = MID
pt = ser.points[1]
pt.format.fill.solid()
pt.format.fill.fore_color.rgb = TEAL

stat_a = box(s, 6.6, 2.7, 2.9, 1.5,
             [("-28%", STAT, True, TEAL),
              ("Bilateral trade, 2024 to 2025 (USD 2.46bn to 1.77bn)", BODY, False, TEXT)],
             fill=LIGHT, align=PP_ALIGN.LEFT)
stat_b = box(s, 9.8, 2.7, 2.9, 1.5,
             [("-54%", STAT, True, TEAL),
              ("Exports to Afghanistan in ten years", BODY, False, TEXT)],
             fill=LIGHT, align=PP_ALIGN.LEFT)
switch = box(s, 6.6, 4.5, 2.75, 1.3,
             [("Switch", BODY, True, NAVY), ("Open or shut, with nothing in between", BODY, False, TEXT)],
             fill=LIGHT)
arr5 = arrow(s, 9.45, 4.97, w=0.6, h=0.32, fill=TEAL)
gauge = box(s, 10.15, 4.5, 2.55, 1.3,
            [("Gauge", BODY, True, WHITE), ("Quota, conduct and published triggers", BODY, False, WHITE)],
            fill=TEAL)
policy = text(s, 6.6, 6.0, 6.1, 0.8, [
    ("Trade policy has swung between full closure and full opening, and each swing fed smugglers.",
     BODY, False, TEXT)])
footer(s, "Source: Part III Abridged, notes 3 and 4 (PIDE and PAJCCI estimates; State Bank of Pakistan "
          "export data FY2015 and FY2024-25)")
add_click_steps(s, [[chart_title, gf], [stat_a, stat_b], [switch, arr5, gauge], [policy]])
notes(s, "Takeaway 1. Exports to Afghanistan fell from USD 1.70bn (FY2015) to USD 0.77bn (FY2024-25), "
         "a 54 per cent fall in ten years. Bilateral trade fell 28 per cent in 2025 on chamber and PIDE "
         "estimates. The switch-to-gauge point is the shift in policy the takeaway argues for.")

# ---------------- slide 6: takeaway 2, people and access ----------------
s = prs.slides.add_slide(BLANK)
header(s, "PART III | AFGHANISTAN, TAKEAWAY 2 OF 4",
       "People and access: kin and patients seen as a risk can become a managed channel")
aspect_strip(s, active=0)
left6 = box(s, 0.6, 2.9, 5.2, 2.7,
            [("Seen as", BODY, True, GREY_TXT),
             ("A risk or a burden", HEAD, True, NAVY),
             ("Kin movement and patients from Afghanistan have been treated as a problem to contain.",
              BODY, False, TEXT)],
            fill=LIGHT, anchor=MSO_ANCHOR.TOP, margin=0.25)
arr6 = arrow(s, 6.0, 4.0, w=1.3, h=0.45, fill=TEAL)
right6 = box(s, 7.5, 2.9, 5.2, 2.7,
             [("Can be", BODY, True, WHITE),
              ("A managed channel", HEAD, True, WHITE),
              ("Keeps kinship and care inside lawful and checked paths, and earns goodwill.",
               BODY, False, WHITE)],
             fill=TEAL, anchor=MSO_ANCHOR.TOP, margin=0.25)
bottom6 = text(s, 0.6, 6.0, 12.1, 0.6, [
    ("The opportunity: goodwill, earned through checked and lawful paths", BODY, True, NAVY)])
footer(s)
add_click_steps(s, [[left6], [arr6, right6], [bottom6]])
notes(s, "Takeaway 2. Framed as a shift in treatment, not as data. The supporting examples in the "
         "Abridged text are struck in the Conclusions document and are not used.")

# ---------------- slide 7: takeaway 3, dialogue and verification ----------------
s = prs.slides.add_slide(BLANK)
header(s, "PART III | AFGHANISTAN, TAKEAWAY 3 OF 4",
       "Dialogue and verification: talks have rested on assurances")
aspect_strip(s, active=0)
left7 = box(s, 0.6, 2.9, 3.4, 2.7,
            [("Talks have rested on", BODY, True, GREY_TXT),
             ("Assurances", HEAD, True, NAVY)],
            fill=LIGHT, anchor=MSO_ANCHOR.MIDDLE, margin=0.25)
arr7a = arrow(s, 4.2, 4.0, w=0.45, h=0.36, fill=TEAL)
inputs7 = []
for i, lab in enumerate(["Custom", "Independent verifier", "Area language"]):
    inputs7.append(box(s, 4.85, 2.9 + i * 0.95, 3.7, 0.75,
                       [(lab, BODY, True, NAVY)], fill=WHITE, line=TEAL))
arr7b = arrow(s, 8.7, 4.0, w=0.45, h=0.36, fill=TEAL)
right7 = box(s, 9.3, 2.9, 3.4, 2.7,
             [("A structure", BODY, True, WHITE),
              ("Pakistan can stand behind", HEAD, True, WHITE)],
             fill=TEAL, anchor=MSO_ANCHOR.MIDDLE, margin=0.25)
footer(s)
add_click_steps(s, [[left7], inputs7, [arr7a, arr7b, right7]])
notes(s, "Takeaway 3. Three inputs turn assurances into a structure. The Doha and Istanbul examples "
         "in the Abridged text are struck in the Conclusions document and are not shown.")

# ---------------- slide 8: takeaway 4, connectivity ----------------
s = prs.slides.add_slide(BLANK)
header(s, "PART III | AFGHANISTAN, TAKEAWAY 4 OF 4",
       "Connectivity and shared risk: a shared interest that starts now")
aspect_strip(s, active=0)
a8 = box(s, 0.6, 3.0, 3.6, 2.3,
         [("Today", BODY, True, GREY_TXT),
          ("Connectivity has been a reward after stability", BODY, False, TEXT)],
         fill=LIGHT, anchor=MSO_ANCHOR.TOP, margin=0.22)
arr8a = arrow(s, 4.3, 3.9, w=0.45, h=0.36, fill=TEAL)
b8 = box(s, 4.85, 3.0, 3.6, 2.3,
         [("Start now", BODY, True, WHITE),
          ("Humanitarian data and a first segment inside Pakistan", BODY, False, WHITE)],
         fill=TEAL, anchor=MSO_ANCHOR.TOP, margin=0.22)
arr8b = arrow(s, 8.55, 3.9, w=0.45, h=0.36, fill=TEAL)
c8 = box(s, 9.1, 3.0, 3.6, 2.3,
         [("Result", BODY, True, NAVY),
          ("A shared interest that starts now", HEAD, True, NAVY)],
         fill=WHITE, line=TEAL, anchor=MSO_ANCHOR.TOP, margin=0.22)
footer(s)
add_click_steps(s, [[a8], [arr8a, b8], [arr8b, c8]])
notes(s, "Takeaway 4. Connectivity moves from a reward after stability to a shared interest that starts "
         "now. The rail cost estimates in the Abridged text are struck in the Conclusions and are not shown.")

prs.save(OUT)
print("saved", OUT)
