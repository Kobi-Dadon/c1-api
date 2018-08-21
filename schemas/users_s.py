from flask_restplus import fields
from app import get_app
app = get_app()


users_schema_in = app.api.model('New User', {
    'first_name': fields.String(required=True, description='First Name'),
    'last_name': fields.String(required=True, description='Last Name'),
    'email': fields.String(required=True, description='Email')
})

users_schema_out = app.api.model('User response', {
    'in_process': fields.Boolean(description='if user in process, return his session'),
    'user_session': fields.String(description='users session'),
    'user_id': fields.String(description='users session'),
    'time_left': fields.String(description='check if session is active')
})