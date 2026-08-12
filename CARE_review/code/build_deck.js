const pptxgen = require("pptxgenjs");

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE";            // 13.3 x 7.5
pres.author = "CARE / ScaleWorks evidence review";
pres.title  = "Scaling High-Impact Nutrition Interventions";

// ---- palette: deep pine + sage, burnt clay accent ------------------------
const PINE   = "1F3D2B";
const PINE_D = "162C1F";
const SAGE   = "5C8A6A";
const SAGE_L = "E8EFE9";
const CLAY   = "C1622F";
const CLAY_L = "F7EAE1";
const INK    = "22282A";
const MUTE   = "6B7671";
const WHITE  = "FFFFFF";

const HEAD = "Cambria";
const BODY = "Calibri";

const W = 13.3, H = 7.5, M = 0.62;

// ---- helpers -------------------------------------------------------------
function shadow() { return { type: "outer", angle: 90, blur: 12, offset: 3, color: "1F3D2B", opacity: 0.13 }; }

function darkSlide() {
  const s = pres.addSlide();
  s.background = { color: PINE };
  return s;
}
function lightSlide() {
  const s = pres.addSlide();
  s.background = { color: WHITE };
  return s;
}

function title(s, text, opts = {}) {
  s.addText(text, {
    x: M, y: opts.y ?? 0.52, w: W - M * 2, h: opts.h ?? 0.85,
    fontFace: HEAD, fontSize: opts.size ?? 32, bold: true,
    color: opts.color ?? PINE, align: "left", valign: "middle", margin: 0,
  });
}
function kicker(s, text, opts = {}) {
  s.addText(text.toUpperCase(), {
    x: M, y: opts.y ?? 0.32, w: W - M * 2, h: 0.26,
    fontFace: BODY, fontSize: 11, bold: true, charSpacing: 2.2,
    color: opts.color ?? CLAY, align: "left", valign: "middle", margin: 0,
  });
}
function source(s, text) {
  s.addText(text, {
    x: M, y: H - 0.66, w: W - M * 2, h: 0.32,
    fontFace: BODY, fontSize: 9, italic: true, color: MUTE, margin: 0, valign: "middle",
  });
}
// numbered badge — the repeated motif
function badge(s, n, x, y, opts = {}) {
  const d = opts.d ?? 0.46;
  s.addShape(pres.ShapeType.ellipse, {
    x, y, w: d, h: d, fill: { color: opts.fill ?? CLAY },
  });
  s.addText(String(n), {
    x, y, w: d, h: d, fontFace: BODY, fontSize: opts.fs ?? 15, bold: true,
    color: opts.color ?? WHITE, align: "center", valign: "middle", margin: 0,
  });
}
function card(s, x, y, w, h, fill) {
  s.addShape(pres.ShapeType.roundRect, {
    x, y, w, h, rectRadius: 0.09,
    fill: { color: fill ?? SAGE_L }, shadow: shadow(),
  });
}

// =========================================================== 1. TITLE
{
  const s = darkSlide();
  // motif: three overlapping rings = the three interventions
  const rings = [[9.55, 1.55], [10.75, 3.05], [9.55, 4.55]];
  rings.forEach(([x, y]) => {
    s.addShape(pres.ShapeType.ellipse, {
      x, y, w: 2.0, h: 2.0, fill: { color: WHITE, transparency: 92 },
      line: { color: SAGE, width: 1.25 },
    });
  });
  s.addText("CMAM", { x: 9.55, y: 1.55, w: 2.0, h: 2.0, fontFace: BODY, fontSize: 13, bold: true, color: WHITE, align: "center", valign: "middle", margin: 0 });
  s.addText("Breast-\nfeeding", { x: 10.75, y: 3.05, w: 2.0, h: 2.0, fontFace: BODY, fontSize: 13, bold: true, color: WHITE, align: "center", valign: "middle", margin: 0 });
  s.addText("MMS", { x: 9.55, y: 4.55, w: 2.0, h: 2.0, fontFace: BODY, fontSize: 13, bold: true, color: WHITE, align: "center", valign: "middle", margin: 0 });

  s.addText("EVIDENCE REVIEW  ·  AUGUST 2026", {
    x: M, y: 1.55, w: 8.4, h: 0.3, fontFace: BODY, fontSize: 12, bold: true,
    charSpacing: 2.4, color: SAGE, margin: 0, valign: "middle",
  });
  s.addText("Scaling High-Impact\nNutrition Interventions", {
    x: M, y: 2.05, w: 8.4, h: 1.9, fontFace: HEAD, fontSize: 40, bold: true,
    color: WHITE, margin: 0, valign: "top", lineSpacing: 46,
  });
  s.addText("CMAM · Breastfeeding Support · Antenatal MMS", {
    x: M, y: 4.05, w: 8.4, h: 0.4, fontFace: BODY, fontSize: 17, color: SAGE_L, margin: 0, valign: "middle",
  });
  s.addText("Prepared for CARE and IA partners — Save the Children and Mercy Corps", {
    x: M, y: 4.62, w: 8.4, h: 0.4, fontFace: BODY, fontSize: 13, italic: true, color: MUTE, margin: 0, valign: "middle",
  });
  s.addNotes("Condensed from the full evidence review. Every number is cited to a source study.");
}

