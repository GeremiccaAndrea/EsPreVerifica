from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/formegeometriche' , methods = ['GET'])
def formegeometriche():
    base = int(request.args.get('base')) #request.args.get serve per creare una variabile in python avente il valore del parametro che inserisco in html
    altezza = int(request.args.get('altezza'))
    formageometrica = request.args.get('formageometrica')
    area = base * altezza 
    if formageometrica == 'rettangolo':
        return render_template("risultato.html", formageometrica = formageometrica, area = area)
    else:
        return render_template("risultato.html", formageometrica = formageometrica, area = area)
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)