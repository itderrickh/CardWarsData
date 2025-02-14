from PIL import Image
import os

# Set folder path (change this to your directory)
folder_path = "../images"
output_path = '../images/xsmall'

# Ensure output directory exists
os.makedirs(folder_path, exist_ok=True)

# Process each PNG file in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith(".png"):
        img_path = os.path.join(folder_path, filename)
        
        with Image.open(img_path) as img:
            # Convert to 8-bit (reduce color depth) to reduce size
            img = img.convert("P", palette=Image.ADAPTIVE, colors=256)

            # Save optimized PNG
            output_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}-small.png")
            img.save(output_path, "PNG", optimize=True)
            
            print(f"Compressed: {filename} -> {output_path}")

print("✅ Compression complete!")