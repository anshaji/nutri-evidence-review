---
marp: true
theme: default
paginate: false
size: 16:9
style: |

    @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@400;500;600;700&display=swap');

    :root {
      --navy: #1b365d;
      --mid-blue: #2e5c8a;
      --teal: #0e7c7b;
      --green: #1e7a3c;
      --amber: #b8860b;
      --red: #c0392b;
      --text: #1a1a2e;
      --muted: #5a6c7d;
      --bg: #fafafa;
      --dark-bg: #0f1b2d;
      --alt-row: #edf2f7;
    }

    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Source Serif 4', 'Georgia', serif; color: var(--text); line-height: 1.5; }

    .slide { width: 100%; height: 100%; margin: 0; background: var(--bg); padding: 45px 55px; position: relative; box-shadow: none; overflow: hidden; }
    .slide.dark { background: var(--dark-bg); color: #e0e0e0; }

    .slide-number { position: absolute; bottom: 12px; right: 20px; font-family: 'Inter', sans-serif; font-size: 11px; color: var(--muted); }
    .dark .slide-number { color: #556677; }

    h1 { font-family: 'Inter', sans-serif; font-size: 22px; font-weight: 700; color: var(--navy); border-bottom: 2.5px solid var(--teal); padding-bottom: 8px; margin-bottom: 16px; letter-spacing: 0.3px; }
    .dark h1 { color: #7ec8c8; border-bottom-color: #7ec8c8; }
    h2 { font-family: 'Inter', sans-serif; font-size: 15px; font-weight: 600; color: var(--mid-blue); margin: 12px 0 8px; }
    .dark h2 { color: #7ec8c8; }
    h3 { font-family: 'Inter', sans-serif; font-size: 13px; font-weight: 600; color: var(--teal); margin: 10px 0 6px; }
    p, li { font-size: 13px; line-height: 1.55; }
    .small { font-size: 11.5px; }
    .footnote { font-size: 10.5px; color: var(--muted); font-style: italic; margin-top: 8px; }
    .fig-caption { font-family: 'Inter', sans-serif; font-size: 11px; color: var(--text); margin-bottom: 8px; }
    .fig-caption strong { color: var(--navy); }

    table { width: 100%; border-collapse: collapse; font-size: 11.5px; margin: 8px 0; }
    th { background: var(--navy); color: white; padding: 7px 10px; text-align: left; font-family: 'Inter', sans-serif; font-weight: 600; font-size: 11px; }
    td { padding: 6px 10px; border: 1px solid #ddd; vertical-align: top; }
    tr:nth-child(even) td { background: var(--alt-row); }
    .dark th { background: #1a3a5c; }
    .dark td { background: #152238; border-color: #2a3a54; color: #e0e0e0; }
    .dark tr:nth-child(even) td { background: #1a2a44; }

    /* Pipeline */
    .pipeline { display: flex; align-items: stretch; gap: 0; margin: 12px 0; }
    .stage { flex: 1; background: white; border: 1.5px solid var(--mid-blue); padding: 10px 12px; position: relative; margin-right: 28px; }
    .stage:last-child { margin-right: 0; }
    .stage-header { font-family: 'Inter', sans-serif; background: var(--mid-blue); color: white; margin: -10px -12px 8px; padding: 6px 12px; font-size: 10px; font-weight: 700; letter-spacing: 1px; }
    .stage-header span { display: block; font-weight: 400; font-size: 9.5px; letter-spacing: 0; margin-top: 1px; }
    .stage ul { list-style: none; padding: 0; }
    .stage li { font-size: 10px; padding: 2px 0; color: var(--text); }
    .stage li::before { content: "·"; margin-right: 5px; color: var(--mid-blue); font-weight: bold; }
    .stage .stat { margin-top: 8px; background: #e8f4fd; padding: 4px 8px; text-align: center; font-family: 'Inter', sans-serif; font-size: 10px; font-weight: 600; color: var(--mid-blue); border-radius: 2px; }
    .stage.final .stage-header { background: var(--green); }
    .stage.final { border-color: var(--green); }
    .stage.final .stat { background: #e8f8e8; color: var(--green); }
    .arrow { position: absolute; right: -20px; top: 50%; transform: translateY(-50%); font-size: 16px; color: var(--mid-blue); }
    .scoring-bar { display: flex; gap: 4px; margin-top: 10px; }
    .score-chip { flex: 1; background: var(--navy); color: white; text-align: center; padding: 5px 4px; font-family: 'Inter', sans-serif; font-size: 9px; font-weight: 500; line-height: 1.3; }
    .score-chip span { display: block; color: #7ec8c8; font-size: 9px; margin-top: 2px; }

    /* Two-column layout */
    .two-col { display: flex; gap: 25px; }
    .col { flex: 1; }
    .check-list, .x-list { list-style: none; padding: 0; }
    .check-list li, .x-list li { padding: 5px 0 5px 24px; position: relative; font-size: 11.5px; line-height: 1.45; border-bottom: 1px solid #eee; }
    .check-list li::before { content: "✓"; position: absolute; left: 0; color: var(--green); font-weight: 700; font-size: 14px; }
    .x-list li::before { content: "✗"; position: absolute; left: 0; color: var(--red); font-weight: 700; font-size: 14px; }
    .x-list li strong { color: var(--red); }

    .callout { border: 2px solid; padding: 12px 14px; margin: 10px 0; font-size: 10.5px; line-height: 1.5; }
    .callout-amber { border-color: var(--amber); background: #fdf8e8; }
    .callout-red { border-color: var(--red); background: #fde8e8; }
    .callout h3 { margin: 0 0 6px; font-size: 11.5px; }
    .callout-amber h3 { color: var(--amber); }
    .callout-red h3 { color: var(--red); }

    /* Summary */
    .funnel { display: flex; align-items: center; gap: 8px; margin: 12px 0 18px; }
    .funnel-step { text-align: center; border: 1.5px solid; padding: 8px 16px; min-width: 100px; font-family: 'Inter', sans-serif; }
    .funnel-step .num { font-size: 22px; font-weight: 700; display: block; }
    .funnel-step .label { font-size: 9px; color: #aaa; display: block; margin-top: 2px; }
    .funnel-arrow { font-size: 16px; color: #556677; }
    .lim-list { list-style: none; padding: 0; }
    .lim-list li { padding: 4px 0 4px 18px; position: relative; font-size: 12px; line-height: 1.5; }
    .lim-list li::before { content: "▸"; position: absolute; left: 0; color: var(--amber); font-weight: bold; }

    /* SVG figure styling */
    .fig-wrapper { display: flex; gap: 20px; align-items: flex-start; }
    .fig-panel { flex-shrink: 0; }
    .fig-side { flex: 1; min-width: 0; }
    section { padding: 0; margin: 0; }
    section::after { content: none; }
---

<div class="slide dark" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;">
  <div style="border-top:3px solid #7ec8c8;width:80px;margin-bottom:30px;"></div>
  <h1 style="border:none;font-size:30px;margin-bottom:8px;letter-spacing:1px;">Nutrition Interventions in LMICs</h1>
  <h2 style="font-size:18px;font-weight:400;color:#aaa;margin:0 0 30px;">Automated Evidence Synthesis &amp; Prioritization</h2>
  <div style="display:flex;gap:40px;margin:10px 0 30px;">
    <div><span style="font-family:Inter;font-size:30px;font-weight:700;color:#7ec8c8;">100</span><br><span style="font-size:11px;color:#778899;">Papers Reviewed</span></div>
    <div><span style="font-family:Inter;font-size:30px;font-weight:700;color:#7ec8c8;">57</span><br><span style="font-size:11px;color:#778899;">Full-Text (PMC)</span></div>
    <div><span style="font-family:Inter;font-size:30px;font-weight:700;color:#7ec8c8;">24</span><br><span style="font-size:11px;color:#778899;">Interventions Ranked</span></div>
    <div><span style="font-family:Inter;font-size:30px;font-weight:700;color:#7ec8c8;">3</span><br><span style="font-size:11px;color:#778899;">Evidence Tiers</span></div>
  </div>
  <p style="font-size:11px;color:#667788;">PubMed + OpenAlex systematic search · Pipeline v2.0 · May 2026</p>
  <div class="slide-number">1</div>
</div>

---

<div class="slide">
  <h1>Automated Evidence Synthesis Pipeline</h1>
  <div class="pipeline">
    <div class="stage">
      <div class="stage-header">STAGE 1 <span>Multi-Source Retrieval</span></div>
      <ul><li>PubMed: 12 domains × 2 passes (MA + SR)</li><li>OpenAlex: 4 economics/development queries</li><li>Track B: Cost-effectiveness analyses</li></ul>
      <div class="stat">~3,900 papers</div>
      <span class="arrow">▶</span>
    </div>
    <div class="stage">
      <div class="stage-header">STAGE 2 <span>Dedup + Scoring</span></div>
      <ul><li>3-phase dedup (PMID, OA ID, DOI)</li><li>7-component composite score (0–85)</li><li>MeSH + publication type based ranking</li></ul>
      <div class="stat">2,700 ranked</div>
      <span class="arrow">▶</span>
    </div>
    <div class="stage">
      <div class="stage-header">STAGE 3.5 <span>Full-Text Retrieval</span></div>
      <ul><li>PMID → PMCID conversion (batch 200)</li><li>PMC XML fetch + structured parsing</li><li>Results sections, tables, subgroups</li></ul>
      <div class="stat">57/100 full text</div>
      <span class="arrow">▶</span>
    </div>
    <div class="stage final">
      <div class="stage-header">STAGE 4 <span>LLM Review</span></div>
      <ul><li>Batched review (top 40, then 41–100)</li><li>Effect sizes extracted with CIs</li><li>Interventions tiered and ranked</li></ul>
      <div class="stat">24 interventions</div>
    </div>
  </div>
  <h2>Scoring Components <span style="font-weight:400;font-size:12px;color:var(--muted);">(max 85 points)</span></h2>
  <div class="scoring-bar">
    <div class="score-chip">Study Design<span>0–20</span></div>
    <div class="score-chip">Topic Relevance<span>0–25</span></div>
    <div class="score-chip">Setting<span>0–10</span></div>
    <div class="score-chip">Recency<span>0–10</span></div>
    <div class="score-chip">Citation Impact<span>0–12</span></div>
    <div class="score-chip">Open Access<span>0–3</span></div>
    <div class="score-chip">Tier Bonus<span>0–5</span></div>
  </div>
  <p class="footnote" style="margin-top:14px;">Sources: PubMed E-Utilities (MeSH indexing) · OpenAlex (economics/development) · PMC Open Access (full text) · NCBI ID Converter API</p>
  <div class="slide-number">2</div>
</div>

---

<div class="slide">
  <h1>Evidence Prioritization Framework</h1>
  <p class="fig-caption"><strong>Figure 1.</strong> Twenty-four nutrition interventions positioned by evidence strength and effect size (x-axis) against implementation readiness, a composite of cost-effectiveness and proven scalability (y-axis). Dashed lines delineate four action quadrants. Dot colour indicates evidence tier.</p>
  <div class="fig-wrapper">
    <div class="fig-panel">
      <svg width="640" height="480" viewBox="0 0 640 480" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;">
        <rect x="70" y="10" width="260" height="215" fill="#e8f4fd" opacity="0.5"/>
        <rect x="330" y="10" width="260" height="215" fill="#e8f8e8" opacity="0.5"/>
        <rect x="70" y="225" width="260" height="215" fill="#fde8e8" opacity="0.5"/>
        <rect x="330" y="225" width="260" height="215" fill="#fdf8e8" opacity="0.5"/>
        <text x="200" y="30" text-anchor="middle" font-size="9" font-weight="600" fill="#2e5c8a" letter-spacing="0.5">II. MONITOR &amp; EVALUATE</text>
        <text x="460" y="30" text-anchor="middle" font-size="9" font-weight="600" fill="#1e7a3c" letter-spacing="0.5">I. SCALE NOW</text>
        <text x="200" y="245" text-anchor="middle" font-size="9" font-weight="600" fill="#c0392b" letter-spacing="0.5">III. RESEARCH PRIORITY</text>
        <text x="460" y="245" text-anchor="middle" font-size="9" font-weight="600" fill="#b8860b" letter-spacing="0.5">IV. INVEST TO SCALE</text>
        <line x1="330" y1="10" x2="330" y2="440" stroke="#1b365d" stroke-width="1" stroke-dasharray="6,4" opacity="0.5"/>
        <line x1="70" y1="225" x2="590" y2="225" stroke="#1b365d" stroke-width="1" stroke-dasharray="6,4" opacity="0.5"/>
        <line x1="70" y1="440" x2="600" y2="440" stroke="#1b365d" stroke-width="2"/>
        <line x1="70" y1="440" x2="70" y2="5" stroke="#1b365d" stroke-width="2"/>
        <polygon points="600,435 600,445 612,440" fill="#1b365d"/>
        <polygon points="65,5 75,5 70,-5" fill="#1b365d"/>
        <text x="340" y="470" text-anchor="middle" font-size="11" font-weight="600" fill="#1b365d">Evidence Strength &amp; Effect Size</text>
        <text x="90" y="455" font-size="8" fill="#5a6c7d">Low</text>
        <text x="570" y="455" font-size="8" fill="#5a6c7d" text-anchor="end">High</text>
        <text x="15" y="225" text-anchor="middle" font-size="11" font-weight="600" fill="#1b365d" transform="rotate(-90,15,225)">Implementation Readiness</text>
        <text x="58" y="435" font-size="8" fill="#5a6c7d" text-anchor="end">Low</text>
        <text x="58" y="20" font-size="8" fill="#5a6c7d" text-anchor="end">High</text>
        <line x1="200" y1="440" x2="200" y2="445" stroke="#1b365d" stroke-width="1"/>
        <line x1="330" y1="440" x2="330" y2="445" stroke="#1b365d" stroke-width="1"/>
        <line x1="460" y1="440" x2="460" y2="445" stroke="#1b365d" stroke-width="1"/>
        <line x1="70" y1="335" x2="65" y2="335" stroke="#1b365d" stroke-width="1"/>
        <line x1="70" y1="225" x2="65" y2="225" stroke="#1b365d" stroke-width="1"/>
        <line x1="70" y1="115" x2="65" y2="115" stroke="#1b365d" stroke-width="1"/>
        <circle cx="520" cy="55" r="7" fill="#1e7a3c" opacity="0.85"/>
        <text x="532" y="52" font-size="8.5" fill="#1a1a2e" font-weight="500">Vitamin A suppl.</text>
        <text x="532" y="62" font-size="7" fill="#5a6c7d">RR 0.88 mortality</text>
        <circle cx="500" cy="95" r="7" fill="#1e7a3c" opacity="0.85"/>
        <text x="512" y="92" font-size="8.5" fill="#1a1a2e" font-weight="500">Iron–folic acid</text>
        <text x="512" y="102" font-size="7" fill="#5a6c7d">RR 0.52 anaemia</text>
        <circle cx="470" cy="72" r="7" fill="#1e7a3c" opacity="0.85"/>
        <text x="370" y="69" font-size="8.5" fill="#1a1a2e" font-weight="500">MMS</text>
        <text x="370" y="79" font-size="7" fill="#5a6c7d">RR 0.88 LBW</text>
        <circle cx="540" cy="40" r="7" fill="#1e7a3c" opacity="0.85"/>
        <text x="475" y="37" font-size="8.5" fill="#1a1a2e" font-weight="500">Fortification</text>
        <text x="475" y="47" font-size="7" fill="#5a6c7d">RR 0.66 anaemia</text>
        <circle cx="450" cy="105" r="7" fill="#1e7a3c" opacity="0.85"/>
        <text x="350" y="108" font-size="8.5" fill="#1a1a2e" font-weight="500">Breastfeeding promo.</text>
        <circle cx="430" cy="135" r="7" fill="#1e7a3c" opacity="0.85"/>
        <text x="442" y="132" font-size="8.5" fill="#1a1a2e" font-weight="500">Zinc (therapeutic)</text>
        <text x="442" y="142" font-size="7" fill="#5a6c7d">RR 0.73 diarrhoea d7</text>
        <circle cx="240" cy="90" r="6" fill="#2e5c8a" opacity="0.85"/>
        <text x="252" y="87" font-size="8.5" fill="#1a1a2e" font-weight="500">Nutrition education</text>
        <text x="252" y="97" font-size="7" fill="#5a6c7d">OR 2.80 IFAS compliance</text>
        <circle cx="210" cy="120" r="6" fill="#2e5c8a" opacity="0.85"/>
        <text x="222" y="117" font-size="8.5" fill="#1a1a2e" font-weight="500">Iron (school-age)</text>
        <text x="222" y="127" font-size="7" fill="#5a6c7d">SMD 0.50 cognition</text>
        <circle cx="190" cy="75" r="6" fill="#2e5c8a" opacity="0.85"/>
        <text x="100" y="68" font-size="8.5" fill="#1a1a2e" font-weight="500">CCTs</text>
        <text x="100" y="78" font-size="7" fill="#5a6c7d">HAZ +0.20 to +0.43</text>
        <circle cx="180" cy="140" r="6" fill="#2e5c8a" opacity="0.85"/>
        <text x="90" y="140" font-size="8.5" fill="#1a1a2e" font-weight="500">IMCI</text>
        <text x="90" y="150" font-size="7" fill="#5a6c7d">RR 0.85 U5 mort.</text>
        <circle cx="260" cy="155" r="6" fill="#2e5c8a" opacity="0.85"/>
        <text x="272" y="152" font-size="8.5" fill="#1a1a2e" font-weight="500">Calcium</text>
        <text x="272" y="162" font-size="7" fill="#5a6c7d">RR 0.30 pre-eclampsia</text>
        <circle cx="420" cy="290" r="6" fill="#b8860b" opacity="0.85"/>
        <text x="432" y="287" font-size="8.5" fill="#1a1a2e" font-weight="500">LNS (children)</text>
        <text x="432" y="297" font-size="7" fill="#5a6c7d">RR 0.93 stunting</text>
        <circle cx="460" cy="310" r="6" fill="#b8860b" opacity="0.85"/>
        <text x="472" y="307" font-size="8.5" fill="#1a1a2e" font-weight="500">CMAM / RUTF</text>
        <text x="472" y="317" font-size="7" fill="#5a6c7d">RR 0.52 SAM mort.</text>
        <circle cx="400" cy="340" r="6" fill="#b8860b" opacity="0.85"/>
        <text x="412" y="337" font-size="8.5" fill="#1a1a2e" font-weight="500">Comp. feeding</text>
        <text x="412" y="347" font-size="7" fill="#5a6c7d">SMD 0.22–0.39 HAZ</text>
        <circle cx="380" cy="300" r="6" fill="#b8860b" opacity="0.85"/>
        <text x="340" y="270" font-size="8.5" fill="#1a1a2e" font-weight="500">MNP</text>
        <text x="340" y="280" font-size="7" fill="#5a6c7d">RR 0.82 anaemia</text>
        <circle cx="370" cy="370" r="6" fill="#b8860b" opacity="0.85"/>
        <text x="382" y="367" font-size="8.5" fill="#1a1a2e" font-weight="500">Zinc (preventive)</text>
        <text x="382" y="377" font-size="7" fill="#5a6c7d">RR 0.87 diarrhoea</text>
        <circle cx="340" cy="330" r="6" fill="#b8860b" opacity="0.85"/>
        <text x="340" y="350" font-size="8.5" fill="#1a1a2e" font-weight="500">Prenatal LNS</text>
        <text x="340" y="360" font-size="7" fill="#5a6c7d">+49g birthweight</text>
        <circle cx="350" cy="390" r="6" fill="#b8860b" opacity="0.85"/>
        <text x="362" y="393" font-size="8.5" fill="#1a1a2e" font-weight="500">MAM mgmt</text>
        <circle cx="130" cy="350" r="5.5" fill="#c0392b" opacity="0.85"/>
        <text x="142" y="347" font-size="8.5" fill="#1a1a2e" font-weight="500">Agricultural</text>
        <text x="142" y="357" font-size="7" fill="#5a6c7d">No anthro. effect</text>
        <circle cx="160" cy="310" r="5.5" fill="#c0392b" opacity="0.85"/>
        <text x="172" y="307" font-size="8.5" fill="#1a1a2e" font-weight="500">Vitamin D</text>
        <text x="172" y="317" font-size="7" fill="#5a6c7d">Limited LMIC data</text>
        <circle cx="120" cy="390" r="5.5" fill="#c0392b" opacity="0.85"/>
        <text x="132" y="390" font-size="8.5" fill="#1a1a2e" font-weight="500">Growth monitoring</text>
        <circle cx="155" cy="370" r="5.5" fill="#c0392b" opacity="0.85"/>
        <text x="167" y="373" font-size="8.5" fill="#1a1a2e" font-weight="500">Egg suppl.</text>
        <circle cx="200" cy="280" r="5.5" fill="#c0392b" opacity="0.85"/>
        <text x="212" y="277" font-size="8.5" fill="#1a1a2e" font-weight="500">Protein-energy</text>
        <text x="212" y="287" font-size="7" fill="#5a6c7d">SMD 0.20 BW</text>
        <circle cx="170" cy="260" r="5.5" fill="#c0392b" opacity="0.85"/>
        <text x="80" y="260" font-size="8.5" fill="#1a1a2e" font-weight="500">WASH</text>
        <text x="80" y="270" font-size="7" fill="#5a6c7d">SMD 0.14 HAZ</text>
        <rect x="72" y="10" width="100" height="2" fill="none"/>
        <g transform="translate(420,410)">
          <rect x="0" y="0" width="170" height="28" fill="white" stroke="#ddd" stroke-width="0.5" rx="2"/>
          <circle cx="12" cy="14" r="5" fill="#1e7a3c" opacity="0.85"/>
          <text x="20" y="17" font-size="7.5" fill="#1a1a2e">Tier 1 (A)</text>
          <circle cx="70" cy="14" r="4.5" fill="#2e5c8a" opacity="0.85"/>
          <text x="78" y="17" font-size="7.5" fill="#1a1a2e">Tier 2 (B/B+)</text>
          <circle cx="132" cy="14" r="4" fill="#c0392b" opacity="0.85"/>
          <text x="140" y="17" font-size="7.5" fill="#1a1a2e">Tier 3 (C)</text>
        </g>
      </svg>
    </div>
    <div class="fig-side">
      <h3>Quadrant Decision Rules</h3>
      <table style="font-size:10.5px;margin-top:4px;">
        <tr><th style="padding:5px 8px;width:30px;">Q</th><th style="padding:5px 8px;">Action</th><th style="padding:5px 8px;">Criteria</th></tr>
        <tr><td style="color:var(--green);font-weight:700;">I</td><td>Scale now</td><td>Evidence A + proven national + high cost-effectiveness</td></tr>
        <tr><td style="color:var(--mid-blue);font-weight:700;">II</td><td>Monitor &amp; evaluate</td><td>Good platforms, moderate evidence (B/B+)</td></tr>
        <tr><td style="color:var(--red);font-weight:700;">III</td><td>Research priority</td><td>Emerging evidence (C/C+), insufficient for policy</td></tr>
        <tr><td style="color:var(--amber);font-weight:700;">IV</td><td>Invest to scale</td><td>Evidence A but higher cost or subnational only</td></tr>
      </table>
      <h3 style="margin-top:14px;">Axis Composition</h3>
      <table style="font-size:10px;margin-top:4px;">
        <tr><th style="padding:4px 8px;">Axis</th><th style="padding:4px 8px;">Composed of</th></tr>
        <tr><td><strong>Evidence</strong> (x)</td><td>GRADE certainty · # Cochrane reviews · pooled effect magnitude · consistency</td></tr>
        <tr><td><strong>Readiness</strong> (y)</td><td>Cost-effectiveness · delivery platform maturity · # countries with programmes</td></tr>
      </table>
    </div>
  </div>
  <div class="slide-number">3</div>
</div>

---

<div class="slide">
  <h1>Children Under 5 — Intervention Prioritization</h1>
  <p class="fig-caption"><strong>Figure 2.</strong> Child nutrition interventions (6–59 months) positioned by effect size on primary outcome (x-axis) against annual cost per child (y-axis, inverted — lower cost is higher). All interventions shown carry Evidence Rating A. Dot size proportional to evidence base breadth.</p>
  <div class="fig-wrapper">
    <div class="fig-panel">
      <svg width="560" height="430" viewBox="0 0 560 430" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;">
        <rect x="70" y="10" width="225" height="195" fill="#e8f4fd" opacity="0.4"/>
        <rect x="295" y="10" width="225" height="195" fill="#e8f8e8" opacity="0.4"/>
        <rect x="70" y="205" width="225" height="195" fill="#fde8e8" opacity="0.4"/>
        <rect x="295" y="205" width="225" height="195" fill="#fdf8e8" opacity="0.4"/>
        <line x1="295" y1="10" x2="295" y2="400" stroke="#1b365d" stroke-width="0.8" stroke-dasharray="5,4" opacity="0.4"/>
        <line x1="70" y1="205" x2="520" y2="205" stroke="#1b365d" stroke-width="0.8" stroke-dasharray="5,4" opacity="0.4"/>
        <line x1="70" y1="400" x2="530" y2="400" stroke="#1b365d" stroke-width="2"/>
        <line x1="70" y1="400" x2="70" y2="5" stroke="#1b365d" stroke-width="2"/>
        <polygon points="530,395 530,405 542,400" fill="#1b365d"/>
        <polygon points="65,5 75,5 70,-5" fill="#1b365d"/>
        <text x="300" y="425" text-anchor="middle" font-size="10.5" font-weight="600" fill="#1b365d">Effect Size (Mortality / Morbidity Reduction)</text>
        <text x="90" y="415" font-size="8" fill="#5a6c7d">Moderate</text>
        <text x="500" y="415" font-size="8" fill="#5a6c7d" text-anchor="end">Large</text>
        <text x="15" y="210" text-anchor="middle" font-size="10.5" font-weight="600" fill="#1b365d" transform="rotate(-90,15,210)">Cost-Effectiveness (lower cost = higher)</text>
        <text x="58" y="395" font-size="8" fill="#5a6c7d" text-anchor="end">$200+</text>
        <text x="58" y="210" font-size="8" fill="#5a6c7d" text-anchor="end">$5–50</text>
        <text x="58" y="25" font-size="8" fill="#5a6c7d" text-anchor="end">&lt;$5</text>
        <line x1="70" y1="205" x2="65" y2="205" stroke="#1b365d" stroke-width="1"/>
        <line x1="295" y1="400" x2="295" y2="405" stroke="#1b365d" stroke-width="1"/>
        <circle cx="440" cy="55" r="9" fill="#1e7a3c" opacity="0.8"/>
        <text x="455" y="48" font-size="9" fill="#1a1a2e" font-weight="600">Vitamin A suppl.</text>
        <text x="455" y="59" font-size="7.5" fill="#5a6c7d">RR 0.88 mortality · $1–3/yr</text>
        <text x="455" y="69" font-size="7" fill="#888">3 Cochrane, n=1.2M</text>
        <circle cx="380" cy="40" r="8" fill="#1e7a3c" opacity="0.8"/>
        <text x="310" y="30" font-size="9" fill="#1a1a2e" font-weight="600">Zinc (therapeutic)</text>
        <text x="310" y="41" font-size="7.5" fill="#5a6c7d">RR 0.73 at day 7 · $0.50</text>
        <circle cx="200" cy="75" r="7.5" fill="#1e7a3c" opacity="0.8"/>
        <text x="215" y="70" font-size="9" fill="#1a1a2e" font-weight="600">Micronutrient powders</text>
        <text x="215" y="81" font-size="7.5" fill="#5a6c7d">RR 0.82 anaemia · $3.60/yr</text>
        <circle cx="170" cy="50" r="7.5" fill="#1e7a3c" opacity="0.8"/>
        <text x="82" y="54" font-size="9" fill="#1a1a2e" font-weight="600">Zinc (preventive)</text>
        <text x="82" y="65" font-size="7.5" fill="#5a6c7d">RR 0.87 · $1–2/yr</text>
        <circle cx="190" cy="260" r="7" fill="#b8860b" opacity="0.8"/>
        <text x="205" y="255" font-size="9" fill="#1a1a2e" font-weight="600">LNS (6–23 mo)</text>
        <text x="205" y="266" font-size="7.5" fill="#5a6c7d">RR 0.93 stunting · $50–60/yr</text>
        <circle cx="470" cy="340" r="8" fill="#b8860b" opacity="0.8"/>
        <text x="370" y="345" font-size="9" fill="#1a1a2e" font-weight="600">CMAM / RUTF</text>
        <text x="370" y="356" font-size="7.5" fill="#5a6c7d">RR 0.52 SAM mort. · $200</text>
        <text x="370" y="366" font-size="7" fill="#888">48% mortality reduction</text>
        <circle cx="230" cy="170" r="6.5" fill="#1e7a3c" opacity="0.8"/>
        <text x="244" y="167" font-size="9" fill="#1a1a2e" font-weight="600">Comp. feeding</text>
        <text x="244" y="178" font-size="7.5" fill="#5a6c7d">SMD 0.22–0.39 HAZ</text>
        <g transform="translate(350,385)">
          <rect x="0" y="0" width="165" height="15" fill="white" stroke="#ddd" stroke-width="0.5" rx="2"/>
          <circle cx="10" cy="7.5" r="4" fill="#1e7a3c" opacity="0.8"/>
          <text x="18" y="11" font-size="7" fill="#1a1a2e">Tier 1 (Evidence A)</text>
          <circle cx="100" cy="7.5" r="4" fill="#b8860b" opacity="0.8"/>
          <text x="108" y="11" font-size="7" fill="#1a1a2e">High cost (A)</text>
        </g>
      </svg>
    </div>
    <div class="fig-side">
      <h3>Supporting Data</h3>
      <table style="font-size:10px;">
        <tr><th style="padding:4px 6px;">Intervention</th><th style="padding:4px 6px;">Key Effect</th><th style="padding:4px 6px;">95% CI</th><th style="padding:4px 6px;">Cost</th></tr>
        <tr><td>VAS (6–59 mo)</td><td>RR 0.88 mortality</td><td>0.83–0.93</td><td>$1–3/yr</td></tr>
        <tr><td>Zinc (therapeutic)</td><td>RR 0.73 at day 7</td><td>0.61–0.88</td><td>$0.50</td></tr>
        <tr><td>MNP</td><td>RR 0.82 anaemia</td><td>0.76–0.90</td><td>$3.60/yr</td></tr>
        <tr><td>Zinc (preventive)</td><td>RR 0.87 diarrhoea</td><td>0.85–0.89</td><td>$1–2/yr</td></tr>
        <tr><td>Comp. feeding</td><td>SMD 0.22 HAZ</td><td>0.01–0.43</td><td>Variable</td></tr>
        <tr><td>LNS (6–23 mo)</td><td>RR 0.93 stunting</td><td>0.88–0.98</td><td>$50–60/yr</td></tr>
        <tr><td>CMAM / RUTF</td><td>RR 0.52 mortality</td><td>0.43–0.64</td><td>$200</td></tr>
      </table>
      <p class="footnote">All interventions shown carry Evidence A (multiple Cochrane reviews/meta-analyses). Higher-cost interventions (LNS, CMAM) are justified in high-burden settings where the absolute number of cases averted offsets unit cost.</p>
    </div>
  </div>
  <div class="slide-number">4</div>
</div>

---

<div class="slide">
  <h1>Pregnant Women — Intervention Prioritization</h1>
  <p class="fig-caption"><strong>Figure 3.</strong> Maternal nutrition interventions positioned by effect size on primary outcome (x-axis) against cost per pregnancy (y-axis, inverted). Dot colour indicates evidence rating. Evidence ratings shown in parentheses.</p>
  <div class="fig-wrapper">
    <div class="fig-panel">
      <svg width="560" height="430" viewBox="0 0 560 430" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;">
        <rect x="70" y="10" width="225" height="195" fill="#e8f4fd" opacity="0.4"/>
        <rect x="295" y="10" width="225" height="195" fill="#e8f8e8" opacity="0.4"/>
        <rect x="70" y="205" width="225" height="195" fill="#fde8e8" opacity="0.4"/>
        <rect x="295" y="205" width="225" height="195" fill="#fdf8e8" opacity="0.4"/>
        <line x1="295" y1="10" x2="295" y2="400" stroke="#1b365d" stroke-width="0.8" stroke-dasharray="5,4" opacity="0.4"/>
        <line x1="70" y1="205" x2="520" y2="205" stroke="#1b365d" stroke-width="0.8" stroke-dasharray="5,4" opacity="0.4"/>
        <line x1="70" y1="400" x2="530" y2="400" stroke="#1b365d" stroke-width="2"/>
        <line x1="70" y1="400" x2="70" y2="5" stroke="#1b365d" stroke-width="2"/>
        <polygon points="530,395 530,405 542,400" fill="#1b365d"/>
        <polygon points="65,5 75,5 70,-5" fill="#1b365d"/>
        <text x="300" y="425" text-anchor="middle" font-size="10.5" font-weight="600" fill="#1b365d">Effect Size (LBW / Anaemia Reduction)</text>
        <text x="90" y="415" font-size="8" fill="#5a6c7d">Moderate</text>
        <text x="500" y="415" font-size="8" fill="#5a6c7d" text-anchor="end">Large</text>
        <text x="15" y="210" text-anchor="middle" font-size="10.5" font-weight="600" fill="#1b365d" transform="rotate(-90,15,210)">Cost-Effectiveness (lower cost = higher)</text>
        <text x="58" y="25" font-size="8" fill="#5a6c7d" text-anchor="end">&lt;$2</text>
        <text x="58" y="210" font-size="8" fill="#5a6c7d" text-anchor="end">$3–10</text>
        <text x="58" y="395" font-size="8" fill="#5a6c7d" text-anchor="end">$10+</text>
        <line x1="70" y1="205" x2="65" y2="205" stroke="#1b365d" stroke-width="1"/>
        <line x1="295" y1="400" x2="295" y2="405" stroke="#1b365d" stroke-width="1"/>
        <circle cx="480" cy="40" r="9" fill="#1e7a3c" opacity="0.8"/>
        <text x="400" y="28" font-size="9" fill="#1a1a2e" font-weight="600">Iron–folic acid (A)</text>
        <text x="400" y="39" font-size="7.5" fill="#5a6c7d">RR 0.52 anaemia · $0.50–2</text>
        <circle cx="410" cy="80" r="8.5" fill="#1e7a3c" opacity="0.8"/>
        <text x="425" y="75" font-size="9" fill="#1a1a2e" font-weight="600">MMS (A)</text>
        <text x="425" y="86" font-size="7.5" fill="#5a6c7d">RR 0.88 LBW · $1.50–3.50</text>
        <circle cx="300" cy="55" r="7" fill="#2e5c8a" opacity="0.8"/>
        <text x="314" y="50" font-size="9" fill="#1a1a2e" font-weight="600">Nutrition education (B+)</text>
        <text x="314" y="61" font-size="7.5" fill="#5a6c7d">OR 2.80 IFAS compliance</text>
        <circle cx="380" cy="155" r="7" fill="#2e5c8a" opacity="0.8"/>
        <text x="394" y="150" font-size="9" fill="#1a1a2e" font-weight="600">Calcium (B)</text>
        <text x="394" y="161" font-size="7.5" fill="#5a6c7d">RR 0.30 pre-eclampsia</text>
        <circle cx="310" cy="270" r="6.5" fill="#b8860b" opacity="0.8"/>
        <text x="325" y="265" font-size="9" fill="#1a1a2e" font-weight="600">Prenatal SQ-LNS (B+)</text>
        <text x="325" y="276" font-size="7.5" fill="#5a6c7d">+49g birthweight</text>
        <circle cx="170" cy="290" r="5.5" fill="#c0392b" opacity="0.8"/>
        <text x="185" y="287" font-size="9" fill="#1a1a2e" font-weight="600">Protein-energy (B)</text>
        <text x="185" y="298" font-size="7.5" fill="#5a6c7d">SMD 0.20 birthweight</text>
        <circle cx="130" cy="330" r="5" fill="#c0392b" opacity="0.8"/>
        <text x="145" y="327" font-size="9" fill="#1a1a2e" font-weight="600">Vitamin D (C+)</text>
        <text x="145" y="338" font-size="7.5" fill="#5a6c7d">Limited LMIC evidence</text>
        <g transform="translate(340,385)">
          <rect x="0" y="0" width="175" height="15" fill="white" stroke="#ddd" stroke-width="0.5" rx="2"/>
          <circle cx="10" cy="7.5" r="4" fill="#1e7a3c" opacity="0.8"/>
          <text x="18" y="11" font-size="7" fill="#1a1a2e">Evidence A</text>
          <circle cx="68" cy="7.5" r="3.5" fill="#2e5c8a" opacity="0.8"/>
          <text x="76" y="11" font-size="7" fill="#1a1a2e">B / B+</text>
          <circle cx="115" cy="7.5" r="3" fill="#c0392b" opacity="0.8"/>
          <text x="122" y="11" font-size="7" fill="#1a1a2e">C / C+</text>
        </g>
      </svg>
    </div>
    <div class="fig-side">
      <h3>Key Policy Insight</h3>
      <p style="font-size:11.5px;line-height:1.55;margin-top:6px;">MMS costs only <strong>$1–2 more</strong> than IFA per pregnancy but prevents <strong>12% more low-birthweight births</strong> (RR 0.88 vs IFA alone). WHO conditionally recommended the IFA → MMS transition in 2020.</p>
      <h3 style="margin-top:12px;">The Compliance Bottleneck</h3>
      <p style="font-size:11.5px;line-height:1.55;margin-top:6px;">IFA supplement adherence in Sub-Saharan Africa is only <strong>39.2%</strong>. Nutrition education <strong>triples adherence</strong> (OR 2.80) — making it a force-multiplier for any supplementation programme.</p>
      <h3 style="margin-top:12px;">Supporting Data</h3>
      <table style="font-size:10px;">
        <tr><th style="padding:4px 6px;">Intervention</th><th style="padding:4px 6px;">Key Effect</th><th style="padding:4px 6px;">95% CI</th></tr>
        <tr><td>IFA</td><td>RR 0.52 anaemia</td><td>0.41–0.66</td></tr>
        <tr><td>MMS</td><td>RR 0.88 LBW</td><td>0.85–0.91</td></tr>
        <tr><td>Nutrition ed.</td><td>OR 2.80 compliance</td><td>2.04–3.83</td></tr>
        <tr><td>Calcium</td><td>RR 0.30 pre-eclampsia</td><td>0.17–0.52</td></tr>
        <tr><td>Prenatal LNS</td><td>+49g birthweight</td><td>IPD, 4 RCTs</td></tr>
        <tr><td>Vitamin D</td><td>RR 0.40 LBW</td><td>0.23–0.71</td></tr>
      </table>
    </div>
  </div>
  <div class="slide-number">5</div>
</div>

---

<div class="slide">
  <h1>Population-Level Interventions — Evidence vs. Reach</h1>
  <p class="fig-caption"><strong>Figure 4.</strong> Population-level and nutrition-sensitive interventions positioned by evidence strength (x-axis) against implementation coverage across LMICs (y-axis). Dot size reflects number of countries with programmes.</p>
  <div class="fig-wrapper">
    <div class="fig-panel">
      <svg width="560" height="430" viewBox="0 0 560 430" xmlns="http://www.w3.org/2000/svg" style="font-family:Inter,sans-serif;">
        <rect x="70" y="10" width="225" height="195" fill="#e8f4fd" opacity="0.4"/>
        <rect x="295" y="10" width="225" height="195" fill="#e8f8e8" opacity="0.4"/>
        <rect x="70" y="205" width="225" height="195" fill="#fde8e8" opacity="0.4"/>
        <rect x="295" y="205" width="225" height="195" fill="#fdf8e8" opacity="0.4"/>
        <line x1="295" y1="10" x2="295" y2="400" stroke="#1b365d" stroke-width="0.8" stroke-dasharray="5,4" opacity="0.4"/>
        <line x1="70" y1="205" x2="520" y2="205" stroke="#1b365d" stroke-width="0.8" stroke-dasharray="5,4" opacity="0.4"/>
        <line x1="70" y1="400" x2="530" y2="400" stroke="#1b365d" stroke-width="2"/>
        <line x1="70" y1="400" x2="70" y2="5" stroke="#1b365d" stroke-width="2"/>
        <polygon points="530,395 530,405 542,400" fill="#1b365d"/>
        <polygon points="65,5 75,5 70,-5" fill="#1b365d"/>
        <text x="300" y="425" text-anchor="middle" font-size="10.5" font-weight="600" fill="#1b365d">Evidence Strength</text>
        <text x="90" y="415" font-size="8" fill="#5a6c7d">Low (C)</text>
        <text x="500" y="415" font-size="8" fill="#5a6c7d" text-anchor="end">High (A)</text>
        <text x="15" y="210" text-anchor="middle" font-size="10.5" font-weight="600" fill="#1b365d" transform="rotate(-90,15,210)">Implementation Coverage</text>
        <text x="58" y="395" font-size="8" fill="#5a6c7d" text-anchor="end">Pilot</text>
        <text x="58" y="210" font-size="8" fill="#5a6c7d" text-anchor="end">Subnational</text>
        <text x="58" y="25" font-size="8" fill="#5a6c7d" text-anchor="end">National</text>
        <line x1="70" y1="205" x2="65" y2="205" stroke="#1b365d" stroke-width="1"/>
        <line x1="295" y1="400" x2="295" y2="405" stroke="#1b365d" stroke-width="1"/>
        <circle cx="490" cy="35" r="11" fill="#1e7a3c" opacity="0.8"/>
        <text x="400" y="22" font-size="9" fill="#1a1a2e" font-weight="600">Large-scale fortification</text>
        <text x="400" y="33" font-size="7.5" fill="#5a6c7d">RR 0.66 anaemia · >120 countries</text>
        <circle cx="450" cy="75" r="10" fill="#1e7a3c" opacity="0.8"/>
        <text x="350" y="68" font-size="9" fill="#1a1a2e" font-weight="600">Breastfeeding promotion</text>
        <text x="350" y="79" font-size="7.5" fill="#5a6c7d">823K deaths/yr avoidable · >150 BFHI</text>
        <circle cx="230" cy="80" r="8" fill="#2e5c8a" opacity="0.8"/>
        <text x="110" y="78" font-size="9" fill="#1a1a2e" font-weight="600">CCTs</text>
        <text x="110" y="89" font-size="7.5" fill="#5a6c7d">HAZ +0.20–0.43</text>
        <circle cx="200" cy="110" r="7.5" fill="#2e5c8a" opacity="0.8"/>
        <text x="215" y="107" font-size="9" fill="#1a1a2e" font-weight="600">IMCI</text>
        <text x="215" y="118" font-size="7.5" fill="#5a6c7d">RR 0.85 U5 mortality · >100 countries</text>
        <circle cx="180" cy="240" r="6.5" fill="#c0392b" opacity="0.8"/>
        <text x="195" y="237" font-size="9" fill="#1a1a2e" font-weight="600">WASH (combined)</text>
        <text x="195" y="248" font-size="7.5" fill="#5a6c7d">HAZ SMD 0.14 · borderline</text>
        <circle cx="120" cy="330" r="5.5" fill="#c0392b" opacity="0.8"/>
        <text x="135" y="327" font-size="9" fill="#1a1a2e" font-weight="600">Agricultural</text>
        <text x="135" y="338" font-size="7.5" fill="#5a6c7d">No anthropometric effect</text>
        <g transform="translate(340,385)">
          <rect x="0" y="0" width="175" height="15" fill="white" stroke="#ddd" stroke-width="0.5" rx="2"/>
          <circle cx="10" cy="7.5" r="4" fill="#1e7a3c" opacity="0.8"/>
          <text x="18" y="11" font-size="7" fill="#1a1a2e">Evidence A</text>
          <circle cx="68" cy="7.5" r="3.5" fill="#2e5c8a" opacity="0.8"/>
          <text x="76" y="11" font-size="7" fill="#1a1a2e">B / B+</text>
          <circle cx="115" cy="7.5" r="3" fill="#c0392b" opacity="0.8"/>
          <text x="122" y="11" font-size="7" fill="#1a1a2e">C / C+</text>
        </g>
      </svg>
    </div>
    <div class="fig-side">
      <h3>Cross-Cutting Finding</h3>
      <p style="font-size:11.5px;line-height:1.55;margin-top:6px;"><strong>76%</strong> of studies combining multisectoral policies with nutritional supplementation successfully reduced stunting, vs. variable results for single-sector approaches (PMID 31666032).</p>
      <h3 style="margin-top:12px;">The Anaemia Paradox</h3>
      <p style="font-size:11.5px;line-height:1.55;margin-top:6px;">Iron deficiency explains only <strong>25% of anaemia</strong> in preschool children — far below the commonly assumed 50%. Inflammation, malaria, helminth infections, and other micronutrient deficiencies must be addressed concurrently (PMID 27827838).</p>
      <h3 style="margin-top:12px;">Supporting Data</h3>
      <table style="font-size:10px;">
        <tr><th style="padding:4px 6px;">Intervention</th><th style="padding:4px 6px;">Key Effect</th><th style="padding:4px 6px;">Countries</th></tr>
        <tr><td>Fortification</td><td>RR 0.66 anaemia</td><td>>120</td></tr>
        <tr><td>Breastfeeding</td><td>823K deaths/yr</td><td>>150 (BFHI)</td></tr>
        <tr><td>CCTs</td><td>HAZ +0.20–0.43</td><td>Brazil, Mexico, Peru</td></tr>
        <tr><td>IMCI</td><td>RR 0.85 U5 mort.</td><td>>100</td></tr>
        <tr><td>WASH</td><td>HAZ SMD 0.14</td><td>Several (CLTS)</td></tr>
        <tr><td>Agricultural</td><td>Diet diversity ↑</td><td>Growing</td></tr>
      </table>
    </div>
  </div>
  <div class="slide-number">6</div>
</div>

---

<div class="slide">
  <h1>Interventions by Delivery Platform &amp; Evidence Tier</h1>
  <p class="fig-caption"><strong>Table 5.</strong> Classification of all 24 interventions by delivery mechanism and evidence strength. Community-based platforms concentrate the largest number of Evidence A interventions.</p>
  <table style="font-size:11px;">
    <thead>
      <tr>
        <th style="width:170px;">Delivery Platform</th>
        <th style="background:#1e7a3c;">Evidence A (Strong)</th>
        <th style="background:var(--mid-blue);">Evidence B / B+ (Moderate)</th>
        <th style="background:var(--red);">Evidence C / C+ (Emerging)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Health Facility</strong><br><em style="font-size:10px;color:#888;">ANC / Postnatal</em></td>
        <td style="background:#e8f8e8;">Iron–folic acid<br>Multiple micronutrient suppl.<br>Zinc for diarrhoea treatment</td>
        <td style="background:#e8f4fd;">Calcium supplementation<br>Nutrition education<br>Iron suppl. (school-age)<br>Prenatal SQ-LNS</td>
        <td style="background:#fde8e8;">Vitamin D supplementation</td>
      </tr>
      <tr>
        <td><strong>Community-Based</strong><br><em style="font-size:10px;color:#888;">CHW Delivery</em></td>
        <td style="background:#e8f8e8;">Vitamin A supplementation<br>Micronutrient powders<br>SAM management (CMAM)<br>Complementary feeding<br>Breastfeeding promotion<br>Preventive zinc suppl.</td>
        <td style="background:#e8f4fd;">WASH interventions<br>Community case mgmt<br>MAM management</td>
        <td style="background:#fde8e8;">Growth monitoring<br>Egg-based supplementation</td>
      </tr>
      <tr>
        <td><strong>Food System</strong><br><em style="font-size:10px;color:#888;">Fortification / Production</em></td>
        <td style="background:#e8f8e8;">Large-scale fortification<br>(iron, iodine, folic acid)</td>
        <td style="background:var(--alt-row);color:#999;text-align:center;">—</td>
        <td style="background:#fde8e8;">Agricultural interventions<br>Biofortification</td>
      </tr>
      <tr>
        <td><strong>Cash / Social Protection</strong></td>
        <td style="background:var(--alt-row);color:#999;text-align:center;">—</td>
        <td style="background:#e8f4fd;">Conditional cash transfers<br>IMCI strategy</td>
        <td style="background:var(--alt-row);color:#999;text-align:center;">—</td>
      </tr>
    </tbody>
  </table>
  <p class="footnote">6 of 10 Evidence A interventions are deliverable through community health worker networks — the primary scaling vehicle for child nutrition in LMICs. Health facility–based interventions concentrate in the maternal/pregnancy domain.</p>
  <div class="slide-number">7</div>
</div>

---

<div class="slide">
  <h1 style="border-bottom-color:var(--green);">Vitamin A Supplementation — What the Pipeline Did Well</h1>
  <div class="two-col">
    <div class="col">
      <h2 style="color:var(--green);">Pipeline Strengths</h2>
      <ul class="check-list">
        <li>Surfaced the <strong>three landmark syntheses</strong>: Imdad 2011 (CHERG/LiST) + Cochrane CD008524 (2017 &amp; 2022 update)</li>
        <li>Extracted <strong>detailed effect sizes with CIs</strong> across mortality, morbidity, and deficiency outcomes</li>
        <li>Distinguished <strong>neonatal VAS</strong> (no benefit; possible harm in Africa) from <strong>6–59 month VAS</strong></li>
        <li>Detected the <strong>fixed vs random divergence</strong>: RR 0.88 vs 0.76 for all-cause mortality</li>
        <li>Flagged <strong>Asia vs Africa differential</strong>: RR 0.69 vs 0.85 in mortality reduction</li>
        <li>Identified <strong>adverse effects</strong>: vomiting RR 1.97, bulging fontanelle in &lt;6 mo</li>
        <li>Noted <strong>declining absolute benefit</strong> as vitamin A deficiency prevalence falls — important for programme reassessment</li>
      </ul>
    </div>
    <div class="col">
      <h2>The Three Landmark Syntheses</h2>
      <table style="font-size:9.5px;">
        <tr><th style="padding:4px 6px;">Paper</th><th style="padding:4px 6px;">Type</th><th style="padding:4px 6px;">All-cause mortality</th><th style="padding:4px 6px;">N children</th></tr>
        <tr><td>Imdad 2011<br><span style="color:#888;">BMC Public Health</span></td><td>CHERG meta-analysis (for LiST)</td><td>RR 0.75 (0.64–0.88)<br><span style="color:#888;">random</span></td><td>~250K</td></tr>
        <tr><td>Cochrane 2017<br><span style="color:#888;">CD008524.pub3</span></td><td>Systematic review + GRADE</td><td>RR 0.88 (0.83–0.93) fixed<br>0.76 (0.66–0.88) random</td><td>1,202,382</td></tr>
        <tr><td>Cochrane 2022<br><span style="color:#888;">CD008524 update</span></td><td>Update — <strong>no new RCTs</strong></td><td>Identical to 2017</td><td>Identical</td></tr>
      </table>
      <p class="footnote" style="margin-top:10px;">Two of the "three" are the <strong>same Cochrane review</strong> (2022 found no new trials); Imdad 2011 is a <strong>CHERG meta-analysis, not Cochrane</strong>. The fixed/random split is driven by one trial — see next slide.</p>
    </div>
  </div>
  <div class="slide-number">8</div>
</div>

---

<div class="slide">
  <h1 style="border-bottom-color:var(--red);">Vitamin A Supplementation — Pipeline Limitations</h1>
  <div class="two-col">
    <div class="col" style="flex:1.15;">
      <h2 style="color:var(--red);">Structural Gaps</h2>
      <ul class="x-list">
        <li><strong>Study-type misclassification:</strong> Labelled Imdad 2011 (a CHERG meta-analysis in <em>BMC Public Health</em>) a "Cochrane review," and counted a no-new-evidence update as a third independent generation</li>
        <li><strong>Couldn't trace the divergence to its cause:</strong> Flagged fixed 0.88 vs random 0.76 but never identified <strong>DEVTA</strong> as the driver (see callout)</li>
        <li><strong>Mechanism left unexamined:</strong> The thin link is <em>cause-specific</em> mortality (diarrhoea/measles pathways underpowered), not the all-cause finding the deck dwelt on</li>
        <li><strong>CEA blind spot:</strong> Rated "Very High" cost-effectiveness but zero cost-effectiveness papers were retrieved</li>
        <li><strong>External knowledge leak:</strong> "$1–3/child/yr" comes from LLM training data, not from any retrieved paper</li>
        <li><strong>Misattribution:</strong> "823,000 deaths preventable" cited from PMID 26869575 — but that is the Lancet <em>Breastfeeding</em> Series, not VAS</li>
      </ul>
    </div>
    <div class="col" style="flex:0.85;">
      <div class="callout callout-amber">
        <h3>The CEA Blind Spot</h3>
        <p>The search included a dedicated cost-effectiveness track (Track B) but retrieved <strong>zero usable papers</strong> for VAS. All cost claims rely on LLM external knowledge. The synthesis acknowledges this but the confidence of the "Very High" rating does not reflect the gap.</p>
      </div>
      <div class="callout callout-red">
        <h3>It's One Trial: DEVTA</h3>
        <p>Fixed-effect RR 0.88 vs random-effects RR 0.76 isn't an abstract "model choice" — it's <strong>DEVTA</strong> (India, ~1M children, RR ~0.96), which carries <strong>61.7% of the fixed-effect weight</strong> and drags the pooled estimate up. Down-weight it (random-effects) and you recover Imdad 2011's ~24% reduction. A domain expert names DEVTA in one sentence; the LLM produced only a vague "models differ."</p>
      </div>
    </div>
  </div>
  <p class="footnote">A mix of LLM reasoning gaps (study-type misclassification, missing DEVTA, mechanism left unexamined) and structural pipeline gaps (no CEA source, no trial-overlap detection). Fixes need both better prompting and pipeline changes — see notes.</p>
  <div class="slide-number">9</div>
</div>

---

<div class="slide dark">
  <h1 style="border-bottom-color:#7ec8c8;">Summary &amp; Key Takeaways</h1>
  <div class="funnel">
    <div class="funnel-step" style="border-color:#2e5c8a;"><span class="num" style="color:#5a9bd5;">3,900</span><span class="label">Retrieved</span></div>
    <span class="funnel-arrow">▶</span>
    <div class="funnel-step" style="border-color:#2e5c8a;"><span class="num" style="color:#5a9bd5;">2,700</span><span class="label">Deduplicated</span></div>
    <span class="funnel-arrow">▶</span>
    <div class="funnel-step" style="border-color:#0e7c7b;"><span class="num" style="color:#7ec8c8;">100</span><span class="label">Reviewed</span></div>
    <span class="funnel-arrow">▶</span>
    <div class="funnel-step" style="border-color:#0e7c7b;"><span class="num" style="color:#7ec8c8;">57</span><span class="label">Full Text</span></div>
    <span class="funnel-arrow">▶</span>
    <div class="funnel-step" style="border-color:#1e7a3c;"><span class="num" style="color:#4eca6a;">24</span><span class="label">Ranked</span></div>
  </div>
  <h2>Top 5 "Scale Now" Interventions</h2>
  <table style="font-size:11px;">
    <tr><th style="width:30px;text-align:center;">#</th><th>Intervention</th><th>Key Effect (95% CI)</th><th>Cost</th><th>Evidence</th></tr>
    <tr><td style="text-align:center;">1</td><td>Vitamin A suppl. (6–59 mo)</td><td>RR 0.88 all-cause mortality (0.83–0.93)</td><td>$1–3/child/yr</td><td>A — 3 Cochrane</td></tr>
    <tr><td style="text-align:center;">2</td><td>Iron–folic acid (pregnancy)</td><td>RR 0.52 maternal anaemia (0.41–0.66)</td><td>$0.50–2/pregnancy</td><td>A</td></tr>
    <tr><td style="text-align:center;">3</td><td>Multiple micronutrient suppl.</td><td>RR 0.88 low birthweight (0.85–0.91)</td><td>$1.50–3.50/pregnancy</td><td>A — Cochrane</td></tr>
    <tr><td style="text-align:center;">4</td><td>Large-scale fortification</td><td>RR 0.66 anaemia (0.59–0.74)</td><td>$0.05–0.50/person/yr</td><td>A</td></tr>
    <tr><td style="text-align:center;">5</td><td>Exclusive breastfeeding promo.</td><td>823K under-5 deaths preventable/yr</td><td>Very low per beneficiary</td><td>A</td></tr>
  </table>
  <h2 style="color:#d4a017;margin-top:14px;">Key Limitations</h2>
  <ul class="lim-list" style="color:#ccc;">
    <li><strong style="color:#d4a017;">No cost-effectiveness papers retrieved</strong> despite dedicated search track — all cost ratings rely on LLM external knowledge</li>
    <li><strong style="color:#d4a017;">43/100 papers abstract-only</strong> — effect sizes not independently verified from full text for nearly half the evidence base</li>
    <li><strong style="color:#d4a017;">Geographic concentration</strong> in South Asia and East/West Africa — Latin America, Central Asia, Pacific Islands underrepresented</li>
  </ul>
  <div class="slide-number">10</div>
</div>
