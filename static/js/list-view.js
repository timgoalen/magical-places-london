/* jshint esversion: 8 */

const listSortOptions = Array.from(document.getElementsByClassName("list-sort-item"));
const footer = document.getElementById("list-view-footer");
const spinnerContainer = document.getElementById("spinner-container");

// Show list-sort chosen option in UI.
function updateSortOptionUi(element) {
    element.classList.remove("inactive-option");
    element.classList.add("active-option");
}

// 'USER_SORT_SELECTION' is sent from Django to the template, and passed to JS in a script.
if (USER_SORT_SELECTION === "default") {
    updateSortOptionUi(listSortOptions[1]);
} else if (USER_SORT_SELECTION === "a-z") {
    updateSortOptionUi(listSortOptions[0]);
} else if (USER_SORT_SELECTION === "newest") {
    updateSortOptionUi(listSortOptions[1]);
} else if (USER_SORT_SELECTION === "my-favourites") {
    updateSortOptionUi(listSortOptions[2]);
}

// Hide footer on down-scroll, reveal on up-scroll.
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

// -- GET PHOTOS FROM GOOGLE PLACES ON PAGE LOAD --

// Get JSON data from the json_script tag in the 'list-view.html' template.
let jsonData = JSON.parse(document.getElementById("places-json-data").textContent);

// Create an new array of objects from the JSON data to get the Google Place IDs.
const places = jsonData.map(function (place) {
    const id = place.id;
    const google_place_id = place.google_place_id;

    return {
        id: id,
        google_place_id: google_place_id,
    };
});

// Get an up-to-date URL of the Google photo by passing the Google 'place_id'.
function getNewPhotoLink(id) {
    return new Promise((resolve, reject) => {
        let map;

        map = new google.maps.Map(document.createElement("div"));

        const request = {
            placeId: id,
            fields: ["photos"]
        };

        function callback(place, status) {
            if (status == google.maps.places.PlacesServiceStatus.OK) {
                if (place.photos) {
                    const googlePhotoUrl = place.photos[0].getUrl({
                        maxHeight: 550,
                        maxWidth: 550,
                    });
                    resolve(googlePhotoUrl);
                } else {
                    // Handle when no Google photo exists.
                    const googlePhotoUrl = "no photo found";
                    resolve(googlePhotoUrl);
                }
            } else {
                reject(new Error("Error fetching place details"));
            }
        }
        // Send the request to Google.
        var service = new google.maps.places.PlacesService(map);
        service.getDetails(request, callback);
    });
}

// On page load, get a new photo URL and add it to the img.src.
window.addEventListener("load", async function () {
    for (const place of places) {
        try {
            const googlePlaceId = place.google_place_id;
            const placePhoto = await getNewPhotoLink(googlePlaceId);
            const imageElement = document.getElementById(`img-for-place-${place.id}`);
            if (imageElement) {
                if (placePhoto == "no photo found") {
                    console.log(`No Google photo exists for the place with this id: ${googlePlaceId}.`);
                } else {
                    imageElement.src = placePhoto;
                }
            } else {
                console.log("This place isn't in the user's favourites");
            }
        } catch (error) {
            console.error(error);
        }
    }
    // Once finished, hide the div that covers the loading.
    setTimeout(() => {
        spinnerContainer.classList.add("hide-spinner");
      }, 300);
});

document.addEventListener("DOMContentLoaded", () => {
    window.addEventListener("scroll", collapseFooter);
});