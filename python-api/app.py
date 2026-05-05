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

    except FileNotFoundError:
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
            port=5432,
            database="tmdb",
            user="tm",
            password="eneas"
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
            port=5432,
            database="base_que_no_existe",
            user="tm",
            password="password_incorrecta",
            connect_timeout=3
        )

        conexion.close()

        return jsonify({
            "ok": True,
            "message": "Esto no debería ejecutarse"
        }), 200

    except psycopg2.OperationalError as e:
        return jsonify({
            "ok": False,
            "critical": False,
            "errorType": "DB_CONNECTION_ERROR",
            "userMessage": "No se puede conectar con la base de datos.",
            "technicalMessage": str(e)
        }), 500

    except Exception as e:
        return jsonify({
            "ok": False,
            "critical": True,
            "errorType": type(e).__name__,
            "userMessage": "Se ha producido un error inesperado al acceder a la base de datos.",
            "technicalMessage": str(e)
        }), 500
        
@app.route("/api/pokemon/ok")
def pokemon_ok():
    try:
        respuesta = requests.get(
            "https://pokeapi.co/api/v2/pokemon/pikachu",
            timeout=5
        )
        respuesta.raise_for_status()

        datos = respuesta.json()

        return jsonify({
            "estado": "OK",
            "mensaje": "Llamada correcta a la API externa",
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
        respuesta = requests.get(
            "https://pokeapi.co/api/v2/pokemon/noexiste123456",
            timeout=5
        )
        respuesta.raise_for_status()

        return jsonify(respuesta.json()), 200

    except requests.exceptions.HTTPError:
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


@app.route("/")
def index():
    return jsonify({
        "mensaje": "API Flask funcionando correctamente",
        "endpoints": [
            "/api/archivo/ok",
            "/api/archivo/error",
            "/api/db/ok",
            "/api/db/error",
            "/api/pokemon/ok",
            "/api/pokemon/error"
        ]
    }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)