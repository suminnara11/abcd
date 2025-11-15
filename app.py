styles.css
:root {
--bg: #0f1220;
--card: #171a2b;
--text: #e6e6e6;
--accent: #7c5cff;
}
* { box-sizing: border-box; }
body {
margin: 0;
font-family: Arial, sans-serif;
background: var(--bg);
color: var(--text);
}
header {
padding: 1rem;
background: #1e1f2a;
display: flex;
justify-content: space-between;
align-items: center;
}
nav a { color: #ddd; margin: 0 8px; text-decoration: none; }
section { padding: 2rem; }

#games .card {
background: var(--card);
padding: 1rem;
margin: 0.5rem 0;
border-radius: 8px;
}

footer { padding: 1rem; text-align: center; color: #aaa; }

4) script.js
// 예시 데이터
const games = [
{ id: 1, title: "슈게임 스타일 미니게임 1", desc: "간단한 미니게임 예시" },
{ id: 2, title: "슈게임 스타일 미니게임 2", desc: "다른 미니게임 예시" }
];

// 렌더링
function renderGames() {
const list = document.getElementById("game-list");
list.innerHTML = "";
games.forEach(g => {
const div = document.createElement("div");
div.className = "card";
div.innerHTML =
${g.title}
${g.desc}

;
list.appendChild(div);
});
}

// 리더보드 예시
function renderLeaderboard() {
const ol = document.getElementById("leaderboard-list");
const scores = [
{ name: "홍길동", score: 120 },
{ name: "김영희", score: 95 },
];
ol.innerHTML = "";
scores.forEach(s => {
const li = document.createElement("li");
li.textContent = ${s.name} - ${s.score}점;
ol.appendChild(li);
});
}

document.addEventListener("DOMContentLoaded", () => {
renderGames();
renderLeaderboard();
});
