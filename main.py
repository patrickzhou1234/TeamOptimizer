from flask import Flask, render_template, request

namelist = {
  
}

idlist = {

}

nameidlist = {

}

synergylist = []

i=0

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def renderresult():
  if 'synergyMembers' in request.form and 'synergyScore' in request.form:
    synergyElement = []
    synergyMembers = request.form['synergyMembers']
    synergyScore = request.form['synergyScore']
    synergyMembers = synergyMembers.split(":")
    synergyElement.append(synergyMembers)
    synergyElement.append(synergyScore)
    synergylist.append(synergyElement)
  elif 'name' in request.form and 'score' in request.form:
    global i
    name = request.form['name']
    score = request.form['score']
    namelist[name]=score
    idlist[i]=score
    nameidlist[name]=i
    i+=1
  return render_template('index.html', namelist=namelist, idlist=idlist, nameidlist=nameidlist, synergylist=synergylist)

app.run(host='0.0.0.0', port=80)