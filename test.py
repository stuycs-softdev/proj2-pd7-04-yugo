from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
  return render_template("compile.html")




if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=5000)


"""
http://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&sensor=false
"""
