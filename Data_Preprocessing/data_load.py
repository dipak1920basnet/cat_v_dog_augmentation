import os 
import sys
from pathlib import Path

# Directory containing data_load.py
CURRENT_DIR = Path(__file__).resolve().parent

# Go up two levels to ug_lab
PROJECT_ROOT = CURRENT_DIR.parent.parent

sys.path.insert(0, str(PROJECT_ROOT))

import build_data  # Import the module from the parent folder


class DataLoader:

    def __init__(self):

        self.BASE_DIR = build_data.new_path()  # Call the function from build_data.py
        self.train_dir = os.path.join(self.BASE_DIR, "train")
        self.validation_dir = os.path.join(self.BASE_DIR, "validation")

        # dir with train cat picutre
        self.train_cats_dir = os.path.join(self.train_dir, "cats")
        # dir with train dog picutre
        self.train_dogs_dir = os.path.join(self.train_dir, "dogs")

        # dir with validation cat picture 
        self.validation_cats_dir = os.path.join(self.validation_dir, "cats")

        # dir with validation dog picture 
        self.validation_dogs_dir = os.path.join(self.validation_dir, "dogs")

    def show(self):
        print(f"Contents of base directory: {os.listdir(self.BASE_DIR)}")
        print(f"\nContents of train directory: {os.listdir(self.train_dir)}")
        print(f"\nContents of validation directory: {os.listdir(self.validation_dir)}")

    def count_images(self):
        return {
            "train_cats": len(os.listdir(self.train_cats_dir)),
            "train_dogs": len(os.listdir(self.train_dogs_dir)),
            "validation_cats":len(os.listdir(self.validation_cats_dir)),
            "validation_dogs":len(os.listdir(self.validation_dogs_dir))
        }

