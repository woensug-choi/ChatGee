# -*- coding: utf-8 -*-

# ############################################### #
CONFIG_FILE_PATH = "settings.yaml"
# ############################################### #

from flask import Flask, request, jsonify, render_template, url_for
from base.chatgee import ChatGeeOBJ
from base.utility import read_yaml, send_query_local
import time

# ---------------     Flask     ----------------- #
app = Flask(__name__, static_url_path='/static')

# -------------- Initiate Modules,--------------- #
# Read Config File
ChatGee_Config = read_yaml(CONFIG_FILE_PATH)
# Initiate ChatGee Library
ChatGee = ChatGeeOBJ(ChatGee_Config)

# -----------------  Flask Routes  --------------- #
# Base Route
@app.route("/")
def index():
    return {'message': 'Welcome to the Kakatotalk ChatGPT AI Chatbot API' \
                        '\n https://github.com/woensug-choi/ChatGee'}

# Chat Route
@app.route("/prompt", methods=['POST'])
def prompt():
    return jsonify(ChatGee.prompt_received(request.get_json()))

# Usage Route
@app.route('/usage/<userid>')
def usage_count(userid):
    usage_count = ChatGee.get_usage_count(userid)
    chart_data = {
        'labels': ['Usage Count'],
        'datasets': [{
            'label': 'Usage Count',
            'backgroundColor': 'rgba(255, 20, 147, 0.2)', 
            'borderColor': 'rgba(255, 99, 132, 1)',
            'borderWidth': 1,
            'data': [usage_count],
        }]
    }
    return render_template('usage.html', userid=userid, usage_count=usage_count, chart_data=chart_data)

# Send Dummy Route
@app.route("/local_test", methods=["GET", "POST"])
def local_query():
    system_prompt = ChatGee_Config['SETTINGS']['SYSTEM_PROMPT']
    
    # If the form has been submitted
    if request.method == "POST":
        query = request.form["question"]
        if query:
            start_time = time.time()
            response = send_query_local(query, ChatGee_Config)
            answer = ""
            if response != None:
                answer = response.replace('\n', '<br>')
            return render_template("local_test.html",
                    question=query, answer=answer,
                    time_elapsed=round((time.time() - start_time), 2),
                    system_prompt=system_prompt)
    else:
        # Render the local_test HTML template without any question or answer
        return render_template("local_test.html")

if __name__ == "__main__":
    app.run(host=ChatGee_Config['SERVER']['HOST_NAME'],
            port=ChatGee_Config['SERVER']['PORT_NUMBER'],
            debug=ChatGee_Config['SERVER']['DEBUG_FLASK'],
            extra_files=[CONFIG_FILE_PATH])