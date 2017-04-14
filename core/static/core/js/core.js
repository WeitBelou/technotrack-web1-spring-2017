$(document).ready(
    function () {
        $('.autoload').each(function () {
            $(this).load($(this).attr('data-url'));
        });
    }
);

$(function () {
        $('.load-on-click').click(function () {
            $(this).load($this).attr('data-url');
        });
    }
);