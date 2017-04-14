$(document).ready(
    function () {
        $('.autoload').each(function () {
            $(this).load($(this).attr('data-url'));
        });
        setInterval(function () {
            $('.autoload').each(function () {
                $(this).load($(this).attr('data-url'))
            });
        }, 3000);
    }
);

$(function () {
        $('.load-on-click').click(function () {
            var data = $(this).data();
            $(data.destination).load(data.url);
        });
    }
);