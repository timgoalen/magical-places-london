const searchInput = document.getElementById("search-input");
const nameField = document.getElementById("name-field");
const latitudeField = document.getElementById("latitude-field");
const longitudeField = document.getElementById("longitude-field");
const addressField = document.getElementById("address-field");
const googlePlaceIdField = document.getElementById("google-place-id-field");

// Create Google Places autocomplete functionality for place searches. 
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
        fields: ["formatted_address", "geometry", "name", "photos", "place_id"],
        strictBounds: true,
    };

    const autocomplete = new google.maps.places.Autocomplete(searchInput, options);

    // When a place is chosen, automatically fill in the hidden form fields.
    autocomplete.addListener("place_changed", () => {
        const place = autocomplete.getPlace();
        const coordinates = place.geometry.location;
        const latitude = coordinates.lat();
        const longitude = coordinates.lng();

        nameField.value = place.name;
        latitudeField.value = latitude;
        longitudeField.value = longitude;
        addressField.value = place.formatted_address;
        googlePlaceIdField.value = place.place_id;

        // Get a single photo URL from Google Places.
        if (place.photos && place.photos.length > 0) {
            // Get the URL of the first photo in the array.
            const photoUrl = place.photos[0].getUrl({
                maxHeight: 750, maxWidth: 750,
            });

            // Set the src attribute of the img element in the place card.
            const imgElement = document.getElementById("photo");
            imgElement.src = photoUrl;

            // Set the alt title.
            imgElement.alt = place.name + " Photo";
        }

        // Show the place card once the user has clicked on a place.
        const placeAddForm = document.getElementById("place-add-form");
        const placeTitle = document.getElementById("add-form-title");
        const placeAddress = document.getElementById("add-form-address");

        placeAddForm.style.display = "flex";
        placeTitle.textContent = place.name;
        placeAddress.textContent = place.formatted_address;
    });
}

// Call the function on window load.
window.addEventListener("load", initAutocomplete);