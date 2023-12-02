from flask import Flask,render_template,request
from weather import main as get_weather
app= Flask(__name__,template_folder='templates')
secret_key="hello"
@app.route('/',methods=("GET","POST")) #so that you don"t get 404 errror
def index():
    data = None#so that we have already have data for the website
    if request.method=="POST":

        city= request.form["cityName"]
        state= request.form["stateName"]
        country=request.form["countryName"]
        data=get_weather(city,state,country)

    return render_template("index.html",data=data)
if __name__=="__main__":# to check error
    app.run(debug=True)
 

#when you run flask on production then we have to put debug to false
#export FLASK_APP=main.py