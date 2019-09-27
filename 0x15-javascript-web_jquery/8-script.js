$.get('https://swapi.co/api/films/?format=json', function (data) {
  data.results.forEach(dict => {
    $('#list_movies')
      .append('<li>' + dict.title + '</li>');
  });
}, 'json');
