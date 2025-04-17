from flask import Flask
app= Flask(__name__)

@app.route('/hello/<name>')
def hello():
    return 'Hello %s!' % name

if __name__=='__main__':
    app.run(debug=True)
# This code creates a simple Flask web application that returns "Hello" when accessed at the root URL.