from flask import Flask, jsonify
from flask_cors import CORS
import requests
import psycopg2

app = Flask(__name__)
CORS(app)


@app.route("/api/archivo/ok")
def archivo_ok():
    try:
        with open("datos/ejemplo.txt", "r", encoding="utf-8") as fichero:
            contenido = fichero.read()

        return jsonify({
            "estado": "OK",
            "mensaje": "Archivo leído correctamente",
            "contenido": contenido
        }), 200

    except Exception as e:
        return jsonify({
            "estado": "ERROR",
            "tipo": type(e).__name__,
            "mensaje": str(e)
        }), 500


@app.route("/api/archivo/error")
def archivo_error():
    try:
        with open("datos/no_existe.txt", "r", encoding="utf-8") as fichero:
            contenido = fichero.read()

        return jsonify({
            "estado": "OK",
            "contenido": contenido
        }), 200

    except FileNotFoundError as e:
        return jsonify({
            "estado": "ERROR",
            "tipo": "FileNotFoundError",
            "mensaje": "No se ha encontrado el archivo solicitado"
        }), 500

    except Exception as e:
        return jsonify({
            "estado": "ERROR",
            "tipo": type(e).__name__,
            "mensaje": str(e)
        }), 500


@app.route("/api/db/ok")
def db_ok():
    try:
        conexion = psycopg2.connect(
            host="postgres-db",
            database="basicosd",
            user="postgres",
            password="postgres"
        )

        cursor = conexion.cursor()
        cursor.execute("SELECT version();")
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()

        return jsonify({
            "estado": "OK",
            "mensaje": "Conexión a base de datos correcta",
            "version": resultado[0]
        }), 200

    except Exception as e:
        return jsonify({
            "estado": "ERROR",
            "tipo": type(e).__name__,
            "mensaje": str(e)
        }), 500


@app.route("/api/db/error")
def db_error():
    try:
        conexion = psycopg2.connect(
            host="postgres-db",
            database="base_que_no_existe",
            user="postgres",
            password="password_incorrecta"
        )

        conexion.close()

        return jsonify({
            "estado": "OK",
            "mensaje": "Esto no debería ejecutarse"
        }), 200

    except Exception as e:
        return jsonify({
            "estado": "ERROR",
            "tipo": type(e).__name__,
            "mensaje": "Error simulado al acceder a la base de datos"
        }), 500


@app.route("/api/pokemon/ok")
def pokemon_ok():
    try:
        respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu", timeout=5)
        respuesta.raise_for_status()

        datos = respuesta.json()

        return jsonify({
            "estado": "OK",
            "nombre": datos["name"],
            "id": datos["id"]
        }), 200

    except requests.exceptions.RequestException as e:
        return jsonify({
            "estado": "ERROR",
            "tipo": type(e).__name__,
            "mensaje": "Error al llamar a la API de Pokémon"
        }), 500


@app.route("/api/pokemon/error")
def pokemon_error():
    try:
        respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/noexiste123456", timeout=5)
        respuesta.raise_for_status()

        return jsonify(respuesta.json()), 200

    except requests.exceptions.HTTPError as e:
        return jsonify({
            "estado": "ERROR",
            "tipo": "HTTPError",
            "mensaje": "La API externa ha devuelto un error HTTP"
        }), 500

    except requests.exceptions.RequestException as e:
        return jsonify({
            "estado": "ERROR",
            "tipo": type(e).__name__,
            "mensaje": "Error general al llamar a la API externa"
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)