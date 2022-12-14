import pypyodbc
from datetime import date

date = date.today()
today = date.strftime("%d/%m/%Y")

conn = pypyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-DQ67SQN\SQLEXPRESS;'
                      'Database=CutPanelAudit;'
                      'Trusted_Connection=yes;')


def record_data(adevratio_float, pdevratio_float, shaperesult_float, shape, shrinkage, result, sales_order_number, docket_number, cut_number, size, style, panel_number, location):

    query = "Insert Into CutPanelAudit Values(?,?,?,?,?,?,?,?,?,?,?,?,?)"
    cursor = conn.cursor()

    # Execute the sql query
    cursor.execute(query, [today, cut_number, panel_number, sales_order_number, docket_number, size, style, adevratio_float, pdevratio_float, shaperesult_float, shape, shrinkage, result])

    # Commit the data
    conn.commit()
    status = '----------------------- Data Added To the Database -----------------------'
    print('---Data Added To the Database---')

    return status