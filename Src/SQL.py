import pypyodbc
from datetime import date

date = date.today()
today = date.strftime("%d/%m/%Y")

conn = pypyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-DQ67SQN\SQLEXPRESS;'
                      'Database=CutPanelAudit;'
                      'Trusted_Connection=yes;')


def record_data(adevratio_float, pdevratio_float, shaperesult_float, shape, shrinkage, result):

    query = "Insert Into CutPanelAudit1 Values(?,?,?,?,?,?,?,?,?)"
    cursor = conn.cursor()

    # Execute the sql query
    cursor.execute(query, [today, '1', '2', adevratio_float, pdevratio_float, shaperesult_float, shape, shrinkage, result])

    # Commit the data
    conn.commit()
    print('---Data Added To the Database---')

    # Close the connection
    conn.close()
