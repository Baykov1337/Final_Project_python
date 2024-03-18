class Create_VIEW():
    def __init__(self) -> None:
        pass


    def sql_query():
        sql_query = """
            CREATE VIEW IF NOT EXISTS v_expenses_income AS
            SELECT 
                IFNULL(b.id, a.id) AS id,  
                (IFNULL(b.FirstName, a.FirstName) || ' ' || IFNULL(b.LastName, a.LastName)) AS FullName, 
                IFNULL(b.description, '') AS description_expenses, 
                IFNULL(b.expenses, 0) AS expenses,
                IFNULL(b.source, '') AS source_expenses, 
                IFNULL(b.date, a.date) AS date_expenses, 
                IFNULL(a.description, '') AS description_income,  
                IFNULL(a.income, 0) AS income, 
                IFNULL(a.source, '') AS source_income,  
                IFNULL(a.date, '') AS date_income
            FROM 
                (SELECT 
                    row_number() OVER (PARTITION BY strftime('%Y-%m', i.date), user_id ) AS rw, 
                    u.id, u.FirstName, u.LastName, i.Income, i.Description, i.Source, i.Date, strftime('%Y-%m', i.date) AS mnt
                FROM 
                    users u
                JOIN 
                    income i ON u.id = i.user_id) a
            FULL JOIN 
                (SELECT 
                    row_number() OVER (PARTITION BY strftime('%Y-%m', e.date), user_id ) AS rw1, 
                    u.id, u.FirstName, u.LastName, e.expenses, e.description, e.source, e.date, strftime('%Y-%m', e.date) AS mnt
                FROM 
                    users u
                JOIN 
                    expenses e ON u.id = e.user_id) b 
            ON 
                a.id = b.id AND a.rw = b.rw1 AND a.mnt = b.mnt
            """
        return sql_query
