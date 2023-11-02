const backBtn = document.getElementById("back-btn");
const magicalPlacesUrl = "https://magical-places-london-7d2df0d61638.herokuapp.com/";

const placeDetailPhoto = document.getElementById("place-detail-photo");

/**
 * Create back-button functionality for detail_view.html.
 * - if a user's previous window.history is an external site, send them back to the home page.
 * - if a user's referrer page is a 'comment' CRUD page, send them back to 'list_view.html'.
 * - els send them back to the previous visited page.
 */
function goBack() {
    if (window.history.length > 1) {
        const currentUrl = window.location.href;
        const referredUrl = document.referrer;
        const comment = "comment";
        const listViewUrl = magicalPlacesUrl + "list_view/";

        if (referredUrl.startsWith(magicalPlacesUrl)) {
            if (referredUrl.includes(comment)) {
                window.location.href = listViewUrl;
                // Send user back 2 steps if they've pressed the 'favourite' button.
            } else if (currentUrl === referredUrl) {
                window.history.go(-2);
            } else {
                window.history.back();
            }
        } else {
            window.location.href = magicalPlacesUrl;
        }
    } else {
        window.location.href = magicalPlacesUrl;
    }
}

backBtn.addEventListener("click", goBack);

// ADD COMMENT:

function getNewPhotoLink() {
    var map;
    let googlePhotoUrl;

    map = new google.maps.Map(
        document.getElementById('map'), {});

    var request = {
        placeId: GOOGLE_PLACE_ID,
        fields: ['photos',]
    };

    function callback(place, status) {
        if (status == google.maps.places.PlacesServiceStatus.OK) {
            googlePhotoUrl = place.photos[0].getUrl({
                maxHeight: 800
            });
            placeDetailPhoto.src = googlePhotoUrl;

        }
    }

    var service = new google.maps.places.PlacesService(map);
    service.getDetails(request, callback);

    return newPhotoUrl;
}

window.addEventListener('load', function() {
    // Your function to be executed on page load
    getNewPhotoLink();
  });