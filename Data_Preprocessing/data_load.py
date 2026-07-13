
import os 
import sys
from pathlib import Path

# Add the parent folder of the current notebook/script to Python's search path.
# This allows Python to find modules (e.g., build_data.py) located one level above.
sys.path.append(str(Path.cwd().parent))

import build_data  # Import the module from the parent folder

BASE_DIR = build_data.new_path()  # Call the function from build_data.py


train_dir = os.path.join(BASE_DIR, "train")
validation_dir = os.path.join(BASE_DIR, "validation")

# dir with train cat picutre
train_cats_dir = os.path.join(train_dir, "cats")
# dir with train dog picutre
train_dogs_dir = os.path.join(train_dir, "dogs")

# dir with validation cat picture 
validation_cats_dir = os.path.join(validation_dir, "cats")

# dir with validation dog picture 
validation_dogs_dir = os.path.join(validation_dir, "dogs")

print(f"Contents of base directory: {os.listdir(BASE_DIR)}")

print(f"\nContents of train directory: {os.listdir(train_dir)}")

print(f"\nContents of validation directory: {os.listdir(validation_dir)}")


