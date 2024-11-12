import comtypes
from flask import Flask, render_template, request, jsonify, url_for
import pyttsx3
import os
from uuid import uuid4

app = Flask(__name__)

# Rota inicial


@app.route('/')
def index():
    return render_template('index.html')

# Rota de conversão de texto em fala


@app.route('/convert', methods=['POST'])
def convert():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Nenhum texto fornecido"}), 400

    # Inicializar o COM antes de usar o pyttsx3
    comtypes.CoInitialize()

    # Configuração para converter o texto em fala e salvar como arquivo temporário
    engine = pyttsx3.init()

    # Defina o caminho do arquivo dentro de static/audio
    audio_dir = os.path.join(app.static_folder, 'audio')

    # Verifique se a pasta "audio" existe, se não, crie
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)

    # Defina o nome do arquivo com UUID
    audio_file = f'{uuid4()}.mp3'
    audio_path = os.path.join(audio_dir, audio_file)

    # Salve o arquivo de áudio
    engine.save_to_file(text, audio_path)
    engine.runAndWait()

    # Retorne a URL do arquivo de áudio
    return jsonify({"audio_url": url_for('static', filename=f'audio/{audio_file}')})


if __name__ == '__main__':
    app.run(debug=True)
