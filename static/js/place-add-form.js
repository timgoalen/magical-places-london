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

        // const photosArray = place.photos;
        // console.log(photosArray[0]);
        // console.log(photosArray[0].getUrl);

        if (place.photos && place.photos.length > 0) {
            // Access the first photo in the array
            const firstPhoto = place.photos[0];

            // Get the URL of the photo with a maximum width of 400 pixels
            const photoUrl = firstPhoto.getUrl({ maxHeight: 200 });

            // Set the src attribute of an img element to display the photo
            const imgElement = document.getElementById("photo");
            imgElement.src = photoUrl;

            // Set alt title
            imgElement.alt = place.name + " Photo";

            photoUrlField.value = photoUrl

            // TODO could also set a backup image if there aren't any from google
        }
    })
}

// or DOM on load??..
window.onload = initAutocomplete;