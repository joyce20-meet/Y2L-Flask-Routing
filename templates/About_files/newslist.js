
$(document).ready(function () {

    new URL(location.href).searchParams.forEach((value, name, searchParams) => {
        $('[data-toggle=' + name + "]").val(value);
    });

    $("[data-toggle]").change(function (obj) {
        var url = new URL(location.href);
        url.searchParams.set(obj.target.getAttribute("data-toggle"), $(this).val());
        window.location.replace(url.toString());
    });
    
});