// =========================================================== 2. WHAT WAS ASKED
{
  const s = lightSlide();
  kicker(s, "The brief");
  title(s, "Three interventions, reviewed in depth");
  s.addText("CARE and IA partners narrowed an initial 15-intervention synthesis to three.", {
    x: M, y: 1.36, w: 9.6, h: 0.34, fontFace: BODY, fontSize: 15, color: INK, margin: 0, valign: "middle",
  });

  const items = [
    ["CMAM", "Community-based Management of Acute Malnutrition", "Treating already-malnourished children at home rather than in hospital"],
    ["Breastfeeding", "Promotion and support", "Facility support around delivery, plus community counselling afterwards"],
    ["MMS", "Antenatal Multiple Micronutrient Supplementation", "A daily supplement in pregnancy, replacing iron-folic acid"],
  ];
  items.forEach(([name, full, desc], i) => {
    const x = M + i * 4.12;
    card(s, x, 2.02, 3.86, 2.52, SAGE_L);
    badge(s, i + 1, x + 0.28, 2.28);
    s.addText(name, { x: x + 0.86, y: 2.26, w: 2.8, h: 0.42, fontFace: HEAD, fontSize: 19, bold: true, color: PINE, margin: 0, valign: "middle" });
    s.addText(full, { x: x + 0.28, y: 2.82, w: 3.3, h: 0.6, fontFace: BODY, fontSize: 11, bold: true, color: SAGE, margin: 0, valign: "top" });
    s.addText(desc, { x: x + 0.28, y: 3.44, w: 3.3, h: 0.94, fontFace: BODY, fontSize: 12.5, color: INK, margin: 0, valign: "top" });
  });

  card(s, M, 4.86, W - M * 2, 0.92, CLAY_L);
  s.addText([
    { text: "Cost is out of scope. ", options: { bold: true, color: PINE } },
    { text: "Deliberately and throughout — excluded from searches, extraction and synthesis. It is the subject of a separate phase.", options: { color: INK } },
  ], { x: M + 0.34, y: 4.86, w: W - M * 2 - 0.68, h: 0.92, fontFace: BODY, fontSize: 13.5, margin: 0, valign: "middle" });
}

// =========================================================== 3. HEADLINE
{
  const s = darkSlide();
  kicker(s, "What we found", { color: SAGE });
  s.addText("All three interventions work.\nNone fails on evidence.", {
    x: M, y: 1.35, w: 11.4, h: 1.7, fontFace: HEAD, fontSize: 38, bold: true,
    color: WHITE, margin: 0, valign: "top", lineSpacing: 44,
  });
  s.addText([
    { text: "In every case, the gap between trial performance and programme performance is larger than the gap between the intervention and its comparator.", options: { bold: true, color: SAGE_L } },
  ], { x: M, y: 3.25, w: 11.4, h: 0.8, fontFace: BODY, fontSize: 19, margin: 0, valign: "top", lineSpacing: 27 });

  s.addText("That is the operationalization gap — and it is where the returns are.", {
    x: M, y: 4.18, w: 11.4, h: 0.4, fontFace: BODY, fontSize: 15, italic: true, color: MUTE, margin: 0, valign: "middle",
  });

  s.addShape(pres.ShapeType.roundRect, {
    x: M, y: 5.0, w: 11.4, h: 1.15, rectRadius: 0.09,
    fill: { color: WHITE, transparency: 90 },
  });
  s.addText("This review does not grade the three against one another. They are measured on different outcomes, against different comparators, in literatures at different stages — a common scale would imply a comparability the evidence does not support.", {
    x: M + 0.34, y: 5.0, w: 11.4 - 0.68, h: 1.15, fontFace: BODY, fontSize: 13, color: SAGE_L, margin: 0, valign: "middle",
  });
}

// =========================================================== 4. THE GAP, QUANTIFIED
{
  const s = lightSlide();
  kicker(s, "The operationalization gap");
  title(s, "What programmes actually achieve");

  const stats = [
    ["38.3%", "of malnutrition cases reached", "Across 44 assessments in 21 countries, 2012–13. In Ethiopia — the only country at national scale — recovery fell from 72% to 69% as the programme matured.", "DOI 10.1371/journal.pone.0128666 · PMID 32631260"],
    ["41–46%", "of women take antenatal supplements", "Where adherence has been pooled, in Ethiopia. Rates elsewhere run much higher — 77–82% in parts of north India — so this is a documented problem, not a universal rate.", "DOI 10.1186/s12884-020-2835-0"],
    ["< 70%", "breastfeeding coverage, near-universally", "Below the global target almost everywhere measured. West Africa: exclusive breastfeeding 36.5%, early initiation 48.7%.", "PMID 39764605"],
  ];
  stats.forEach(([big, label, detail, cite], i) => {
    const x = M + i * 4.12;
    card(s, x, 1.72, 3.86, 3.9, i === 0 ? CLAY_L : SAGE_L);
    s.addText(big, { x: x + 0.3, y: 1.95, w: 3.3, h: 1.0, fontFace: HEAD, fontSize: 46, bold: true, color: i === 0 ? CLAY : PINE, margin: 0, valign: "middle" });
    s.addText(label, { x: x + 0.3, y: 3.0, w: 3.3, h: 0.62, fontFace: BODY, fontSize: 13.5, bold: true, color: PINE, margin: 0, valign: "top" });
    s.addText(detail, { x: x + 0.3, y: 3.68, w: 3.3, h: 1.5, fontFace: BODY, fontSize: 11.5, color: INK, margin: 0, valign: "top" });
    s.addText(cite, { x: x + 0.3, y: 5.2, w: 3.3, h: 0.3, fontFace: BODY, fontSize: 8, italic: true, color: MUTE, margin: 0, valign: "top" });
  });

  s.addText("Efficacy is not what is failing. Delivery is.", {
    x: M, y: 5.86, w: W - M * 2, h: 0.44, fontFace: HEAD, fontSize: 18, bold: true, italic: true,
    color: PINE, margin: 0, valign: "middle",
  });
}

