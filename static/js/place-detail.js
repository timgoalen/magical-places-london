const backBtn = document.getElementById("back-btn");

function goBack() {
    if (window.history.length > 1) {
        const referredUrl = document.referrer;
        // ***CHANGE WHEN DEPLOYED
        const magicalPlacesUrl = "https://8000-timgoalen-magicalplaces-xikc2aho5al.ws-eu105.gitpod.io/";

        if (referredUrl.startsWith(magicalPlacesUrl)) {
            window.history.back();
        } else {
            window.location.href = magicalPlacesUrl;
        }
    } else {
        window.location.href = magicalPlacesUrl;
    }
}

backBtn.addEventListener("click", goBack);