from flask import Flask, request
from flask import render_template
from flaskext.mysql import MySQL
from flask import request
import time


#from peewee import *

#from flask import request

#con = db.connect(host='localhost', user='trevor', passwd='pw', db='aqi');

app = Flask(__name__)
mysql = MySQL(app)


app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mamprabha'
app.config['MYSQL_DATABASE_DB'] = 'python_apc'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

@app.route('/testui')
def mynewfunc():
    return render_template('testui.html')

@app.route('/test121',methods=['POST'])
def datinsert():
    valuein = request.form['2']
    return 'output : {}'.format(valuein)


@app.route('/sk')
def users():
    conn = mysql.connect()
    cur = cursor = conn.cursor()
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



@app.route('/step2/', methods=['POST','GET'])
def second():
    data = gh = request.args
    orde = int(time.time()) % 100000


    conn98 = mysql.connect()
    cur_insert_init = cursor = conn98.cursor()
    # cur_insert = cursor = mysql.get_db().cursor()

    cur_insert_init.execute("""INSERT into oreder_detail (order_no) VALUES (%s)""", (orde))
    conn98.commit()


    con1 = mysql.connect()

    for key in data:
        if(data[key]!=""):

            a=key
            b=data[key]
            #print(type(orde))
            #print(a,b,orde)
            conn = mysql.connect()
            cur_insert = cursor = conn.cursor()
           #cur_insert = cursor = mysql.get_db().cursor()

            cur_insert.execute("""INSERT into orders (order_no, p_id, p_quantity) VALUES (%s,%s,%s)""",(orde,a,b))
            conn.commit()
            # second part started sql

            con1 = mysql.connect()
            cur_insert_two = cursor = con1.cursor()

            cur_insert_two.execute("""SELECT * FROM orders JOIN products
                           WHERE  orders.p_id  = products.p_id AND orders.order_no = %s""",(orde))
            data_two = cur_insert_two.fetchall()
            calculations(data_two,orde)
            con1.commit()

            con92 = mysql.connect()
            cur_insert_view = cursor = con92.cursor()

            cur_insert_view.execute("""SELECT * FROM orders JOIN products
                                       WHERE  orders.p_id  = products.p_id AND orders.order_no = %s""", (orde))
            data_view = cur_insert_view.fetchall()
            con92.commit()

            con93 = mysql.connect()
            cur_insert_view_sum = cursor = con93.cursor()

            cur_insert_view_sum.execute("""SELECT * FROM oreder_detail WHERE order_no = %s""",(orde))
            data_view_sum = cur_insert_view_sum.fetchall()
            con93.commit()
    context = {"date_view": data_view,"date_view_sum" : data_view_sum}
    return render_template("summary.html", **context)

    #return ' dsjkjkj {}'.format(data_view)


def calculations(dataone,orderno):
    data_two = dataone
    ordern = orderno
    for loopforprice in data_two:
        conn2 = mysql.connect()
        cur_insert_three = cursor = conn2.cursor()
        ppu = int(loopforprice[2]) * int(loopforprice[7])
        item_id = int(loopforprice[3])
        #print(ppu)

        cur_insert_three.execute("""UPDATE orders SET price = %s WHERE item_no = %s""", ((ppu,loopforprice[3])))
        conn2.commit()

    conn34 = mysql.connect()
    cur_insert_four = cursor = conn34.cursor()
    cur_insert_four.execute("""SELECT SUM(price) from orders WHERE order_no = %s""",(ordern))
    sum = cur_insert_four.fetchall()
    conn34.commit()

    conn35 = mysql.connect()
    cur_insert_five = cursor = conn35.cursor()
    for sumloop in sum:
        cur_insert_five.execute("""UPDATE oreder_detail SET total = %s WHERE order_no = %s""",(sumloop[0],ordern))
    conn35.commit()

@app.route('/step3/', methods=['POST','GET'])
def third():
    data = gh = request.form
    for key in data:
        if (data[key] != ""):
            a = key
            b = data[key]
            print(a,b)
        conn35 = mysql.connect()
        cur_insert_five = cursor = conn35.cursor()

        cur_insert_five.execute("""UPDATE oreder_detail SET status = %s WHERE order_no = %s""", (1, b))
        conn35.commit()
    print(b)
    context = {"ordrno": b}
    return render_template("ready.html", **context)

@app.route('/orders_complete/<order_no>')
def order_complete(order_no = '1'):
    con92 = mysql.connect()
    cur_insert_view = cursor = con92.cursor()

    cur_insert_view.execute("""SELECT * FROM orders JOIN products
                                           WHERE  orders.p_id  = products.p_id AND orders.order_no = %s""", (order_no))
    data_view = cur_insert_view.fetchall()
    con92.commit()
   # print(data_view)
    context = {"date_view": data_view,"order":order_no}
    return render_template("order_complete.html", **context)

@app.route('/complete_update/', methods=['POST','GET'])
def complete_update():
    data = gh = request.form
    for key in data:
        if (data[key] != ""):
            a = key
            b = data[key]
            con92 = mysql.connect()
            cur_insert_view = cursor = con92.cursor()

            cur_insert_view.execute("""UPDATE oreder_detail SET sucess = %s WHERE order_no = %s""", (1, b))
            data_view = cur_insert_view.fetchall()
            con92.commit()
        #print(data_view)
    return 'Information Updated'

@app.route('/manager_view')
def manager_view():
    con92 = mysql.connect()
    cur_insert_view = cursor = con92.cursor()

    cur_insert_view.execute("""SELECT * FROM oreder_detail WHERE  status  = 1 AND sucess = 0""")
    data_view = cur_insert_view.fetchall()
    con92.commit()
    # print(data_view)
    context = {"date_view": data_view}
    return render_template("manager_view.html", **context)

@app.route('/final_ready')
def final_ready():
    con92 = mysql.connect()
    cur_insert_view = cursor = con92.cursor()

    cur_insert_view.execute("""SELECT order_no FROM oreder_detail WHERE  status  = 1 AND sucess = 1""")
    data_view = cur_insert_view.fetchall()
    con92.commit()
    # print(data_view)
    context = {"date_view": data_view}
    return render_template("order_ready_public.html", **context)


if __name__ == '__main__':
    app.run()
