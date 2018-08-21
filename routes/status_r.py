from app import get_app
from flask_restplus import Resource
from namespaces import ns_status

app = get_app()


@ns_status.route("")
class Status(Resource):

    @app.api.doc(
        responses={
            200: 'Success',
            404: 'Not found'
        },
        description='Get status'
    )
    def get(self):
        return "Healthy", 200
