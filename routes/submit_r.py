from app import get_app
from flask_restplus import Resource, abort
from flask import session
from models.sessions_m import Sessions
from models.submitted_m import Submitted
from namespaces import ns_submit
from schemas.submit_s import submit_schema_in
from settings import Q_NUM
from utils.decorators import check_session

app = get_app()
db = app.db.session

@ns_submit.route("")
class Submit(Resource):

    @app.api.doc(
        responses={
            201: 'Success',
            404: 'Not found',
            409: 'Question already submitted',
            401: 'Not authorized',
            408: 'Time limitation exceeded'
        },
        description='Submit answer'
    )
    @check_session
    @app.api.expect(submit_schema_in)
    def post(self):
        payload = app.api.payload
        # check that we don't submit the same question twice
        if db.query(Submitted, Sessions)\
                .filter(Sessions.unique_key == session.get('user')) \
                .filter(Submitted.sessions_id == Sessions.id) \
                .filter(Submitted.question_id == payload.get('question_id')) \
                .first():
            abort(409, 'Question was already submitted.')

        # save the answer for this session
        payload['sessions_id'] = db.query(Sessions).filter(Sessions.unique_key == session.get('user')).first().id
        submit_obj = Submitted(**payload)
        db.add(submit_obj)
        db.flush()

        # if it's the last question, raise the is_done flag for this session.
        if db.query(Submitted).filter(Submitted.sessions_id == submit_obj.sessions_id).count() >= Q_NUM:
            db.query(Sessions).filter(Sessions.id == submit_obj.sessions_id).update({"is_done": True})
        db.commit()
        return 201
