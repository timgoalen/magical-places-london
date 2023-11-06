const placeDetailPhoto = document.getElementById("place-detail-photo");

function getNewPhotoLink() {
    var map;
    let googlePhotoUrl;

    map = new google.maps.Map(document.createElement("div"));

    var request = {
        placeId: GOOGLE_PLACE_ID,
        fields: ["photos", ]
    };

    function callback(place, status) {
        if (status == google.maps.places.PlacesServiceStatus.OK) {
            googlePhotoUrl = place.photos[0].getUrl({
                maxHeight: 650,
                maxWidth: 650,
            });
            placeDetailPhoto.src = googlePhotoUrl;
        }
    }

    var service = new google.maps.places.PlacesService(map);
    service.getDetails(request, callback);
}

window.addEventListener("load", () => {
    getNewPhotoLink();
    placeDetailPhoto.classList.add("show-photo");
});