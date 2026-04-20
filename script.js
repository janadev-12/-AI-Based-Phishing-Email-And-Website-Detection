const commands = [
    "Initializing AI...",
    "Scanning input...",
    "Extracting features...",
    "Running ML model...",
    "Finalizing result..."
];

async function startAnalysis() {

    let terminal = document.getElementById("terminal");
    let resultBox = document.getElementById("resultBox");
    let resultText = document.getElementById("resultText");
    let progress = document.getElementById("progress");

    terminal.innerHTML = "";
    resultBox.style.display = "none";
    progress.style.width = "0%";

    for (let cmd of commands) {
        await typeLine(cmd, terminal);
        await delay(400);
    }

    let input = document.getElementById("inputText").value;

    let response = await fetch("http://127.0.0.1:5000/detect", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email: input,
            url: input
        })
    });

    let data = await response.json();

    resultBox.style.display = "block";
    resultText.innerText = `${data.result} (${data.confidence}%)`;

    let percent = data.result === "Phishing" ? 85 : 25;

    let width = 0;
    let interval = setInterval(() => {
        if (width >= percent) clearInterval(interval);
        width++;
        progress.style.width = width + "%";
    }, 15);
}

function typeLine(text, element) {
    return new Promise(resolve => {
        let i = 0;
        let line = document.createElement("div");
        element.appendChild(line);

        let interval = setInterval(() => {
            line.innerHTML += text.charAt(i);
            i++;
            if (i >= text.length) {
                clearInterval(interval);
                resolve();
            }
        }, 20);
    });
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
// MATRIX EFFECT (FIXED)

window.onload = function () {

    const canvas = document.getElementById("matrix");
    if (!canvas) return;

    const ctx = canvas.getContext("2d");

    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }

    resizeCanvas();

    const letters = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const fontSize = 14;
    const columns = Math.floor(canvas.width / fontSize);

    const drops = Array(columns).fill(1);

    function draw() {
        ctx.fillStyle = "rgba(0, 0, 0, 0.08)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);

        ctx.fillStyle = "#00ff00";
        ctx.font = fontSize + "px monospace";

        for (let i = 0; i < drops.length; i++) {
            const text = letters.charAt(Math.floor(Math.random() * letters.length));
            ctx.fillText(text, i * fontSize, drops[i] * fontSize);

            if (drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                drops[i] = 0;
            }

            drops[i]++;
        }
    }

    setInterval(draw, 33);

    window.addEventListener("resize", resizeCanvas);
};