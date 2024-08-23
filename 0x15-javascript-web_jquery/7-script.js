#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
$(document).ready(function (event) {
	$.getJSON(url, function (data) {
		$("#character").text(data.name);
	})
})
