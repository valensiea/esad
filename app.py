from flask import Flask, request, render_template

app = Flask(__name__)



@app.route('/')
def form():
    return('hello')

if __name__ == '__main__':
    app.run(debug=True)
