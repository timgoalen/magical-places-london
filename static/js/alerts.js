const messagesContainer = document.querySelector("messages");

function closeMessage() {
    messagesContainer.style.display = "none";
}

messagesContainer.addEventListener("click", closeMessage);