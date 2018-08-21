from flask_restplus import fields
from app import get_app
app = get_app()

answers_schema_out = app.api.model('Question Data', {
    'id': fields.Integer(description='answer ID'),
    'text': fields.String(description='answer body')
})

questions_schema_out = app.api.model('Question Data', {
    'id': fields.Integer(description='question ID'),
    'difficulty': fields.Integer(description='question difficulty'),
    'text': fields.String(description='question body'),
    'answers': fields.List(fields.Nested(answers_schema_out), required=True, description='Data Files')
})

questions_schema_in = app.api.model('Submit Answer', {
    'question_id': fields.Integer(description='question ID'),
    'answer_id': fields.Integer(description='answer ID')
})