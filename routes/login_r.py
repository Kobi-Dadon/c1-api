from app import get_app
from flask_restplus import Resource
from controller.login_c import LoginController
from namespaces import login
from schemas.users_s import users_schema_in, users_schema_out

app = get_app()
db = app.db.session

@login.route("")
class Login(Resource):

    @app.api.doc(
        responses={
            200: 'Success',
            404: 'Not found'
        },
        description='Login new user'
    )
    @app.api.expect(users_schema_in)
    @app.api.marshal_with(users_schema_out)
    def post(self):
        # create a new user or return details of existing user if trying to re login
        login = LoginController()
        response = login.build_response()
        return response, 200