// =========================================================== 5. THE THREE, SIDE BY SIDE
{
  const s = lightSlide();
  kicker(s, "Side by side");
  title(s, "What each evidence base shows");

  const rows = [
    [{ text: "", options: {} }, { text: "What the evidence establishes" }, { text: "What it does not show" }, { text: "Binding constraint" }],
    ["CMAM", "Home-based treatment of acute malnutrition works, and how to deliver it", "The size of the benefit against no treatment — never measured, and now unmeasurable", "Coverage: under 40% of cases reached"],
    ["Breastfeeding", "Support works via professionals or peers, and better in LMICs than high-income settings. Kangaroo Mother Care cuts newborn deaths RR 0.68, high certainty", "How the facility and community components hand over to each other", "Contact intensity and coverage"],
    ["MMS", "Outperforms iron-folic acid on low birthweight (RR 0.85), small-for-gestational-age and stillbirth, across very large samples", "Any reduction in perinatal mortality", "Adherence, and effectiveness rather than efficacy evidence"],
  ];
  const table = rows.map((r, ri) =>
    r.map((cell, ci) => {
      const txt = typeof cell === "string" ? cell : (cell.text ?? "");
      if (ri === 0) return { text: txt, options: { bold: true, color: WHITE, fill: { color: PINE }, fontSize: 12 } };
      return {
        text: txt,
        options: {
          bold: ci === 0, color: ci === 0 ? PINE : INK,
          fill: { color: ri % 2 === 0 ? SAGE_L : WHITE }, fontSize: 11.5,
        },
      };
    })
  );
  s.addTable(table, {
    x: M, y: 1.62, w: W - M * 2, colW: [1.95, 4.1, 3.0, 2.96],
    border: { type: "solid", color: "DCE4DD", pt: 0.75 },
    fontFace: BODY, valign: "middle", rowH: [0.42, 1.05, 1.35, 1.15], margin: 0.09,
  });
  source(s, "RR is a risk ratio: 1.00 means no difference, below 1 is fewer events. A bracketed range crossing 1.00 is not statistically significant.");
}

// =========================================================== 6. KMC
{
  const s = lightSlide();
  kicker(s, "Finding 1 of 3 — against intuition");
  title(s, "Kangaroo Mother Care is the strongest result here");

  card(s, M, 1.78, 4.5, 3.7, PINE);
  s.addText("32%", { x: M + 0.3, y: 2.1, w: 3.9, h: 1.35, fontFace: HEAD, fontSize: 68, bold: true, color: WHITE, margin: 0, valign: "middle" });
  s.addText("fewer newborn deaths", { x: M + 0.3, y: 3.42, w: 3.9, h: 0.4, fontFace: BODY, fontSize: 16, bold: true, color: SAGE_L, margin: 0, valign: "middle" });
  s.addText("RR 0.68 (0.53–0.87)\n12 studies · 10,505 infants", { x: M + 0.3, y: 3.94, w: 3.9, h: 0.8, fontFace: BODY, fontSize: 13, color: SAGE, margin: 0, valign: "top", lineSpacing: 19 });
  s.addText("DOI 10.1136/bmjgh-2022-010728", { x: M + 0.3, y: 4.92, w: 3.9, h: 0.3, fontFace: BODY, fontSize: 8.5, italic: true, color: SAGE, margin: 0, valign: "middle" });

  const pts = [
    ["The only high-certainty rating in the review", "Across all three interventions, no other finding carries a formal high-certainty grade."],
    ["No commodity. No equipment.", "Continuous skin-to-skin holding of the newborn — it requires staff time and space, not a supply chain."],
    ["It works in both settings", "Facility-initiated RR 0.62, community-initiated RR 0.71 — which is why the delivery channel is not the choice to make."],
  ];
  pts.forEach(([h, d], i) => {
    const y = 1.86 + i * 1.24;
    badge(s, i + 1, 5.5, y + 0.02, { d: 0.4, fs: 13 });
    s.addText(h, { x: 6.08, y: y - 0.02, w: 6.6, h: 0.4, fontFace: BODY, fontSize: 15, bold: true, color: PINE, margin: 0, valign: "middle" });
    s.addText(d, { x: 6.08, y: y + 0.38, w: 6.6, h: 0.72, fontFace: BODY, fontSize: 12.5, color: INK, margin: 0, valign: "top" });
  });
}

