import panel as pn
import pandas as pd
from alchemy import  Views, Session


session = Session.return_session()

class tabulator():
    pass

    def create_tabulator():
        pn.extension('tabulator')

        df = pd.read_sql(session.query(Views).with_entities(Views.id, Views.FullName, Views.description_expenses, Views.expenses, Views.source_expenses, Views.date_expenses,
                                                            Views.description_income, Views.income, Views.source_income, Views.date_income).statement, session.bind)

        tabulator = pn.widgets.Tabulator(df, pagination='local', page_size=10)
        styles = {
        'background-color': '#F6F6F6', 'border': '1px solid black',
        'border-radius': '15px', 'padding': '30px',
        'text-align': 'left',
        'align-items': 'center'
        }
        sum_html = pn.pane.HTML("""<table>
                                <tr>
                                    <th>Общо Приходи</th>
                                    <th>Общо Разходи</th>
                                    <th>Среден отчет</th>
                                </tr>
                                <td>Общо Приходи: лв.0.00</td>
                                <td>Общо Разходи: лв.0.00</td>
                                <td>Среден отчет: лв.0.00</td>
                                </tr>
                                </table>""", styles=styles)
    
        unique_firstname = df['FullName'].unique().tolist()
        select_firstname = pn.widgets.Select(options=unique_firstname, name='Select Full Name')

        unique_dates = pd.to_datetime(df['date_expenses']).dt.to_period('M').astype(str).unique().tolist()
        select_start_date = pn.widgets.Select(options=unique_dates, name='Select Start Date')
        select_end_date = pn.widgets.Select(options=unique_dates, name='Select End Date')

        @pn.depends(select_firstname.param.value, select_start_date.param.value, select_end_date.param.value)
        def update_table(selected_firstname, start_date, end_date):
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)
                    
            start_month = start_date.month, 
            start_year = start_date.year
            end_month = end_date.month 
            end_year = end_date.year

            filtered_df = df[(df['FullName'] == selected_firstname) & 
                            ((pd.to_datetime(df['date_expenses']).dt.month >= start_month) & 
                            (pd.to_datetime(df['date_expenses']).dt.year >= start_year) & 
                            (pd.to_datetime(df['date_expenses']).dt.month <= end_month) & 
                            (pd.to_datetime(df['date_expenses']).dt.year <= end_year))]

            tabulator.value = filtered_df
            if filtered_df.empty:
                total_income = 0.0
                total_expenses = 0.0
                total_overerall = 0.0
            else:
                total_income = filtered_df['income'].sum()
                total_expenses = filtered_df['expenses'].sum()
                total_overerall = filtered_df['income'].sum() - filtered_df['expenses'].sum()
            sum_html.object = f"""<table>
                                <tr>
                                    <th>Общо Приходи</th>
                                    <th>Общо Разходи</th>
                                    <th>Среден отчет</th>
                                </tr>
                                    <td>{total_income} лв.</td>
                                    <td>{total_expenses} лв.</td>
                                    <td>{total_overerall} лв.</td>
                                </tr>
                                </table>"""
        layout = pn.Column(pn.Row(select_firstname, select_start_date, select_end_date), tabulator,sum_html, update_table).servable()

        return layout