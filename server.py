from flask import Flask, render_template
app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/income_assurance/')
def income_assurance():
    return render_template('income_assurance.html')   


@app.route('/prisat_hov/')
def prisat_hov():
    return render_template('prisat_hov.html')       

if __name__ == '__main__':
    app.run( debug = True)