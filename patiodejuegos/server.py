#ACTIVIDAD PATIO DE JUEGOS
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play", methods=['GET'])
def play_cajas():
    color = "CornflowerBlue"
    return render_template("index.html", num1=3, color=color)

@app.route("/play/<int:num1>", methods=['GET'])
def play_cajas_veces(num1):
    color = "CornflowerBlue"
    return render_template("index.html", num1=num1, color=color)

#algunas ideas de colores de css a elegir para la ruta: 
# crimson  -  hotpink - khaki - plum - mediumaqua 
@app.route("/play/<int:num1>/<string:color>", methods=['GET'])
def play_cajas_veces_color(num1, color):
    return render_template("index.html", num1=num1, color=color)


if __name__ == "__main__": #esto permite que solo se ejecute cuando estoy dentro de este proyecto
    app.run( debug = True , port = 5003 )

