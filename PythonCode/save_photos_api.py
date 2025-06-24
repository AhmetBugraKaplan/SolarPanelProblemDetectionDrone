from flask import Flask, request
from datetime import datetime
import os


SAVE_DIR = "esp_photos"


os.makedirs(SAVE_DIR, exist_ok=True)

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_photo():
    
    img_data = request.data

   
    filename = datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".jpg"
    filepath = os.path.join(SAVE_DIR, filename)

    # Fotoğrafı kaydet
    with open(filepath, "wb") as f:
        f.write(img_data)

    print(f"Kaydedildi: {filepath}")
    return {"status": "ok", "filename": filename}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
