from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sqlite3
from datetime import datetime
from alchemy import User, Income, Expenses,  Session
from tabulator import tabulator

conn = sqlite3.connect('finance.db', check_same_thread=False)
cur = conn.cursor()

session = Session.return_session()


app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = 'super strong random key'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index2')
def index2():
    tabulator1 = tabulator.create_tabulator()
    template_folder = os.path.join(os.getcwd(),'web')
    template_folder = os.path.join(template_folder,'static')
    tabulator_html_path = os.path.join(template_folder, 'tabulator_app.html')
    tabulator1.save(filename=tabulator_html_path, embed=True)
      
    return render_template('index2.html', tabulator=tabulator)

@app.route('/index3', methods=['GET', 'POST'])
def Index3():
    cur.execute("SELECT FirstName, LastName  FROM users")
    user_names = [f"{row[0]} {row[1]}" for row in cur.fetchall()]
    #print (user_names)
    if request.method == 'POST':
        selected_user_name = request.form.get('user_name')
        
        if selected_user_name:
            cur.execute("""SELECT i.id, i.user_id, u.FirstName, u.LastName, i.income, i.description, i.source, i.date   
                            FROM income i 
                            JOIN users u ON u.id = i.user_id
                            WHERE u.FirstName || ' ' || u.LastName = ?""", (selected_user_name,))
        else:
            cur.execute("""SELECT i.id, i.user_id, u.FirstName, u.LastName, i.income, i.description, i.source, i.date   
                            FROM income i 
                            JOIN users u ON u.id = i.user_id""")

        income_data = cur.fetchall()

    else:
        cur.execute("""SELECT i.id, i.user_id, u.FirstName, u.LastName, i.income, i.description, i.source, i.date 
                        FROM income i 
                        JOIN users u ON u.id = i.user_id""")
        income_data = cur.fetchall()


    return render_template('index3.html', income=income_data, user_names=user_names)


@app.route('/index3/insert', methods=['POST'])
def insert_income():
    if request.method == "POST":
        user_id = request.form['user_id']
        income_amount = request.form['income']
        description = request.form['description']
        source = request.form['source']
        date = request.form['date']
        date = datetime.strptime(date, '%Y-%m-%d').date()
        
        user = session.query(User).filter_by(id=user_id).first()
        if user is None:
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            new_user = User(id=user_id, FirstName=first_name, LastName=last_name)
            session.add(new_user)
            session.commit()

        new_income = Income(user_id=user_id,
                            income=income_amount,
                            description=description,
                            source=source,
                            date=date)
        session.add(new_income)
        session.commit()
        
        flash("Data Inserted Successfully")
        return redirect(url_for('Index3')) 
    
@app.route('/index3/delete/<int:id_data>', methods=['GET'])
def delete_income(id_data):
    income_record = session.query(Income).filter_by(id=id_data).first()
        
    if income_record:
        session.delete(income_record)
        session.commit()
        flash("Record Has Been Deleted Successfully")
        cur.execute("""delete from users  
                       where id not in (select user_id from income )  and id not in (select user_id from expenses ) """)
        conn.commit()
    else:
        flash("Record not found")

    return redirect(url_for('Index3'))

@app.route('/index3/update', methods=['POST'])
def update_income():
    if request.method == 'POST':
        user_id = request.form['id']
        income = request.form['income']
        description = request.form['description']
        source = request.form['source']
        date = request.form['date']
        date = datetime.strptime(date, '%Y-%m-%d').date()

        income_record = session.query(Income).filter_by(id=user_id).first()

        if income_record:
            income_record.income = income
            income_record.description = description
            income_record.source = source
            income_record.date = date
            
            session.commit()
            flash("Data Updated Successfully")
        else:
            flash("Record not found")

        return redirect(url_for('Index3'))


@app.route('/index4', methods=['GET', 'POST'])
def index4():
    cur.execute("SELECT FirstName, LastName FROM users")
    user_names = [f"{row[0]} {row[1]}" for row in cur.fetchall()]

    if request.method == 'POST':
        selected_user_name = request.form.get('user_name')
        
        if selected_user_name:
            cur.execute("""SELECT i.id, i.user_id, u.FirstName, u.LastName, i.expenses, i.description, i.source, i.date   
                            FROM expenses i 
                            JOIN users u ON u.id = i.user_id
                            WHERE u.FirstName || ' ' || u.LastName = ?""", (selected_user_name,))
        else:
            cur.execute("""SELECT i.id, i.user_id, u.FirstName, u.LastName, i.expenses, i.description, i.source, i.date   
                            FROM expenses i 
                            JOIN users u ON u.id = i.user_id""")

        expenses_data = cur.fetchall()

    else:
        cur.execute("""SELECT i.id, i.user_id, u.FirstName, u.LastName, i.expenses, i.description, i.source, i.date 
                        FROM expenses i 
                        JOIN users u ON u.id = i.user_id""")
        expenses_data = cur.fetchall()


    return render_template('index4.html', expenses=expenses_data, user_names=user_names)

@app.route('/index4/insert', methods = ['POST'])
def insert_expenses():
    if request.method == "POST":
        user_id = request.form['user_id']
        expenses = request.form['expenses']
        description = request.form['description']
        source = request.form['source']
        date = request.form['date']
        date = datetime.strptime(date, '%Y-%m-%d').date()
        
        new_income = Expenses(user_id=user_id,
                            expenses=expenses,
                            description=description,
                            source=source,
                            date=date)
        session.add(new_income)

        session.commit()
        flash("Data Inserted Successfully")
        return redirect(url_for('index4'))   


@app.route('/index4/delete/<string:id_data>', methods = ['GET'])
def delete_expenses(id_data):
    expesnes_record = session.query(Expenses).filter_by(id=id_data).first()

    if expesnes_record:
        session.delete(expesnes_record)
        session.commit()
        flash("Record Has Been Deleted Successfully")
        cur.execute("""delete from users  
                       where id not in (select user_id from income )  and id not in (select user_id from expenses ) """)
        conn.commit()
    else:
        flash("Record not found")

    return redirect(url_for('index4'))

@app.route('/index4/update',methods=['POST'])
def update_expenses():

    if request.method == 'POST':
        user_id = request.form['id'] 
        expenses = request.form['expenses']
        description = request.form['description']
        source = request.form['source']
        date = request.form['date']
        date = datetime.strptime(date, '%Y-%m-%d').date()

        expenses_record = session.query(Expenses).filter_by(id=user_id).first()

        if expenses_record:
            expenses_record.expenses = expenses
            expenses_record.description = description
            expenses_record.source = source
            expenses_record.date = date
            
            session.commit()
            flash("Data Updated Successfully")
        else:
            flash("Record not found")  
        return redirect(url_for('index4')) 

if __name__ == '__main__':
    app.run(debug=True)