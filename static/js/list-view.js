const footer = document.getElementById("list-view-footer");
let prevScrollPosition = 0;

function collapseFooter() {
    const scrollPosition = window.scrollY;

    if (scrollPosition > prevScrollPosition) {
        footer.style.transform = "translateY(100%)";
    } else {
        footer.style.transform = "translateY(0)";
    }

    prevScrollPosition = scrollPosition;
}

window.addEventListener("scroll", collapseFooter);