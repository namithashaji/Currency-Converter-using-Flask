from flask import Flask, render_template, request

app = Flask(__name__)
# app.config.from_object(__name__)

@app.route('/')
def welcome():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def result():
    currency = request.form.get("currency")
    var_1 = request.form.get("var_1", type=float, default=0)
    convert = request.form.get("convert")
    if(currency == 'Rupee'and convert == 'Rupee'):
        result = var_1
    elif(currency == 'Rupee'and convert == 'USD'):
        result = var_1* 0.012
    elif(currency == 'Rupee'and convert == 'Euro'):
        result = var_1* 0.011 
    elif(currency == 'Rupee'and convert == 'Pound'):
        result = var_1 * 0.010
    elif(currency == 'Rupee'and convert == 'Dinar'):
        result = var_1 * 0.0037
    elif(currency == 'Rupee'and convert == 'Yuan'):
        result = var_1 * 0.084

    elif(currency == 'USD'and convert == 'Rupee'):
        result = var_1 * 82.02
    elif(currency == 'USD'and convert == 'USD'):
        result = var_1
    elif(currency == 'USD'and convert == 'Euro'):
        result = var_1* 0.94
    elif(currency == 'USD'and convert == 'Pound'):
        result = var_1 * 0.83
    elif(currency == 'USD'and convert == 'Dinar'):
        result = var_1 * 0.31
    elif(currency == 'USD'and convert == 'Yuan'):
        result = var_1 * 6.91

    elif(currency == 'Euro'and convert == 'Rupee'):
        result = var_1 * 87.40
    elif(currency == 'Euro'and convert == 'USD'):
        result = var_1 * 1.07
    elif(currency == 'Euro'and convert == 'Euro'):
        result = var_1
    elif(currency == 'Euro'and convert == 'Pound'):
        result = var_1 * 0.89
    elif(currency == 'Euro'and convert == 'Dinar'):
        result = var_1 * 0.33
    elif(currency == 'Euro'and convert == 'Yuan'):
        result = var_1 * 7.36

    elif(currency == 'Pound'and convert == 'Rupee'):
        result = var_1 * 98.70
    elif(currency == 'Pound'and convert == 'USD'):
        result = var_1 * 1.20
    elif(currency == 'Pound'and convert == 'Euro'):
        result = var_1 * 1.13
    elif(currency == 'Pound'and convert == 'Pound'):
        result = var_1
    elif(currency == 'Pound'and convert == 'Dinar'):
        result = var_1 * 0.37
    elif(currency == 'Pound'and convert == 'Yuan'):
        result = var_1 * 8.31

    elif(currency == 'Dinar'and convert == 'Rupee'):
        result = var_1 * 267.20
    elif(currency == 'Dinar'and convert == 'USD'):
        result = var_1 * 3.26
    elif(currency == 'Dinar'and convert == 'Euro'):
        result = var_1 * 3.06
    elif(currency == 'Dinar'and convert == 'Pound'):
        result = var_1 * 2.71
    elif(currency == 'Dinar'and convert == 'Dinar'):
        result = var_1 
    elif(currency == 'Dinar'and convert == 'Yuan'):
        result = var_1 * 22.50

    elif(currency == 'Yuan'and convert == 'Rupee'):
        result = var_1 * 11.88
    elif(currency == 'Yuan'and convert == 'USD'):
        result = var_1 * 0.14
    elif(currency == 'Yuan'and convert == 'Euro'):
        result = var_1 * 0.14
    elif(currency == 'Yuan'and convert == 'Pound'):
        result = var_1 * 0.12
    elif(currency == 'Yuan'and convert == 'Dinar'):
        result = var_1 * 0.044
    elif(currency == 'Yuan'and convert == 'Yuan'):
        result = var_1 

    else:
        result = 0
    entry = result
    return render_template('form.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)