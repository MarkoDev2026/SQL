from flask import Flask, request

app = Flask(__name__)

# Esta ruta atrapa los datos que manda el archivo frontend.html
@app.route('/guardar_registro', methods=['POST'])
def guardar():
    # 1. Recibimos los datos del HTML
    sueno = request.form['horas_sueno']
    estres = request.form['nivel_estres']
    fecha = request.form['fecha']
    
    # 2. Aquí armamos la orden SQL para insertar la información
    orden_sql = f"INSERT INTO Registro_Diario (id_usuario, fecha, horas_sueno, nivel_estres) VALUES (1, '{fecha}', {sueno}, {estres});"
    
    # 3. Confirmación en pantalla
    print("EJECUTANDO SQL:", orden_sql)
    return f"¡Datos recibidos con éxito! Se guardaron {sueno} horas de sueño para la fecha {fecha}."

if __name__ == '__main__':
    app.run(debug=True, port=5000)