from app import get_app

app = get_app()

ns_status = app.api.namespace('status', description='check API status')
ns_question = app.api.namespace('question', description='get question')
login = app.api.namespace('login', description='login new user')
ns_submit = app.api.namespace('submit', description='submit an answer')