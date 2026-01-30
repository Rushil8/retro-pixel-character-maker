window.addEventListener("DOMContentLoaded", () => {

    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d");

    const generateBtn = document.getElementById("generateBtn");
    const downloadBtn = document.getElementById("downloadBtn");

    // 🔴 SAFETY CHECK
    if (!downloadBtn) {
        alert("Download button not found (ID mismatch)");
        return;
    }

    generateBtn.addEventListener("click", generate);
    downloadBtn.addEventListener("click", downloadImage);

    async function generate() {
        console.log("Generate clicked");

        const fileInput = document.getElementById("upload");
        if (!fileInput || !fileInput.files.length) {
            alert("Please select an image");
            return;
        }

        // Always disable before generating
        downloadBtn.disabled = true;

        const data = new FormData();
        data.append("image", fileInput.files[0]);
        data.append("pixel", document.getElementById("pixel").value);
        data.append("palette", document.getElementById("palette").value);
        data.append("paletteType", "default"); // safe

        const response = await fetch("/api/pixelate", {
            method: "POST",
            body: data
        });

        if (!response.ok) {
            alert("Server error");
            return;
        }

        const blob = await response.blob();
        const img = new Image();

        img.onload = () => {
            console.log("Image loaded");

            canvas.width = img.width;
            canvas.height = img.height;

            ctx.imageSmoothingEnabled = false;
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(img, 0, 0);

            // ✅ FORCE ENABLE HERE
            downloadBtn.disabled = false;
            console.log("Download enabled");
        };

        img.src = URL.createObjectURL(blob);
    }

    function downloadImage() {
        if (downloadBtn.disabled) {
            alert("Download still disabled");
            return;
        }

        if (canvas.width === 0 || canvas.height === 0) {
            alert("No image to download");
            return;
        }

        const link = document.createElement("a");
        link.download = "pixel_character.png";
        link.href = canvas.toDataURL("image/png");

        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
});
