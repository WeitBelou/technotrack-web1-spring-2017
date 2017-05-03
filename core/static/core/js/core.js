$(function () {
        // Автообновляемые элементы
        function loadItems() {
            $('.autoload').each(function () {
                $(this).load($(this).attr('data-url'));
            });
        }

        loadItems();
        setInterval(loadItems, 3000);

        // Отклики на лайки
        $(this).on('click', 'a.ajaxlike', function () {
            var likeHeart = $(this);

            var data = likeHeart.data();

            var likesSpan = $('#likes-' + data.postId);

            $.ajax({url: data.url, method: 'post'}).done(function (data, status, response) {
                var responseData = $.parseJSON(response.responseText);

                // \todo Переписать на toggleClass
                if (responseData.is_liked) {
                    likeHeart.removeClass("text-muted").addClass("text-danger");
                } else {
                    likeHeart.removeClass("text-danger").addClass("text-muted");
                }

                likesSpan.html(responseData.n_likes);
            });

            return false;
        });


        // Настраиваем django-fm
        $.fm({debug: false});

        // Настройка автокомплита в select'ах
        $('select').select2();
        $('body').on("fm.ready", function () {
            $('select', this).select2();
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