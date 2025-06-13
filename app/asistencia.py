from flask import Blueprint, render_template, request
from datetime import datetime

asistencia_bp = Blueprint('asistencia', __name__, template_folder='templates')

@asistencia_bp.route('/entrada', methods=['GET', 'POST'])
def entrada():
    if request.method == 'POST':
        legajo = request.form.get('legajo')
        dni_ultimos = request.form.get('dni_ultimos')
        dependencia = request.form.get('dependencia')
        fecha_hora = datetime.now()

        return f"Entrada registrada: Legajo {legajo}, DNI ****{dni_ultimos}, Dependencia {dependencia}, Hora: {fecha_hora}"

    return render_template('entrada.html')


@asistencia_bp.route('/salida', methods=['GET', 'POST'])
def salida():
    if request.method == 'POST':
        legajo = request.form.get('legajo')
        dni_ultimos = request.form.get('dni_ultimos')
        fecha_hora = datetime.now()

        return f"Salida registrada: Legajo {legajo}, DNI ****{dni_ultimos}, Hora: {fecha_hora}"

    return render_template('salida.html')
