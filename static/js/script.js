/* jshint esversion: 8 */

// Initialize the map.
let map;

// Set london bounds to restrict map size.
const LONDON_BOUNDS = {
    north: 51.709761,
    south: 51.300915,
    west: -0.516783,
    east: 0.270798,
};

// Set london center coordinates.
const LONDON = {
    lat: 51.50758960849218,
    lng: -0.12495345904150813
};

// Get JSON data from the json_script tag in the home.html template.
const jsonData = JSON.parse(document.getElementById("places-json-data").textContent);

// Iniltialise an array to hold URLs from Google Places library.
const photoUrlsArray = [];

// Create an new array of objects from the JSON data: the main "locations" data.
const places = jsonData.map(function (place) {
    const title = place.place_name;
    const position = {
        lat: place.latitude,
        lng: place.longitude
    };
    const id = place.id;
    const googlePlaceId = place.google_place_id;
    const commentsCount = place.comments_count;

    return {
        title: title,
        position: position,
        id: id,
        googlePlaceId: googlePlaceId,
        commentsCount: commentsCount,
    };
});

// MAIN 'CREATE MAP' FUNCTION:

async function initMap() {
    // Request needed libraries.
    const {
        Map,
        InfoWindow
    } = await google.maps.importLibrary("maps");
    const {
        Places
    } = await google.maps.importLibrary("places");
    const {
        AdvancedMarkerElement,
        PinElement
    } = await google.maps.importLibrary(
        "marker",
    );

    // The map, centered and restricted to London.
    map = new Map(document.getElementById("map"), {
        center: LONDON,
        restriction: {
            latLngBounds: LONDON_BOUNDS,
            strictBounds: false,
        },
        zoom: 12,
        // Link to Google Cloud custom map preferences.
        mapId: "3d039a2500323a92",
        // Disable unwanted controls.
        disableDefaultUI: true,
        zoomControl: true,
        mapTypeControl: false,
        scaleControl: true,
        streetViewControl: false,
        rotateControl: false,
        fullscreenControl: false
    });

    // Create info window to be shared between markers.
    const infoWindow = new InfoWindow({
        maxWidth: 180
    });

    // WIP: GETTING PHOTOS...
    const getPhotoPromises = places.map(({
        id,
        googlePlaceId
    }) => {
        return new Promise((resolve, reject) => {
            const request = {
                placeId: googlePlaceId,
                fields: ['photos']
            };

            function callback(place, status) {
                if (status == google.maps.places.PlacesServiceStatus.OK) {
                    const googlePhotoUrl = place.photos[0].getUrl({
                        maxHeight: 150, maxWidth: 150,
                    });
                    photoUrlsArray.push({
                        url: googlePhotoUrl,
                        id: id
                    });
                    resolve();
                } else {
                    reject(new Error(`Error fetching photo for place with id ${id}`));
                }
            }

            const service = new google.maps.places.PlacesService(map);
            service.getDetails(request, callback);
        });
    });

    // Wait for all photo fetching promises to resolve.
    Promise.all(getPhotoPromises)
        .then(() => {
            // All photos have been fetched, and photoUrlsArray is populated.
            console.log({
                photoUrlsArray
            });

            // Now photoUrlsArray is available to get photo URLs for markers.
            // Create markers from the 'places' array.
            places.forEach(({
                position,
                title,
                id,
                googlePlaceId,
                commentsCount,
            }, ) => {
                // Set pin.
                const customPin = new PinElement({
                    background: "#BF553B",
                    scale: 0.9,
                    borderColor: "#fff",
                    glyphColor: "#fff",
                });
                // Set content.
                const detailUrl = `/place/${id}/`;
                const htmlH2 = `<h2 class="map-view-place-title"><a href="${detailUrl}">${title}</a></h2>`;

                // WIP: get url from 'photoUrlsArray'.
                const targetId = id;
                const targetObject = photoUrlsArray.find(obj => obj.id === targetId);
                const photoUrlForMarker = targetObject.url;
                console.log({
                    photoUrlForMarker
                });

                const htmlPhoto = `<a href="${detailUrl}"><img src="${photoUrlForMarker}" alt="${title} Photo" class="map-place-photo"></a>`;

                let commentsMessage = "Comments";
                if (commentsCount == 1) {
                    commentsMessage = "Comment";
                }
                const htmlCommentsCount = `<a href="${detailUrl}" class="comments-count-text">${commentsCount} ${commentsMessage}</a>`;

                const titleHtml = htmlPhoto + htmlH2 + htmlCommentsCount;

                const marker = new AdvancedMarkerElement({
                    position,
                    map,
                    title: titleHtml,
                    content: customPin.element,
                });

                // Add a click listener for each marker, and set up the info window.
                marker.addListener("click", ({
                    domEvent,
                    latLng
                }) => {
                    const {
                        target
                    } = domEvent;

                    infoWindow.close();
                    infoWindow.setContent(marker.title);
                    infoWindow.open(marker.map, marker);
                });

                map.addListener("click", function () {
                    if (infoWindow) infoWindow.close();
                });
            });
        })
        .catch(error => {
            console.error(error);
        });
}

// Call function on window load.
window.addEventListener("load", initMap);