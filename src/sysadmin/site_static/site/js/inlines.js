$(function () {

    // когда пользователь нажимает, добавляет больше кнопок картинок
    $('.add-images').click(function(ev) {
        ev.preventDefault();
        var $total_forms = $('#id_images-TOTAL_FORMS');
        var $max_num_forms = $('#id_images-MAX_NUM_FORMS');
        if ($total_forms.val() < $max_num_forms.val()) {
            var rows = $('#item-images').children();
            var count = rows.not('.empty-form').length;
            var empty_form = rows.filter('.empty-form').first();
            var new_form = empty_form.clone(true);
            var compiledTmpl = $(new_form.html().replace(/__prefix__/g, count));
            var new_elem = $('<tr id="images-' + count + '" class="hide_all"></tr>');
            var test = new_elem.append(compiledTmpl);
            $('#item-images').append(test);

            // обновить количество форм
            $total_forms.val(count+1);
        }
    });

    // $('.remove-images').click(function(ev) {
    //     ev.preventDefault();
    //     var $total_forms = $('#id_images-TOTAL_FORMS');
    //     var $min_num_forms = $('#id_images-MIN_NUM_FORMS');
    //     if ($total_forms.val() > $min_num_forms.val()) {
    //         var rows = $('#item-images').children();
    //         var visible_rows = rows.not('.empty-form');
    //         var count = visible_rows.length;
    //         var last_row = visible_rows.last();
    //         last_row.remove();

    //         // обновить количество форм
    //         $total_forms.val(count-1);
    //     }
    // });

    // Действия при нажатии check is_primary
    $(document).on('change', "input:checkbox[id$='-is_primary']", function (e) {
        e.preventDefault();
        $.each($("input:checkbox[id$='-is_primary']"), function(i, item) {
            $(item).prop('checked', false);
        });
        $(this).prop('checked', true);
    });
    
    // Установка primary, если не указано ни одной primary картинки
    function set_primary_if_not_exist() {
        var $input_checkbox = $("input:checkbox[id$='-is_primary']");
        var $primary_exists = false;
        $.each($input_checkbox, function(i, item) {
            $primary_exists = $primary_exists || $(item).prop('checked');
        });
        if (!$primary_exists) {
            $input_checkbox.first().prop('checked', true);
        }
    }

    // Утсановка primary при первой загрузке
    set_primary_if_not_exist();
});

