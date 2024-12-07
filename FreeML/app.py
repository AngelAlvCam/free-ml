# Se importa a las bibliotecas necesarias
from flask import Flask, render_template, session, redirect, url_for
from werkzeug.utils import secure_filename

import apriori_dir.exe_apriori as apriori_exe
import metricasd_dir.exe_metricas as metricasd_exe
import caracteristicas_dir.exe_sel_car as selcar_exe
from forms import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'


@app.route('/')
def index():
    return render_template('home.html')

# Para algoritmo apriori
@app.route('/apriori_form',methods=['GET','POST'])
def apriori_form():
    form = apriori_form_class()   # S crea una instancia del formulario
    if form.validate_on_submit():
        filename = secure_filename(form.input_file.data.filename)
        form.input_file.data.save('static/' + filename)
        support = form.min_support.data
        confidence = form.min_confidence.data
        lift = form.min_lift.data
        session['filename'] = "static/" + filename
        session['support'] = support
        session['confidence'] = confidence
        session['lift'] = lift
        return redirect(url_for('apriori_result'))
    return render_template('apriori.html', form=form)

@app.route('/apriori_form/result')
def apriori_result():
    reglas_asociacion = apriori_exe.exe(session['filename'],float(session['support']),float(session["confidence"]),float(session["lift"]))
    return render_template('apriori_result.html', reglas = reglas_asociacion)

# Para cálculo de métricas de distancia
@app.route('/metricasd_form',methods=['GET','POST'])
def metricasd_form():
    form = metricasd_form_class()   # S crea una instancia del formulario
    if form.validate_on_submit():
        filename = secure_filename(form.input_file.data.filename)
        form.input_file.data.save('static/' + filename)
        session['filename'] = "static/" + filename
        session['metric'] = form.metric.data
        session['std'] = form.std.data
        return redirect(url_for('metricasd_result'))
    return render_template('metricasd.html', form=form)

@app.route('/metricasd_form/result')
def metricasd_result():
    distancia = metricasd_exe.exe(session['filename'],session['metric'],session['std'])
    return render_template('metricasd_result.html',distancia=distancia)

# Para selección de características
@app.route('/selcar_form',methods=['GET','POST'])
def selcar_form():
    form = selcar_form_class()   # S crea una instancia del formulario
    if form.validate_on_submit():
        filename = secure_filename(form.input_file.data.filename)
        form.input_file.data.save('static/' + filename)
        return redirect(url_for('selcar_result'))
    return render_template('sel_car.html', form=form)

@app.route('/selcar_form/result')
def selcar_result():
    matrizcorr = selcar_exe.exe(session['filename'])
    return render_template('sel_car_result.html',matrizcorr = matrizcorr)

if __name__ == '__main__':
    app.run(debug=True)