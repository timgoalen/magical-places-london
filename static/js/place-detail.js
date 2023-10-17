const backBtn = document.getElementById("back-btn");
// *** CHANGE WHEN DEPLOYED
const magicalPlacesUrl = "https://8000-timgoalen-magicalplaces-xikc2aho5al.ws-eu105.gitpod.io/";

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