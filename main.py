from flask import Flask, render_template, request
import TeamOptimizer

namelist = {
  
}

idlist = {

}

nameidlist = {

}

synergyList = []

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
    synergyScore = int(request.form['synergyScore'])
    synergyMembers = synergyMembers.split(":")
    synergyElement.append(synergyMembers)
    synergyElement.append(synergyScore)
    synergyList.append(synergyElement)
    for n in range(0, len(synergyList)):
      for k in range(0, len(synergyList[n][0])):
        if (synergyList[n][0][k] in nameidlist.keys()):
          synergyList[n][0][k] = nameidlist[synergyList[n][0][k]]

  elif 'name' in request.form and 'score' in request.form:
    global i
    name = request.form['name']
    score = int(request.form['score'])
    namelist[name]=score
    idlist[i]=score
    nameidlist[name]=i
    i+=1
    for n in range(0, len(synergyList)):
      for k in range(0, len(synergyList[n][0])):
        if (synergyList[n][0][k] in nameidlist.keys()):
          synergyList[n][0][k] = nameidlist[synergyList[n][0][k]]
  elif 'numberTeams' in request.form:
    numberTeams = request.form['numberTeams']
    finalResult = TeamOptimizer.simulate(idlist, int(numberTeams), synergyList)
    return render_template('index.html', namelist=namelist, idlist=idlist, nameidlist=nameidlist, synergyList=synergyList, finalResult=finalResult)
  else:
    namelist.clear()
    idlist.clear()
    nameidlist.clear()
    synergyList.clear()
  
  return render_template('index.html', namelist=namelist, idlist=idlist, nameidlist=nameidlist, synergyList=synergyList)

app.run(host='0.0.0.0', port=80)