let currentQuestionIndex = 0;
let questions;
let UUID;
const chatContainer = document.getElementById('chat-content');

async function get_uuid(url) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
        });

        const result = await response.json();
        
        UUID = result.UUID
        questions = result.questions

    } catch (error) {
        console.error('Error fetching UUID:', error);
        throw error;
    }
}

const observer = new MutationObserver(() => {
  scrollToBottom();
});

observer.observe(chatContainer, {
  childList: true,
  subtree: true
});

function selectAnswer(answer) {
    document.getElementById("input-answer").value = answer;
    submitAnswer();
}

function displayQuestion() {
    const chatContent = document.getElementById("chat-content");
    const currentQuestion = questions[currentQuestionIndex];
    const questionText = document.createElement("p");
    questionText.textContent = currentQuestion.question;

    if (currentQuestion.type === 'multiple') {
        const optionsList = document.createElement("ul");
        optionsList.classList.add("options-list");

        currentQuestion.options.forEach(option => {
            const li = document.createElement("li");
            const a = document.createElement("a");
            a.href = "#";
            a.textContent = option;
            li.onclick = () => selectAnswer(option);
            li.appendChild(a);
            optionsList.appendChild(li);
        });

        const questionContainer = document.createElement("div");
        questionContainer.classList.add("question-container");
        questionContainer.appendChild(questionText);
        questionContainer.appendChild(optionsList);
        chatContent.appendChild(questionContainer);
    } else if (currentQuestion.type === 'open') {
        const questionContainer = document.createElement("div");
        questionContainer.classList.add("question-container");
        questionContainer.appendChild(questionText);
        chatContent.appendChild(questionContainer);
    }

    scrollToBottom();
}

function submitAnswer() {
    const inputAnswer = document.getElementById("input-answer").value.trim();
    const chatContent = document.getElementById("chat-content");

    if (inputAnswer === "") {
        alert("Vui lòng nhập câu trả lời.");
        return;
    }

    let userMessage = document.createElement("div");
    userMessage.classList.add("user-message");
    userMessage.textContent = inputAnswer;
    chatContent.appendChild(userMessage);

    scrollToBottom();

    currentQuestionIndex++;

    if (currentQuestionIndex < questions.length) {
        setTimeout(() => {
            displayQuestion();
        }, 2000);
    } else {
        let endMessage = document.createElement("div");
        endMessage.classList.add("bot-message");
        endMessage.textContent = "Cảm ơn bạn đã tham gia khảo sát của chúng mình!";
        chatContent.appendChild(endMessage);
    }

    document.getElementById("input-answer").value = "";
}

function scrollToBottom() {
    const chatContent = document.getElementById("chat-content");

    const isAtBottom = chatContent.scrollHeight - chatContent.scrollTop === chatContent.clientHeight;

    if (isAtBottom) {
        chatContent.scrollTop = chatContent.scrollHeight;
    } else {
        chatContent.scrollTop = chatContent.scrollTop;
    }
}

function startSurvey() {
    const chatContent = document.getElementById("chat-content");
    const startMessage = document.createElement("div");
    startMessage.classList.add("bot-message");
    startMessage.textContent = "Chào bạn! Chúng tôi muốn biết ý kiến của bạn về mỉa mai. Bạn có sẵn sàng tham gia khảo sát không?";
    chatContent.appendChild(startMessage);

    scrollToBottom();

}

window.onload = function() {
    get_uuid("https://nguyien.app.n8n.cloud/webhook-test/90048586-d1ac-402c-b584-192b5105c3d5")
    startSurvey();
};
