$(function(){
	$('button').click(function(){
		var bottles = $('#bottles').val();
		$.ajax({
			url: '/check_prices',
			data: $('bottles').serialize(),
			type: 'POST',
			success: function(check_prices){
				console.log(rand);
			},
			
		});
	});
});






$(document).ready(function (e) {
    $('#imageUploadForm').on('submit',(function(e) {
        e.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            type:'POST',
            url: $(this).attr('action'),
            data:formData,
            cache:false,
            contentType: false,
            processData: false,
            success:function(data){
                console.log(rand);
            },
            }
        });
    }));

    $("#ImageBrowse").on("change", function() {
        $("#imageUploadForm").submit();
    });
});