from flask import Flask, render_template, request, jsonify
from mylib import myfunct

app = Flask(__name__)

@app.route('/')
def home():
    # You can pass variables into the template
    name = "Yut"
    return render_template('index.html', name=name)

@app.route('/tech')
def tech():
    return render_template('tech.html')

@app.route('/draw/<int:s>')
def draw(s):
    # print("-" * 50)
    texthtml = ""
    for i in range(1,s+1):
        texthtml += (myfunct("Hi!", i)) +"<br>"  
    # return texthtml
    return render_template('draw.html',count=s,textto='OK',txt = texthtml)

@app.route('/myid')
def myid():
    data = '68130239'
    return jsonify(data)

@app.route('/submit', methods=['POST'])
def submit():
    user_text = request.form.get('user_text')
    return render_template('index.html', name="Yut", message=f"You entered: {user_text}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

