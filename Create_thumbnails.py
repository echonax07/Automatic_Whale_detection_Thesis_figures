import os
from PIL import Image

# Paths
input_folder = 'imgs'
output_folder = 'imgs_low_res'

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Open an image file
        with Image.open(os.path.join(input_folder, filename)) as img:
            # Calculate new size
            new_width = int(img.width * 0.10)
            new_height = int(img.height * 0.10)
            new_size = (new_width, new_height)
            
            # Resize image
            img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Save the resized image
            img_resized.save(os.path.join(output_folder, filename))

print("Resizing complete!")