// =========================================================== 7. MMS + SURVIVAL
{
  const s = lightSlide();
  kicker(s, "Finding 2 of 3 — against intuition");
  title(s, "MMS and survival: more mixed than it looks");
  s.addText("A simple summary would say MMS improves birth outcomes but not survival. The evidence separates into three groups of genuinely different strength.", {
    x: M, y: 1.42, w: 11.6, h: 0.56, fontFace: BODY, fontSize: 13.5, color: INK, margin: 0, valign: "middle",
  });

  const rows = [
    [CLAY, "Stillbirth is reduced", "RR 0.91 · 22 studies · N=96,772", "Replicated across four of five large syntheses on samples approaching 100,000 pregnancies. A stillbirth is a death — so this is a survival benefit.", "PMID 37051178"],
    [PINE, "Perinatal mortality is not", "RR 1.00 (0.90–1.11) · 16 studies", "A tight interval centred on no effect. This is a well-powered null — real evidence of no benefit, not an absence of data.", "PMID 32075071"],
    [MUTE, "Maternal & long-term: unknown", "CI 0.71–1.51 and −5.25 to 5.15", "Intervals this wide are compatible with almost anything. Absence of evidence, not evidence of absence — do not cite these as showing no effect.", "PMID 27306908"],
  ];
  rows.forEach(([col, h, stat, d, cite], i) => {
    const y = 2.05 + i * 1.44;
    card(s, M, y, W - M * 2, 1.26, i === 0 ? CLAY_L : SAGE_L);
    s.addShape(pres.ShapeType.ellipse, { x: M + 0.3, y: y + 0.41, w: 0.44, h: 0.44, fill: { color: col } });
    s.addText(h, { x: M + 0.94, y: y + 0.15, w: 3.5, h: 0.44, fontFace: BODY, fontSize: 15.5, bold: true, color: PINE, margin: 0, valign: "middle" });
    s.addText(stat, { x: M + 0.94, y: y + 0.6, w: 3.5, h: 0.4, fontFace: BODY, fontSize: 12, bold: true, color: col, margin: 0, valign: "middle" });
    s.addText(d, { x: M + 4.62, y: y + 0.18, w: 6.2, h: 0.92, fontFace: BODY, fontSize: 12.5, color: INK, margin: 0, valign: "middle" });
    s.addText(cite, { x: W - M - 1.5, y: y + 0.44, w: 1.4, h: 0.4, fontFace: BODY, fontSize: 8.5, italic: true, color: MUTE, margin: 0, valign: "middle", align: "right" });
  });
}

// =========================================================== 8. BF PACKAGES
{
  const s = lightSlide();
  kicker(s, "Finding 3 of 3 — against intuition");
  title(s, "Facility and community are not alternatives");

  const boxW = 4.6;
  card(s, M, 1.9, boxW, 2.5, SAGE_L);
  s.addText("At the facility", { x: M + 0.3, y: 2.12, w: boxW - 0.6, h: 0.4, fontFace: HEAD, fontSize: 18, bold: true, color: PINE, margin: 0, valign: "middle" });
  s.addText([
    { text: "Kangaroo Mother Care", options: { bullet: true, breakLine: true } },
    { text: "Skin-to-skin contact", options: { bullet: true, breakLine: true } },
    { text: "Early initiation within the first hour", options: { bullet: true } },
  ], { x: M + 0.3, y: 2.6, w: boxW - 0.6, h: 1.3, fontFace: BODY, fontSize: 13, color: INK, margin: 0, valign: "top", paraSpaceAfter: 5 });
  s.addText("Supplies the mortality intervention and the birth-moment contact", { x: M + 0.3, y: 3.86, w: boxW - 0.6, h: 0.44, fontFace: BODY, fontSize: 11.5, italic: true, color: SAGE, margin: 0, valign: "middle" });

  s.addShape(pres.ShapeType.rightArrow, { x: M + boxW + 0.32, y: 2.92, w: 0.86, h: 0.46, fill: { color: CLAY } });

  const x2 = M + boxW + 1.5;
  card(s, x2, 1.9, boxW, 2.5, SAGE_L);
  s.addText("Then in the community", { x: x2 + 0.3, y: 2.12, w: boxW - 0.6, h: 0.4, fontFace: HEAD, fontSize: 18, bold: true, color: PINE, margin: 0, valign: "middle" });
  s.addText([
    { text: "CHW-delivered postnatal counselling", options: { bullet: true, breakLine: true } },
    { text: "4–8 contacts — the dose that works", options: { bullet: true, breakLine: true } },
    { text: "Peer support, strongest in LMICs", options: { bullet: true } },
  ], { x: x2 + 0.3, y: 2.6, w: boxW - 0.6, h: 1.3, fontFace: BODY, fontSize: 13, color: INK, margin: 0, valign: "top", paraSpaceAfter: 5 });
  s.addText("Supplies the repeated contact that sustains the behaviour", { x: x2 + 0.3, y: 3.86, w: boxW - 0.6, h: 0.44, fontFace: BODY, fontSize: 11.5, italic: true, color: SAGE, margin: 0, valign: "middle" });

  card(s, M, 4.72, W - M * 2, 1.28, CLAY_L);
  s.addText([
    { text: "Why they combine rather than compete.  ", options: { bold: true, color: PINE } },
    { text: "They act at different moments, deliver different outcomes, and each is insufficient alone — and Kangaroo Mother Care works in both settings, so the channel is not the choice. The untested part is the handover between them.", options: { color: INK } },
  ], { x: M + 0.34, y: 4.72, w: W - M * 2 - 0.68, h: 1.28, fontFace: BODY, fontSize: 13, margin: 0, valign: "middle" });
  source(s, "PMID 36282618 · DOI 10.1136/bmjgh-2022-010728");
}

