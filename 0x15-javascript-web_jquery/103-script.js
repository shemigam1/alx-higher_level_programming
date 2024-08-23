#!/usr/bin/node

$(document).ready(function () {
	function fetchTranslation() {
		const langCode = $('#language_code').val();
		const apiUrl = `https://www.fourtonfish.com/hellosalut/?lang=${langCode}`;
		$.getJSON(apiUrl, function (data) {
			$('#hello').text(data.hello);
		})
	}
	$('#btn_translate').click(function () {
		fetchTranslation();
	})
	$('#language_code').keypress(function (event) {
		if (event.which === 13) {
			fetchTranslation()
		}
	})
})
