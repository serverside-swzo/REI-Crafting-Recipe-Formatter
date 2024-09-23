import os
from PIL import Image

def remove_columns_and_stitch(image_path, output_path):
    # Open the image
    img = Image.open(image_path)
    width, height = img.size

    # Check if the image is 450x198
    if width != 450 or height != 198:
        raise ValueError(f"The input image {image_path} must be 450x198 in size")

    # Define the regions to keep
    # Region 1: Left part (0 to 9)
    left_part = img.crop((0, 0, 12, height))  # Keep columns 0-9

    # Region 2: Middle part (43 to 408)
    middle_part = img.crop((45, 0, 408, height))  # Keep columns 43-408

    # Region 3: Right part (442 to 449)
    right_part = img.crop((442, 0, 449, height))  # Keep columns 442-449

    # Calculate the new width after removing the specified columns
    new_width = left_part.width + middle_part.width + right_part.width

    # Create a new blank image to stitch the parts together
    new_img = Image.new("RGBA", (new_width, height))

    # Paste the left, middle, and right parts together
    new_img.paste(left_part, (0, 0))
    new_img.paste(middle_part, (left_part.width, 0))
    new_img.paste(right_part, (left_part.width + middle_part.width, 0))

    # Save the new stitched image
    new_img.save(output_path)

def process_images(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through all files in the input folder
    for file_name in os.listdir(input_folder):
        # Construct the full file path
        file_path = os.path.join(input_folder, file_name)

        # Check if it's an image file
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                output_path = os.path.join(output_folder, file_name)
                remove_columns_and_stitch(file_path, output_path)
                print(f"Processed {file_name} and saved to {output_path}")
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

# Define input and output directories
input_folder = "images"
output_folder = "output"

# Run the image processing
process_images(input_folder, output_folder)
