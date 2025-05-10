Articles Database- Rest  API.

This API is developed with Python, Flask & SQLAlchemy.

--ORM MODEL
    Author - Article (Many-To-Many)
    Article - Tag (Many-To-Many)
    Article - Comments (One-to-Many)

--Installation
    This API was developed in python 3.10.10.
    Run the command 'pip install -r requirements.txt' to install the necessary libs.

--Start the API
    Run the command 'python app.py' to start the server. The api will 'listen'
    to http://localhost:5000/

--Database preloading
    Upon starting the database is filled with fake Authors, Tags, Articles and Comments
    on each article.

--Pagination
    Every result that has Article return in pages, with each page having up to 100 Articles.
    The page number is specified to the json body.
    !!!In every /getAll endpoint, the page is given in the URL for more comfortable validation.
    For example: http://127.0.0.1:5000/authors/getAll/page/1

--Filtering Articles
    Assuming we want to filter with all fields included. The SQL command would be something like this:
    SELECT article
    FROM Articles
    WHERE
    (
        author_id = 1 OR author_id = 2
    ) AND (
        EXTRACT(YEAR FROM publication_date) = 2023 OR EXTRACT(YEAR FROM publication_date) = 2021
    ) AND (
        tag_id = 1 OR tag_id = 2
    ) AND (
        abstract ILIKE '%Such%' OR abstract ILIKE '%Most%'
    ) AND (
        title ILIKE '%Most%' OR abstract ILIKE '%Most%' OR
        title ILIKE '%End%' OR abstract ILIKE '%End%'
    )
    would translate to this JSON body:
    {
        "authors":[
            {"id":1},
            {"id":2}
         ],
        "title": ["UFOs FOUND IN ALASKA", "GREECE IS EUROPE'S CHAMPION"],
        "year": ["2023", "2021"],
        "tags": [
            {"id":1},
            {"id":2}
        ],
        "abstract": ["Such", "Most"],
        "keywords":["Most", "End"],
        "page_number": 1
    }
    !!! For the Author and the Tag filters, only the id is needed. Also its not obligatory to have all the fields in the
        JSON body.

--Downloading a .csv file after filtering
    Open a CMD and copy paste the command below. The filtering works in the same way with the \filter endpoint. Afterward it just exports the Articles
    to a .csv file. Using browser on app like Postman would not trigger the file to download.
    curl -X POST http://localhost:5000/articles/downloadcsv -H "Content-Type: application/json" -d "{\"title\": [\"Exist\"]}" --output filtered_articles.csv

--Endpoints
    Every model entity has the basic CRUD(Create, Read, Update, Delete) operations. A user can only update & delete their
    own Articles & Comments.
    For example, http://localhost:5000/Tag/getAll/page/2,  http://localhost:5000/Author/delete
    Except the /getAll endpoints, every other endpoint needs JSON body for the required information.

    1)http://127.0.0.1:5000/articles/update
        "user" : "...",
		"abstract": "...",
		"authors": [
			{
				"id": 4,
				"name": "..."
			},
			{
				"id": 5,
				"name": "..."
			}
		],
		"comments": [
			{
				"article_id": 2,
				"author": "...",
				"content": "...",
				"id": 3
			}
		],
		"id": 2,
		"identifier": "...",
		"tags": [
			{
				"content": "...",
				"id": 1
			},
			{
				"content": "...",
				"id": 3
			}
		],
		"title": "..."

    2)http://127.0.0.1:5000/articles/delete
        {
            "article_id": 1,
            "user": "user's name"

        }
    3)http://127.0.0.1:5000/articles/create
        {
		"title": "...",
		"publication_date": "...",
		"authors" :["...", "..."]
	    }

    4)http://127.0.0.1:5000/comments/update
        {
		"article_id": 2,
		"user": "user'name",
		"content": "new content",
		"id": 3
	    }
	5) http://127.0.0.1:5000/comments/delete
	    {
            "user": "user's name",
		    "id": 3
	    }
    6) http://127.0.0.1:5000/comments/create
        {
            "content":"hi",
            "user": "Jordan fan",
            "article_id": "..."
        }
    7) http://127.0.0.1:5000/comments/getComments
        {
            "article_id": "1"
        }
    8)  http://127.0.0.1:5000/authors/create
        {
            "name": "..."
        }
    9) http://127.0.0.1:5000/authors/delete
        {
		"author_id": "..."
        }
    10) http://127.0.0.1:5000/authors/update
        {
        "name": "...",
        "id": "..."
        }
    11) http://127.0.0.1:5000/tags/create
        {
            "content": "..."
        }
    12) http://127.0.0.1:5000/tags/delete
        {
            "id": "..."
        }
    13) http://127.0.0.1:5000/tags/update
        {
            "id": "...",
            "content": "..."
        }








