from flask import Blueprint, render_template, request

registro_bp = Blueprint('registro', __name__, template_folder='templates')

@registro_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        dni = request.form.get('dni')
        correo = request.form.get('correo')
        legajo = request.form.get('legajo')
        horas = request.form.get('horas')
        funcion = request.form.get('funcion')
        dependencia = request.form.get('dependencia')

        return f"Trabajador registrado: {nombre} {apellido}, DNI: {dni}, Correo: {correo}, Legajo: {legajo}, Horas: {horas}, Función: {funcion}, Dependencia: {dependencia}"

    return render_template('registro.html')
