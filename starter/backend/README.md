# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

## API Endpoints Explanation
## GET /categories

This endpoint fetches a dictionary of categories which has a key value pairing of id and type
Request Arguments: None
Example Response

{
categories: [
{
id: 1,
type: "Geography"
},
{
id: 2,
type: "Knowledge"
},
{
id: 3,
type: "Technical"
}
],
success: true
}

## GET/questions?page=<int:page_number>

This endpoint fetches a dictionary of categories with the key value pair of id and type.
In addition, it references the current_category 
It also displays the questions dictionary that stores key value pairs for each question. It stores the answer, category, difficulty, id and the question in string format.

The results are returned via pagination and it only displays 10 questions per page specified in the request parameters. It also returns the total number of questions that are stored in the database

Request Arguments:Page Number
Example Response 

{
categories: [
{
id: 1,
type: "Geography"
},
{
id: 2,
type: "Knowledge"
},
{
id: 3,
type: "Technical"
}
],
current_category: null,
questions: [
{
answer: "Ottawa",
category: "1",
difficulty: 5,
id: 9,
question: "What is the capital of Canada?"
},
{
answer: "Washington",
category: "2",
difficulty: 5,
id: 10,
question: "What is the capital of United States of America?"
},
{
answer: "Steve Wozniak",
category: "6",
difficulty: null,
id: 11,
question: "Who was the technical cofounder of Apple Inc"
}
],
success: true,
total_questions: 11
}

## DELETE /questions/<int:question_id>

This endpoint allows the user to delete a question and remove it from the database
Request Parameter = Question_id

Example response: 
{
    'success': True/False
}


## POST /questions

This endpoint allows the user to create a new question and store it in the database
Request parameter = question, answer, difficulty, and category

Example Request JSONContent to be Posted {
    "question":"What is the capital of China?",
    "answer":"Beijing",
    "difficulty":"5",
    "category":1
}

Example Response {
    "success": True
}

## POST /searchQuestions

This endpoint allows the user to search through the database with a search query string and get results based on the contents of the query string

Request Arguments: Page_number
Request Body: search_data

Example Search Response {
    "searchTerm":"Beijing"
}

## GET /categories/<int:category_id>/questions

This endpoint allows the user to browse through the questions of the provided category with its specified Id.

Example Response {
category: {
id: 1,
type: "Geography"
},
questions: [
{
answer: "Ottawa",
category: "1",
difficulty: 5,
id: 9,
question: "What is the capital of Canada?"
}
],
success: true,
total_questions: 11
}

## POST /quizzes

This allows the user to get questions to play the trivia quiz.
Request body: quiz_category and previous_questions
Response: Random questions within the given category

Example {
    "previous_questions":[],
    "quiz_category":{"type":"Technical","id":"3"}
}

Example Response

{
    "question": {
    "answer":"Washington",
    "category":1,
    "difficulty":4,
    "id":1,
    "question":"What is the capital of USA?"
    },
    "success":true
}

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
