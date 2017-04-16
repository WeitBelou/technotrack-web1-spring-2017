$(function () {
        $('.autoload').each(function () {
            $(this).load($(this).attr('data-url'));
        });

        setInterval(function () {
            $('.autoload').each(function () {
                $(this).load($(this).attr('data-url'))
            });
        }, 3000);

        $('select').select2();

        $.fm({debug: false});
        $('body').on("fm.ready", function () {
            $('select').select2();
        })
    }
);