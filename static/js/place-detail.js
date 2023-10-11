const backBtn = document.getElementById("back-btn");

// Back button functionalty in detail view (**explain the logic)

function goBack() {
    if (window.history.length > 1) {
        const currentUrl = window.location.href;
        const referredUrl = document.referrer;
        // ***CHANGE WHEN DEPLOYED
        const magicalPlacesUrl = "https://8000-timgoalen-magicalplaces-xikc2aho5al.ws-eu105.gitpod.io/";
        const comment = "comment";
        const listViewUrl = magicalPlacesUrl + "list_view/"

        // TODO: explain logic in comments
        if (referredUrl.startsWith(magicalPlacesUrl)) {
            if (referredUrl.includes(comment)) {
                window.location.href = listViewUrl;
            // send user back 2 steps if they've pressed the 'favourite' button
            // (if they press it twice there's a bug where they'll have to press back twice)
            } else if (currentUrl === referredUrl){
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