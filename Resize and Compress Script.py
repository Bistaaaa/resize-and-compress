import tinify
import os
from PIL import Image

# set your TinyPNG API key
tinify.key = "YOUR_API_KEY"

def resize_and_compress_image(input_path, output_path, width):
    with Image.open(input_path) as img:
        if img.size[0] > width:
            ratio = width / float(img.size[0])
            height = int(img.size[1] * ratio)
            img = img.resize((width, height), Image.LANCZOS)
        img.save(output_path, 'JPEG')

    # Use tinify to compress the image
    source = tinify.from_file(output_path)
    source.to_file(output_path)

input_directory = r'C:\Users\Administrator\Desktop\pics'
output_directory = r'C:\Users\Administrator\Desktop\pics\output'
width = 1500

os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(input_directory):
    if filename.lower().endswith(".jpeg"):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)
        print(f"Processing file {input_path} ...")
        resize_and_compress_image(input_path, output_path, width)
        print(f"Saved processed image to {output_path}")
