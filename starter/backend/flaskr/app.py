import os
from flask import Flask, request, abort, jsonify, json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
CATEGORIES_PER_PAGE = 10


def paginate_questions(request, selection):

    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start: end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE, OPTIONS')
        return response

    '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''

    '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''

    @app.route('/categories')
    def retrieve_categories():
        # Create a new list
        # Map the elements from Category.format with the values provided by Category.query.all
        # Return the jsonify

        categories = list(map(Category.format, Category.query.all()))

        result = {
            'success': True,
            'categories': categories
        }

        return jsonify(result)

    '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

    @app.route('/questions')
    def retrieve_questions():

        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)
        categories = list(map(Category.format, Category.query.all()))

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(Question.query.all()),
            'current_category': None,
            'categories': categories
        })

    '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

    @app.route("/questions/<int:question_id>", methods=['DELETE'])
    def delete_question(question_id):
        question_query = Question.query.get(question_id)

        if question_query:
            Question.delete(question_query)
            return jsonify({
                'success': True
            })
        else:
            abort(404)
    '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

    @app.route('/questions', methods=["POST"])
    def add_question():
        if request.data:

            body = request.get_json()

            new_question = body.get('question', None)
            new_answer = body.get('answer', None)
            new_category = body.get('category', None)
            new_difficulty = body.get('difficulty', None)

            if new_question is not None and new_answer is not None and new_category is not None and new_difficulty is not None:
                new_question = Question(
                    question=new_question, answer=new_answer, category=new_category, difficulty=new_difficulty)
                Question.insert(new_question)

                return jsonify({
                    'success': True,
                    'questions': len(Question.query.all())
                })

            abort(400)
        abort(422)

    '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

    @app.route('/searchQuestions', methods=['POST'])
    def search_questions():
        if request.data:
            body = request.get_json()
            new_search_term = body.get('searchTerm', None)
            if new_search_term is not None:
                selection = Question.query.filter(
                    Question.question.ilike('%' + new_search_term + '%'))
                current_search_questions = paginate_questions(
                    request, selection)
                questions = list(map(Question.format, selection))

                if len(questions) > 0:
                    return jsonify({
                        'success': True,
                        'questions': current_search_questions,
                        'total_questions': len(Question.query.all()),
                        'current_category': None,
                    })
            abort(404)
        abort(422)

    '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''

    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_questions_with_category(category_id):
        # Request data is required when we post something
        category_query = Category.query.get(category_id)

        question_query = Question.query.filter_by(
            category=str(category_id)).all()
        current_questions = paginate_questions(request, question_query)

        questions = list(map(Question.format, question_query))

        if len(questions) > 0:
            return jsonify({
                'success': True,
                'questions': current_questions,
                'category': Category.format(category_query),
                'total_questions': len(Question.query.all()),


            })
        else:
            return jsonify({
                "success": False,
                "message": "Category does not exist"
            })
        abort(422)
    '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

    @app.route("/quizzes", methods=['POST'])
    def get_question_for_quiz():
        if request.data:
            search_data = json.loads(request.data.decode('utf-8'))
            if (('quiz_category' in search_data
                 and 'id' in search_data['quiz_category'])
                    and 'previous_questions' in search_data):
                questions_query = Question.query.filter_by(
                    category=search_data['quiz_category']['id']
                ).filter(
                    Question.id.notin_(search_data["previous_questions"])
                ).all()
                length_of_available_question = len(questions_query)
                if length_of_available_question > 0:
                    result = {
                        "success": True,
                        "question": Question.format(
                            questions_query[random.randrange(
                                0,
                                length_of_available_question
                            )]
                        )
                    }
                else:
                    result = {
                        "success": True,
                        "question": None
                    }
                return jsonify(result)
            abort(404)
        abort(422)
    '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''

    @app.errorhandler(400)
    def not_found(error):
        error_data = {
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }
        return jsonify(error_data)

    @app.errorhandler(404)
    def not_found(error):
        error_data = {
            "success": False,
            "error": 404,
            "message": "Resource not found"
        }
        return jsonify(error_data)

    @app.errorhandler(422)
    def unprocessable(error):
        error_data = {
            "success": False,
            "error": 422,
            "message": "Unprocessable"
        }
        return jsonify(error_data)

    @app.errorhandler(405)
    def method_not_allowed(error):
        error_data = {
            "success": False,
            "error": 405,
            "message": "The method is not allowed for the requested URL"
        }
        return jsonify(error_data)

    return app
