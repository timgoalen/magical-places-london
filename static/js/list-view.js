const footer = document.getElementById("list-view-footer");
const listSortOptions = Array.from(document.getElementsByClassName("list-sort-item"));

// Hide footer on down-scroll

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

// Show list-sort chosen option in UI

function updateSortOptionUi(element) {
    element.classList.remove("inactive-option");
    element.classList.add("active-option");
}

if (USER_SORT_SELECTION === "default") {
    updateSortOptionUi(listSortOptions[1]);
} else if (USER_SORT_SELECTION === "a-z") {
    updateSortOptionUi(listSortOptions[0]);
} else if (USER_SORT_SELECTION === "newest") {
    updateSortOptionUi(listSortOptions[1]);
} else if (USER_SORT_SELECTION === "my-favourites") {
    updateSortOptionUi(listSortOptions[2]);
}