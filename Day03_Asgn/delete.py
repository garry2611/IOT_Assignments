#check Error

import dbconn

def delete_empinfo(empid):

    conn = dbconn.get_connection()

    query = f" Delete from empinfo where empid = %s ;"
    val = (empid , )

    cursor = conn.cursor()

    cursor.execute(query , val)

    conn.commit()

    cursor.close()

    conn.close()

delete_empinfo(7)