$(function () {
        $('.autoload').each(function () {
            $(this).load($(this).attr('data-url'));
        });

        setInterval(function () {
            $('.autoload').each(function () {
                $(this).load($(this).attr('data-url'))
            });
        }, 3000);

        $('.selectmultiple').chosen();
        $.fm({debug: false})
    }
);