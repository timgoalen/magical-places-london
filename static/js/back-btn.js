const backBtn = document.getElementById("close-btn");

// function navigateBack() {

// }

backBtn.addEventListener("click", () => {
    window.history.back();
})