// =========================================================== 9. THE LEVER
{
  const s = darkSlide();
  kicker(s, "The one lever that recurs", { color: SAGE });
  s.addText("Moving delivery from facilities\nto community health workers", {
    x: M, y: 1.3, w: 11.5, h: 1.7, fontFace: HEAD, fontSize: 36, bold: true, color: WHITE, margin: 0, valign: "top", lineSpacing: 42,
  });
  s.addText("It appears in all three interventions — the closest thing to a transferable finding in this review.", {
    x: M, y: 3.12, w: 11.5, h: 0.62, fontFace: BODY, fontSize: 16, color: SAGE_L, margin: 0, valign: "middle",
  });

  const cols = [
    ["Malnutrition treatment", "Large coverage gains in Mali, Tanzania and Mauritania"],
    ["Breastfeeding", "Home visits cut newborn deaths — but only when CHWs deliver them"],
    ["Supplementation", "Central to Nepal's national coverage rise"],
  ];
  cols.forEach(([h, d], i) => {
    const x = M + i * 3.88;
    s.addShape(pres.ShapeType.roundRect, { x, y: 3.95, w: 3.62, h: 1.72, rectRadius: 0.09, fill: { color: WHITE, transparency: 90 } });
    s.addText(h, { x: x + 0.28, y: 4.14, w: 3.06, h: 0.4, fontFace: BODY, fontSize: 14, bold: true, color: WHITE, margin: 0, valign: "middle" });
    s.addText(d, { x: x + 0.28, y: 4.58, w: 3.06, h: 0.94, fontFace: BODY, fontSize: 12, color: SAGE_L, margin: 0, valign: "top" });
  });
  s.addText("Stated precisely on the next slide — the detail changes what you can claim.", {
    x: M, y: 6.0, w: 11.5, h: 0.4, fontFace: BODY, fontSize: 12.5, italic: true, color: MUTE, margin: 0, valign: "middle",
  });
}

// =========================================================== 10. THE LEVER, PRECISELY
{
  const s = lightSlide();
  kicker(s, "The same lever, stated precisely");
  title(s, "What each case actually shows");

  const cases = [
    ["Mali", "28.7% → 57.1%", "and 20.4% → 61.1% in a second district", "But no change in a third (28.4% → 28.5%). The authors attribute the difference to where workers were placed relative to underserved populations.", "DOI 10.1186/s12960-022-00771-8"],
    ["Tanzania", "80.9% vs 41.7%", "CHW home treatment vs comparison area", "A comparison between two areas, not a before-and-after — and a non-randomised pilot.", "DOI 10.1038/s41598-021-81811-6"],
    ["Nepal", "23% → 91%", "national supplement coverage, 2001–2016", "The rise closely tracked antenatal coverage, which went from 49% to 94% over the same period. The volunteers cannot be credited alone.", "DOI 10.1111/mcn.13173"],
  ];
  cases.forEach(([c, big, sub, caveat, cite], i) => {
    const x = M + i * 4.12;
    card(s, x, 1.68, 3.86, 4.0, WHITE);
    s.addShape(pres.ShapeType.roundRect, { x, y: 1.68, w: 3.86, h: 0.92, rectRadius: 0.09, fill: { color: PINE } });
    s.addText(c, { x: x + 0.3, y: 1.68, w: 3.26, h: 0.92, fontFace: HEAD, fontSize: 20, bold: true, color: WHITE, margin: 0, valign: "middle" });
    s.addText(big, { x: x + 0.3, y: 2.76, w: 3.26, h: 0.6, fontFace: HEAD, fontSize: 26, bold: true, color: CLAY, margin: 0, valign: "middle" });
    s.addText(sub, { x: x + 0.3, y: 3.36, w: 3.26, h: 0.5, fontFace: BODY, fontSize: 11.5, color: MUTE, margin: 0, valign: "top" });
    s.addText([
      { text: "Caveat.  ", options: { bold: true, color: CLAY } },
      { text: caveat, options: { color: INK } },
    ], { x: x + 0.3, y: 3.94, w: 3.26, h: 1.42, fontFace: BODY, fontSize: 11.5, margin: 0, valign: "top" });
    s.addText(cite, { x: x + 0.3, y: 5.32, w: 3.26, h: 0.28, fontFace: BODY, fontSize: 8, italic: true, color: MUTE, margin: 0, valign: "middle" });
  });

  s.addText("The direction is consistent. The magnitude is not — and it depends on placement.", {
    x: M, y: 5.9, w: W - M * 2, h: 0.42, fontFace: HEAD, fontSize: 17, bold: true, italic: true, color: PINE, margin: 0, valign: "middle",
  });
}

// =========================================================== 11. QUALIFICATIONS
{
  const s = lightSlide();
  kicker(s, "Three qualifications travel with it");
  title(s, "Where the lever does not hold");

  const qs = [
    ["Coverage gains are not quality gains", "In Pakistan, community-delivered treatment achieved lower recovery than facility care — 76.0% against 82.95%.", "DOI 10.1186/s12889-018-6382-9"],
    ["Finding people is not treating them", "A Mali programme raised screening coverage 40 percentage points while treatment coverage stayed at 7.6%.", "DOI 10.1371/journal.pmed.1002892"],
    ["These cadres are already overloaded", "Frequently unpaid, and carrying family planning, immunisation and emergency response. Adding a mandate is a design risk, not a free win.", ""],
  ];
  qs.forEach(([h, d, cite], i) => {
    const y = 1.82 + i * 1.42;
    card(s, M, y, W - M * 2, 1.24, i % 2 === 0 ? SAGE_L : WHITE);
    badge(s, i + 1, M + 0.34, y + 0.39, { d: 0.46 });
    s.addText(h, { x: M + 1.02, y: y + 0.14, w: 4.5, h: 0.46, fontFace: BODY, fontSize: 15.5, bold: true, color: PINE, margin: 0, valign: "middle" });
    s.addText(d, { x: M + 1.02, y: y + 0.58, w: 8.0, h: 0.58, fontFace: BODY, fontSize: 12.5, color: INK, margin: 0, valign: "top" });
    if (cite) s.addText(cite, { x: W - M - 2.5, y: y + 0.42, w: 2.4, h: 0.4, fontFace: BODY, fontSize: 8.5, italic: true, color: MUTE, margin: 0, valign: "middle", align: "right" });
  });
  source(s, "Any coverage target should specify whether it means finding people or treating them, and should be paired with a quality measure.");
}

