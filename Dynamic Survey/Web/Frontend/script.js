const chatContent = document.getElementById("chat-content");
const input = document.getElementById("input-answer");
const sessionId = Date.now().toString();

function addMessage(message, isUser = false) {
  if (!chatContent || !message.trim()) return;

  const div = document.createElement("div");
  div.className = isUser ? "message user-message" : "message ai-message";
  div.textContent = message;
  chatContent.appendChild(div);
  chatContent.scrollTop = chatContent.scrollHeight;
}

async function fetchFirstQuestion() {
  try {
    const response = await fetch("https://hanlg23416.app.n8n.cloud/webhook/sarcasm");
    const result = await response.json();
    addMessage(result.message || "Không có câu hỏi khởi động.");
  } catch (err) {
    addMessage("Lỗi khi lấy câu hỏi đầu tiên.");
  }
}

async function submitAnswer() {
  const answer = input?.value.trim();
  if (!answer) return;

  addMessage(answer, true);
  input.value = "";

  try {
    const response = await fetch("https://hanlg23416.app.n8n.cloud/webhook/sarcasm", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ sessionId, answer })
    });

    const result = await response.json();
    addMessage(result.message || "Không có phản hồi từ AI.");
  } catch (error) {
    addMessage("Lỗi kết nối tới AI.");
  }
}

input?.addEventListener("keypress", (e) => {
  if (e.key === "Enter") submitAnswer();
});

// Gọi câu đầu tiên khi trang vừa mở
window.addEventListener("DOMContentLoaded", fetchFirstQuestion);
