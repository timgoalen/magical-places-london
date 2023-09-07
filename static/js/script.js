// "use strict";

// Initialize and add the map
let map;

// set london bounds to restrict map size
const LONDON_BOUNDS = {
    north: 51.709761,
    south: 51.300915,
    west: -0.516783,
    east: 0.270798,
};

// set london center coordinates
const LONDON = {
    lat: 51.50758960849218,
    lng: -0.12495345904150813
};

// Get JSON data from the json_script tag in the home.html template
let jsonData = JSON.parse(document.getElementById("places-json-data").textContent);

// Create an new array of objects from the JSON data: our main "locations" data
const locations = jsonData.map(function (place) {
    const title = place.place_name;
    const position = {
        lat: place.latitude,
        lng: place.longitude,
    };

    return {
        title: title,
        position: position,
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
        AdvancedMarkerElement,
        PinElement
    } = await google.maps.importLibrary(
        "marker",
    );

    // The map, centered and restricted to London
    map = new Map(document.getElementById("map"), {
        center: LONDON,
        restriction: {
            latLngBounds: LONDON_BOUNDS,
            strictBounds: false,
        },
        zoom: 12,
        // TG: links to google cloud map preferences
        mapId: "3d039a2500323a92",
        // TG: to disable unwanted controls
        disableDefaultUI: true,
        zoomControl: true,
        mapTypeControl: false,
        scaleControl: true,
        streetViewControl: false,
        rotateControl: false,
        fullscreenControl: false
    });

    // create info window to be shared between markers
    const infoWindow = new InfoWindow();

    // create markers with custom pin appearance
    locations.forEach(({
        position,
        title
    }, ) => {
        const customPin = new PinElement({
            background: "#6a86d8",
            scale: 0.8,
            borderColor: "#000",
            glyphColor: "#6a86d8",
        });

        const marker = new AdvancedMarkerElement({
            position,
            map,
            title: `${title}`,
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

        map.addListener('click', function () {
            if (infoWindow) infoWindow.close();
        });
    });
}

initMap();