// =========================================================== 12. THREE OPTIONS
{
  const s = lightSlide();
  kicker(s, "Three packaged options");
  title(s, "What the evidence supports as coherent packages");

  const head = ["", "A — Facility newborn", "B — Community treatment", "C — Antenatal commodity"];
  const body = [
    ["What it is", "KMC, skin-to-skin and early initiation at the facility, then community counselling at 4–8 contacts", "Malnutrition treatment decentralised to CHWs, simplified protocol, plus supervision and supply chain", "Switching antenatal supplements from iron-folic acid to MMS, with contact and counselling intensification"],
    ["Scaling position", "Health-system platform + behavioural", "Health-system treatment", "Commodity"],
    ["Strongest evidence", "Mortality, high certainty (RR 0.68)", "Large coverage gains, replicated", "Birth outcomes, settled (RR 0.73–0.85)"],
    ["Mortality benefit?", "Yes", "Indirectly — treats a condition with ~11% case fatality", "Stillbirth only"],
    ["Channel exists?", "Partly", "Rarely — only Ethiopia at national scale", "Yes — replaces an existing commodity"],
    ["Hardest part", "Facility coverage", "Quality and supply at scale", "Adherence"],
  ];
  const table = [head.map((h, ci) => ({
    text: h, options: { bold: true, color: WHITE, fill: { color: ci === 0 ? PINE : PINE }, fontSize: 12.5 },
  }))].concat(body.map((r, ri) => r.map((cell, ci) => ({
    text: cell,
    options: {
      bold: ci === 0, color: ci === 0 ? PINE : INK,
      fill: { color: ri % 2 === 0 ? SAGE_L : WHITE }, fontSize: 11,
    },
  }))));
  s.addTable(table, {
    x: M, y: 1.6, w: W - M * 2, colW: [1.85, 3.4, 3.4, 3.41],
    border: { type: "solid", color: "DCE4DD", pt: 0.75 },
    fontFace: BODY, valign: "middle", rowH: [0.4, 1.0, 0.52, 0.62, 0.62, 0.62, 0.42], margin: 0.08,
  });
  source(s, "They map onto the three scaling positions partners chose these interventions to test.");
}

// =========================================================== 13. CHOOSING
{
  const s = lightSlide();
  kicker(s, "Choosing between them");
  title(s, "Three observations that should drive the decision");

  const obs = [
    ["They are not equally novel", "Option C is a substitution into an existing channel. Option B often means building a service that does not yet exist. That difference matters more for feasibility than any effect size in this review.", CLAY],
    ["A and B compete for the same cadre", "Both load community health workers — one with postnatal visits, one with treatment. Running both is the highest-risk configuration here, and should be costed as a workforce expansion, not an add-on.", PINE],
    ["Only A carries high-certainty mortality", "If the objective is deaths averted on the firmest evidence, that is the discriminating fact. If it is reach, B addresses the largest coverage gap. If it is a fast tractable win, C is least disruptive.", SAGE],
  ];
  obs.forEach(([h, d, col], i) => {
    const x = M + i * 4.12;
    card(s, x, 1.82, 3.86, 3.42, WHITE);
    s.addShape(pres.ShapeType.ellipse, { x: x + 0.3, y: 2.1, w: 0.52, h: 0.52, fill: { color: col } });
    s.addText(String.fromCharCode(65 + i), { x: x + 0.3, y: 2.1, w: 0.52, h: 0.52, fontFace: BODY, fontSize: 17, bold: true, color: WHITE, align: "center", valign: "middle", margin: 0 });
    s.addText(h, { x: x + 0.3, y: 2.78, w: 3.26, h: 0.76, fontFace: HEAD, fontSize: 17, bold: true, color: PINE, margin: 0, valign: "top", lineSpacing: 21 });
    s.addText(d, { x: x + 0.3, y: 3.62, w: 3.26, h: 1.42, fontFace: BODY, fontSize: 12, color: INK, margin: 0, valign: "top" });
  });

  card(s, M, 5.5, W - M * 2, 0.82, CLAY_L);
  s.addText("Note that these options are not a menu of equals — they answer different objectives.", {
    x: M + 0.34, y: 5.5, w: W - M * 2 - 0.68, h: 0.82, fontFace: BODY, fontSize: 13.5, bold: true, color: PINE, margin: 0, valign: "middle",
  });
}

