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
},
{
answer: "Steve Wozniak",
category: "6",
difficulty: null,
id: 21,
question: "Who was the technical cofounder of Apple Inc"
},
{
answer: "Steve Wozniak",
category: "6",
difficulty: null,
id: 22,
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

<<<<<<< HEAD

=======
```
# API Endpoints Documentation

API Endpoints Explanation
GET /categories
Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category.
Request Arguments: None
Returns: List of available categories.
Example Response {"categories":[{"id":1,"type":"Science"},{"id":2,"type":"Art"},{"id":3,"type":"Geography"},{"id":4,"type":"History"},{"id":5,"type":"Entertainment"},{"id":6,"type":"Sports"}],"success":true}

GET /questions?page=<page_number>
Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category.
Fetches a dictionary of questions in which the keys are the answer, category, difficulty, id and question.
Request Arguments: Page Number
Returns: List of questions, number of total questions, current category and categories.
Example Response {"categories":[{"id":1,"type":"Science"},{"id":2,"type":"Art"},{"id":3,"type":"Geography"},{"id":4,"type":"History"},{"id":5,"type":"Entertainment"},{"id":6,"type":"Sports"}],"current_category":null,"questions":[{"answer":"Muhammad Ali","category":4,"difficulty":1,"id":9,"question":"What boxer's original name is Cassius Clay?"},{"answer":"Apollo 13","category":5,"difficulty":4,"id":2,"question":"What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"},{"answer":"Tom Cruise","category":5,"difficulty":4,"id":4,"question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"},{"answer":"Edward Scissorhands","category":5,"difficulty":3,"id":6,"question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"},{"answer":"Brazil","category":6,"difficulty":3,"id":10,"question":"Which is the only team to play in every soccer World Cup tournament?"},{"answer":"Uruguay","category":6,"difficulty":4,"id":11,"question":"Which country won the first ever soccer World Cup in 1930?"},{"answer":"George Washington Carver","category":4,"difficulty":2,"id":12,"question":"Who invented Peanut Butter?"},{"answer":"Lake Victoria","category":3,"difficulty":2,"id":13,"question":"What is the largest lake in Africa?"},{"answer":"The Palace of Versailles","category":3,"difficulty":3,"id":14,"question":"In which royal palace would you find the Hall of Mirrors?"},{"answer":"Agra","category":3,"difficulty":2,"id":15,"question":"The Taj Mahal is located in which Indian city?"}],"success":true,"total_questions":26}

DELETE /questions/<question_id>
Delete question from the questions list.
Request Arguments: Question Id
Returns: true if successfully deleted.
Example Response {"success":true}

POST /questions
Create a new question
Request Body: question, answer, difficulty and category.
Returns: true if successfully created.
Example Request Payload {"question":"aa","answer":"a","difficulty":"3","category":1}

Example Response {"success":true}

POST /searchQuestions
Searches for the questions
Request Arguments: Page Number
Request Body: search_data
Returns: List of questions, number of total questions and current category.
Example Request Payload {"searchTerm":"a"}

Example Response {"current_category":null,"questions":[{"answer":"Apollo 13","category":5,"difficulty":4,"id":2,"question":"What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"},{"answer":"Tom Cruise","category":5,"difficulty":4,"id":4,"question":"What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"},{"answer":"Edward Scissorhands","category":5,"difficulty":3,"id":6,"question":"What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"},{"answer":"Brazil","category":6,"difficulty":3,"id":10,"question":"Which is the only team to play in every soccer World Cup tournament?"},{"answer":"George Washington Carver","category":4,"difficulty":2,"id":12,"question":"Who invented Peanut Butter?"},{"answer":"Lake Victoria","category":3,"difficulty":2,"id":13,"question":"What is the largest lake in Africa?"},{"answer":"The Palace of Versailles","category":3,"difficulty":3,"id":14,"question":"In which royal palace would you find the Hall of Mirrors?"},{"answer":"Agra","category":3,"difficulty":2,"id":15,"question":"The Taj Mahal is located in which Indian city?"},{"answer":"Escher","category":2,"difficulty":1,"id":16,"question":"Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"},{"answer":"Mona Lisa","category":2,"difficulty":3,"id":17,"question":"La Giaconda is better known as what?"}],"success":true,"total_questions":23}

GET /categories/<int:category_id>/questions
To get questions based on category
Request Arguments: Category Id and Page Number.
Returns: List of questions, number of total questions, current category and categories.
Example Response {"categories":[{"id":1,"type":"Science"},{"id":2,"type":"Art"},{"id":3,"type":"Geography"},{"id":4,"type":"History"},{"id":5,"type":"Entertainment"},{"id":6,"type":"Sports"}],"current_category":{"id":3,"type":"Geography"},"questions":[{"answer":"Lake Victoria","category":3,"difficulty":2,"id":13,"question":"What is the largest lake in Africa?"},{"answer":"The Palace of Versailles","category":3,"difficulty":3,"id":14,"question":"In which royal palace would you find the Hall of Mirrors?"},{"answer":"Agra","category":3,"difficulty":2,"id":15,"question":"The Taj Mahal is located in which Indian city?"}],"success":true,"total_questions":3}

POST /quizzes
To get questions to play the quiz.
Request Body: quiz_category and previous_questions.
Returns: Random questions within the given category.
Example Request Payload {"previous_questions":[],"quiz_category":{"type":"Science","id":1}}

Example Response {"question":{"answer":"Blood","category":1,"difficulty":4,"id":22,"question":"Hematology is a branch of medicine involving the study of what?"},"success":true}
>>>>>>> b4ad0a03fdf6373bd3029c3b75faeb73c32c2ca8

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
