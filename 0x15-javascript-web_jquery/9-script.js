#!/usr/bin/node

const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr'
$(document).ready(function (event) {
	$.getJSON(url, function (data) {
		$("#hello").text(data.hello);
	})
})
