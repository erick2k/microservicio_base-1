from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Microservicio activo'})


@app.route('/api/sumar', methods=['POST'])
def sumar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Parámetros a y b requeridos'}), 400
    return jsonify({'resultado': a + b})

# erick herrera


@app.route('/api/restar', methods=['POST'])
def restar():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Parámetros a y b requeridos'}), 400
    return jsonify({'resultado': a - b})

# erick herrera


@app.route('/api/multi', methods=['POST'])
def multi():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')
    if a is None or b is None:
        return jsonify({'error': 'Parámetros a y b requeridos'}), 400
    return jsonify({'resultado': a * b})


@app.route('/api/info', methods=['GET'])
def info():
    return jsonify({
        'autor': 'Equipo X',
        'version': '1.0',
        'descripcion': 'Microservicio de ejemplo para clases de cloud, APIs y Docker.'
    })


@app.route('/api/info_personal', methods=['GET'])
def info_personal():
    return jsonify({
        "dni": "0911446322",
        "nombres": "CARLOS JOSE",
        "apellidos": "HERRERA PEREZ",
        "correo": "erick222k1995@hotmail.com",
        "sexo": "Masculino",
        "tel": "0990725765",
        "fnacimiento": "1995-09-22",
        "forma_pago": "EFECTIVO",
        "precio": "50.90"
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
