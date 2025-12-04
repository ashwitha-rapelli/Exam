from flask import Flask, render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def submit():
    uname = request.form['uname']
    age = request.form['age']
    return render_template('greeting.html', uname=uname, age=age)
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)