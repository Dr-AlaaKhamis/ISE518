```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Power System Reliability — Executive Fault Dashboard</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
  :root{
    --bg:#f4f6fa; --card:#ffffff; --ink:#0f172a; --muted:#64748b; --line:#e2e8f0;
    --accent:#2563eb; --accent-soft:#eff6ff; --bad:#dc2626; --good:#16a34a;
    --font: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  }
  *{box-sizing:border-box}
  html,body{margin:0;padding:0}
  body{background:var(--bg);color:var(--ink);font-family:var(--font);font-size:14px;line-height:1.45;-webkit-font-smoothing:antialiased}

  /* ---------- Header ---------- */
  .topbar{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.94);backdrop-filter:blur(6px);border-bottom:1px solid var(--line)}
  .wrap{max-width:1480px;margin:0 auto;padding:0 20px}
  .topbar-inner{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:12px 0}
  h1{font-size:20px;margin:0;font-weight:700;letter-spacing:-.01em}
  h1 .bolt{color:var(--accent)}
  #subtitle{margin:3px 0 0;color:var(--muted);font-size:13px}
  #subtitle b{color:var(--ink)}
  .btn{font:inherit;font-size:13px;font-weight:600;border:1px solid var(--accent);color:var(--accent);background:#fff;border-radius:8px;padding:8px 14px;cursor:pointer;white-space:nowrap;transition:background .15s}
  .btn:hover{background:var(--accent-soft)}
  .btn.dim{opacity:.55}

  /* ---------- Grid ---------- */
  main{padding-top:18px;padding-bottom:32px}
  .grid{display:grid;grid-template-columns:repeat(12,minmax(0,1fr));gap:16px}
  .span-2{grid-column:span 2}.span-3{grid-column:span 3}.span-4{grid-column:span 4}
  .span-5{grid-column:span 5}.span-7{grid-column:span 7}.span-8{grid-column:span 8}.span-12{grid-column:span 12}

  .card{background:var(--card);border-radius:12px;box-shadow:0 1px 2px rgba(15,23,42,.06),0 4px 14px rgba(15,23,42,.05);padding:16px 18px;position:relative;min-width:0}
  .card h3{font-size:15px;margin:0;line-height:1.35;font-weight:650;color:var(--ink)}
  .cap{margin:4px 0 8px;font-size:12px;color:var(--muted)}
  .plot{width:100%;height:300px}
  .plot.h-lg{height:420px}
  .plot.h-md{height:330px}

  /* ---------- Filters ---------- */
  .filters h2{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin:0 0 10px;font-weight:700}
  .filter-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px 20px}
  .fhead{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px;font-size:12px;font-weight:650;color:var(--ink)}
  .link{font:inherit;font-size:11px;font-weight:600;color:var(--accent);background:none;border:none;cursor:pointer;padding:0}
  .chips{display:flex;flex-wrap:wrap;gap:6px}
  .chip{display:inline-flex;align-items:center;gap:6px;border:1px solid var(--line);background:#fff;border-radius:999px;padding:4px 10px;font:inherit;font-size:12px;cursor:pointer;color:var(--muted);transition:all .12s}
  .chip:hover{border-color:#94a3b8}
  .chip.on{background:var(--accent-soft);border-color:#bfdbfe;color:var(--ink)}
  .chip .dot{width:8px;height:8px;border-radius:50%;flex:none}
  .chip:not(.on) .dot{opacity:.3}
  .chip .cnt{font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums}

  /* Dual-handle range slider: two stacked native range inputs */
  .rval{font-weight:600;color:var(--accent);font-variant-numeric:tabular-nums}
  .range-wrap{position:relative;height:28px}
  .range-track,.range-fill{position:absolute;top:12px;height:4px;border-radius:4px}
  .range-track{left:0;right:0;background:var(--line)}
  .range-fill{background:var(--accent)}
  .range-wrap input[type=range]{position:absolute;left:0;top:6px;width:100%;height:16px;margin:0;background:none;pointer-events:none;-webkit-appearance:none;appearance:none}
  .range-wrap input[type=range]::-webkit-slider-runnable-track{background:transparent;height:16px}
  .range-wrap input[type=range]::-moz-range-track{background:transparent;height:16px}
  .range-wrap input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;pointer-events:auto;width:16px;height:16px;border-radius:50%;background:#fff;border:2px solid var(--accent);box-shadow:0 1px 3px rgba(0,0,0,.2);cursor:pointer}
  .range-wrap input[type=range]::-moz-range-thumb{pointer-events:auto;width:13px;height:13px;border-radius:50%;background:#fff;border:2px solid var(--accent);box-shadow:0 1px 3px rgba(0,0,0,.2);cursor:pointer}
  .range-wrap input[type=range]:focus{outline:none}
  .range-wrap input[type=range]:focus-visible::-webkit-slider-thumb{box-shadow:0 0 0 4px rgba(37,99,235,.25)}
  .range-ends{display:flex;justify-content:space-between;font-size:11px;color:var(--muted);font-variant-numeric:tabular-nums}

  /* ---------- KPI cards ---------- */
  .kpi{padding:14px 16px;border-top:3px solid var(--accent)}
  .kpi .label{font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);font-weight:700}
  .kpi .value{font-size:27px;font-weight:700;margin:4px 0 2px;font-variant-numeric:tabular-nums;letter-spacing:-.01em}
  .kpi .value small{font-size:15px;font-weight:600;color:var(--muted);margin-left:2px}
  .kpi .ctx{font-size:12px;color:var(--muted)}
  .bad{color:var(--bad);font-weight:600}.good{color:var(--good);font-weight:600}.flat{color:var(--muted);font-weight:600}

  /* ---------- Insights ---------- */
  .insights ul{list-style:none;margin:8px 0 0;padding:0}
  .insights li{position:relative;padding:9px 0 9px 22px;border-bottom:1px solid var(--line);font-size:13.5px;line-height:1.45}
  .insights li:last-child{border-bottom:none}
  .insights li::before{content:"";position:absolute;left:4px;top:15px;width:8px;height:8px;border-radius:50%;background:var(--accent)}
  .insights b{color:var(--ink)}

  /* ---------- Empty state ---------- */
  .empty-msg{display:none;position:absolute;inset:70px 18px 18px 18px;align-items:center;justify-content:center;text-align:center;color:var(--muted);font-size:13px;background:repeating-linear-gradient(45deg,#fafbfc,#fafbfc 8px,#f4f6f9 8px,#f4f6f9 16px);border-radius:8px}
  body.is-empty .empty-msg{display:flex}
  body.is-empty .plot{visibility:hidden}
  .banner{display:none;background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;border-radius:10px;padding:10px 14px;font-size:13px}
  body.is-empty .banner{display:block}

  /* ---------- Responsive ---------- */
  @media (max-width:1100px){
    .span-2{grid-column:span 4}
    .span-3,.span-4{grid-column:span 6}
    .span-5,.span-7,.span-8{grid-column:span 12}
    .md-12{grid-column:span 12}
  }
  @media (max-width:720px){
    .topbar{position:static}
    .topbar-inner{flex-direction:column;align-items:flex-start}
    .span-2{grid-column:span 6}
    .span-3,.span-4,.md-12{grid-column:span 12}
    h1{font-size:17px}
    .plot.h-lg{height:360px}
  }
  @media (max-width:480px){
    .span-2{grid-column:span 12}
    .wrap{padding:0 12px}
  }
</style>
</head>
<body>

<header class="topbar">
  <div class="wrap topbar-inner">
    <div>
      <h1><span class="bolt">⚡</span> Power System Reliability — Executive Fault Dashboard</h1>
      <p id="subtitle">Loading…</p>
    </div>
    <button class="btn" id="resetBtn" type="button" title="Clear every slicer">Reset filters</button>
  </div>
</header>

<main class="wrap">
  <div class="grid">

    <!-- ===== Slicers ===== -->
    <section class="card filters span-12" aria-label="Filters">
      <h2>Filters</h2>
      <div class="filter-grid">
        <div class="fgroup"><div class="fhead"><span>Fault type</span><button class="link" data-all="fault_type" type="button">All</button></div><div class="chips" id="chips-fault_type"></div></div>
        <div class="fgroup"><div class="fhead"><span>Weather condition</span><button class="link" data-all="weather" type="button">All</button></div><div class="chips" id="chips-weather"></div></div>
        <div class="fgroup"><div class="fhead"><span>Maintenance status</span><button class="link" data-all="maintenance" type="button">All</button></div><div class="chips" id="chips-maintenance"></div></div>
        <div class="fgroup"><div class="fhead"><span>Component health</span><button class="link" data-all="health" type="button">All</button></div><div class="chips" id="chips-health"></div></div>
        <div class="fgroup" id="range-downtime"></div>
        <div class="fgroup" id="range-seq"></div>
      </div>
    </section>

    <div class="banner span-12">No faults match the current filters. Widen a slicer or press <b>Reset filters</b>.</div>

    <!-- ===== KPI cards (filled by JS) ===== -->
    <div class="card kpi span-2" id="kpi-faults"></div>
    <div class="card kpi span-2" id="kpi-downtime"></div>
    <div class="card kpi span-2" id="kpi-avgdown"></div>
    <div class="card kpi span-2" id="kpi-avgdur"></div>
    <div class="card kpi span-2" id="kpi-notnormal"></div>
    <div class="card kpi span-2" id="kpi-pending"></div>

    <!-- ===== Row 1: trend + insights ===== -->
    <section class="card span-8">
      <h3 id="t-trend">Reliability trend</h3>
      <p class="cap">Avg downtime (blue, left axis) and fault count (grey, right axis) per 25 consecutive events; dashed line = average of current selection.</p>
      <div class="plot h-md" id="c-trend"></div>
      <div class="empty-msg">No faults match the current filters.</div>
    </section>
    <section class="card insights span-4 md-12">
      <h3>Key insights</h3>
      <p class="cap">Auto-generated from the current selection.</p>
      <ul id="insights"></ul>
    </section>

    <!-- ===== Row 2: bar + heatmap + donut ===== -->
    <section class="card span-4">
      <h3 id="t-bar">Downtime by fault type</h3>
      <p class="cap">Total downtime hours by fault type · click a bar to filter.</p>
      <div class="plot" id="c-bar"></div>
      <div class="empty-msg">No faults match the current filters.</div>
    </section>
    <section class="card span-5 md-12">
      <h3 id="t-heat">Avg downtime by fault type × weather</h3>
      <p class="cap">Average downtime hours per fault (n = faults in cell) · click a cell to focus.</p>
      <div class="plot" id="c-heat"></div>
      <div class="empty-msg">No faults match the current filters.</div>
    </section>
    <section class="card span-3">
      <h3 id="t-donut">Maintenance status</h3>
      <p class="cap">Share of faults by maintenance status · click a slice to filter.</p>
      <div class="plot" id="c-donut"></div>
      <div class="empty-msg">No faults match the current filters.</div>
    </section>

    <!-- ===== Row 3: map + treemap ===== -->
    <section class="card span-7">
      <h3 id="t-map">Where faults occur</h3>
      <p class="cap">Each dot is a fault · size = downtime hours · colour = fault type · map auto-fits to the selection.</p>
      <div class="plot h-lg" id="c-map"></div>
      <div class="empty-msg">No faults match the current filters.</div>
    </section>
    <section class="card span-5">
      <h3 id="t-tree">Fault mix by weather</h3>
      <p class="cap">Tile size = fault count (Weather → Fault type) · colour = avg downtime · click a tile to filter.</p>
      <div class="plot h-lg" id="c-tree"></div>
      <div class="empty-msg">No faults match the current filters.</div>
    </section>

    <!-- ===== Row 4: scatter ===== -->
    <section class="card span-12">
      <h3 id="t-scatter">Load vs downtime</h3>
      <p class="cap">Each dot is a fault, coloured by component health · load values are whole MW, so dots are jittered ±0.25 MW horizontally for visibility (hover shows exact values).</p>
      <div class="plot" id="c-scatter"></div>
      <div class="empty-msg">No faults match the current filters.</div>
    </section>

  </div>
</main>

<script>
/* =====================================================================
   DATA — replaced with a JSON array of row objects before opening.
   ===================================================================== */
const RAW_DATA = __DATA_JSON__;

/* =====================================================================
   1. CONFIGURATION (edit here to restyle / re-tune)
   ===================================================================== */
const FONT   = 'system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif';
const ACCENT = '#2563eb';
const BUCKET = 25;   // events per bucket in the trend chart
const MIN_N  = 3;    // minimum faults in a group before it can be called "worst"/"best"
const EPS    = 1e-9; // float tolerance for range filters

const DIMS = ['fault_type', 'weather', 'maintenance', 'health'];
const DIM_LABEL = { fault_type:'Fault type', weather:'Weather', maintenance:'Maintenance', health:'Health' };

// Preferred display order of known categories (unknown ones are appended alphabetically).
const KNOWN = {
  fault_type:  ['Line Breakage', 'Overheating', 'Transformer Failure'],
  weather:     ['Clear', 'Rainy', 'Snowy', 'Thunderstorm', 'Windstorm'],
  maintenance: ['Completed', 'Scheduled', 'Pending'],
  health:      ['Normal', 'Overheated', 'Faulty']
};

// One categorical palette per dimension — shared by every chart & chip.
const PALETTE = {
  fault_type:  { 'Line Breakage':'#06b6d4', 'Overheating':'#f97316', 'Transformer Failure':'#8b5cf6' },
  weather:     { 'Clear':'#fbbf24', 'Rainy':'#3b82f6', 'Snowy':'#7dd3fc', 'Thunderstorm':'#475569', 'Windstorm':'#14b8a6' },
  maintenance: { 'Completed':'#0f766e', 'Scheduled':'#93c5fd', 'Pending':'#d97706' },
  health:      { 'Normal':'#16a34a', 'Overheated':'#f59e0b', 'Faulty':'#dc2626' }
};
const FALLBACK_COLORS = ['#64748b', '#e11d48', '#84cc16', '#0ea5e9', '#a855f7', '#78716c'];

// Sequential scale for "avg downtime" (light = short, dark red = long). Used by treemap & heatmap.
const DOWN_SCALE = [[0, '#fff7ed'], [0.5, '#fb923c'], [1, '#b91c1c']];

const PLOT_CONFIG = {
  responsive: true, displaylogo: false, displayModeBar: 'hover',
  modeBarButtonsToRemove: ['select2d', 'lasso2d', 'autoScale2d', 'toggleSpikelines',
                           'hoverCompareCartesian', 'hoverClosestCartesian']
};

/* =====================================================================
   2. HELPERS — formatting & maths
   ===================================================================== */
const fmt1 = v => Number.isFinite(v) ? v.toLocaleString('en-US', { minimumFractionDigits: 1, maximumFractionDigits: 1 }) : '—';
const fmt0 = v => Number.isFinite(v) ? Math.round(v).toLocaleString('en-US') : '—';
const pct1 = v => Number.isFinite(v) ? fmt1(v) + '%' : '—';
const signed1 = v => (v > 0 ? '+' : v < 0 ? '−' : '') + fmt1(Math.abs(v));
const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' }[c]));
const num = v => { const n = typeof v === 'number' ? v : parseFloat(v); return Number.isFinite(n) ? n : NaN; };

function hexA(hex, a) { // '#rrggbb' -> 'rgba(r,g,b,a)'
  const h = hex.replace('#', '');
  const n = parseInt(h.length === 3 ? h.split('').map(c => c + c).join('') : h, 16);
  return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`;
}
function colorOf(dim, cat) {
  if (PALETTE[dim] && PALETTE[dim][cat]) return PALETTE[dim][cat];
  let h = 0; for (const ch of String(cat)) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
  return FALLBACK_COLORS[h % FALLBACK_COLORS.length];
}
// Aggregate a list of rows into count / total / averages (NaN-safe).
function agg(rows) {
  let tot = 0, dur = 0, nd = 0;
  for (const r of rows) {
    if (Number.isFinite(r.downtime_h)) tot += r.downtime_h;
    if (Number.isFinite(r.duration_h)) { dur += r.duration_h; nd++; }
  }
  const n = rows.length;
  return { n, total: tot, avg: n ? tot / n : NaN, avgDur: nd ? dur / nd : NaN };
}
// Group rows by a field and aggregate each group -> Map(category -> agg)
function groupAgg(rows, field) {
  const buckets = new Map();
  for (const r of rows) { if (!buckets.has(r[field])) buckets.set(r[field], []); buckets.get(r[field]).push(r); }
  const out = new Map(); buckets.forEach((rs, k) => out.set(k, agg(rs))); return out;
}
function pearson(xs, ys) {
  const n = xs.length; if (n < 3) return NaN;
  const mx = xs.reduce((a, b) => a + b, 0) / n, my = ys.reduce((a, b) => a + b, 0) / n;
  let sxy = 0, sxx = 0, syy = 0;
  for (let i = 0; i < n; i++) { const dx = xs[i] - mx, dy = ys[i] - my; sxy += dx * dy; sxx += dx * dx; syy += dy * dy; }
  return (sxx && syy) ? sxy / Math.sqrt(sxx * syy) : NaN;
}
// Deterministic pseudo-random jitter in [-0.5, 0.5) keyed by event seq (stable across re-renders).
const jitter = seq => (((seq * 9301 + 49297) % 233280) / 233280) - 0.5;

