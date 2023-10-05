const backBtn = document.getElementById("back-btn");

function goBack() {
    if (window.history.length > 1) {
        const referredUrl = document.referrer;
        // ***CHANGE WHEN DEPLOYED
        const magicalPlacesUrl = "https://8000-timgoalen-magicalplaces-xikc2aho5al.ws-eu105.gitpod.io/";
        const comment = "comment";
        const listViewUrl = magicalPlacesUrl + "list_view/"

        // TODO: explain logic in comments
        if (referredUrl.startsWith(magicalPlacesUrl)) {
            if (referredUrl.includes(comment)) {
                window.location.href = listViewUrl;
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