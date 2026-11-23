from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def inicio():
    temperatura = round(random.uniform(20, 30), 1)
    umidade= round(random.uniform(40, 80), 1)

    horario=datetime.now ().strftime("%d/%m/%Y %H:%M:%S")
    return render_template(
    'index.html', 
    temperatura=temperatura, 
    umidade=umidade, 
    horario=horario
    )

if __name__ == '__main__':
    app.run(debug=True)
