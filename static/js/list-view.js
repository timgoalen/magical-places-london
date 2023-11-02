const listSortOptions = Array.from(document.getElementsByClassName("list-sort-item"));
const footer = document.getElementById("list-view-footer");

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

window.addEventListener("scroll", collapseFooter);

// PHOTOS WIP...

// Get JSON data from the json_script tag in the home.html template.
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

// function getNewPhotoLink(id) {
//     var map;
//     let googlePhotoUrl;

//     map = new google.maps.Map(
//         document.getElementById('map'), {});

//     var request = {
//         placeId: id,
//         fields: ['photos',]
//     };

//     function callback(place, status) {
//         if (status == google.maps.places.PlacesServiceStatus.OK) {
//             googlePhotoUrl = place.photos[0].getUrl({
//                 maxHeight: 800
//             });
//             // googlePhotoUrl = googlePhotoUrl;
//             // console.log(googlePhotoUrl);
//         }
//     }

//     var service = new google.maps.places.PlacesService(map);
//     service.getDetails(request, callback);

//     return googlePhotoUrl;
// }

// window.addEventListener('load', function() {
//     // Your function to be executed on page load
//     // getNewPhotoLink();
//     for (const place of places) {
//         console.log(place);
//         let googlePlaceId = place.google_place_id;
//         // getNewPhotoLink(googlePlaceId);
//         let placePhoto = getNewPhotoLink(googlePlaceId);
//         console.log({ placePhoto })
//     }
//   });

function getNewPhotoLink(id) {
    return new Promise((resolve, reject) => {
        var map;

        map = new google.maps.Map(document.getElementById("map"), {});

        var request = {
            placeId: id,
            fields: ["photos"]
        };

        function callback(place, status) {
            if (status == google.maps.places.PlacesServiceStatus.OK) {
                const googlePhotoUrl = place.photos[0].getUrl({
                    maxHeight: 800
                });
                resolve(googlePhotoUrl);
            } else {
                reject(new Error("Error fetching place details"));
            }
        }

        var service = new google.maps.places.PlacesService(map);
        service.getDetails(request, callback);
    });
}

window.addEventListener("load", async function () {
    for (const place of places) {
        try {
            const googlePlaceId = place.google_place_id;
            const placePhoto = await getNewPhotoLink(googlePlaceId);
            console.log({placePhoto});
            const imageElement = document.getElementById(`img-for-place-${place.id}`);
            imageElement.src = placePhoto;
        } catch (error) {
            console.error(error);
        }
    }
});