/* =====================================================================
   3. DATA PREPARATION — coerce types once
   ===================================================================== */
const DATA = (Array.isArray(RAW_DATA) ? RAW_DATA : []).map((r, i) => {
  const s = num(r.seq);
  const seq = Number.isFinite(s) ? s : (parseInt(String(r.fault_id || '').replace(/\D/g, ''), 10) || i + 1);
  return {
    fault_id: String(r.fault_id ?? ('F' + seq)), seq,
    fault_type: String(r.fault_type ?? 'Unknown'), weather: String(r.weather ?? 'Unknown'),
    maintenance: String(r.maintenance ?? 'Unknown'), health: String(r.health ?? 'Unknown'),
    voltage_v: num(r.voltage_v), current_a: num(r.current_a), load_mw: num(r.load_mw),
    temp_c: num(r.temp_c), wind_kmh: num(r.wind_kmh),
    duration_h: num(r.duration_h), downtime_h: num(r.downtime_h),
    lat: num(r.lat), lon: num(r.lon)
  };
});

// Category lists: known order first, then any unexpected values found in the data.
const CATS = {};
DIMS.forEach(d => {
  const present = new Set(DATA.map(r => r[d]));
  CATS[d] = DATA.length
    ? KNOWN[d].filter(c => present.has(c)).concat([...present].filter(c => !KNOWN[d].includes(c)).sort())
    : KNOWN[d].slice();
});

