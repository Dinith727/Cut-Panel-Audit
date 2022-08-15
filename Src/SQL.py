import pypyodbc
from datetime import date

date = date.today()
today = date.strftime("%d/%m/%Y")

Cut_No = '1'
Panel_No = '2'
Sales_Order_No = '2'
Docket_No = '2'
Size = 'M'
Style = '2'


conn = pypyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-DQ67SQN\SQLEXPRESS;'
                      'Database=CutPanelAudit;'
                      'Trusted_Connection=yes;')


def record_data(adevratio_float, pdevratio_float, shaperesult_float, shape, shrinkage, result):

    query = "Insert Into CutPanelAudit Values(?,?,?,?,?,?,?,?,?,?,?,?,?)"
    cursor = conn.cursor()

    # Execute the sql query
    cursor.execute(query, [today, Cut_No, Panel_No, Sales_Order_No, Docket_No, Size, Style, adevratio_float, pdevratio_float, shaperesult_float, shape, shrinkage, result])

    # Commit the data
    conn.commit()
    print('---Data Added To the Database---')

    # Close the connection
    conn.close()
