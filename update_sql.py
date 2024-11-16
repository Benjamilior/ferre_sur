import mysql.connector
from mysql.connector import Error

# Configura tus credenciales y datos de conexión
host = 'viaduct.proxy.rlwy.net'
port = 10876
database = 'railway'
user = 'root'
password = 'YhEGXkbjstktPJEYJIhXsrHlAsQnnawr'

df = pd.DataFrame(results)

try:
    # Establecer la conexión
    connection = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        print("Conexión exitosa a la base de datos")

        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Insertar datos
        insert_query = """
        INSERT INTO ferre_sur (product, sku, competitor, price, price_off,date) 
        VALUES (%s, %s, %s, %s, %s)
        """
        now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for index, row in df.iterrows():
            values = (row['SKU'], row['Precio'], row['Precio_oferta'], now_str)
            cursor.execute(insert_query, values)
        
       
        # Confirmar los cambios
        connection.commit()
        
        print("Datos insertados exitosamente")

except Error as e:
    print("Error al conectar a la base de datos:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexión a la base de datos cerrada")
