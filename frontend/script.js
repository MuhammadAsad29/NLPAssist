async function askQuestion() {
    const input = document.getElementById("question");
    const question = input.value.trim();
    if (!question) return;

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="user">You: ${question}</div>`;
    input.value = "";

    const thinking = document.createElement("div");
    thinking.className = "bot";
    thinking.innerText = "Thinking...";
    chatBox.appendChild(thinking);

    const response = await fetch("http://127.0.0.1:8000/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
    });

    const data = await response.json();
    chatBox.removeChild(thinking);

    chatBox.innerHTML += `
        <div class="bot">
            Bot: ${data.answer}<br>
            <small>Source: ${data.sources.join(", ")}</small>
        </div>
    `;
}