// Dataset-wide baseline (used for KPI context lines and slider bounds).
const BASE = (() => {
  const a = agg(DATA);
  const dts = DATA.map(r => r.downtime_h).filter(Number.isFinite);
  const seqs = DATA.map(r => r.seq).filter(Number.isFinite);
  const geo = DATA.filter(r => Number.isFinite(r.lat) && Number.isFinite(r.lon));
  return {
    ...a,
    pctNotNormal: a.n ? DATA.filter(r => r.health !== 'Normal').length / a.n * 100 : NaN,
    pctPending:   a.n ? DATA.filter(r => r.maintenance === 'Pending').length / a.n * 100 : NaN,
    dtMin: dts.length ? Math.floor(Math.min(...dts) * 10) / 10 : 0,
    dtMax: dts.length ? Math.ceil(Math.max(...dts) * 10) / 10 : 1,
    seqMin: seqs.length ? Math.min(...seqs) : 1,
    seqMax: seqs.length ? Math.max(...seqs) : 1,
    center: geo.length
      ? { lat: geo.reduce((s, r) => s + r.lat, 0) / geo.length, lon: geo.reduce((s, r) => s + r.lon, 0) / geo.length }
      : { lat: 0, lon: 0 }
  };
})();

/* =====================================================================
   4. FILTER STATE
   ===================================================================== */
function defaultState() {
  return {
    sets: Object.fromEntries(DIMS.map(d => [d, new Set(CATS[d])])),
    downtime: [BASE.dtMin, BASE.dtMax],
    seq: [BASE.seqMin, BASE.seqMax]
  };
}
let state = defaultState();

