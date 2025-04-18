const questions = [
    { type: 'multiple', question: "Bạn có dễ dàng nhận ra mỉa mai trong một cuộc trò chuyện không?", options: ["Có", "Không", "Thỉnh thoảng"] },
    { type: 'multiple', question: "Khi ai đó nói 'Ôi tuyệt vời, lại một thứ Hai nữa!', bạn sẽ hiểu thế nào?", options: ["Lạc quan", "Mỉa mai", "Đang vui"] },
    { type: 'multiple', question: "Mỉa mai có thể gây hại trong một cuộc thảo luận nghiêm túc không?", options: ["Có", "Không", "Tuỳ vào tình huống"] },
    { type: 'open', question: "Bạn nghĩ rằng mỉa mai có thể giúp giảm căng thẳng trong các tình huống khó xử không?", options: [] },
    { type: 'open', question: "Khi bạn nghe ai đó nói 'Chắc chắn, tôi yêu việc làm thêm giờ!', bạn nghĩ họ đang nói thật hay đang mỉa mai?", options: [] }
];

let currentQuestionIndex = 0;
const chatContainer = document.getElementById('chat-content');

const observer = new MutationObserver(() => {
  scrollToBottom();
});

observer.observe(chatContainer, {
  childList: true,
  subtree: true
});

function selectAnswer(answer) {
    const inputAnswer = document.getElementById("input-answer");
    inputAnswer.value = answer;
    return false;
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
            a.onclick = () => selectAnswer(option);
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

window.onload = function() {
    displayQuestion();
    scrollToBottom();
};
