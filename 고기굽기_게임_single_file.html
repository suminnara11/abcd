<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>고기굽기 게임</title>
  <style>
    :root{ --bg:#1b1b1f; --panel:#111; --accent:#ff7a18; --grill:#2b2b2b; --meat:#c94b3b; --charcoal:#111; }
    *{box-sizing:border-box}
    body{margin:0; font-family:Inter, Noto Sans KR, system-ui, Arial; background:linear-gradient(180deg,#0f0f12 0%, #1c1c22 100%); color:#eee; display:flex; align-items:center; justify-content:center; height:100vh}
    .wrap{width:980px; max-width:96vw; background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); border-radius:14px; padding:18px; box-shadow:0 10px 30px rgba(0,0,0,0.6); display:grid; grid-template-columns: 1fr 340px; gap:16px}

    /* GAME AREA */
    .game{background:var(--panel); border-radius:10px; padding:12px; display:flex; flex-direction:column; gap:10px}
    .topbar{display:flex; justify-content:space-between; align-items:center}
    .score{font-weight:700}
    .controls button{background:transparent; border:1px solid rgba(255,255,255,0.06); color:#eee; padding:6px 10px; border-radius:8px; cursor:pointer}

    .playfield{background:linear-gradient(180deg,#111 0%, #151515 100%); border-radius:8px; padding:18px; display:flex; gap:18px}
    .left{flex:2; display:flex; flex-direction:column; gap:12px}
    .right{flex:1}

    /* grill */
    .grill-wrap{background:linear-gradient(180deg,#2b2b2b,#222); border-radius:8px; padding:14px; position:relative; height:360px}
    .grate{position:absolute; inset:22px; border-radius:6px; background:linear-gradient(180deg,#222,#1b1b1b); display:flex; flex-wrap:wrap; gap:6px; padding:8px; align-content:flex-start}
    .grate .spot{width:calc(33.333% - 6px); height:80px; border-radius:6px; background:linear-gradient(180deg,#212121,#161616); display:flex; align-items:center; justify-content:center; position:relative}

    /* meat */
    .meat{width:80px; height:48px; border-radius:8px; background:linear-gradient(180deg,var(--meat), #852e28); box-shadow:0 6px 10px rgba(0,0,0,0.6); display:flex; align-items:center; justify-content:center; color:#fff; font-weight:700; cursor:grab; user-select:none}
    .meat.cooked-1{filter:brightness(1.05) saturate(1.05)}
    .meat.cooked-2{filter:brightness(0.9) saturate(0.9); background:linear-gradient(180deg,#a84a37,#6b2a24)}
    .meat.burn{filter:grayscale(0.6) brightness(0.7); background:linear-gradient(180deg,#4b2a2a,#2b1a1a)}

    .hud{display:flex; gap:10px; align-items:center}
    .bar{height:12px; width:150px; background:rgba(255,255,255,0.06); border-radius:8px; overflow:hidden}
    .bar > i{display:block; height:100%; background:linear-gradient(90deg,var(--accent),#ffd76b); width:0%}

    /* right panel */
    .panel{background:linear-gradient(180deg,#111,#0d0d0d); border-radius:8px; padding:12px; display:flex; flex-direction:column; gap:10px}
    .panel h3{margin:0; font-size:16px}
    .inventory{display:flex; gap:8px; flex-wrap:wrap}
    .btn{padding:8px 10px; background:transparent; border:1px solid rgba(255,255,255,0.06); border-radius:8px; cursor:pointer}

    /* footer instructions */
    .instructions{font-size:13px; color:rgba(255,255,255,0.7)}

    /* small */
    @media (max-width:880px){.wrap{grid-template-columns:1fr;}}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="game">
      <div class="topbar">
        <div class="score">점수: <span id="score">0</span></div>
        <div class="controls"><button id="spawn">고기 추가</button> <button id="reset">초기화</button></div>
      </div>

      <div class="playfield">
        <div class="left">
          <div class="grill-wrap">
            <div class="grate" id="grate">
              <!-- 6 grill spots -->
            </div>
            <div style="position:absolute; right:12px; bottom:10px; color:rgba(255,255,255,0.5); font-size:12px">숯불: <span id="coals">100%</span></div>
          </div>

          <div class="hud">
            <div>남은 시간</div>
            <div class="bar"><i id="timerBar"></i></div>
            <div id="timeText">00:00</div>
          </div>

          <div class="instructions">조작: 고기를 드래그해서 구이 칸에 올려보세요. 위아래로 뒤집기(click) — 잘 구워서 점수 획득! 타이머가 끝나면 게임 종료.</div>
        </div>

        <div class="right">
          <div class="panel">
            <h3>인벤토리</h3>
            <div class="inventory" id="inventory">
              <!-- meats spawn here -->
            </div>
            <h3>등급</h3>
            <div>생고기: 0점 / 적당히 구움: 10점 / 잘 구움: 25점 / 탄것: -5점</div>
            <hr style="border:none; height:1px; background:rgba(255,255,255,0.04)">
            <div>목표 점수: <strong id="target">150</strong></div>
          </div>
        </div>
      </div>
    </div>

    <div class="panel">
      <h3>게임 설명</h3>
      <p>이 작은 '고기굽기' 게임은 HTML/CSS/JS로 구성된 단일 파일입니다. 고기를 그릴에 올려서 클릭으로 뒤집고, 상태바를 보고 타이밍을 맞춰 익히세요. 시간이 끝나면 최종 점수가 나옵니다.</p>
      <h3>팁</h3>
      <ul>
        <li>고기를 너무 오래 두면 탄다. 미리 뒤집어야 한다.</li>
        <li>숯이 줄어들면 굽기 속도가 느려진다.</li>
      </ul>
      <div style="display:flex; gap:8px; margin-top:8px"><button class="btn" id="downloadBtn">파일로 저장</button> <button class="btn" id="more">추가 기능 제안</button></div>
    </div>
  </div>

  <script>
    // --- init ---
    const grate = document.getElementById('grate');
    const inventory = document.getElementById('inventory');
    const scoreEl = document.getElementById('score');
    const timerBar = document.getElementById('timerBar');
    const timeText = document.getElementById('timeText');
    const coalsEl = document.getElementById('coals');
    const targetEl = document.getElementById('target');

    const spawnBtn = document.getElementById('spawn');
    const resetBtn = document.getElementById('reset');
    const downloadBtn = document.getElementById('downloadBtn');
    const moreBtn = document.getElementById('more');

    let score = 0;
    let gameDuration = 90; // seconds
    let timeLeft = gameDuration;
    let coals = 100; // percent
    let spots = [];
    const maxSpots = 6;

    // create grill spots
    for(let i=0;i<maxSpots;i++){
      const s = document.createElement('div');
      s.className='spot';
      s.dataset.index = i;
      s.addEventListener('dragover', e=>e.preventDefault());
      s.addEventListener('drop', onDropToSpot);
      grate.appendChild(s);
      spots.push(s);
    }

    // timer
    let timerInterval = null;
    function startTimer(){
      if(timerInterval) return;
      timerInterval = setInterval(()=>{
        timeLeft -= 1;
        if(timeLeft < 0){
          clearInterval(timerInterval);
          timerInterval = null;
          endGame();
          return;
        }
        updateTimerUI();
        // coals slowly drop
        if(timeLeft % 4 === 0){ coals = Math.max(0, coals - 1); updateCoals(); }
        // update meat cooking speed
        document.querySelectorAll('.meat.on-grill').forEach(el=>{
          const state = el.dataset.state || 'raw';
          let progress = Number(el.dataset.progress || 0);
          // cooking speed scales with coal
          const speed = 1 + (coals/100)*0.6;
          progress += 0.6 * speed;
          el.dataset.progress = progress;
          updateMeatVisual(el);
        });
      }, 1000);
    }

    function updateTimerUI(){
      const pct = Math.max(0, (timeLeft/gameDuration)*100);
      timerBar.style.width = pct+'%';
      const mm = String(Math.floor(timeLeft/60)).padStart(2,'0');
      const ss = String(timeLeft%60).padStart(2,'0');
      timeText.textContent = `${mm}:${ss}`;
    }

    function updateCoals(){ coalsEl.textContent = Math.round(coals)+'%'; }

    function endGame(){
      alert(`게임 종료! 최종 점수: ${score}`);
    }

    // spawn meat into inventory
    function spawnMeat(){
      const m = document.createElement('div');
      m.className='meat';
      m.draggable = true;
      m.textContent = '고기';
      m.dataset.progress = 0; // 0..100
      m.dataset.state = 'raw';
      m.addEventListener('dragstart', e=>{
        e.dataTransfer.setData('text/plain', 'meat');
        e.dataTransfer.setData('text/id', m.dataset.id || '');
        // reference element id
        dragged = m;
      });
      m.addEventListener('click', ()=>{
        // if on grill, flip / speed change
        if(m.classList.contains('on-grill')){
          m.dataset.flipped = (m.dataset.flipped === '1') ? '0' : '1';
          // flipping reduces progress slightly (simulating thicker side)
          m.dataset.progress = Math.max(0, Number(m.dataset.progress) - 6);
          updateMeatVisual(m);
        }
      });
      inventory.appendChild(m);
      startTimer();
      return m;
    }

    spawnBtn.addEventListener('click', ()=>spawnMeat());
    resetBtn.addEventListener('click', ()=>location.reload());

    // drop handler
    let dragged = null;
    function onDropToSpot(e){
      e.preventDefault();
      const spot = e.currentTarget;
      // find first empty spot element inside
      if(spot.querySelector('.meat')){
        // if spot occupied, swap back to inventory
        return; // do nothing
      }
      if(!dragged){
        // if text drop, try to clone
        return;
      }
      // move dragged into spot
      spot.appendChild(dragged);
      dragged.classList.add('on-grill');
      dragged.dataset.progress = Number(dragged.dataset.progress || 0);
      updateMeatVisual(dragged);
      dragged = null;
    }

    // update meat appearance based on progress
    function updateMeatVisual(el){
      const p = Number(el.dataset.progress || 0);
      // thresholds
      if(p < 30){ el.dataset.state='raw'; el.classList.remove('cooked-1','cooked-2','burn'); }
      else if(p < 60){ el.dataset.state='cooked-1'; el.classList.add('cooked-1'); el.classList.remove('cooked-2','burn'); }
      else if(p < 90){ el.dataset.state='cooked-2'; el.classList.add('cooked-2'); el.classList.remove('cooked-1','burn'); }
      else { el.dataset.state='burn'; el.classList.add('burn'); el.classList.remove('cooked-1','cooked-2'); }

      // small scaled transform to show progress
      el.style.transform = `scale(${1 + Math.min(0.06, p/1000)})`;
    }

    // periodic check for cooked meat to score
    setInterval(()=>{
      document.querySelectorAll('.meat.on-grill').forEach(m=>{
        const p = Number(m.dataset.progress || 0);
        const state = m.dataset.state;
        // if fully cooked/burned beyond certain threshold, auto remove and score
        if(p >= 95){
          // score based on state
          if(state === 'cooked-2') score += 25;
          else if(state === 'cooked-1') score += 10;
          else if(state === 'raw') score += 0;
          else if(state === 'burn') score -= 5;
          scoreEl.textContent = score;
          // remove meat
          m.remove();
        }
      });
    }, 1200);

    // allow removing from grill by clicking while holding alt
    document.addEventListener('keydown', e=>{ if(e.key==='Escape') location.reload(); });

    // download file
    downloadBtn.addEventListener('click', ()=>{
      const blob = new Blob([document.documentElement.outerHTML], {type:'text/html'});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url; a.download = 'gogi-gubgi-game.html';
      document.body.appendChild(a); a.click(); a.remove();
      URL.revokeObjectURL(url);
    });

    moreBtn.addEventListener('click', ()=>{
      alert('추가 기능 제안: 레벨 시스템, 배경음악, 멀티플레이, 다양한 고기(돼지/소/닭) 추가 등을 원하시면 알려주세요!');
    });

    // initial spawn
    for(let i=0;i<3;i++) spawnMeat();
    updateTimerUI(); updateCoals();

    // touch support for mobile (simple) - tap to pick/drop
    let touchPicked = null;
    document.addEventListener('touchstart', e=>{
      const t = e.target.closest('.meat');
      if(t){ touchPicked = t; }
    });
    document.addEventListener('touchend', e=>{ touchPicked = null; });

    // small helper: click meat in inventory to move to first empty spot
    inventory.addEventListener('click', e=>{
      const m = e.target.closest('.meat');
      if(!m) return;
      // find empty spot
      const empty = spots.find(s=>!s.querySelector('.meat'));
      if(empty){ empty.appendChild(m); m.classList.add('on-grill'); startTimer(); }
    });

  </script>
</body>
</html>
