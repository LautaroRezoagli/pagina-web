from flask import Flask, render_template
from registro import registro_bp
from asistencia import asistencia_bp

app = Flask(__name__)

app.register_blueprint(registro_bp)
app.register_blueprint(asistencia_bp)

@app.route('/')
def menu():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True)
