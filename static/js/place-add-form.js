const searchInput = document.getElementById("search-input");

const photoField = document.getElementById("photo");

const nameField = document.getElementById("name-field");
const latitudeField = document.getElementById("latitude-field");
const longitudeField = document.getElementById("longitude-field");
const addressField = document.getElementById("address-field");
const photoUrlField = document.getElementById("photoUrl-field");

function initAutocomplete() {

    const LONDON_BOUNDS = {
        north: 51.709761,
        south: 51.300915,
        west: -0.516783,
        east: 0.270798,
    };

    const options = {
        bounds: LONDON_BOUNDS,
        componentRestrictions: {
            country: ["uk"]
        },
        fields: ["formatted_address", "geometry", "name", "photos"],
        strictBounds: true,
        // types: ??
    };

    const autocomplete = new google.maps.places.Autocomplete(searchInput, options);

    // note, "addListener" rather than "addEventListener":
    autocomplete.addListener("place_changed", () => {
        const place = autocomplete.getPlace();
        const coordinates = place.geometry.location;
        const latitude = coordinates.lat();
        const longitude = coordinates.lng();

        nameField.value = place.name;
        latitudeField.value = latitude;
        longitudeField.value = longitude;
        addressField.value = place.formatted_address;

        // Get the photo URL from Google Places
        if (place.photos && place.photos.length > 0) {
            // Access the first photo in the array
            const firstPhoto = place.photos[0];

            // Get the URL of the photo
            const photoUrl = firstPhoto.getUrl({
                maxHeight: 800
            });

            // Set the src attribute of the img element
            const imgElement = document.getElementById("photo");
            imgElement.src = photoUrl;

            // Set the alt title
            imgElement.alt = place.name + " Photo";

            photoUrlField.value = photoUrl;

            // TODO: could also set a backup image if there aren't any from google
        }

        // Show the form once the user has clicked on a place
        const placeAddForm = document.getElementById("place-add-form")
        placeAddForm.style.display = "flex";

        // Move focus to the 'Save' button [doesn't work]
        // const saveBtn = document.getElementById("place-add-save-bt");
        // saveBtn.focus();
        
        // const saveBtn = document.getElementById("place-add-save-bt");
        // saveBtn.addEventListener("click", function () {
        //     alert(`Thanks for submitting ${place.name}!`)
        // })
    })
}

// or DOM on load??..
window.onload = initAutocomplete;