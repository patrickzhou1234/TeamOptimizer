from flask import Flask, render_template, request

list = {
  
}

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def renderresult():
  name = request.form['name']
  score = request.form['score']
  list[name]=score
  return render_template('index.html', result=list)

app.run(host='0.0.0.0', port=80)