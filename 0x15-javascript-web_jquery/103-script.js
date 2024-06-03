$(document).ready(function () {
    function fetchHello() {
        const lang = $('#language_code').val();
        const url = `https://fourtonfish.com/hellosalut/?lang=${lang}`;
        $.get(url, function (data) {
            $('#hello').text(data.hello);
        });
    }
    $('#btn_translate').click(fetchHello);
    $('#language_code').keypress(function (e) {
        if (e.which === 13) {
            fetchHello();
        }
    });
});