// Apply every filter; `except` skips one categorical dimension (used for chip counts).
function filterRows(except = null) {
  const [dLo, dHi] = state.downtime, [sLo, sHi] = state.seq;
  return DATA.filter(r => {
    for (const d of DIMS) if (d !== except && !state.sets[d].has(r[d])) return false;
    if (!(r.downtime_h >= dLo - EPS && r.downtime_h <= dHi + EPS)) return false;
    if (r.seq < sLo || r.seq > sHi) return false;
    return true;
  });
}
function rangeIsDefault(key) {
  const def = key === 'downtime' ? [BASE.dtMin, BASE.dtMax] : [BASE.seqMin, BASE.seqMax];
  return Math.abs(state[key][0] - def[0]) < EPS && Math.abs(state[key][1] - def[1]) < EPS;
}
function isFiltered() {
  return DIMS.some(d => state.sets[d].size !== CATS[d].length) || !rangeIsDefault('downtime') || !rangeIsDefault('seq');
}

/* Cross-filter "toggle" used by chart clicks:
   - if every category is selected, the click focuses on the clicked one;
   - otherwise it toggles that category in/out of the selection;
   - if that would leave nothing selected, the slicer resets to all. */
function focusCategory(dim, cat) {
  if (!CATS[dim].includes(cat)) return;
  const s = state.sets[dim];
  if (s.size === CATS[dim].length) state.sets[dim] = new Set([cat]);
  else if (s.has(cat)) { s.delete(cat); if (s.size === 0) state.sets[dim] = new Set(CATS[dim]); }
  else s.add(cat);
}

/* =====================================================================
   5. SLICER UI — chips and dual-handle range sliders
   ===================================================================== */
function buildChips() {
  DIMS.forEach(d => {
    const box = document.getElementById('chips-' + d);
    box.innerHTML = CATS[d].map(c =>
      `<button type="button" class="chip on" data-dim="${d}" data-cat="${esc(c)}" aria-pressed="true">
         <span class="dot" style="background:${colorOf(d, c)}"></span>${esc(c)} <span class="cnt"></span></button>`).join('');
    box.addEventListener('click', e => {
      const b = e.target.closest('.chip'); if (!b) return;
      const s = state.sets[d], c = b.dataset.cat;
      s.has(c) ? s.delete(c) : s.add(c);      // plain toggle (empty allowed → friendly empty state)
      render();
    });
  });
  document.querySelectorAll('[data-all]').forEach(btn => btn.addEventListener('click', () => {
    state.sets[btn.dataset.all] = new Set(CATS[btn.dataset.all]); render();
  }));
}
// Refresh chip on/off styling and counts (count = faults matching all OTHER filters).
function syncChips() {
  DIMS.forEach(d => {
    const counts = new Map(); filterRows(d).forEach(r => counts.set(r[d], (counts.get(r[d]) || 0) + 1));
    document.querySelectorAll(`#chips-${d} .chip`).forEach(b => {
      const on = state.sets[d].has(b.dataset.cat);
      b.classList.toggle('on', on); b.setAttribute('aria-pressed', on);
      b.querySelector('.cnt').textContent = fmt0(counts.get(b.dataset.cat) || 0);
    });
  });
}

const RANGE_DEF = {
  downtime: { label: 'Downtime (hrs)', step: 0.1, dec: 1, fmt: v => fmt1(v) + ' h',
              get min() { return BASE.dtMin; }, get max() { return BASE.dtMax; } },
  seq:      { label: 'Event sequence (seq)', step: 1, dec: 0, fmt: v => '#' + fmt0(v),
              get min() { return BASE.seqMin; }, get max() { return BASE.seqMax; } }
};
function buildRange(key) {
  const R = RANGE_DEF[key], root = document.getElementById('range-' + key);
  root.innerHTML = `
    <div class="fhead"><span>${R.label}</span><span class="rval" id="rval-${key}"></span></div>
    <div class="range-wrap">
      <div class="range-track"></div><div class="range-fill" id="rfill-${key}"></div>
      <input type="range" id="rlo-${key}" min="${R.min}" max="${R.max}" step="${R.step}" aria-label="${R.label} minimum">
      <input type="range" id="rhi-${key}" min="${R.min}" max="${R.max}" step="${R.step}" aria-label="${R.label} maximum">
    </div>
    <div class="range-ends"><span>${R.fmt(R.min)}</span><span>${R.fmt(R.max)}</span></div>`;
  const lo = document.getElementById('rlo-' + key), hi = document.getElementById('rhi-' + key);
  const round = v => +(+v).toFixed(R.dec);
  lo.addEventListener('input', () => { state[key][0] = Math.min(round(lo.value), state[key][1]); syncRange(key); scheduleRender(); });
  hi.addEventListener('input', () => { state[key][1] = Math.max(round(hi.value), state[key][0]); syncRange(key); scheduleRender(); });
}
function syncRange(key) {
  const R = RANGE_DEF[key], [a, b] = state[key];
  const lo = document.getElementById('rlo-' + key), hi = document.getElementById('rhi-' + key);
  lo.value = a; hi.value = b;
  const span = (R.max - R.min) || 1;
  const fill = document.getElementById('rfill-' + key);
  fill.style.left = ((a - R.min) / span * 100) + '%';
  fill.style.width = ((b - a) / span * 100) + '%';
  // Keep the low thumb grabbable when both handles sit near the top end.
  lo.style.zIndex = (a - R.min) / span > 0.5 ? 5 : 3; hi.style.zIndex = 4;
  document.getElementById('rval-' + key).textContent = `${R.fmt(a)} – ${R.fmt(b)}`;
}

/* =====================================================================
   6. HEADER & KPI CARDS
   ===================================================================== */
function renderHeader(rows) {
  const parts = [];
  DIMS.forEach(d => {
    const s = state.sets[d];
    if (s.size !== CATS[d].length) parts.push(`${DIM_LABEL[d]}: ${s.size ? CATS[d].filter(c => s.has(c)).map(esc).join(', ') : 'none'}`);
  });
  if (!rangeIsDefault('downtime')) parts.push(`Downtime ${fmt1(state.downtime[0])}–${fmt1(state.downtime[1])} h`);
  if (!rangeIsDefault('seq')) parts.push(`Events #${fmt0(state.seq[0])}–#${fmt0(state.seq[1])}`);
  document.getElementById('subtitle').innerHTML =
    `Showing <b>${fmt0(rows.length)}</b> of ${fmt0(BASE.n)} fault records · ` + (parts.length ? parts.join(' · ') : 'No filters applied');
  document.getElementById('resetBtn').classList.toggle('dim', !isFiltered());
}

