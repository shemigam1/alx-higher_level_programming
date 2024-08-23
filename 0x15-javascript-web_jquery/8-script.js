#!/usr/bin/node

const url = 'https://swapi-api.alx-tools.com/api/films/?format=json'
$(document).ready(function (event) {
	$.getJSON(url, function (data) {
		data.results.forEach((movie) => {
			$("#list_movies").append('<li>' + movie.title + '</li>');
		})
	})
})
