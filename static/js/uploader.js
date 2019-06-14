window.onload = function() {
    document.getElementById('spinner').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    document.getElementById('success').style.display = 'none';
    document.getElementById('submitButton').addEventListener('click', onClick);
    $('#imageForm').submit((event) => {
        event.preventDefault();
        const $form = $('#imageForm')
        const formData = new FormData($form.get()[0]);
        $.ajax({
            url: $form.attr('action'),
            type: $form.attr('method'),
            dataType: 'json',
            processData: false,
            contentType: false,
            data: formData,
        }).done((data) => {
            document.getElementById('spinner').style.display = 'none';
            console.log(data);
            if (data == null) {
                document.getElementById('error').style.display = 'block';
                document.getElementById('success').style.display = 'none';
            } else {
                const text = `正常な画像です。スコア:${data.result.score} / カテゴリー:${data.result.name}`;
                document.getElementById('success').style.display = 'block';
                document.getElementById('success').innerText = text;
                document.getElementById('error').style.display = 'none';
            }
        }).fail((data) => {
        }); 
    });
}

function onClick() {
    document.getElementById('spinner').style.display = 'block';
}