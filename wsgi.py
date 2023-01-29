from main import app

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=443, ssl_context=('fullchain.pem', 'privkey.pem'))
    app.run(host='0.0.0.0', port=80)