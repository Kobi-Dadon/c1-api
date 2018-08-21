from flask_restplus import fields
from app import get_app
app = get_app()


submit_schema_in = app.api.model('Submit answer', {
    'question_id': fields.Integer(description='question ID'),
    'answer_id': fields.Integer(description='answer ID')
})