from flask import Flask, request
from flask import render_template
from flaskext.mysql import MySQL


#from peewee import *

#from flask import request

#con = db.connect(host='localhost', user='trevor', passwd='pw', db='aqi');

app = Flask(__name__)
mysql = MySQL(app)

app.config['MYSQL_DATABASE_USER'] = 'satyamkapoor'
app.config['MYSQL_DATABASE_PASSWORD'] = 'MACS2016'
app.config['MYSQL_DATABASE_DB'] = 'satyamkapoor$students'
app.config['MYSQL_DATABASE_HOST'] = 'satyamkapoor.mysql.pythonanywhere-services.com'

@app.route('/testui')
def mynewfunc():
    return render_template('testui.html')

@app.route('/test121',methods=['POST'])
def datinsert():
    valuein = request.form['2']
    return 'output : {}'.format(valuein)


@app.route('/sk')
def users():
    cur = cursor = mysql.get_db().cursor()
    cur1 = cursor = mysql.get_db().cursor()
    cur.execute('SELECT * FROM table01')
    cur1.execute('SELECT name FROM table01')
    data = cur.fetchall()
    data1 = cur1.fetchall()
    #return render_template('list.html', data=data)
    #return str(data)
    context = {"rv": data, "rv1":data1}
    return render_template('list.html', **context)


@app.route('/') #decorator - a function which covers around another function to do something super amazing...
@app.route('/<name>')
def namaste(name = ' <br> try putting a forward slash (/) and writing something after the url : http://satyamkapoor.pythonanywhere.com/writehere '): #if you give a name here then that's the default value taken is nothing is given next to route
    #name = "ddhh"
    #name = request.args.get('name', name)
    return 'Hello Friends! {}'.format(name)

@app.route('/add/<int:num1>/<int:num2>')#int because the inputs are in a form of string
@app.route('/add/<float:num1>/<float:num2>')
def add(num1,num2):
        context = {'Num1': num1, 'Num2': num2}
       #return "{}".format(num1+num2) #return needs to be in a string
        return render_template("homepage.html", **context)
@app.route('/homepage/')
def homepage():
    cur_beer = cursor = mysql.get_db().cursor()
    cur_cocktail = cursor = mysql.get_db().cursor()
    cur_app = cursor = mysql.get_db().cursor()
    cur_beer.execute("""SELECT * FROM products
                   WHERE type = %s""",('beer'))
    cur_cocktail.execute("""SELECT * FROM products
                   WHERE type = %s""",('cocktail'))
    cur_app.execute("""SELECT * FROM products
                   WHERE type = %s""",('app'))
    data_beer = cur_beer.fetchall()
    data_cocktail = cur_cocktail.fetchall()
    data_app = cur_app.fetchall()
    #data1 = cur1.fetchall()
    context = {"beer": data_beer,"cocktail" : data_cocktail,"app" : data_app }
    return render_template("index.html", **context)

if __name__ == '__main__':
    app.run()
