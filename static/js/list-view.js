const footer = document.getElementById("list-view-footer");
const listSortOptions = Array.from(document.getElementsByClassName("list-sort-item"));

let prevScrollPosition = 0;

// Hide footer on down-scroll

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

// function updateSortOptionUi(event) {
//     window.onload = function() {
//         listSortOptions.forEach(option => {
//             option.classList.remove("active-option");
//             option.classList.add("inactive-option");
//         });
//         event.target.classList.remove("inactive-option");
//         event.target.classList.add("active-option");
//     }
// }

// listSortOptions.forEach(option => option.addEventListener("click", updateSortOptionUi));
