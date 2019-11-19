$(document).ready(function () {
    var currentPage = $('#Url').val();
    $('#vacancies-page__filter').val(currentPage);

    $('#vacancies-page__filter').on('change', function () {
        var currentPage = $('#Url').val();
        if (this.value != currentPage) {
            window.location.replace(this.value);
        }
    });
});