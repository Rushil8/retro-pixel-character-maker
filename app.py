from flask import Flask,render_template
from PIL import Image
import io
from flask import request, send_file, abort
from image_utils import pixelate

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/pixelate", methods=["POST"])
def pixelate_api():
    print("Pixelate API called")
    file = request.files.get("image")
    pixel_size = int(request.form.get("pixel", 16))
    palette = int(request.form.get("palette", 16))
    palette_type = request.form.get("paletteType","default")
    img = Image.open(file.stream).convert("RGB")
    result = pixelate(img,pixel_size,palette,palette_type)

    buf = io.BytesIO()
    result.save(buf,format="PNG")
    buf.seek(0)

    return send_file(buf,mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)