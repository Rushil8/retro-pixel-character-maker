# Retro Pixel Character Maker
Retro Pixel Character Maker is a web-based application that transforms user-uploaded photos into retro-style pixel art game characters. The project combines image processing and computer vision techniques to automatically detect faces, crop images, apply pixelation, and generate nostalgic game-inspired avatars.
The application is designed to be simple, interactive, and fun, while also demonstrating practical use of backend–frontend integration and image processing workflows.

## Features
* Upload images and generate pixel-art characters
* Automatic face detection and smart cropping
* Adjustable pixel size and color depth
* Retro color palette support (GameBoy and NES styles)
* Download generated character as PNG
* Clean and user-friendly interface

## Tech Stack
**Frontend**
* HTML
* CSS
* JavaScript

**Backend**
* Python
* Flask

**Image Processing**
* Pillow
* OpenCV
* NumPy

## How It Works

1. The user uploads an image through the web interface.
2. The backend detects the face and crops the image into a square format.
3. The image is resized and processed using pixelation techniques.
4. Optional retro color palettes are applied.
5. The final pixel character is rendered on the canvas and made available for download.


## Installation and Local Setup

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open your browser and visit:
```
http://127.0.0.1:5000
```

## Live Demo
https://retro-pixel-character-maker.onrender.com/

## Future Enhancements

* Live preview while adjusting pixel size and palette
* Sprite animation generation (idle and walking frames)
* Support for multiple face detection
* Improved UI and mobile responsiveness
* Performance optimization for faster image processing

## Author
**Rushil Goyal**
