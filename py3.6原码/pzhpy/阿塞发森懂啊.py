from bottle import get, run
 
@get('/')
def homepage():
    return '<p style="color:red">Hello World!</p>'

run(host='', port=25252)