// =========================================================== 14. COMBINING
{
  const s = lightSlide();
  kicker(s, "Can interventions be combined?");
  title(s, "Partly — and less than partners may hope");

  card(s, M, 1.76, 5.9, 1.28, PINE);
  s.addText([
    { text: "173", options: { fontSize: 26, bold: true, color: WHITE, fontFace: HEAD } },
    { text: "  of 648 records discuss combination — but only  ", options: { fontSize: 13.5, color: SAGE_L } },
    { text: "9", options: { fontSize: 26, bold: true, color: CLAY, fontFace: HEAD } },
    { text: "  actually test one", options: { fontSize: 13.5, color: SAGE_L } },
  ], { x: M + 0.34, y: 1.76, w: 5.22, h: 1.28, fontFace: BODY, margin: 0, valign: "middle" });

  card(s, M, 3.22, 5.9, 2.32, SAGE_L);
  s.addText("Well evidenced", { x: M + 0.34, y: 3.40, w: 5.22, h: 0.4, fontFace: HEAD, fontSize: 18, bold: true, color: PINE, margin: 0, valign: "middle" });
  s.addText([
    { text: "Combining within an intervention — simplified protocols merging severe and moderate treatment; the facility-plus-community breastfeeding configuration", options: { bullet: true, breakLine: true } },
    { text: "Pairing with a demand-side mechanism — cash added to treatment improved recovery (HR 1.35) and cut relapse (HR 0.21); women's groups plus cash raised supplement consumption 2.5–4.6 fold in Nepal", options: { bullet: true } },
  ], { x: M + 0.34, y: 3.86, w: 5.22, h: 1.6, fontFace: BODY, fontSize: 11.5, color: INK, margin: 0, valign: "top", paraSpaceAfter: 7 });

  const x2 = M + 6.2;
  card(s, x2, 1.76, 5.86, 3.78, CLAY_L);
  s.addText("Not evidenced — and one warning", { x: x2 + 0.34, y: 1.98, w: 5.18, h: 0.4, fontFace: HEAD, fontSize: 18, bold: true, color: PINE, margin: 0, valign: "middle" });
  s.addText("No trial in our corpus combines the three interventions with each other.", {
    x: x2 + 0.34, y: 2.46, w: 5.18, h: 0.5, fontFace: BODY, fontSize: 12.5, color: INK, margin: 0, valign: "top",
  });
  s.addShape(pres.ShapeType.roundRect, { x: x2 + 0.34, y: 3.04, w: 5.18, h: 2.3, rectRadius: 0.08, fill: { color: WHITE } });
  s.addText([
    { text: "Integration backfired once.  ", options: { bold: true, color: CLAY } },
    { text: "Adding supplements to community screening in Mali raised screening coverage 40 percentage points — but produced no improvement in treatment coverage, and ", options: { color: INK } },
    { text: "reduced enrolment", options: { bold: true, color: INK } },
    { text: " in the malnutrition programme it was added to.", options: { color: INK } },
  ], { x: x2 + 0.62, y: 3.2, w: 4.62, h: 1.5, fontFace: BODY, fontSize: 12.5, margin: 0, valign: "top" });
  s.addText("DOI 10.1371/journal.pmed.1002892", { x: x2 + 0.62, y: 4.82, w: 4.62, h: 0.3, fontFace: BODY, fontSize: 8.5, italic: true, color: MUTE, margin: 0, valign: "middle" });

  card(s, M, 5.74, W - M * 2, 0.78, WHITE);
  s.addText([
    { text: "Bundling is not additive.  ", options: { bold: true, color: PINE } },
    { text: "Adding a task to a community platform can displace an existing one. Any combined design should treat “does enrolment in the existing service hold?” as a measured outcome.", options: { color: INK } },
  ], { x: M + 0.34, y: 5.74, w: W - M * 2 - 0.68, h: 0.78, fontFace: BODY, fontSize: 13, margin: 0, valign: "middle" });
}

// =========================================================== 15. COUNTRIES
{
  const s = lightSlide();
  kicker(s, "Where — countries");
  title(s, "Eleven countries carry evidence across all three");

  const cs = [
    ["Ethiopia", "The only country where all three interventions already run through a single government community platform — roughly 40,000 Health Extension Workers. Also where the quality problem is best documented: recovery fell as the programme matured."],
    ["India", "The densest formal platform architecture and live national missions. Failures documented in inter-sectoral coordination and frontline-worker incentives rather than in platform existence."],
    ["Nepal", "The clearest national coverage turnaround in the corpus — and its own literature proposes that platform for the iron-folic-acid-to-MMS switch."],
    ["Pakistan", "A national MMS commitment already made — and the sharpest counter-signal, where community-delivered treatment under-performed facility care."],
  ];
  cs.forEach(([c, d], i) => {
    const x = M + (i % 2) * 6.2;
    const y = 1.72 + Math.floor(i / 2) * 1.72;
    card(s, x, y, 5.86, 1.54, i % 2 === 0 ? SAGE_L : WHITE);
    s.addText(c, { x: x + 0.32, y: y + 0.16, w: 5.2, h: 0.4, fontFace: HEAD, fontSize: 18, bold: true, color: PINE, margin: 0, valign: "middle" });
    s.addText(d, { x: x + 0.32, y: y + 0.58, w: 5.2, h: 0.86, fontFace: BODY, fontSize: 11.5, color: INK, margin: 0, valign: "top" });
  });

  s.addText("Bangladesh, Kenya, Ghana, Malawi, Niger, Indonesia and Nigeria all carry enough evidence to describe.", {
    x: M, y: 5.2, w: W - M * 2, h: 0.36, fontFace: BODY, fontSize: 12.5, color: INK, margin: 0, valign: "middle",
  });
  card(s, M, 5.64, W - M * 2, 0.86, CLAY_L);
  s.addText([
    { text: "Read country evidence volume as research attention, not suitability.  ", options: { bold: true, color: PINE } },
    { text: "A country appears prominently because it has been studied.", options: { color: INK } },
  ], { x: M + 0.34, y: 5.64, w: W - M * 2 - 0.68, h: 0.86, fontFace: BODY, fontSize: 13, margin: 0, valign: "middle" });
}

