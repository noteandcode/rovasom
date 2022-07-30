import re
from flask import Flask, request, render_template
import scoring

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action-page', methods=["POST"]) # Itt fontos, megadni hogy POST metódust tudjon fogadni
def results():
    # Ez a rész csinálja a kiértékelés
    # A kiértékelő függvényt a scoring.py-ból hozzuk be
    if request.method == "POST":
       # getting input with name = fname in HTML form
       url1 = request.form.get("source1")
       # getting input with name = lname in HTML form
       url2 = request.form.get("source2")
       url3 = request.form.get("source3")
       url4 = request.form.get("source4")
       url5 = request.form.get("source5")
       url6 = request.form.get("source6")
       url7 = request.form.get("source7")
       url8 = request.form.get("source8")
       url9 = request.form.get("source9")
       url10 = request.form.get("source10")
       score = url1 + url2 + url3 + url4 + url5 + url6 + url7 + url8 + url9 + url10
    
    return render_template("action-page.html", url1=url1, url2=url2, url3=url3, url4=url4, url5=url5, url6=url6, url7=url7, url8=url8, url9=url9, url10=url10)
        
@app.route('/robot-page')
def robotpage():
    return render_template('robot-page.html')




app.run(debug=True)