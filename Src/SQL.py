import pypyodbc
from datetime import date

date = date.today()
today = date.strftime("%y/%m/%d")

conn = pypyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-ETPEQC8\SQLEXPRESS;'
                      'Database=CutPanelAudit;'
                      'Trusted_Connection=yes;')


def record_data(adevratio_float, pdevratio_float, shaperesult_float, shape, shrinkage, result, sales_order_number, docket_number, cut_number, size, style, panel_number, location):

    query = "Insert Into CutPanelAuditDB Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    cursor = conn.cursor()

    # Execute the sql query
    cursor.execute(query, [today, cut_number, panel_number, sales_order_number, docket_number, size, style, adevratio_float, pdevratio_float, shaperesult_float, shape, shrinkage, result,"kj"])

    # Commit the data
    conn.commit()
    status = '----------------------- Data Added To the Database -----------------------'
    print('---Data Added To the Database---')

    return status