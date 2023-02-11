import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def renderresult():
  number = request.form['text']
  if (number=="1"):
    result="true"
  else:
    result="false"
  print(number)

  return render_template('index.html', result=result)

app.run(host='0.0.0.0', port=80)