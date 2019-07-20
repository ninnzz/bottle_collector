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

