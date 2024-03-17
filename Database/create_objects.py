import sqlite3
from users import Users
import finances_db as finances


conn = sqlite3.connect('finance.db')

cur = conn.cursor()

cur.execute('PRAGMA foreign_keys=on;')
conn.commit()

cur.execute('drop table if exists users')
conn.commit()
cur.execute('drop table if exists income')
conn.commit()
cur.execute('drop table if exists expenses')
conn.commit()
cur.execute('drop view if exists v_expenses_income')
conn.commit()

cur.execute("""create table if not exists users 
            (
                Id integer PRIMARY KEY AUTOINCREMENT,
                FirstName text, 
                LastName text 
            )""")

conn.commit()

cur.execute("""create table if not exists income 
            (
                Id integer PRIMARY KEY AUTOINCREMENT,
                user_id integer not null, 
                income float default 0,
                description text DEFAULT "income" NOT NULL,
                source text not null,
                date DATE DEFAULT (datetime('now','localtime')),
                CONSTRAINT [FK_user_id] 
                FOREIGN KEY(user_id) 
                REFERENCES [users] (Id) 
                ON DELETE CASCADE
            )""")

conn.commit()

cur.execute("""create table if not exists expenses 
            (
                Id integer PRIMARY KEY AUTOINCREMENT,
                user_id integer not null, 
                expenses float default 0 ,
                description text DEFAULT "expenses" NOT NULL,
                source text not null,
                date DATE DEFAULT (datetime('now','localtime')),
                CONSTRAINT [FK_user_id] 
                FOREIGN KEY([user_id]) 
                REFERENCES [users] ([Id]) 
                ON DELETE CASCADE
            )""")

conn.commit()


def insert_user(emp):
    with conn:
        cur.execute("insert into users (FirstName, LastName) values (:FirstName, :LastName)", {'FirstName':emp.FirstName,'LastName':emp.LastName })
        return cur.lastrowid

def insert_income(value):
    with conn:
        cur.execute("insert into income (user_id, income, description, source, date) values (:user_id, :income, :description, :source, :date )", 
                    {'user_id':value.user_id ,'income':value.income , 'description': value.description, 'source':value.source, 'date':value.date })

def insert_expenses(value):
    with conn:
        cur.execute("insert into expenses (user_id, expenses, description, source, date) values (:user_id, :expenses, :description, :source, :date )", 
                    {'user_id':value.user_id ,'expenses':value.expenses , 'description': value.description, 'source':value.source, 'date':value.date })

def select_user(emp):
    with conn:
        id = cur.execute("select id from users  where FirstName = :FirstName and LastName = :LastName ", {'FirstName':emp.FirstName,'LastName':emp.LastName }).fetchone()
        if id is not None:
            id = id[0]
        else:
            pass
        return id


user1 = Users('Boyan', 'Baykov')
user_id = insert_user(user1)
#insert income fro user 1 
income_user1 = finances.Income(user_id, 150.0, 'Sold Vacuum Cleaner','Income','2024-03-09' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 100.0, 'Sold 100kg Potatoes','Income','2024-03-02' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 1850.0, 'Monly Salary','Income','2024-03-01' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 300.0, 'Working on a webpage','Income','2024-03-22' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 50.0, 'CLean the stairway','Income','2024-03-29' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 50.0, 'Reinstalling computer','Income','2024-03-02' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 50.0, 'Reinstalling computer','Income','2024-03-15' )
insert_income(income_user1 )
conn.commit()

#insert expences fro user 1 
expenses_user1 = finances.Expenses(user_id, 450.0, 'Appartment rental','expenses','2024-03-01' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 120.0, 'Electricity','expenses','2024-03-06' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 35.0, 'Water bill','expenses','2024-03-09' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 25.0, 'Internet','expenses','2024-03-22' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 30.0, 'Satelite TV','expenses','2024-03-29' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 30.0, 'Mobile Phone','expenses','2024-03-02' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 60.0, 'Garage rental','expenses','2024-03-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 260.0, 'New clothes','expenses','2024-03-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 260.0, 'Food','expenses','2024-03-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 80.0, 'Personal Accessories','expenses','2024-03-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 120.0, 'Car Fuel','expenses','2024-03-15' )
insert_expenses(expenses_user1 )
conn.commit()


user2 = Users('Petar', 'Ivanov')
user_id2 = insert_user(user2)
#insert income fro user 1 
income_user1 = finances.Income(user_id2, 8150.0, 'Sold my Car','Income','2024-03-09' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id2, 100.0, 'Unknown','Income','2024-03-02' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id2, 2450.0, 'Monly Salary','Income','2024-03-01' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id2, 600.0, 'Winning a lottery','Income','2024-03-22' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id2, 150.0, 'Hidding taxes','Income','2024-03-02' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id2, 450.0, 'Playing video games','Income','2024-03-15' )
insert_income(income_user1 )
conn.commit()

