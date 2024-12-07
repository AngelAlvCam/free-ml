from flask_wtf import FlaskForm
from wtforms import (StringField,BooleanField,DateTimeField,RadioField,SelectField,
                    TextAreaField,TextField,SubmitField,FileField,FloatField)
from wtforms.validators import DataRequired

# Esta clase representa al formulario para el algoritmo apriori
class apriori_form_class(FlaskForm):
    input_file = FileField("Inserte el archivo en formato CSV sin header")
    min_support = FloatField("Soporte mínimo")
    min_confidence = FloatField("Confianza mínima")
    min_lift = FloatField("Elevación")
    submit = SubmitField('Calcular')


# Esta clase representa al formulario para el algoritmo de metricas de distancia
class metricasd_form_class(FlaskForm):
    input_file = FileField("Inserte el archivo en formato CSV sin header, con datos únicamente numéricos")
    metric = SelectField('Seleccione el tipo de métrica de distancia: ', choices=[('0','Euclidea'),('1','Chebyshev'),('2','Manhattan')])
    std = SelectField('Seleccione el tipo de estandarización: ', choices=[('0','Estandarización'),('1','Normalización')])
    submit = SubmitField('Calcular')


# Esta clase representa al formulario para selección de características
class selcar_form_class(FlaskForm):
    input_file = FileField("Inserte el archivo en formato CSV sin header, con datos únicamente numéricos")
    submit = SubmitField('Calcular')