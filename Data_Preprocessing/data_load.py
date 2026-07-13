import os 
import sys
from pathlib import Path

# Directory containing data_load.py
CURRENT_DIR = Path(__file__).resolve().parent

# Go up two levels to ug_lab
PROJECT_ROOT = CURRENT_DIR.parent.parent

sys.path.insert(0, str(PROJECT_ROOT))

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


if __name__ == "__main__":
    main()