#insert expences fro user 1 
expenses_user1 = finances.Expenses(user_id2, 400.0, 'Appartment rental','expenses','2024-03-01' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 170.0, 'Electricity','expenses','2024-03-06' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 45.0, 'Water bill','expenses','2024-03-09' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 33.0, 'Internet','expenses','2024-03-22' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 40.0, 'Satelite TV','expenses','2024-03-29' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 32.0, 'Mobile Phone','expenses','2024-03-02' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 70.0, 'Garage rental','expenses','2024-03-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 444.0, 'New clothes','expenses','2024-03-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 344.0, 'Food','expenses','2024-03-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 220.0, 'Cigaretes','expenses','2024-03-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 120.0, 'Personal Accessories','expenses','2024-03-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 800.0, 'Playing Lottery','expenses','2024-03-29' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id2, 200.0, 'Car Fuel','expenses','2024-03-29' )
insert_expenses(expenses_user1 )
conn.commit()


user2 = Users('Petar', 'Ivanov')
user_id = select_user(user2)

#insert income fro user 1 
income_user1 = finances.Income(user_id, 8150.0, 'Sold my Car','Income','2024-04-09' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 100.0, 'Unknown','Income','2024-04-02' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 2450.0, 'Monly Salary','Income','2024-04-01' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 600.0, 'Winning a lottery','Income','2024-04-22' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 150.0, 'Hidding taxes','Income','2024-04-02' )
insert_income(income_user1 )
income_user1 = finances.Income(user_id, 450.0, 'Playing video games','Income','2024-04-15' )
insert_income(income_user1 )
conn.commit()

#insert expences fro user 1 
expenses_user1 = finances.Expenses(user_id, 400.0, 'Appartment rental','expenses','2024-04-01' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 170.0, 'Electricity','expenses','2024-04-06' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 45.0, 'Water bill','expenses','2024-04-09' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 33.0, 'Internet','expenses','2024-04-22' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 40.0, 'Satelite TV','expenses','2024-04-29' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 32.0, 'Mobile Phone','expenses','2024-04-02' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 70.0, 'Garage rental','expenses','2024-04-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 444.0, 'New clothes','expenses','2024-04-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 344.0, 'Food','expenses','2024-04-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 220.0, 'Cigaretes','expenses','2024-04-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 120.0, 'Personal Accessories','expenses','2024-04-15' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 800.0, 'Playing Lottery','expenses','2024-04-29' )
insert_expenses(expenses_user1 )
expenses_user1 = finances.Expenses(user_id, 200.0, 'Car Fuel','expenses','2024-04-29' )
insert_expenses(expenses_user1 )
conn.commit()


#create overview of all needed data.
cur.execute(""" create view if not exists v_expenses_income
            as
            select 
                IFNULL(b.id, a.id) as id,  
                (IFNULL(b.FirstName, a.FirstName) || ' ' ||   IFNULL(b.LastName, a.LastName)) as FullName , 
                IFNULL(b.description, '') as description_expenses, 
                IFNULL(b.expenses, 0) as expenses,
                IFNULL(b.source, '') as source_expenses, 
                IFNULL(b.date, a.date) as date_expenses, 
                IFNULL(a.description, '')  as description_income ,  
                IFNULL(a.income, 0) as income , 
                IFNULL(a.source, '') as source_income ,  
                IFNULL(a.date, '')  as date_income,
                strftime('%Y-%m',  IFNULL(a.date, b.date)) as Month
            from 
                (select row_number() over (partition by strftime('%Y-%m', i.date), user_id ) as rw , u.id, u.FirstName, u.LastName, i.Income, i.Description,i.Source, i.Date, strftime('%Y-%m', i.date) as mnt
                from users u
                join income i on u.id = i.user_id  ) a
            full join 
                (select row_number() over (partition by  strftime('%Y-%m', e.date), user_id  ) as rw1 ,u.id, u.FirstName, u.LastName, e.expenses, e.description, e.source, e.date, strftime('%Y-%m', e.date)as mnt
                from users u
                join expenses e on u.id = e.user_id  ) b on a.id = b.id and a.rw = b.rw1 and a.mnt = b.mnt
            """)
conn.commit()




#testing if all good 
# cur.execute("select * from income")
# print(cur.fetchall())
# cur.execute("select * from expenses")
# print(cur.fetchall())


conn.close()

