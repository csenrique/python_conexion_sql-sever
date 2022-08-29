from multiprocessing import connection
import pyodbc

try:
    conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=students;UID=csenrique;PWD=cr3st4b1l')
    print("Conexion Exitosa")

    cursor = conexion.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    print(row)

except Exception as ex:
    print(ex)
finally:
    conexion.close()
    print("Conexion Finalizada")