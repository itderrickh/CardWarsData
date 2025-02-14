from PIL import Image
import os

# Set folder path (change this to your directory)
folder_path = "../images/regular"
output_folder = "../images/xsmall"

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# Process each PNG file in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(folder_path, filename)
        output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.png")

        with Image.open(img_path) as img:
            # Reduce image size (scale down by 50% for example)
            img = img.resize((img.width // 2, img.height // 2), Image.LANCZOS)

            # Convert to 8-bit and reduce colors (e.g., 128 instead of 256)
            img = img.convert("P", palette=Image.ADAPTIVE, colors=128)

            # Remove alpha channel if present
            if img.mode == "RGBA":
                img = img.convert("RGB")

            # Save optimized PNG
            img.save(output_path, "PNG", optimize=True)
            
            print(f"Compressed: {filename} -> {output_path}")

print("✅ Compression complete!")