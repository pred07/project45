from flask import Flask, render_template, request, redirect, url_for
from data import easy

app = Flask(__name__)

#index
@app.route('/')
def index():
    return render_template('index.html')

#startmission
@app.route('/startmission.html')
def startmission():
    return render_template('startmission.html')

@app.route('/portal.html')
def startmissionportal():
    return render_template('portal.html')

@app.route('/success.html')
def startmissionsuccess():
    return render_template('success.html')

@app.route('/ronan.html')
def startmissionronan():
    return render_template('ronan.html')

#mission2
@app.route('/agent.html')
def mission1():
    return render_template('agent.html')
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'agent47' and password == 'missionimpossible':
            return redirect(url_for('success'))
        else:
            return 'Incorrect username or password'
    else:
        return 'Method not allowed'

@app.route('/codeforsuccess')
def success():
    return 'Yeyy!! You got this right...SwastikaCTF{m15510n_p0551bl3}'

#mission3
@app.route('/cookie.html')
def mission2():
    return render_template('cookie.html')

#mission4
@app.route('/easy.html')
def mission3():
    return render_template('easy.html')

@app.route('/submit1', methods=['POST'])
def submit_form1():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if password == '123456':
            return redirect(url_for('success1'))

        else:
            return 'Incorrect username or password'
    else:
        return 'This password is too hard !'

@app.route('/success12prettier')
def success1():
    return easy

#mission5
@app.route('/ironman.html')
def mission4():
    return render_template('ironman.html')

#mission6?????????????????????

if __name__ == '__main__':
    app.run(debug=True)