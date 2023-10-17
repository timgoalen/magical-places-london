const messageContainers = Array.from(document.getElementsByClassName("messages"));

function closeMessage(event) {
    event.target.style.display = "none";
}

// Automatically close Django messages after 1.5 seconds.
messageContainers.forEach(container => {
    setTimeout(() => {
        container.style.display = "none";
    }, 1500);
    // Allow the user to dismiss the modal by clicking anywhere on the screen.
    container.addEventListener("click", closeMessage);
});