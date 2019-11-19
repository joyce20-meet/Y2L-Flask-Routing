$(document).ready(function () {
    if (Cookies.get('pandoragroup-consent') != 'accepted') {
        $(".js--cookie-compliance").show();
    };

    $(document).on("click", ".accept-link",
        function (event) {
            $(".js--cookie-compliance").hide();
            Cookies.set('pandoragroup-consent', 'accepted', { expires: 29, path: '/' });
        });
});