from flask import *
from functions import *
from collections import OrderedDict

app=Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')  
  
@app.route('/addShop', methods=['GET','POST'])
def goto():
    if(request.method=='GET'):
        shops=db.child("shops").get().val()
        return render_template('addShop.html',t=shops)

    else:    
        to = enterShopName(request)
        return render_template('addShop.html', t=to)

@app.route('/customerPage', methods=['GET','POST'])
def goto1():
    if(request.method=='GET'):
        return render_template('customerPage.html')
    else:
        shops=locationwise(request)
        print(shops)
        return render_template('customerPage.html',t=shops)        

if __name__ == "__main__":
    app.run(debug=True)
