from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print('Received webhook payload:', data)
    response = requests.post('http://127.0.0.1:9090/user/create', json=data)
    dataResponse = 'Peticion recibida '
    return  dataResponse

if __name__ == '__main__':
    app.run(debug=True)
