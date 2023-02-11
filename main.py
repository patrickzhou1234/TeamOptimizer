from flask import Flask, render_template, request

namelist = {
  
}

idlist = {

}

nameidlist = {

}

i=0

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def renderresult():
  global i
  name = request.form['name']
  score = request.form['score']
  namelist[name]=score
  idlist[i]=score
  nameidlist[name]=i
  i+=1
  return render_template('index.html', result=namelist, idlist=idlist)

app.run(host='0.0.0.0', port=80)