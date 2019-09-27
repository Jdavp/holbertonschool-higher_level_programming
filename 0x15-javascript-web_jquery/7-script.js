$.get( "https://swapi.co/api/people/5/?format=json", function( data ) {
    $( "body" )
      .append( data.name ); 
  }, "json" );