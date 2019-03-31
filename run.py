from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from app import app
from flask import Flask
from hardware import hardware

application = Flask(__name__)

application.wsgi_app = DispatcherMiddleware(NotFound(), {
    "/app": app,
    '/hardware': hardware,
})

if __name__ == '__main__':
    application.run()
