from flask import Flask,render_template,request,redirect,url_for
import pymysql as sql


app= Flask(__name__)

def db_connect():
    conn= sql.connect(host='localhost',port=3306,user='root',password='the saini',database='portfolio')
    cur = conn.cursor()
    return conn,cur






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio/')
def portfolio():
    return render_template('portfolio.html')

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/aftersubmit/' ,methods=['GET','POST'])
def after_submit():
    if request.method== 'GET':
        return redirect(url_for('contact'))
    else:
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        db,cursor=db_connect()
        cmd=f"select* from contact where email='{email}'"
        data = cursor.execute(cmd)
        if data:
            msg= 'email already exixts..'
            return render_template('contact.html',data=msg)
        else:
            cmd=f"insert into contact values('{name}','{email}',{phone},'{message}')"
            cursor.execute(cmd)
            db.commit()
            db.close()
            msg='details are sent successfully'
            return render_template('contact.html',data=msg)
     
app.run(debug=True)