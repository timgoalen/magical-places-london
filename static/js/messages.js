const messageContainers = document.getElementsByClassName("messages");

function closeMessage(event) {
    event.target.style.display = "none";
}

for (let container of messageContainers) {
    setTimeout(function () {
        container.style.display = "none";
    }, 1500);
    // Option for user to dismiss modal by clicking
    container.addEventListener("click", closeMessage);
}

function checkForCloseBtn() {
    const closeBtn = document.getElementById("close-btn");

    if (!closeBtn) {
        return
    }

    closeBtn.addEventListener("click", () => {
        window.history.back();
    })
}