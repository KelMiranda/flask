#recordar estos comandos $env:FLASK_DEBUG=1  $env:FLASK_APP=main.py pip install -r .\requirements.txt

from flask import Flask, request, make_response, redirect, render_template

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
    return render_template('hello.html', user_ip = user_ip, nameP = 'Kelvin')