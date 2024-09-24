import os
from PIL import Image

# Define the directory containing the images
image_directory = 'images'

# Function to resize images
def resize_images():
    # Get a list of all files in the image directory
    files = os.listdir(image_directory)
    
    # Filter out non-image files
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    # Check if there are images to resize
    if not image_files:
        print("No images found in the directory.")
        return
    
    # Inform the user about the images found
    print(f"Found {len(image_files)} images: {', '.join(image_files)}")
    
    # Ask for user confirmation
    confirm = input("Do you want to resize these images to 450x198 and replace the originals? (yes/no): ")
    
    if confirm.lower() != 'yes':
        print("Operation canceled.")
        return
    
    # Resize each image and save it
    for image_file in image_files:
        image_path = os.path.join(image_directory, image_file)
        
        # Open the image
        with Image.open(image_path) as img:
            # Resize using nearest neighbor
            resized_img = img.resize((450, 198), Image.NEAREST)
            
            # Save the resized image, replacing the original
            resized_img.save(image_path)
            print(f"Resized and replaced: {image_file}")

if __name__ == "__main__":
    resize_images()
