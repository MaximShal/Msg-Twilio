
# Message Twilio

***

**Server for sending sms to phone and making order for box**

Python 3.11

For make docker container:
1. Clone the repository using `git clone`.
2. Create a new file called `.env` in the project root and fill it as shown in `.env.example`.
3. Run `docker-compose up --build` in project root.


To install and run the project follow the instruction below.

1. Clone the repository using `git clone`.
2. Set up a database in `PostgreSQL`.
3. Create a new file called `.env` in the project root and fill it as shown in `.env.example`.
4. Install Poetry `pip install poetry` with active venv.
5. Run `poetry install` in project root.
6. Run the migrations `python manage.py migrate`.
7. Run the project `python manage.py runserver`.
8. For Celery worker:
   * on Windows: 
       * use gevent task pool, run `poetry add gevent`;
       * run in root `celery -A mt worker -l info -P gevent`;
    * on Unix:
       * run in root `celery -A mt worker -l info`;
9. For Celery beat run `celery -A mt beat -l INFO` in project root;