// =========================================================== 16. WHAT WOULD SETTLE IT
{
  const s = darkSlide();
  kicker(s, "What would settle the choice", { color: SAGE });
  s.addText("None of this is in the corpus", {
    x: M, y: 1.14, w: 11.5, h: 0.9, fontFace: HEAD, fontSize: 34, bold: true, color: WHITE, margin: 0, valign: "middle",
  });
  s.addText("In rough order of decisiveness — these are relationship, operational and financing questions, not evidence questions.", {
    x: M, y: 2.08, w: 11.5, h: 0.56, fontFace: BODY, fontSize: 14.5, color: SAGE_L, margin: 0, valign: "middle",
  });

  const fs = ["Government appetite and current policy windows", "CARE and IA operational footprint", "Fragility and security", "The financing landscape", "Cost"];
  fs.forEach((f, i) => {
    const y = 2.74 + i * 0.62;
    badge(s, i + 1, M, y, { d: 0.42, fs: 13 });
    s.addText(f, { x: M + 0.62, y, w: 7.4, h: 0.42, fontFace: BODY, fontSize: 15.5, color: WHITE, margin: 0, valign: "middle" });
  });

  s.addShape(pres.ShapeType.roundRect, { x: 8.5, y: 2.74, w: 4.18, h: 2.5, rectRadius: 0.09, fill: { color: WHITE, transparency: 88 } });
  s.addText("A practical route", { x: 8.82, y: 2.96, w: 3.54, h: 0.4, fontFace: HEAD, fontSize: 17, bold: true, color: WHITE, margin: 0, valign: "middle" });
  s.addText("Pick three or four countries where partners already have a footprint, and assess those against the factors on the left with partner input.", {
    x: 8.82, y: 3.44, w: 3.54, h: 1.6, fontFace: BODY, fontSize: 13, color: SAGE_L, margin: 0, valign: "top",
  });

  s.addText("This review does not score, rank or recommend a country. The corpus supports description, not ordering.", {
    x: M, y: 6.14, w: 11.5, h: 0.4, fontFace: BODY, fontSize: 12.5, italic: true, color: MUTE, margin: 0, valign: "middle",
  });
}

// =========================================================== 17. TRUST + SCOPE
{
  const s = lightSlide();
  kicker(s, "Scope and confidence");
  title(s, "How far to trust this");

  card(s, M, 1.76, 5.9, 2.28, PINE);
  s.addText("0", { x: M + 0.34, y: 1.98, w: 1.4, h: 1.0, fontFace: HEAD, fontSize: 58, bold: true, color: CLAY, margin: 0, valign: "middle" });
  s.addText("claims that cannot be traced\nto a corpus record", { x: M + 1.8, y: 2.06, w: 3.76, h: 0.86, fontFace: BODY, fontSize: 14, bold: true, color: WHITE, margin: 0, valign: "middle", lineSpacing: 19 });
  s.addText("Every numeric claim traces to a specific record in an evidence database built only from the retrieved corpus. An automated verifier checks each cited number against its source.", {
    x: M + 0.34, y: 3.06, w: 5.22, h: 0.86, fontFace: BODY, fontSize: 12, color: SAGE_L, margin: 0, valign: "top",
  });

  const x2 = M + 6.2;
  card(s, x2, 1.76, 5.86, 2.28, CLAY_L);
  s.addText("What that does not establish", { x: x2 + 0.34, y: 1.96, w: 5.18, h: 0.4, fontFace: HEAD, fontSize: 17, bold: true, color: PINE, margin: 0, valign: "middle" });
  s.addText([
    { text: "That the source study is correct", options: { bullet: true, breakLine: true } },
    { text: "That a pooled estimate is well-constructed", options: { bullet: true, breakLine: true } },
    { text: "That our interpretation is the only reasonable one", options: { bullet: true } },
  ], { x: x2 + 0.34, y: 2.42, w: 5.18, h: 1.4, fontFace: BODY, fontSize: 12.5, color: INK, margin: 0, valign: "top", paraSpaceAfter: 5 });

  card(s, M, 4.24, W - M * 2, 1.0, SAGE_L);
  s.addText([
    { text: "A known limit.  ", options: { bold: true, color: PINE } },
    { text: "Retrieval draws on PubMed and OpenAlex, so grey literature and government programme documentation are under-represented — which matters disproportionately for implementation questions.", options: { color: INK } },
  ], { x: M + 0.34, y: 4.24, w: W - M * 2 - 0.68, h: 1.0, fontFace: BODY, fontSize: 13, margin: 0, valign: "middle" });

  card(s, M, 5.44, W - M * 2, 1.0, WHITE);
  s.addText([
    { text: "Not covered.  ", options: { bold: true, color: CLAY } },
    { text: "Cost and cost-effectiveness, deferred by design — though two findings here are cost findings in disguise: a simplified protocol holds recovery on ~46% less therapeutic food, and cutting that food's dairy content, the main cost driver, measurably worsens recovery. And no country recommendation or ranking.", options: { color: INK } },
  ], { x: M + 0.34, y: 5.44, w: W - M * 2 - 0.68, h: 1.0, fontFace: BODY, fontSize: 12.5, margin: 0, valign: "middle" });
}

const out = "/Users/akashshaji/Documents/GitHub/nutri-evidence-review/CARE_review/CARE_DEEPDIVE_DECK.pptx";
pres.writeFile({ fileName: out }).then(() => console.log("wrote " + out));
