from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!... Bonjour à tous"

if __name__ == "__main__":
    application.run()
