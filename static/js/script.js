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
            title: `<h2>${title}</h2>` +
                `<p>Columbia Rd Flower Market on a Sunday morning. Go early, coffee from one of the independent shops or vans, lovely stalls, little shops.

            Down to Spitalfields, drink in the Golden Heart in Commercial St, a proper ‘local’ featuring artwork by the artists who drank there, wander through Spitalfields or Brick Lane.</p>` + `<p>Comment 2...Dim Sum in Chinatown, wander round the little shops in Soho / bookshops on Charing Cross road, then the British Museum</p>` + `<p>Comment 3...St Pancras old church gardens to see the little stone marking where Mary Wollstonecraft was buried. Be sure to go into the stunningly beautiful tiny little church next to it. Easy walk from St Pancras or King’s Cross stations. Bunhill Fields for a tiny historical graveyard, then a wander through the beautiful Barbican estate.

            There are really lovely little community gardens all over the place in London- even really centrally like in the west end- Phoenix Garden, in Angel, Culpeper Garden. Just tiny little scraps of green space but so beautiful and sustaining.</p>`,
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