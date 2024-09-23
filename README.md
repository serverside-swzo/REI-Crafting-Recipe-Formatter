# Image Processor for Roughly Enough Items

This script is designed to process images from the Roughly Enough Items mod, specifically targeting the export crafting recipe function. It removes extra parts from the images to ensure a more uniform and tidy appearance while minimizing the footprint of the images.

## Features

- Removes specified columns from images:
  - Columns **12-42** and **409-441** are removed.
  - Remaining columns are stitched together to create a clean output.
  - The following regions are kept:
    - **Left part:** Columns **0-11**
    - **Middle part:** Columns **43-408**
    - **Right part:** Columns **442-448**
- Processes all images in the `images` subfolder and saves the processed images to the `output` subfolder.

## Example

- **Input Image:**
  
  ![Input Image](https://imgur.com/Qdsdoii.png)
  
  *An image of size 450x198 with unwanted columns between 12-42 and 409-441.*

- **Output Image:**
  
  ![Output Image](https://imgur.com/HWkOpKX.png)
  
  *The processed image will retain columns 0-11, 43-408, and 442-448, resulting in a cleaner appearance.*


## Important!!
- Ensure that the input **images are of size 450x198**; otherwise, the script will skip them and print an error message.
- The **Minecraft GUI scale needs to be set to 3x** for it to work properly!!!!! and this will automattically acheive the **450x198** dimensions when exporting


## Requirements

- Python 3.x
- Pillow library

### Installation

1. Make sure you have Python installed. If not, download it from [python.org](https://www.python.org/downloads/).
2. Install the Pillow library using pip:
   ```bash
   pip install pillow
   
## Usuage
1. Create a folder structure as follows:
	```image_processor/
	├── images/
	│   └── (your input images here)
	├── output/
	│   └── (processed images will be saved here)
	└── process_images.py
3. Place your images in the `images` folder.

4. Run the script

## Note
- If you need any further adjustments or additional information, just let me know!
- I made this for my modrinth mods to simplify the documentation process


## License
 MIT do whatever u want with it i dont care
 