// Context line comparing a value to the dataset baseline. higherIsBad drives red/green.
function deltaLine(cur, base, unit, baseTxt, higherIsBad = true) {
  if (!Number.isFinite(cur) || !Number.isFinite(base)) return '&nbsp;';
  const d = Math.round((cur - base) * 10) / 10;
  if (Math.abs(d) < 0.05) return `<span class="flat">● on par</span> with dataset ${baseTxt}`;
  const bad = higherIsBad ? d > 0 : d < 0;
  return `<span class="${bad ? 'bad' : 'good'}">${d > 0 ? '▲' : '▼'} ${fmt1(Math.abs(d))}${unit}</span> vs dataset ${baseTxt}`;
}
function kpiCard(id, label, valueHTML, ctxHTML) {
  document.getElementById(id).innerHTML =
    `<div class="label">${label}</div><div class="value">${valueHTML}</div><div class="ctx">${ctxHTML}</div>`;
}
function renderKPIs(rows, A) {
  const n = rows.length;
  const notNormal = n ? rows.filter(r => r.health !== 'Normal').length / n * 100 : NaN;
  const pending   = n ? rows.filter(r => r.maintenance === 'Pending').length / n * 100 : NaN;
  kpiCard('kpi-faults', 'Total faults', fmt0(n),
    `${pct1(BASE.n ? n / BASE.n * 100 : NaN)} of ${fmt0(BASE.n)} recorded`);
  kpiCard('kpi-downtime', 'Total downtime', n ? `${fmt1(A.total)}<small>h</small>` : '—',
    `${pct1(BASE.total ? A.total / BASE.total * 100 : NaN)} of ${fmt1(BASE.total)} h dataset total`);
  kpiCard('kpi-avgdown', 'Avg downtime / fault', n ? `${fmt1(A.avg)}<small>h</small>` : '—',
    deltaLine(A.avg, BASE.avg, ' h', `${fmt1(BASE.avg)} h`));
  kpiCard('kpi-avgdur', 'Avg fault duration', n ? `${fmt1(A.avgDur)}<small>h</small>` : '—',
    deltaLine(A.avgDur, BASE.avgDur, ' h', `${fmt1(BASE.avgDur)} h`));
  kpiCard('kpi-notnormal', 'Components not Normal', n ? pct1(notNormal) : '—',
    deltaLine(notNormal, BASE.pctNotNormal, ' pp', pct1(BASE.pctNotNormal)));
  kpiCard('kpi-pending', 'Maintenance Pending', n ? pct1(pending) : '—',
    deltaLine(pending, BASE.pctPending, ' pp', pct1(BASE.pctPending)));
}

/* =====================================================================
   7. CHARTS — each sets its takeaway title from the filtered data
   ===================================================================== */
const setTitle = (id, txt) => { document.getElementById(id).textContent = txt; };
const AXIS = { gridcolor: '#eef2f7', zeroline: false, linecolor: '#cbd5e1', tickfont: { size: 11 }, automargin: true };
function baseLayout(extra) {
  return Object.assign({
    font: { family: FONT, size: 12, color: '#334155' },
    paper_bgcolor: 'rgba(0,0,0,0)', plot_bgcolor: 'rgba(0,0,0,0)',
    margin: { l: 50, r: 20, t: 10, b: 40 },
    hoverlabel: { bgcolor: '#ffffff', bordercolor: '#cbd5e1', font: { family: FONT, size: 12, color: '#0f172a' } },
    showlegend: false
  }, extra);
}
// Pick the group with the max (or min) of `key`, preferring groups with n >= MIN_N.
function pick(list, key, dir = 1) {
  const pool = list.filter(x => x.n >= MIN_N).length ? list.filter(x => x.n >= MIN_N) : list;
  return pool.reduce((best, x) => (best == null || dir * (x[key] - best[key]) > 0) ? x : best, null);
}

/* 7.1 LINE — reliability trend per bucket of 25 events (dual axis) */
function renderTrend(rows, A) {
  const m = new Map();
  rows.forEach(r => { const b = Math.floor((r.seq - BASE.seqMin) / BUCKET); if (!m.has(b)) m.set(b, []); m.get(b).push(r); });
  const buckets = [...m.keys()].sort((a, b) => a - b).map(b => {
    const s = BASE.seqMin + b * BUCKET, e = Math.min(s + BUCKET - 1, BASE.seqMax);
    return { label: `${s}–${e}`, ...agg(m.get(b)) };
  });
  const x = buckets.map(b => b.label);
  Plotly.react('c-trend', [
    { x, y: buckets.map(b => b.avg), name: 'Avg downtime (h)', type: 'scatter', mode: 'lines+markers',
      line: { color: ACCENT, width: 3 }, marker: { size: 6, color: ACCENT },
      hovertemplate: 'Avg downtime: <b>%{y:.1f} h</b><extra></extra>' },
    { x, y: buckets.map(b => b.n), name: 'Faults (count)', yaxis: 'y2', type: 'scatter', mode: 'lines+markers',
      line: { color: '#94a3b8', width: 2, dash: 'dot' }, marker: { size: 5, color: '#94a3b8' },
      hovertemplate: 'Faults: <b>%{y}</b><extra></extra>' }
  ], baseLayout({
    showlegend: true, legend: { orientation: 'h', x: 0, y: 1.12, font: { size: 11 } },
    margin: { l: 52, r: 50, t: 30, b: 60 }, hovermode: 'x unified',
    xaxis: { ...AXIS, type: 'category', title: { text: `Event sequence (buckets of ${BUCKET})`, font: { size: 11 } }, tickangle: -40, showgrid: false },
    yaxis: { ...AXIS, title: { text: 'Avg downtime (h)', font: { size: 11 } } },
    yaxis2: { ...AXIS, title: { text: 'Faults', font: { size: 11 } }, overlaying: 'y', side: 'right', showgrid: false, rangemode: 'tozero' },
    shapes: [{ type: 'line', xref: 'paper', x0: 0, x1: 1, yref: 'y', y0: A.avg, y1: A.avg, line: { color: ACCENT, width: 1.5, dash: 'dash' } }],
    annotations: [{ xref: 'paper', x: 0, xanchor: 'left', yref: 'y', y: A.avg, yanchor: 'bottom', showarrow: false,
                    text: `Avg ${fmt1(A.avg)} h`, font: { size: 11, color: ACCENT }, bgcolor: 'rgba(255,255,255,.8)' }]
  }), PLOT_CONFIG);

  if (buckets.length === 1) {
    setTitle('t-trend', `All selected faults fall in events ${buckets[0].label}: ${fmt1(buckets[0].avg)} h average downtime`);
  } else {
    const peak = pick(buckets, 'avg', 1), last = buckets[buckets.length - 1];
    const rel = last.avg > A.avg + 0.05 ? 'above' : last.avg < A.avg - 0.05 ? 'below' : 'in line with';
    setTitle('t-trend', `Downtime peaked at ${fmt1(peak.avg)} h in events ${peak.label}; latest bucket (${last.label}) is ${rel} the ${fmt1(A.avg)} h average at ${fmt1(last.avg)} h`);
  }
}

