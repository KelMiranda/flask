#recordar estos comandos $env:FLASK_DEBUG=1  $env:FLASK_APP=main.py

from flask import Flask, request, make_response, redirect

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port = 5000, debug = True)

@app.route('/')
def index():
    user_ip = request.remote_addr

    respose = make_response(redirect('/hello'))
    respose.set_cookie('user_ip', user_ip)

    return respose
    

@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return f'Hello usuario tu ip es: {user_ip}'