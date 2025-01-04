from flask import Flask, request, jsonify
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

@app.route("/save-image", methods=["POST"])
def save_image():
    try:
        data = request.json
        image_data = data["image"].split(",")[1]  # Entferne den Präfix "data:image/png;base64,"
        image_bytes = base64.b64decode(image_data)

        # Lade Bild mit Pillow
        image = Image.open(BytesIO(image_bytes))

        # Speichere Bild als BMP
        image.save("bild.bmp", format="BMP")

        return jsonify({"message": "Bild erfolgreich gespeichert!"}), 200
    except Exception as e:
        print(f"Fehler: {e}")
        return jsonify({"message": "Fehler beim Speichern des Bildes."}), 500

if __name__ == "__main__":
    app.run(debug=True)
