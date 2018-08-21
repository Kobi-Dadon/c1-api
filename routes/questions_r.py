from app import get_app
from flask_restplus import Resource
from flask import session
from models.sessions_m import Sessions
from models.submitted_m import Submitted
from namespaces import ns_question
from models.questions_m import Questions
from schemas.questions_s import questions_schema_out
from utils.decorators import check_session

app = get_app()
db = app.db.session


@ns_question.route("")
class Question(Resource):

    @app.api.doc(
        responses={
            200: 'Success',
            404: 'Not found',
            401: 'Not authorized',
            408: 'Time limitation exceeded'
        },
        description='Get question'
    )
    @check_session
    @app.api.marshal_with(questions_schema_out)
    def get(self):
        # get the session object
        session_obj = db.query(Sessions).filter(Sessions.unique_key == session.get('user')).first()

        # get all submitted answers
        submit_obj = [x.question_id for x in db.query(Submitted).filter(Submitted.sessions_id == session_obj.id).all()]

        # get a question that was not already answered
        questions = db.query(Questions).filter(~Questions.id.in_(submit_obj)).first()
        return questions, 200
