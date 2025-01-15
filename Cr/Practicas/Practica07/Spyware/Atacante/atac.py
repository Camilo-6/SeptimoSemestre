from flask import Flask, request

app = Flask(__name__)

@app.route('/api/receptor', methods=['POST'])
def recibir_datos():
    data = request.form.get('data')
    print(f'Datos recibidos: {data}')

    with open('datos_recibidos.txt', 'a') as f:
        f.write(f'{data}\n')

    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
