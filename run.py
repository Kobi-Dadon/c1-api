import settings
from routes import status_r, login_r, questions_r, submit_r
from app import get_app


if __name__ == "__main__":
    app = get_app()
    app.run(debug=True, host='0.0.0.0', port=settings.PORT)
