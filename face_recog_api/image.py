import os

# Specify the directory containing the image files
image_directory = "./photos"

# List all files in the directory
all_files = os.listdir(image_directory)

# Filter for image files (e.g., .jpg, .png, .jpeg)
image_files = [filename for filename in all_files if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', '.bmp'))]


