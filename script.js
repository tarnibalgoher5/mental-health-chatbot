document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('affirmation-button').addEventListener('click', getAffirmation);
document.getElementById('meditation-button').addEventListener('click', getMeditation);

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    displayMessage('You: ' + userInput);
    document.getElementById('user-input').value = '';

    // Call the Python backend to get the AI response
    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        displayMessage('AI: ' + data.response);
    });
}

function getAffirmation() {
    fetch('/affirmation')
    .then(response => response.json())
    .then(data => {
        displayMessage('Affirmation: ' + data.affirmation);
    });
}

function getMeditation() {
    fetch('/meditation')
    .then(response => response.json())
    .then(data => {
        displayMessage('Guided Meditation: ' + data.meditation);
    });
}

function displayMessage(message) {
    const conversation = document.getElementById('conversation');
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    conversation.appendChild(messageDiv);
    conversation.scrollTop = conversation.scrollHeight; // Scroll to the bottom
}