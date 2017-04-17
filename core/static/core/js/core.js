$(function () {
        // Автообновляемые элементы
        $('.autoload').each(function () {
            $(this).load($(this).attr('data-url'));
        });

        setInterval(function () {
            $('.autoload').each(function () {
                $(this).load($(this).attr('data-url'))
            });
        }, 3000);

        // Отклики на лайки
        $(this).on('click', 'a.ajaxlike', function () {
            var data = $(this).data();

            var likesSpan = $('#likes-' + data.postId);
            var likeHeart = $(this);

            $.ajax({url: data.url, method: 'post'}).done(function (data, status, response) {
                    var responseData = $.parseJSON(response.responseText);

                    if (responseData.is_liked) {
                        $(likeHeart).removeClass("text-muted");
                        $(likeHeart).addClass("text-danger");
                    } else {
                        $(likeHeart).removeClass("text-danger");
                        $(likeHeart).addClass("text-muted");
                    }

                    $(likesSpan).html(responseData.n_likes);
                }
            );

            return false;
        });

        // Настройка автокомплита в select'ах
        $('select').select2();

        // Настраиваем django-fm
        $.fm({debug: false});
        $('body').on("fm.ready", function () {
            $('select').select2();
        });

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });
    }
);