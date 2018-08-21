import os

VERSION = "1.00"
LIMITER = ["1000 per day"]
PORT = 5004
SESSION_TYPE = "filesystem"

# change for local DB credentials
POSTGRES_HOSTNAME = os.environ.get("POSTGRES_HOST", "localhost:5432")
POSTGRES_DBNAME = os.environ.get("POSTGRES_DB", 'c1')
POSTGRES_USER_NAME = os.environ.get("POSTGRES_USER", 'postgres')
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", '1qaz2wsx')
SQLALCHEMY_DATABASE_URI = "{schema}://{user}:{password}@{host}/{db}?sslmode=disable".format(schema="postgresql",
                                                                user=POSTGRES_USER_NAME,
                                                                password=POSTGRES_PASSWORD,
                                                                host=POSTGRES_HOSTNAME,
                                                                db=POSTGRES_DBNAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# i was debating too much where to put the questions limitation, ended up with this nasty thing.
Q_NUM = 5