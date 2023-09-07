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

// set locations [will eventually be imported form database]
const locations = [{
        position: {
            lat: 51.51687117269946,
            lng: -0.09765328835864276
        },
        title: '<div class="location-card">' +
            "<h2 class='location-title'>Postman's Park</h2>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<hr>" +
            "<h3>Comments:</h3>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<a>Add a comment</a>" +
            "</div>",
    },
    {
        position: {
            lat: 51.52130447449036,
            lng: -0.0996416719434002
        },
        title: '<div class="location-card">' +
            "<h2 class='location-title'>The Charterhouse</h2>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<hr>" +
            "<h3>Comments:</h3>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<a>Add a comment</a>" +
            "</div>",
    },
    {
        position: {
            lat: 51.509995690319094,
            lng: -0.082391170638249222
        },
        title: '<div class="location-card">' +
            "<h2 class='location-title'>St Dunstan in the East</h2>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<hr>" +
            "<h3>Comments:</h3>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<a>Add a comment</a>" +
            "</div>",
    },
    {
        position: {
            lat: 51.566981762402506,
            lng: -0.16011848670533663
        },
        title: '<div class="location-card">' +
            "<h2 class='location-title'>Kenwood Ladies' Bathing Pond</h2>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<hr>" +
            "<h3>Comments:</h3>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<p class='location-details'>Postman's Park is a public garden in central London, a short distance north of St Paul's Cathedral. Bordered by Little Britain, Aldersgate Street, St. Martin's Le Grand, King Edward Street, and the site of the former headquarters of the General Post Office, it is one of the largest open spaces in the City of London.</p>" +
            "<a>Add a comment</a>" +
            "</div>",
        
    },
];

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
        // restriction: {
        //     latLngBounds: LONDON_BOUNDS,
        //     strictBounds: false,
        // },
        zoom: 11,
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

        map.addListener('click', function() {
            if (infoWindow) infoWindow.close();
        });
    });
}

initMap();