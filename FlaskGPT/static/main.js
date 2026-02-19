document.getElementById('send-btn').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (message === '') return;

    const chatWindow = document.getElementById('chat-window');
    chatWindow.innerHTML += `<div class="user-message">${message}</div>`;
    input.value = '';

    const response = await fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message})
    });

    const data = await response.json();
    chatWindow.innerHTML += `<div class="bot-message">${data.reply}</div>`;
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

