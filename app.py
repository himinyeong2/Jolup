
from flask import Flask, request, render_template,session,redirect,url_for,flash
import pandas as pd

app = Flask(__name__)
app.secret_key='id'

# 기본 페이지 접속
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit_excel",methods=["POST"])
def submit_excel():
    data=request.files['file']
    xlsx = pd.read_excel(data)
    junpil=xlsx[(xlsx['이수구분']=="전필") & (xlsx['등급']!="F")&(xlsx['등급']!="NP")].loc[:,['학점']]
    junsun=xlsx[(xlsx['이수구분']=="전선") & (xlsx['등급']!="F")&(xlsx['등급']!="NP")].loc[:,['학점']]
    gigyo=xlsx[(xlsx['이수구분']=="기교") & (xlsx['등급']!="F")&(xlsx['등급']!="NP")].loc[:,['학점']]
    gyopil=xlsx[(xlsx['이수구분']=="교필") & (xlsx['등급']!="F")&(xlsx['등급']!="NP")].loc[:,['학점']]
    gyosun=xlsx[(xlsx['이수구분']=="교선1") |(xlsx['이수구분']=="교선2") & (xlsx['등급']!="F")&(xlsx['등급']!="NP")].loc[:,['학점']]
    
    dic1={'junpil': 37.0 , 'junsun': 35.0 ,'gigyo': 12.0,'gyopil':15.0,'gyosun':15.0}
    dic2={'junpil':float(junpil.sum()),'junsun':float(junsun.sum()),'gigyo':float(gigyo.sum()),'gyopil':float(gyopil.sum()),'gyosun':float(gyosun.sum())}
    
    return render_template("result.html", jolup=dic1, my=dic2)

if __name__ =='__main__':
    app.run(host='0.0.0.0')
