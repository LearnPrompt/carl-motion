// S25 黑白橡皮管卡通 B：卡尔（简化成 1930 年代橡皮管卡通）追一只跳走的咖啡杯。
// 画风按 L37 / 参考 A：4:3 片门（1440×1080 居中、圆角、两侧黑边）、灰阶、派形眼、白色四指手套、等宽面条四肢、
// 角色逐两格（12fps）、挤压拉伸与预备动作、字幕卡（深色底板＋双线框＋衬线小型大写）、胶片损伤（抖动、闪烁、划痕、灰尘、暗角、颗粒）。
// 同一厨房体系（壁纸＋菱形纹、瓷砖墙、台面、橱柜）；A 是"咖啡杯追方糖"，这里是卡尔追咖啡杯，情节不同。
// 0–1 s 伸手、杯子跳走；1–4 s 追、手臂拉长、杯子从头顶越过（错过）、急刹回头再追；4–6 s 蓄力后扑抓、杯子空中转向；
// 6–8 s 杯子跳回手心，人和杯一起余振。外貌（黑色中分帘式刘海盖耳、粗黑方框眼镜、露齿笑、浅色圆领 T 恤）按用户提供的照片概括。
SCENES['s25_hose'] = (() => {
  const W = 1920, H = 1080, GW = 1440, GX = 240, TAU = Math.PI * 2, { clamp, lerp, ss } = U;
  const G = 806, CS = 1.2, CC = 1.15;               // 台面（脚底）；卡尔、杯子的整体比例（对齐 A 的镜头尺度）
  const INK = '#151515', PAPER = '#f1efe9';
  const ease = u => u * u * (3 - 2 * u);
  const hash = (a, b = 0) => U.hash(a, b);
  const damp = (u, f, k) => Math.exp(-k * u) * Math.sin(f * u);

  // ---------------- 背景（缓存） ----------------
  function room(g) {
    g.fillStyle = '#8b8a86'; g.fillRect(0, 0, GW, 382);
    for (let x = 0; x < GW; x += 120) { g.fillStyle = '#84837f'; g.fillRect(x, 0, 60, 382); }
    g.fillStyle = '#6c6b67';
    for (let y = 40; y < 370; y += 82) for (let x = 30 + ((y / 82) % 2) * 60; x < GW; x += 120) { g.beginPath(); g.moveTo(x, y - 9); g.lineTo(x + 6, y); g.lineTo(x, y + 9); g.lineTo(x - 6, y); g.closePath(); g.fill(); }
    g.fillStyle = '#4b4a47'; g.fillRect(0, 382, GW, 30); g.fillStyle = INK; g.fillRect(0, 408, GW, 4);
    // 瓷砖墙
    g.fillStyle = '#c9c8c3'; g.fillRect(0, 412, GW, 380);
    g.strokeStyle = '#a7a6a1'; g.lineWidth = 3;
    for (let y = 412; y < 792; y += 74) { g.beginPath(); g.moveTo(0, y); g.lineTo(GW, y); g.stroke(); }
    for (let x = 30; x < GW; x += 74) { g.beginPath(); g.moveTo(x, 412); g.lineTo(x, 792); g.stroke(); }
    const tg = g.createLinearGradient(0, 412, 0, 792); tg.addColorStop(0, 'rgba(0,0,0,.12)'); tg.addColorStop(0.4, 'rgba(255,255,255,.06)'); tg.addColorStop(1, 'rgba(0,0,0,.18)'); g.fillStyle = tg; g.fillRect(0, 412, GW, 380);
    // 挂钟（指针在 draw 里走）
    g.beginPath(); g.arc(1200, 200, 78, 0, TAU); g.fillStyle = '#3e3d3a'; g.fill(); g.lineWidth = 6; g.strokeStyle = INK; g.stroke();
    g.beginPath(); g.arc(1200, 200, 62, 0, TAU); g.fillStyle = '#e4e2dc'; g.fill(); g.lineWidth = 4; g.stroke();
    g.fillStyle = INK; for (let k = 0; k < 12; k++) { const a = k * TAU / 12; g.beginPath(); g.arc(1200 + Math.cos(a) * 50, 200 + Math.sin(a) * 50, k % 3 ? 3 : 5.5, 0, TAU); g.fill(); }
    g.strokeStyle = 'rgba(255,255,255,.7)'; g.lineWidth = 5; g.beginPath(); g.arc(1200, 200, 70, 3.6, 4.4); g.stroke();
    // 台面＋前沿＋橱柜
    g.fillStyle = '#dcdbd6'; g.fillRect(0, 792, GW, 24); g.fillStyle = '#b4b3ae'; g.fillRect(0, 816, GW, 28);
    g.strokeStyle = INK; g.lineWidth = 4; [792, 816, 844].forEach(y => { g.beginPath(); g.moveTo(0, y); g.lineTo(GW, y); g.stroke(); });
    g.fillStyle = '#6d6c68'; g.fillRect(0, 846, GW, 234);
    for (let x = -60; x < GW; x += 380) { g.fillStyle = '#62615d'; g.beginPath(); g.roundRect(x + 24, 874, 330, 220, 14); g.fill(); g.lineWidth = 4; g.strokeStyle = INK; g.stroke();
      g.beginPath(); g.roundRect(x + 52, 900, 274, 200, 10); g.lineWidth = 3; g.stroke();
      g.beginPath(); g.arc(x + 300, 930, 11, 0, TAU); g.fillStyle = '#9a9994'; g.fill(); g.stroke(); }
    // 台面右端糖罐、左端盐瓶
    g.save(); g.translate(1330, 794);
    g.beginPath(); g.roundRect(-62, -150, 124, 150, 16); g.fillStyle = '#d9d8d2'; g.fill(); g.lineWidth = 6; g.strokeStyle = INK; g.stroke();
    g.beginPath(); g.roundRect(-70, -168, 140, 26, 10); g.fillStyle = '#4a4946'; g.fill(); g.stroke();
    g.beginPath(); g.arc(0, -172, 13, Math.PI, 0); g.fill(); g.stroke();
    g.font = '28px "Bodoni 72 Smallcaps"'; g.fillStyle = INK; g.textAlign = 'center'; g.fillText('Sugar', 0, -70);
    g.strokeStyle = 'rgba(255,255,255,.75)'; g.lineWidth = 7; g.beginPath(); g.moveTo(-42, -128); g.lineTo(-42, -40); g.stroke();
    g.restore();
    g.save(); g.translate(130, 794);
    g.beginPath(); g.moveTo(-28, 0); g.lineTo(-22, -96); g.quadraticCurveTo(0, -122, 22, -96); g.lineTo(28, 0); g.closePath(); g.fillStyle = '#e2e1dc'; g.fill(); g.lineWidth = 6; g.strokeStyle = INK; g.stroke();
    g.fillStyle = INK; [[-6, -100], [6, -100], [0, -108]].forEach(([x, y]) => { g.beginPath(); g.arc(x, y, 3, 0, TAU); g.fill(); });
    g.restore();
  }

  // ---------------- 手套 ----------------
  function glove(g, x, y, ang, mode, s = 1) {
    g.save(); g.translate(x, y); g.rotate(ang); g.scale(s, s); g.lineJoin = 'round'; g.lineCap = 'round';
    g.fillStyle = '#fbfaf6'; g.strokeStyle = INK; g.lineWidth = 4.5;
    if (mode === 'fist') {
      g.beginPath(); g.ellipse(20, 0, 22, 20, 0, 0, TAU); g.fill(); g.stroke();
      g.lineWidth = 3; for (const yy of [-8, 2, 11]) { g.beginPath(); g.arc(34, yy, 6, -1.4, 1.4); g.stroke(); }
      g.beginPath(); g.ellipse(18, -18, 10, 7, -0.4, 0, TAU); g.fill(); g.lineWidth = 4; g.stroke();
    } else {
      const fan = mode === 'palm' ? [-0.25, 0.05, 0.35, 0.65] : [-0.55, -0.18, 0.18, 0.55];
      fan.forEach(a => { g.beginPath(); g.ellipse(20 + Math.cos(a) * 24, Math.sin(a) * 24, 14, 8, a, 0, TAU); g.fill(); g.stroke(); });
      g.beginPath(); g.ellipse(14 + Math.cos(-1.5) * 18, Math.sin(-1.5) * 20, 12, 7, -1.3, 0, TAU); g.fill(); g.stroke();
      g.beginPath(); g.ellipse(18, 0, 21, 19, 0, 0, TAU); g.fill(); g.stroke();
      g.lineWidth = 3; for (const yy of [-7, 0, 7]) { g.beginPath(); g.moveTo(12, yy); g.lineTo(24, yy * 1.3); g.stroke(); }
    }
    g.beginPath(); g.roundRect(-16, -19, 18, 38, 7); g.fillStyle = '#fbfaf6'; g.fill(); g.lineWidth = 4.5; g.stroke();
    g.lineWidth = 2.5; g.beginPath(); g.moveTo(-9, -15); g.lineTo(-9, 15); g.stroke();
    g.restore();
  }
  // 面条手臂：肩到手一条等宽软管，中段下垂
  function hose(g, A, B, w = 14, sag = 30) {
    const mx = (A[0] + B[0]) / 2, my = (A[1] + B[1]) / 2 + sag;
    g.strokeStyle = INK; g.lineWidth = w; g.lineCap = 'round'; g.beginPath(); g.moveTo(...A); g.quadraticCurveTo(mx, my, ...B); g.stroke();
    return Math.atan2(B[1] - my, B[0] - mx);
  }

  // ---------------- 卡尔：时间线（逐两格） ----------------
  const carlAt = t => {
    const s = { x: 400, dir: 1, sx: 1, sy: 1, rot: 0, lift: 0, run: 0, ph: 0, eyes: 'norm', mouth: 'grin', blink: false, front: null, back: null, grip: 'open', look: 0, lines: 0, dust: 0, speed: 0 };
    if (t < 1.0) {                                    // 伸手 → 杯子跳走 → 愣住
      const lb = ss(0, 0.15, t) * (1 - ss(0.15, 0.4, t)), rch = ss(0.12, 0.5, t);
      s.rot = -0.12 * lb + 0.1 * rch * (1 - ss(0.6, 0.8, t)); s.sy = 1 - 0.06 * lb;
      s.front = [lerp(470, 745, rch), lerp(700, 760, rch)];
      s.grip = t > 0.6 ? 'fist' : 'open';
      if (t > 0.62) { s.eyes = 'wide'; s.mouth = 'o'; s.lines = 1 - ss(0.62, 1.0, t); s.sy = 1 + 0.12 * damp(t - 0.62, 30, 6); s.front = [lerp(745, 520, ss(0.7, 0.95, t)), lerp(760, 700, ss(0.7, 0.95, t))]; }
    } else if (t < 2.6) {                             // 向右追，手臂拉长够杯子
      const u = (t - 1.0) / 1.6; s.x = 400 + 480 * (u < 0.15 ? u * u / 0.3 : u - 0.075) / 0.925;
      s.run = ss(1.0, 1.2, t); s.ph = (t - 1.0) * 2.6; s.rot = 0.16 * s.run; s.speed = s.run;
      s.mouth = 'o'; s.eyes = 'norm';
      const reach = ss(1.6, 2.5, t); s.front = [s.x + 120 + reach * 230, 640 - reach * 60]; s.grip = 'open';
    } else if (t < 3.05) {                            // 杯子从头顶越过：抓空、急刹、抬头看
      const u = clamp((t - 2.6) / 0.45); s.x = 880 + 70 * (1 - (1 - u) * (1 - u));
      s.rot = -0.3 * Math.sin(u * Math.PI * 0.9); s.sy = 0.9; s.sx = 1.08; s.eyes = 'up'; s.mouth = 'o';
      s.front = [s.x + 260 - u * 120, 560 - u * 90]; s.grip = t > 2.66 ? 'fist' : 'open'; s.dust = u; s.look = 1;
    } else if (t < 3.25) {                            // 转身
      const u = (t - 3.05) / 0.2; s.x = 950; s.dir = u < 0.5 ? 1 : -1; s.sx = 1 - 0.5 * Math.sin(u * Math.PI); s.sy = 1.08; s.eyes = 'wide'; s.mouth = 'o';
    } else if (t < 4.0) {                             // 再追（向左）
      const u = (t - 3.25) / 0.75; s.x = 950 - 190 * u; s.dir = -1; s.run = 1 - ss(3.85, 4.0, t); s.ph = (t - 3.25) * 2.6; s.rot = -0.14 * s.run; s.speed = s.run; s.mouth = 'grin';
    } else if (t < 4.7) {                             // 预备：下蹲、往后拉、双臂后甩
      const u = ss(4.0, 4.45, t); s.x = 760 + 20 * u; s.dir = -1; s.sy = 1 - 0.22 * u; s.sx = 1 + 0.16 * u; s.rot = 0.28 * u;
      s.front = [s.x + 150 * u + 60, 700 - 60 * u]; s.back = [s.x + 170 * u + 90, 660 - 40 * u]; s.grip = 'open'; s.mouth = 'grin'; s.frontBehind = true;
      s.sy += 0.02 * Math.sin(t * 60) * u;        // 蓄力抖
    } else if (t < 5.1) {                             // 扑！
      const u = clamp((t - 4.7) / 0.35), e = 1 - (1 - u) * (1 - u); s.x = lerp(780, 480, e); s.dir = -1;
      s.lift = 90 * Math.sin(u * Math.PI); s.rot = -0.9 * Math.sin(Math.min(1, u * 1.3) * Math.PI / 2); s.sx = 1.3 - 0.2 * u; s.sy = 0.82;
      s.front = [s.x - 330, 690 + 30 * u]; s.back = [s.x - 290, 730 + 20 * u]; s.grip = u > 0.8 ? 'fist' : 'open'; s.eyes = 'wide'; s.mouth = 'o'; s.speed = 1;
    } else if (t < 5.6) {                             // 落地重挤压、余振，扑空
      const u = t - 5.1; s.x = 470; s.dir = -1; s.sy = 1 - 0.3 * Math.exp(-6 * u) * Math.cos(u * 22); s.sx = 1 / s.sy; s.rot = -0.25 * Math.exp(-5 * u);
      s.front = [s.x - 120, 760]; s.grip = 'fist'; s.frontBehind = false; s.eyes = 'wide'; s.mouth = 'o'; s.dust = clamp(u / 0.5);
    } else if (t < 6.55) {                            // 转身面向杯子，摊开手心
      s.x = 470; s.dir = t < 5.66 ? -1 : 1; const v = ss(5.6, 5.75, t); s.sx = 1 - 0.45 * Math.sin(v * Math.PI);
      const p = ss(5.8, 6.15, t); s.front = t < 5.75 ? null : [lerp(580, 690, p), lerp(740, 655, p)]; s.grip = 'palm'; s.eyes = t > 6.1 ? 'up' : 'norm'; s.mouth = 'grin';
      s.look = t > 6.1 ? 1 : 0;
    } else {                                          // 接住：人与杯一起余振
      const u = t - 6.55; s.x = 470; s.dir = 1; s.sy = 1 - 0.1 * damp(u, 16, 4); s.sx = 1 / s.sy;
      const bring = ss(7.0, 7.6, t); s.front = [lerp(690, 668, bring), lerp(655, 628, bring) + 34 * damp(u, 15, 4.5)]; s.grip = 'palm'; s.mouth = 'grin';
      s.blink = t > 7.35 && t < 7.47;
    }
    if (!s.blink) s.blink = (t > 1.9 && t < 2.0) || (t > 4.25 && t < 4.33);
    return s;
  };
  // 局部→片门坐标（脚底为原点，先缩放再旋转）
  const tf = (s, px, py) => { const x = px * s.sx * CS, y = py * s.sy * CS, c = Math.cos(s.rot), n = Math.sin(s.rot); return [s.x + x * c - y * n, G - s.lift + x * n + y * c]; };

  function drawCarl(g, s, t) {
    const D = s.dir, off = D * 14;
    const shF = tf(s, 58 * D, -250), shB = tf(s, -58 * D, -250);
    const swing = Math.sin(TAU * s.ph) * s.run;
    const fr = s.front || tf(s, (40 + 70 * swing) * D, -120 - 20 * Math.abs(swing));
    const bk = s.back || tf(s, (-40 - 70 * swing) * D, -120 - 20 * Math.abs(swing));
    // 地面投影
    g.fillStyle = 'rgba(0,0,0,.22)'; g.beginPath(); g.ellipse(s.x, G + 4, 130 - s.lift * 0.4, 15, 0, 0, TAU); g.fill();
    // 后臂（蓄力时前臂也甩到身后）
    const aB = hose(g, shB, bk, 14 * CS, 20); glove(g, ...bk, aB, 'open', CS);
    if (s.frontBehind) { const a = hose(g, shF, fr, 14 * CS, 10); glove(g, ...fr, a, 'open', 1.05 * CS); }
    g.save(); g.translate(s.x, G - s.lift); g.rotate(s.rot); g.scale(s.sx * CS, s.sy * CS); g.lineJoin = 'round'; g.lineCap = 'round';
    // 腿：圆形跑步循环（面条腿＋大鞋）
    [0, 1].forEach(i => { const th = TAU * s.ph + i * Math.PI, hx = (i ? 1 : -1) * 26;
      const fx = lerp(hx, D * 54 * Math.cos(th), s.run), fy = -s.run * 46 * Math.max(0, Math.sin(th));
      g.strokeStyle = INK; g.lineWidth = 15; g.beginPath(); g.moveTo(hx, -112); g.quadraticCurveTo((hx + fx) / 2 - D * 16, (-112 + fy) / 2, fx, fy - 14); g.stroke();
      g.beginPath(); g.ellipse(fx + D * 16, fy - 10, 36, 17, 0, 0, TAU); g.fillStyle = INK; g.fill();
      g.strokeStyle = 'rgba(255,255,255,.75)'; g.lineWidth = 5; g.beginPath(); g.ellipse(fx + D * 22, fy - 16, 16, 6, 0, 3.6, 5.6); g.stroke(); });
    // 躯干：上 T 恤（浅）下短裤（深），梨形
    const body = RIG.smooth([[-52, -272], [52, -272], [74, -200], [80, -138], [60, -100], [-60, -100], [-80, -138], [-74, -200]], true, 0.5);
    g.fillStyle = '#e8e6df'; g.fill(body);
    g.save(); g.clip(body); g.fillStyle = '#2f2e2c'; g.fillRect(-100, -158, 200, 80);
    g.fillStyle = 'rgba(0,0,0,.12)'; g.beginPath(); g.ellipse(-D * 40, -190, 40, 90, 0, 0, TAU); g.fill(); g.restore();
    g.strokeStyle = INK; g.lineWidth = 6; g.stroke(body); g.lineWidth = 4; g.beginPath(); g.moveTo(-78, -158); g.lineTo(78, -158); g.stroke();
    g.beginPath(); g.ellipse(0, -270, 30, 10, 0, 0.1, Math.PI - 0.1); g.lineWidth = 4; g.stroke();     // 圆领
    // 头
    g.save(); g.translate(0, -362);
    g.beginPath(); g.ellipse(0, 0, 90, 96, 0, 0, TAU); g.fillStyle = '#d9d6cf'; g.fill(); g.lineWidth = 6; g.strokeStyle = INK; g.stroke();
    g.fillStyle = 'rgba(0,0,0,.10)'; g.beginPath(); g.ellipse(-D * 30, 30, 50, 60, 0, 0, TAU); g.fill();
    // 头发：中分帘式刘海，两片盖住耳朵到下颌
    const hair = RIG.smooth([[-104, 62], [-112, -10], [-96, -76], [-52, -108], [0, -114], [52, -108], [96, -76], [112, -10], [104, 62], [84, 64], [80, 0], [52, -44], [10, -60], [0, -52], [-10, -60], [-52, -44], [-80, 0], [-84, 64]], true, 0.45);
    g.fillStyle = INK; g.fill(hair);
    g.strokeStyle = 'rgba(255,255,255,.55)'; g.lineWidth = 5; g.beginPath(); g.moveTo(-70, -78); g.quadraticCurveTo(-40, -100, -12, -100); g.stroke();
    g.beginPath(); g.moveTo(30, -96); g.quadraticCurveTo(58, -90, 74, -72); g.stroke();
    // 粗黑方框眼镜＋派形眼
    const ey = s.look ? -12 : 0;
    [-1, 1].forEach(k => { const cx = k * 42 + off;
      g.beginPath(); g.roundRect(cx - 34, -30, 68, 56, 10); g.fillStyle = '#f5f4ef'; g.fill(); g.lineWidth = 10; g.strokeStyle = INK; g.stroke();
      if (s.blink) { g.lineWidth = 5; g.beginPath(); g.moveTo(cx - 14, 0); g.quadraticCurveTo(cx, 8, cx + 14, 0); g.stroke(); return; }
      const big = s.eyes === 'wide' ? 1.25 : 1, px = cx + D * 6, py = ey + (s.eyes === 'up' ? -6 : 0);
      g.save(); g.beginPath(); g.ellipse(px, py, 12 * big, 19 * big, 0, 0, TAU); g.fillStyle = INK; g.fill();
      g.fillStyle = '#f5f4ef'; g.beginPath(); g.moveTo(px + 3 * big, py - 6 * big); g.lineTo(px + 14 * big, py - 18 * big); g.lineTo(px + 14 * big, py - 2 * big); g.closePath(); g.fill(); g.restore(); });
    g.lineWidth = 8; g.beginPath(); g.moveTo(-8 + off, -8); g.quadraticCurveTo(off, -14, 8 + off, -8); g.stroke();
    // 鼻、嘴
    g.fillStyle = INK; g.beginPath(); g.ellipse(off + D * 8, 38, 12, 9, 0, 0, TAU); g.fill();
    g.fillStyle = 'rgba(255,255,255,.7)'; g.beginPath(); g.ellipse(off + D * 4, 35, 4, 2.5, 0, 0, TAU); g.fill();
    if (s.mouth === 'o') { g.fillStyle = INK; g.beginPath(); g.ellipse(off + D * 6, 66, 12, 15, 0, 0, TAU); g.fill(); }
    else { g.beginPath(); g.moveTo(off - 44, 52); g.quadraticCurveTo(off, 104, off + 44, 52); g.quadraticCurveTo(off, 64, off - 44, 52); g.fillStyle = INK; g.fill();
      g.save(); g.clip(); g.fillStyle = '#fbfaf6'; g.fillRect(off - 46, 50, 92, 14); g.restore();
      g.lineWidth = 4; g.strokeStyle = INK; g.beginPath(); g.moveTo(off - 50, 48); g.quadraticCurveTo(off - 46, 54, off - 42, 54); g.moveTo(off + 50, 48); g.quadraticCurveTo(off + 46, 54, off + 42, 54); g.stroke(); }
    g.restore();
    // 惊讶线
    if (s.lines > 0) { g.strokeStyle = INK; g.lineWidth = 6; for (let k = 0; k < 7; k++) { const a = -Math.PI / 2 + (k - 3) * 0.32, r0 = 130 + 10 * (1 - s.lines), r1 = r0 + 50 * s.lines; g.beginPath(); g.moveTo(Math.cos(a) * r0, -362 + Math.sin(a) * r0); g.lineTo(Math.cos(a) * r1, -362 + Math.sin(a) * r1); g.stroke(); } }
    g.restore();
    // 前臂（压在身体前）
    if (!s.frontBehind) { const aF = hose(g, shF, fr, 14 * CS, s.front ? 10 : 20); glove(g, ...fr, s.grip === 'palm' ? 0 : aF, s.grip === 'palm' ? 'palm' : s.grip, 1.05 * CS); }
    // 速度线、急刹烟团
    if (s.speed > 0.3) { g.strokeStyle = 'rgba(20,20,20,.55)'; g.lineWidth = 4; for (let k = 0; k < 3; k++) { const y = G - 120 - k * 90, x0 = s.x - D * (140 + 30 * k); g.beginPath(); g.moveTo(x0, y); g.lineTo(x0 - D * (90 + 20 * hash(k, Math.floor(t * 12))), y); g.stroke(); } }
    if (s.dust > 0 && s.dust < 1) for (let k = 0; k < 4; k++) { const r = 18 + 30 * s.dust + k * 6, x = s.x + (k - 1.5) * 50 * (0.6 + s.dust), y = G - 20 - 30 * s.dust - k * 6;
      g.globalAlpha = 1 - s.dust; g.beginPath(); g.arc(x, y, r, 0, TAU); g.fillStyle = '#d6d5d0'; g.fill(); g.lineWidth = 4; g.strokeStyle = INK; g.stroke(); g.globalAlpha = 1; }
  }

  // ---------------- 杯子：跳跃时间线 ----------------
  const HOPS = [[0.55, 1.05, 760, 1080, 150, 0], [1.42, 1.82, 1080, 1210, 110, 0], [2.22, 2.98, 1210, 540, 600, 0], [3.32, 3.82, 540, 330, 150, 0], [4.42, 5.60, 330, 860, 600, 1]];
  const cupAt = (t, palm) => {
    let x = 760, y = G, sx = 1, sy = 1, rot = 0, dir = -1, spin = 0;
    for (let i = 0; i < HOPS.length; i++) { const [t0, t1, x0, x1, h, sp] = HOPS[i];
      if (t >= t1) { x = x1; dir = Math.sign(x1 - x0); const u = t - t1; if (u < 0.3) { sy = 1 - 0.28 * Math.exp(-9 * u) * Math.cos(u * 30); sx = 1 / sy; } continue; }
      // 转向那一跳（sp）水平方向先慢后快：先直上躲开扑抓
      if (t >= t0) { const u = (t - t0) / (t1 - t0); x = lerp(x0, x1, sp ? u * u : u); y = G - 4 * h * u * (1 - u); dir = Math.sign(x1 - x0); sy = u < 0.5 ? 1.22 : 1.1; sx = 1 / sy; rot = (u - 0.5) * 0.5 * dir;
        if (sp) { spin = u; dir = u < 0.5 ? -1 : 1; rot += u * TAU; } break; }
      if (t > t0 - 0.16) { const u = (t - (t0 - 0.16)) / 0.16; sy = 1 - 0.3 * Math.sin(u * Math.PI / 2); sx = 1 / sy; dir = Math.sign(x1 - x0); }
      break;
    }
    // 6.05 跳进卡尔手心
    if (t >= 5.85 && t < 6.05) { const u = (t - 5.85) / 0.2; sy = 1 - 0.3 * Math.sin(u * Math.PI / 2); sx = 1 / sy; dir = -1; }
    if (t >= 6.05) { const u = clamp((t - 6.05) / 0.5); const tx = palm[0] + 20, ty = palm[1] - 20;
      x = lerp(860, tx, u); y = lerp(G, ty, u) - 4 * 230 * u * (1 - u); dir = -1; sy = u < 0.5 ? 1.2 : 1.08; sx = 1 / sy; rot = -(u - 0.5) * 0.5;
      if (t >= 6.55) { const v = t - 6.55; x = tx; y = ty; sy = 1 - 0.32 * Math.exp(-5 * v) * Math.cos(v * 26); sx = 1 / sy; rot = 0.12 * damp(v, 18, 4); } }
    return { x, y, sx, sy, rot, dir, spin };
  };
  function drawCup(g, c, t, lookAt) {
    const tq = Math.floor(t * 12) / 12;
    if (c.y > G - 10) { g.fillStyle = 'rgba(0,0,0,.22)'; g.beginPath(); g.ellipse(c.x, G + 4, 64, 10, 0, 0, TAU); g.fill(); }
    g.save(); g.translate(c.x, c.y); g.rotate(c.rot); g.scale(c.sx * CC * (c.spin ? Math.cos(c.spin * Math.PI * 2) * 0.5 + 0.5 + 0.0001 : 1), c.sy * CC); g.lineJoin = 'round'; g.lineCap = 'round';
    const D = c.dir;
    // 小腿＋小鞋
    [-1, 1].forEach(k => { const air = c.y < G - 10 ? 1 : 0, fx = k * 18 + air * -D * 8 * k;
      g.strokeStyle = INK; g.lineWidth = 9; g.beginPath(); g.moveTo(k * 18, -34); g.lineTo(fx, -8 + air * 4); g.stroke();
      g.beginPath(); g.ellipse(fx + D * 8, -6 + air * 4, 17, 9, 0, 0, TAU); g.fillStyle = INK; g.fill(); });
    // 把手（在背后）
    g.beginPath(); g.ellipse(-D * 52, -78, 26, 26, 0, 0, TAU); g.lineWidth = 20; g.strokeStyle = INK; g.stroke(); g.lineWidth = 10; g.strokeStyle = '#e9e7e0'; g.stroke();
    // 杯身
    g.beginPath(); g.moveTo(-50, -126); g.lineTo(50, -126); g.lineTo(44, -42); g.quadraticCurveTo(42, -30, 30, -30); g.lineTo(-30, -30); g.quadraticCurveTo(-42, -30, -44, -42); g.closePath();
    g.fillStyle = '#ebe9e3'; g.fill(); g.save(); g.clip(); g.fillStyle = '#3a3936'; g.fillRect(-60, -112, 120, 12); g.fillStyle = 'rgba(0,0,0,.13)'; g.fillRect(D * 10, -130, 60, 110); g.restore();
    g.lineWidth = 6; g.strokeStyle = INK; g.stroke();
    g.beginPath(); g.ellipse(0, -126, 50, 12, 0, 0, TAU); g.fillStyle = '#2b2a28'; g.fill(); g.stroke();
    g.strokeStyle = 'rgba(255,255,255,.75)'; g.lineWidth = 5; g.beginPath(); g.moveTo(-36, -96); g.lineTo(-34, -52); g.stroke();
    // 脸：派形眼看着卡尔
    const lx = clamp((lookAt[0] - c.x) / 300, -1, 1) * 5;
    [-1, 1].forEach(k => { const ex = k * 16 + D * 6; g.beginPath(); g.ellipse(ex, -78, 11, 15, 0, 0, TAU); g.fillStyle = '#fbfaf6'; g.fill(); g.lineWidth = 3.5; g.strokeStyle = INK; g.stroke();
      g.beginPath(); g.ellipse(ex + lx, -76, 6, 9, 0, 0, TAU); g.fillStyle = INK; g.fill(); g.fillStyle = '#fbfaf6'; g.beginPath(); g.moveTo(ex + lx + 1, -80); g.lineTo(ex + lx + 7, -86); g.lineTo(ex + lx + 7, -77); g.closePath(); g.fill(); });
    g.lineWidth = 4; g.strokeStyle = INK; g.beginPath(); g.arc(D * 6, -60, 12, 0.35, Math.PI - 0.35); g.stroke();
    g.restore();
    // 热气（逐两格扭动）
    if (!c.spin) { g.strokeStyle = 'rgba(245,244,239,.9)'; g.lineWidth = 6; g.lineCap = 'round';
      for (let k = -1; k <= 1; k++) { g.beginPath(); for (let j = 0; j <= 10; j++) { const yy = c.y - 140 * CC * c.sy - j * 9, xx = c.x + k * 18 + Math.sin(j * 0.8 + tq * 9 + k) * 7; j ? g.lineTo(xx, yy) : g.moveTo(xx, yy); } g.stroke(); } }
  }

  // ---------------- 字幕卡（同 A：深色底板＋双线框＋衬线小型大写） ----------------
  function card(g, text, a) {
    if (a <= 0) return; g.save(); g.globalAlpha = a; const w = 620, h = 62, x = GW / 2 - w / 2, y = 952;
    g.fillStyle = '#1a1a19'; g.fillRect(x, y, w, h); g.strokeStyle = '#e6e4dd'; g.lineWidth = 2.5; g.strokeRect(x + 6, y + 6, w - 12, h - 12); g.lineWidth = 1.2; g.strokeRect(x + 11, y + 11, w - 22, h - 22);
    g.fillStyle = '#efede6'; g.font = '30px "Bodoni 72 Smallcaps"'; g.textAlign = 'center'; g.textBaseline = 'middle'; g.fillText(text, GW / 2, y + h / 2 + 1);
    g.restore();
  }

  // ---------------- 胶片层：颗粒、暗角、片门 ----------------
  const grains = () => [0, 1, 2, 3, 4, 5].map(k => P.cached('hose_grain' + k, 720, 540, g => { const img = g.createImageData(720, 540), d = img.data, r = U.rng(900 + k);
    for (let i = 0; i < d.length; i += 4) { const v = r() * 255; d[i] = d[i + 1] = d[i + 2] = v; d[i + 3] = 34; } g.putImageData(img, 0, 0); }));
  const P = PAINT;
  const vignette = () => P.cached('hose_vig', GW, H, g => { const v = g.createRadialGradient(GW / 2, H / 2, 300, GW / 2, H / 2, 900); v.addColorStop(0, 'rgba(0,0,0,0)'); v.addColorStop(1, 'rgba(0,0,0,.62)'); g.fillStyle = v; g.fillRect(0, 0, GW, H); });
  const gateCv = () => P.cached('hose_gate', GW, H, () => {});

  return {
    init() { P.cached('hose_room', GW, H, room); grains(); vignette(); },
    draw(c, lt, t) {
      const f = Math.round(t * 30), tq = Math.floor(t * 12) / 12;            // 角色逐两格
      const gc = gateCv(), g = gc.getContext('2d');
      g.setTransform(1, 0, 0, 1, 0, 0); g.globalAlpha = 1; g.globalCompositeOperation = 'source-over';
      g.drawImage(P.cached('hose_room', GW, H, room), 0, 0);
      // 钟的指针（逐两格跳）
      const ma = tq * 1.2 - 1.2, ha = tq * 0.1 + 0.9;
      g.strokeStyle = INK; g.lineCap = 'round'; g.lineWidth = 7; g.beginPath(); g.moveTo(1200, 200); g.lineTo(1200 + Math.cos(ha) * 32, 200 + Math.sin(ha) * 32); g.stroke();
      g.lineWidth = 5; g.beginPath(); g.moveTo(1200, 200); g.lineTo(1200 + Math.cos(ma) * 50, 200 + Math.sin(ma) * 50); g.stroke();
      const s = carlAt(tq), cup = cupAt(tq, s.front || [620, 640]);
      drawCarl(g, s, tq);
      drawCup(g, cup, tq, [s.x, G - 360]);
      // 手心接住后，把手指再画一遍压在杯脚前
      if (tq >= 6.55) { g.save(); g.beginPath(); g.rect(0, s.front[1] - 4, GW, 60); g.clip(); glove(g, ...s.front, 0, 'palm', 1.05 * CS); g.restore(); }
      card(g, 'Hold still, little cup!', ss(0.2, 0.5, t) * (1 - ss(5.85, 6.05, t)));
      card(g, 'Gotcha — good morning!', ss(6.6, 6.9, t));
      // 胶片：闪烁、划痕、灰尘、颗粒、暗角
      g.fillStyle = `rgba(0,0,0,${0.03 + 0.07 * hash(f, 3)})`; g.fillRect(0, 0, GW, H);
      if (hash(f, 5) > 0.82) { g.fillStyle = 'rgba(255,255,255,.05)'; g.fillRect(0, 0, GW, H); }
      const ns = (hash(Math.floor(f / 6), 7) * 3) | 0;
      for (let k = 0; k < ns; k++) { const x = hash(Math.floor(f / 6), 11 + k) * GW + (f % 6) * 1.5; g.strokeStyle = hash(k, 13) > 0.4 ? 'rgba(240,240,236,.35)' : 'rgba(10,10,10,.35)'; g.lineWidth = 1.2 + hash(k, f) * 1.8;
        g.beginPath(); g.moveTo(x, 0); g.lineTo(x + 3, H); g.stroke(); }
      for (let k = 0; k < 7; k++) { if (hash(f, 20 + k) < 0.45) continue; const x = hash(f, 40 + k) * GW, y = hash(f, 60 + k) * H, r = 1.5 + hash(f, 80 + k) * 4;
        g.fillStyle = hash(f, 100 + k) > 0.5 ? 'rgba(15,15,15,.7)' : 'rgba(245,245,240,.6)'; g.beginPath(); g.ellipse(x, y, r, r * (0.4 + hash(k, f)), hash(f, k), 0, TAU); g.fill(); }
      const gr = grains()[f % 6]; g.drawImage(gr, 0, 0, GW, H);
      g.drawImage(vignette(), 0, 0);
      g.globalCompositeOperation = 'multiply'; g.fillStyle = '#f5f0e6'; g.fillRect(0, 0, GW, H); g.globalCompositeOperation = 'source-over';
      // 合成：黑底＋圆角片门＋逐帧抖动
      c.fillStyle = '#000'; c.fillRect(0, 0, W, H);
      const wx = (hash(f, 1) - 0.5) * 3, wy = (hash(f, 2) - 0.5) * 4;
      c.save(); c.beginPath(); c.roundRect(GX + wx, wy, GW, H, 30); c.clip(); c.drawImage(gc, GX + wx, wy); c.restore();
    },
  };
})();
