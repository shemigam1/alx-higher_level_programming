#!/usr/bin/node

$(document).ready(function () {
	$('#btn_translate').click(function() {
		const langCode = $('#language_code').val();
		const apiUrl = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;
		$.getJSON(apiUrl, function(data) {
			$('#hello').text(data.hello);
		})
	})
})
