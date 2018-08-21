from datetime import datetime
from functools import wraps
from flask import session
from flask_restplus import abort
from app import get_app
from models.sessions_m import Sessions

app = get_app()
db = app.db.session

def check_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # check that session exist
        if session.get('user'):
            session_obj = db.query(Sessions).filter(Sessions.unique_key == session.get('user')).first()
            #check that time didn't pass
            if (60-((datetime.now() - session_obj.start_time).seconds//60)%60) < 0:
                abort(408, "The 1 hour limitation has passed.")
            # check that user is not yet done
            elif session_obj.is_done == True:
                abort(401, "You have submitted all questions, good luck!")
            else:
                return func(*args, **kwargs)
        else:
            abort(401, "You need to be logged in to perform this action (/login)")
    return wrapper