/* 7.2 BAR — total downtime by fault type (sorted, top highlighted) */
function renderBar(rows, A) {
  const g = groupAgg(rows, 'fault_type');
  const arr = CATS.fault_type.filter(c => g.has(c)).map(c => ({ c, ...g.get(c) })).sort((a, b) => a.total - b.total);
  const top = arr[arr.length - 1];
  const share = t => A.total ? t / A.total * 100 : 0;
  Plotly.react('c-bar', [{
    type: 'bar', orientation: 'h', y: arr.map(d => d.c), x: arr.map(d => d.total),
    marker: { color: arr.map(d => d === top ? colorOf('fault_type', d.c) : hexA(colorOf('fault_type', d.c), 0.35)) },
    text: arr.map(d => `${fmt1(d.total)} h · ${fmt1(share(d.total))}%`), textposition: 'outside', cliponaxis: false,
    textfont: { size: 11, color: '#334155' },
    customdata: arr.map(d => [d.n, d.avg, share(d.total)]),
    hovertemplate: '<b>%{y}</b><br>Total downtime: %{x:.1f} h<br>Share: %{customdata[2]:.1f}%<br>Faults: %{customdata[0]}<br>Avg per fault: %{customdata[1]:.1f} h<extra></extra>'
  }], baseLayout({
    margin: { l: 10, r: 20, t: 6, b: 40 }, bargap: 0.35,
    xaxis: { ...AXIS, title: { text: 'Total downtime (h)', font: { size: 11 } }, range: [0, (top ? top.total : 1) * 1.45] },
    yaxis: { ...AXIS, showgrid: false }
  }), PLOT_CONFIG);
  setTitle('t-bar', arr.length > 1
    ? `${top.c} drives the most downtime: ${fmt1(top.total)} h (${fmt1(share(top.total))}% of total)`
    : `${top.c}: ${fmt1(top.total)} h of downtime across ${fmt0(top.n)} faults`);
}

/* 7.3 TREEMAP — Weather → Fault type, size = count, colour = avg downtime */
function renderTreemap(rows) {
  const ids = [], labels = [], parents = [], values = [], colors = [], cd = [];
  const tiles = [];
  const byW = groupAgg(rows, 'weather');
  CATS.weather.filter(w => byW.has(w)).forEach(w => {
    const wa = byW.get(w);
    ids.push(w); labels.push(w); parents.push(''); values.push(wa.n); colors.push(wa.avg); cd.push([fmt1(wa.avg), w]);
    const byF = groupAgg(rows.filter(r => r.weather === w), 'fault_type');
    CATS.fault_type.filter(f => byF.has(f)).forEach(f => {
      const fa = byF.get(f);
      ids.push(w + '||' + f); labels.push(f); parents.push(w); values.push(fa.n); colors.push(fa.avg);
      cd.push([fmt1(fa.avg), `${w} › ${f}`]); tiles.push({ w, f, ...fa });
    });
  });
  let cmin = Math.min(...colors), cmax = Math.max(...colors);
  if (cmax - cmin < 0.1) { cmin -= 0.5; cmax += 0.5; }
  Plotly.react('c-tree', [{
    type: 'treemap', ids, labels, parents, values, branchvalues: 'total', customdata: cd,
    marker: { colors, colorscale: DOWN_SCALE, cmin, cmax, showscale: true, line: { color: '#ffffff', width: 2 },
              colorbar: { title: { text: 'Avg h', font: { size: 11 } }, thickness: 10, len: 0.8, tickformat: '.1f', outlinewidth: 0 } },
    root: { color: '#f8fafc' }, pathbar: { visible: false }, tiling: { pad: 3 },
    texttemplate: '<b>%{label}</b><br>%{value} faults · %{customdata[0]} h',
    hovertemplate: '<b>%{customdata[1]}</b><br>Faults: %{value}<br>Avg downtime: %{customdata[0]} h<extra></extra>'
  }], baseLayout({ margin: { l: 0, r: 0, t: 0, b: 0 } }), PLOT_CONFIG);

  const wl = [...byW].map(([k, v]) => ({ k, ...v }));
  const most = wl.reduce((b, x) => (!b || x.n > b.n) ? x : b, null);
  const hot = pick(tiles, 'avg', 1);
  setTitle('t-tree', hot
    ? `${most.k} logs the most faults (${fmt0(most.n)}); costliest tile: ${hot.w} › ${hot.f} at ${fmt1(hot.avg)} h avg`
    : `${most.k} logs the most faults (${fmt0(most.n)})`);
}

/* 7.4 MAP — every fault as a point, auto-fit to the selection */
function fitMap(pts, W, H) {
  if (!pts.length) return { center: BASE.center, zoom: 8 };
  const lats = pts.map(p => p.lat), lons = pts.map(p => p.lon);
  const latMin = Math.min(...lats), latMax = Math.max(...lats), lonMin = Math.min(...lons), lonMax = Math.max(...lons);
  const merc = lat => Math.log(Math.tan(Math.PI / 4 + lat * Math.PI / 360)); // Web-Mercator y (radians)
  const y0 = merc(latMin), y1 = merc(latMax);
  const lonSpan = Math.max(lonMax - lonMin, 0.004), ySpan = Math.max(y1 - y0, 0.00007);
  // 512-px tiles: world width at zoom z = 512·2^z px
  const zLon = Math.log2((W * 360) / (512 * lonSpan));
  const zLat = Math.log2((H * 2 * Math.PI) / (512 * ySpan));
  const zoom = Math.max(1, Math.min(zLon, zLat, 13) - 0.45); // padding so edge dots are not clipped
  const yMid = (y0 + y1) / 2;
  return { center: { lat: (2 * Math.atan(Math.exp(yMid)) - Math.PI / 2) * 180 / Math.PI, lon: (lonMin + lonMax) / 2 }, zoom };
}
function renderMap(rows) {
  const pts = rows.filter(r => Number.isFinite(r.lat) && Number.isFinite(r.lon));
  const traces = CATS.fault_type.filter(f => pts.some(r => r.fault_type === f)).map(f => {
    const rs = pts.filter(r => r.fault_type === f);
    return {
      type: 'scattermap', mode: 'markers', name: f, lat: rs.map(r => r.lat), lon: rs.map(r => r.lon),
      marker: { size: rs.map(r => 5 + (Number.isFinite(r.downtime_h) ? r.downtime_h : 0) * 2.2), color: colorOf('fault_type', f), opacity: 0.72 },
      customdata: rs.map(r => [r.fault_id, r.weather, r.health, fmt1(r.downtime_h), fmt1(r.duration_h), r.maintenance]),
      hovertemplate: '<b>%{customdata[0]}</b> · ' + esc(f) +
        '<br>Weather: %{customdata[1]}<br>Health: %{customdata[2]}<br>Downtime: <b>%{customdata[3]} h</b>' +
        '<br>Duration: %{customdata[4]} h<br>Maintenance: %{customdata[5]}<extra></extra>'
    };
  });
  const el = document.getElementById('c-map');
  const view = fitMap(pts, el.clientWidth || 700, el.clientHeight || 420);
  Plotly.react(el, traces, baseLayout({
    margin: { l: 0, r: 0, t: 0, b: 0 }, showlegend: true,
    legend: { orientation: 'h', x: 0.01, y: 0.99, bgcolor: 'rgba(255,255,255,.88)', bordercolor: '#e2e8f0', borderwidth: 1, font: { size: 11 } },
    map: { style: 'carto-positron', center: view.center, zoom: view.zoom }
  }), PLOT_CONFIG);

  // Takeaway: which sector (relative to the dataset's geographic centre) carries the most downtime.
  const q = new Map(), tot = agg(pts).total;
  pts.forEach(r => {
    const k = `${r.lat >= BASE.center.lat ? 'north' : 'south'}-${r.lon >= BASE.center.lon ? 'east' : 'west'}`;
    q.set(k, (q.get(k) || 0) + (Number.isFinite(r.downtime_h) ? r.downtime_h : 0));
  });
  const best = [...q].sort((a, b) => b[1] - a[1])[0];
  setTitle('t-map', best
    ? `${fmt0(pts.length)} faults mapped — the ${best[0]} sector carries the most downtime (${fmt1(tot ? best[1] / tot * 100 : 0)}% · ${fmt1(best[1])} h)`
    : 'No mappable coordinates in the current selection');
}

