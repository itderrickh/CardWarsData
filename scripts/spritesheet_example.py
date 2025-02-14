import os
import glob
from PIL import Image

def create_spritesheet(image_folder, output_image, output_css, sprite_width, sprite_height, max_columns=10):
    images = sorted(glob.glob(os.path.join(image_folder, "*.*")))[:1000]  # Limit to 1000 files
    
    if not images:
        print("No images found in the folder.")
        return
    
    num_images = len(images)
    columns = min(num_images, max_columns)
    rows = (num_images + columns - 1) // columns  # Round up division
    
    sheet_width = columns * sprite_width
    sheet_height = rows * sprite_height
    
    spritesheet = Image.new("RGBA", (sheet_width, sheet_height))
    css_rules = []
    
    for index, image_path in enumerate(images):
        img = Image.open(image_path).convert("RGBA")
        img = img.resize((sprite_width, sprite_height), Image.LANCZOS)
        
        col = index % columns
        row = index // columns
        x_offset = col * sprite_width
        y_offset = row * sprite_height
        
        spritesheet.paste(img, (x_offset, y_offset))
        
        class_name = os.path.splitext(os.path.basename(image_path))[0]
        css_rules.append(f".{class_name} {{ background: url('{output_image}') -{x_offset}px -{y_offset}px; width: {sprite_width}px; height: {sprite_height}px; }}")
    
    spritesheet.save(output_image)
    
    with open(output_css, "w") as css_file:
        css_file.write("\n".join(css_rules))
    
    print(f"Spritesheet saved as {output_image}")
    print(f"CSS file saved as {output_css}")

# Example usage
create_spritesheet(
    image_folder="data/images",  # Folder containing images
    output_image="spritesheet.png",  # Output spritesheet
    output_css="spritesheet.css",  # Output CSS file
    sprite_width=370,  # Width of each sprite
    sprite_height=516,  # Height of each sprite
    max_columns=10  # Max columns in the spritesheet
)
