import uuid
from datetime import datetime
from flask import session, request
from app import get_app
from models.sessions_m import Sessions
from models.users_m import Users

app = get_app()
db = app.db.session


class LoginController(object):

    def __init__(self):
        # initial response format
        self.response = {
            'in_process': False,
            'user_session': None,
            'user_id': None,
            'time_left': None
        }

    def build_response(self):
        session_obj = db.query(Sessions).filter(Sessions.unique_key == session.get('user')).first()
        if session_obj:
            self.get_existing(session_obj)
        else:
            self.new_user()
        return self.response

    def get_existing(self, session_obj):
        # build existing user response
        self.response['in_process'] = True
        self.response['user_session'] = str(session_obj.unique_key)
        self.response['user_id'] = session_obj.user_id
        self.response['time_left'] = 60-((datetime.now() - session_obj.start_time).seconds//60)%60

    def new_user(self):
        # create new user
        payload = app.api.payload
        ip = request.remote_addr
        user = Users(**payload)
        db.add(user)
        db.flush()

        # create new session
        session_details = {
            "ip": ip,
            "unique_key": uuid.uuid4(),
            "user_id": user.id
        }

        session_obj = Sessions(**session_details)
        db.add(session_obj)
        db.flush()
        db.commit()

        # create user local session
        session['user'] = str(session_obj.unique_key)

        # build new user response
        self.response['user_session'] = str(session_obj.unique_key)
        self.response['user_id'] = session_obj.user_id
        self.response['time_left'] = 60-((datetime.now() - session_obj.start_time).seconds//60)%60