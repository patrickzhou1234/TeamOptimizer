from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def renderresult():
  name = request.form['name']
  number = request.form['score']
  result=name+number
  return render_template('index.html', result=result)

app.run(host='0.0.0.0', port=80)