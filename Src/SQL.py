import pyodbc
from datetime import date

date = date.today()

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-DQ67SQN\SQLEXPRESS;'
                      'Database=CutPanelAudit;'
                      'Trusted_Connection=yes;')


def record_data(area, perimeter):

    query = "Insert Into cutpanel Values(?,?)"
    cursor = conn.cursor()

    # Execute the sql query
    cursor.execute(query, [area, perimeter])

    # Commit the data
    conn.commit()
    print('Data Added To the Database')
    print('Date : ', date)

    # Close the connection
    conn.close()
