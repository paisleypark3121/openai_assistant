import os
import datetime

from dotenv import load_dotenv
from utilities.MongoDB import *

from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash, send_file
from datetime import datetime, timedelta
from flask_session import Session

from routes.auth_routes import auth_blueprint
from routes.credentials_routes import credentials_blueprint

load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path='/')

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_NAME'] = 'assistant_cookie'
app.config['SESSION_COOKIE_HTTPONLY'] = True
#app.config['SESSION_USE_SIGNER'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=15)

Session(app)

app.register_blueprint(auth_blueprint)
app.register_blueprint(credentials_blueprint)

default_model='gpt-3.5-turbo-0613'
#default_model='gpt-4-0613'
#defaul_model='gpt-4-turbo-preview'

from utilities.credentials import *
@app.route("/")
def home():

    # response=insert_user("test_user","test_password")
    # print(response)

    # response=check_credentials("test_user","test_password")
    # print(response)

    # username = 'test_user'
    # additional_fields = {
    #     "thread_id": "thread_1234"
    # }
    # response=update_user(username, additional_fields)
    # print(response)

    # username = 'test_user'
    # response=find_user_by_username(username)
    # print(response)

    # username = 'test_user'
    # response=delete_user(username)
    # print(response)

    #return "HELLO WORLD"

    if 'user_id' in session:
        
        model = session.get("model")
        if model is None:
            model = default_model
            session["model"] = model

        language = session.get("language")
        if language is None:
            language = 'english'
            session["language"] = language

        return render_template(
                "home.html", 
                model=model, 
                language=language)

    else:
        return redirect(url_for("auth.login"))

if __name__ == "__main__":
    app.run(debug=True)
    #app.run("0.0.0.0")