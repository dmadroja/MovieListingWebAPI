"""
	Document for testing the IMDB movie listing api
"""

#To add new genre:

	url: http://imdbapp.heroku.com/genres
	Method: POST
	json data: 
		{
			"genre":"genre name"
		}

#To list genres:

	url: http://imdbapp.heroku.com/genres
	Method: GET


#To add new movie:

	url:http://imdbapp.heroku.com/movies
	Method: POST
	http Autherization header with user: admin and password: admin
	json data:	
		{
	    "99popularity": 83.0,
	    "director": "Victor Fleming",
	    "genre": [
	      "Adventure",
	      "Family",
	      "Fantasy",
	      "Musical"
	    ],
	    "imdb_score": 8.3,
	    "name": "The Wizard of Oz"
	  }


#To edit movie:

	url:http://imdbapp.heroku.com/movies
	Method: PUT
	http Autherization header with user: admin and password: admin
	json data:	
		{
		 "id" = pkId,
	    "99popularity": 83.0,
	    "director": "Victor Fleming",
	    "genre": [
	      "Adventure",
	      "Family",
	      "Fantasy",
	      "Musical"
	    ],
	    "imdb_score": 8.3,
	    "name": "The Wizard of Oz"
	  }


#To delete movie:

	url:http://imdbapp.heroku.com/movies/id (where, id = record pk value)
	Method: DELETE
	http Autherization header with user: admin and password: admin

#To List/search movies:

	url:http://imdbapp.heroku.com/movies/searchParameter (where,searchParameter = search paramter value, with no value it will list all the records)
	Method: GET
	http Autherization header with user: admin and password: admin