/* 7.5 HEATMAP — avg downtime by Fault type × Weather */
function renderHeatmap(rows) {
  const fts = CATS.fault_type.filter(f => rows.some(r => r.fault_type === f));
  const ws  = CATS.weather.filter(w => rows.some(r => r.weather === w));
  const cells = [], z = [], cdat = [];
  fts.forEach(f => {
    const zr = [], cr = [];
    ws.forEach(w => {
      const a = agg(rows.filter(r => r.fault_type === f && r.weather === w));
      zr.push(a.n ? a.avg : null); cr.push(a.n);
      if (a.n) cells.push({ f, w, ...a });
    });
    z.push(zr); cdat.push(cr);
  });
  const vals = cells.map(c => c.avg);
  let zmin = Math.min(...vals), zmax = Math.max(...vals);
  if (zmax - zmin < 0.1) { zmin -= 0.5; zmax += 0.5; }
  const ann = [];
  fts.forEach((f, i) => ws.forEach((w, j) => {
    const v = z[i][j];
    ann.push({ x: w, y: f, showarrow: false,
      text: v == null ? '–' : `<b>${fmt1(v)} h</b><br><span style="font-size:10px">n=${cdat[i][j]}</span>`,
      font: { size: 12, color: v != null && (v - zmin) / (zmax - zmin) > 0.6 ? '#ffffff' : '#0f172a' } });
  }));
  const wrap = s => s.length > 12 ? s.replace(' ', '<br>') : s;
  Plotly.react('c-heat', [{
    type: 'heatmap', x: ws, y: fts, z, customdata: cdat, zmin, zmax, colorscale: DOWN_SCALE, xgap: 3, ygap: 3, hoverongaps: false,
    colorbar: { title: { text: 'Avg h', font: { size: 11 } }, thickness: 10, len: 0.9, tickformat: '.1f', outlinewidth: 0 },
    hovertemplate: '<b>%{y}</b> during <b>%{x}</b><br>Avg downtime: %{z:.1f} h<br>Faults: %{customdata}<extra></extra>'
  }], baseLayout({
    margin: { l: 10, r: 10, t: 6, b: 40 }, annotations: ann,
    xaxis: { ...AXIS, type: 'category', showgrid: false },
    yaxis: { ...AXIS, type: 'category', showgrid: false, tickvals: fts, ticktext: fts.map(wrap) }
  }), PLOT_CONFIG);

  if (cells.length > 1) {
    const worst = pick(cells, 'avg', 1), best = pick(cells, 'avg', -1);
    setTitle('t-heat', `Worst combination: ${worst.f} in ${worst.w} (${fmt1(worst.avg)} h) vs best ${best.f} in ${best.w} (${fmt1(best.avg)} h)`);
  } else setTitle('t-heat', `${cells[0].f} in ${cells[0].w}: ${fmt1(cells[0].avg)} h average downtime`);
}

/* 7.6 DONUT — maintenance status share, Pending % in centre */
function renderDonut(rows) {
  const g = groupAgg(rows, 'maintenance');
  const cats = CATS.maintenance.filter(c => g.has(c));
  const pend = g.get('Pending'), pPct = rows.length ? (pend ? pend.n : 0) / rows.length * 100 : 0;
  Plotly.react('c-donut', [{
    type: 'pie', hole: 0.62, sort: false, direction: 'clockwise',
    labels: cats, values: cats.map(c => g.get(c).n),
    marker: { colors: cats.map(c => colorOf('maintenance', c)), line: { color: '#ffffff', width: 2 } },
    textinfo: 'percent', textfont: { size: 11 }, insidetextorientation: 'horizontal',
    customdata: cats.map(c => [g.get(c).total]),
    hovertemplate: '<b>%{label}</b><br>%{value} faults (%{percent})<br>Downtime: %{customdata[0]:.1f} h<extra></extra>'
  }], baseLayout({
    margin: { l: 10, r: 10, t: 6, b: 10 }, showlegend: true,
    legend: { orientation: 'h', x: 0.5, xanchor: 'center', y: -0.05, font: { size: 11 } },
    annotations: [{ showarrow: false, x: 0.5, y: 0.5, xref: 'paper', yref: 'paper',
      text: `<span style="font-size:22px;color:${colorOf('maintenance', 'Pending')}"><b>${fmt1(pPct)}%</b></span><br><span style="font-size:11px">Pending</span>` }]
  }), PLOT_CONFIG);
  setTitle('t-donut', pend
    ? `${fmt1(pPct)}% of faults (${fmt0(pend.n)}) are on assets with maintenance Pending`
    : 'No faults in view have Pending maintenance');
}

/* 7.7 SCATTER — load vs downtime, coloured by component health */
function renderScatter(rows) {
  const ok = rows.filter(r => Number.isFinite(r.load_mw) && Number.isFinite(r.downtime_h));
  const gh = groupAgg(ok, 'health');
  const traces = CATS.health.filter(h => gh.has(h)).map(h => {
    const rs = ok.filter(r => r.health === h);
    return {
      type: 'scatter', mode: 'markers', name: `${h} · avg ${fmt1(gh.get(h).avg)} h`,
      x: rs.map(r => r.load_mw + jitter(r.seq) * 0.5), y: rs.map(r => r.downtime_h),
      marker: { color: colorOf('health', h), size: 7, opacity: 0.65, line: { color: '#ffffff', width: 0.5 } },
      customdata: rs.map(r => [r.fault_id, r.load_mw, r.fault_type, h]),
      hovertemplate: '<b>%{customdata[0]}</b> · %{customdata[2]}<br>Load: %{customdata[1]} MW<br>Downtime: %{y:.1f} h<br>Health: %{customdata[3]}<extra></extra>'
    };
  });
  Plotly.react('c-scatter', traces, baseLayout({
    showlegend: true, legend: { orientation: 'h', x: 0, y: 1.14, font: { size: 11 } },
    margin: { l: 52, r: 20, t: 30, b: 44 }, hovermode: 'closest',
    xaxis: { ...AXIS, title: { text: 'Power load (MW)', font: { size: 11 } }, dtick: 1 },
    yaxis: { ...AXIS, title: { text: 'Downtime (h)', font: { size: 11 } } }
  }), PLOT_CONFIG);

  const r = pearson(ok.map(d => d.load_mw), ok.map(d => d.downtime_h));
  const hl = [...gh].map(([k, v]) => ({ k, ...v }));
  const worst = pick(hl, 'avg', 1);
  const rTxt = Number.isFinite(r) ? `r = ${signed1(r * 10) === '' ? '' : ''}${r < 0 ? '−' : ''}${Math.abs(r).toFixed(2)}` : 'r n/a';
  const lead = !Number.isFinite(r) ? 'Too few points to judge the load effect'
    : Math.abs(r) < 0.2 ? `Load is not a downtime driver (${rTxt})`
    : r > 0 ? `Higher load means longer downtime (${rTxt})` : `Higher load coincides with shorter downtime (${rTxt})`;
  setTitle('t-scatter', worst && hl.length > 1 ? `${lead}; ${worst.k} components run longest at ${fmt1(worst.avg)} h avg` : lead);
}

