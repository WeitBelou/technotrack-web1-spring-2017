$(document).ready(
    function () {
        $('.autoload').each(function () {
            $(this).load($(this).attr('data-url'));
        })
    }
);