const messageContainers = document.getElementsByClassName("messages");
const closeBtn = document.getElementById("close-btn");

function closeMessage(event) {
    event.target.style.display = "none";
}

for (let container of messageContainers) {
    setTimeout(function () {
        container.style.display = "none";
    }, 1000);
    // Option for user to dismiss modal by clicking
    container.addEventListener("click", closeMessage);
}

closeBtn.addEventListener("click", () => {
    window.history.back();
})