/* =====================================================================
   8. KEY INSIGHTS — plain-language bullets, number first
   ===================================================================== */
function renderInsights(rows, A) {
  const ul = document.getElementById('insights');
  if (!rows.length) { ul.innerHTML = '<li>No faults match the current filters — widen a slicer or reset to see insights.</li>'; return; }
  const out = [], toList = m => [...m].map(([k, v]) => ({ k, ...v }));

  // 1. Top downtime driver by fault type
  const byT = toList(groupAgg(rows, 'fault_type')).sort((a, b) => b.total - a.total);
  if (byT.length > 1) out.push(`<b>${fmt1(A.total ? byT[0].total / A.total * 100 : 0)}% of downtime</b> (${fmt1(byT[0].total)} h) comes from <b>${esc(byT[0].k)}</b> faults — the top target for preventive maintenance.`);
  else out.push(`<b>${fmt1(byT[0].total)} h</b> of downtime from ${fmt0(byT[0].n)} <b>${esc(byT[0].k)}</b> faults in view, averaging ${fmt1(byT[0].avg)} h each.`);

  // 2. Costliest weather condition
  const byW = toList(groupAgg(rows, 'weather'));
  if (byW.length > 1) {
    const w = pick(byW, 'avg', 1), d = w.avg - A.avg;
    out.push(`<b>${fmt1(w.avg)} h</b> average downtime during <b>${esc(w.k)}</b> — ${fmt1(Math.abs(d))} h ${d >= 0 ? 'above' : 'below'} the ${fmt1(A.avg)} h norm and the costliest weather; pre-position crews when it is forecast.`);
  }

  // 3. Downtime on non-Normal components
  const nn = rows.filter(r => r.health !== 'Normal'), nnA = agg(nn);
  const nnCats = CATS.health.filter(h => h !== 'Normal' && nn.some(r => r.health === h));
  if (nn.length) out.push(`<b>${fmt1(A.total ? nnA.total / A.total * 100 : 0)}% of downtime</b> (${fmt1(nnA.total)} h) sits on components flagged ${nnCats.map(esc).join(' or ')} — condition monitoring addresses the bulk of lost hours.`);
  else out.push('<b>100% of faults</b> in view hit components rated Normal — health monitoring is not flagging these failures in advance.');

  // 4. Pending-maintenance exposure
  const pend = rows.filter(r => r.maintenance === 'Pending'), pA = agg(pend);
  if (pend.length) out.push(`<b>${fmt0(pend.length)} faults (${fmt1(pend.length / rows.length * 100)}%)</b> hit assets with maintenance still Pending, costing ${fmt1(pA.total)} h of downtime — clearing that backlog is a direct reliability lever.`);
  else out.push('<b>0 faults</b> in view are on assets with Pending maintenance — the backlog is not a factor for this selection.');

  // 5. Worst fault-type × weather hotspot
  const combos = [];
  byT.forEach(t => byW.forEach(w => {
    const a = agg(rows.filter(r => r.fault_type === t.k && r.weather === w.k));
    if (a.n >= MIN_N) combos.push({ f: t.k, w: w.k, ...a });
  }));
  if (combos.length > 1) {
    const c = pick(combos, 'avg', 1), d = c.avg - A.avg;
    if (d > 0.05) out.push(`<b>${fmt1(c.avg)} h</b> per fault for <b>${esc(c.f)} during ${esc(c.w)}</b> (${fmt0(c.n)} faults) is the worst hotspot, ${fmt1(d)} h above average — prioritise it in readiness plans.`);
  }
  ul.innerHTML = out.slice(0, 5).map(t => `<li>${t}</li>`).join('');
}

/* =====================================================================
   9. RENDER LOOP & CROSS-FILTER WIRING
   ===================================================================== */
let handlersAttached = false;
function attachChartHandlers() {
  if (handlersAttached) return; handlersAttached = true;
  const later = fn => setTimeout(() => { fn(); render(); }, 0); // defer re-render until Plotly finishes its click
  document.getElementById('c-bar').on('plotly_click', e => { const p = e.points && e.points[0]; if (p) later(() => focusCategory('fault_type', p.y)); });
  document.getElementById('c-donut').on('plotly_click', e => { const p = e.points && e.points[0]; if (p) later(() => focusCategory('maintenance', p.label)); });
  document.getElementById('c-heat').on('plotly_click', e => {
    const p = e.points && e.points[0]; if (!p || p.z == null) return;
    later(() => { focusCategory('fault_type', p.y); focusCategory('weather', p.x); });
  });
  // Treemap: cancel Plotly's default zoom (return false) and use the click as a filter instead.
  document.getElementById('c-tree').on('plotly_treemapclick', e => {
    const p = e.points && e.points[0]; if (!p || !p.id) return false;
    const [w, f] = String(p.id).split('||');
    later(() => { focusCategory('weather', w); if (f) focusCategory('fault_type', f); });
    return false;
  });
}

let renderTimer = null;
function scheduleRender() { clearTimeout(renderTimer); renderTimer = setTimeout(render, 90); } // debounce slider drags

function render() {
  const rows = filterRows(), A = agg(rows);
  renderHeader(rows); syncChips(); syncRange('downtime'); syncRange('seq'); renderKPIs(rows, A);
  const empty = rows.length === 0;
  document.body.classList.toggle('is-empty', empty);
  renderInsights(rows, A);
  if (empty) {
    ['t-trend', 't-bar', 't-heat', 't-donut', 't-map', 't-tree', 't-scatter'].forEach(id => setTitle(id, 'No data for the current filters'));
    return;
  }
  renderTrend(rows, A); renderBar(rows, A); renderHeatmap(rows); renderDonut(rows);
  renderMap(rows); renderTreemap(rows); renderScatter(rows);
  attachChartHandlers();
}

/* =====================================================================
   10. BOOT
   ===================================================================== */
(function init() {
  if (typeof Plotly === 'undefined') {
    document.getElementById('subtitle').textContent = 'Charts could not load (Plotly CDN unreachable). Check your internet connection.';
    return;
  }
  buildChips(); buildRange('downtime'); buildRange('seq');
  document.getElementById('resetBtn').addEventListener('click', () => { state = defaultState(); render(); });
  render();
})();
</script>
</body>
</html>
```