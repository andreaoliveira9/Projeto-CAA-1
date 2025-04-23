import os
import shutil

# Define the path to the dataset
original_path = "dataset_original/Garbage classification/Garbage classification"

# Define the categories
categories = os.listdir(original_path)

# Create a new directory to store the organized dataset
new_path_test = "dataset_organized/test/"
new_path_train = "dataset_organized/train/"
new_path_validation = "dataset_organized/validation/"

# Create the new directories if they don't exist
os.makedirs(new_path_test, exist_ok=True)
os.makedirs(new_path_train, exist_ok=True)
os.makedirs(new_path_validation, exist_ok=True)

# Create the subdirectories for each category
for category in categories:
    os.makedirs(os.path.join(new_path_test, category), exist_ok=True)
    os.makedirs(os.path.join(new_path_train, category), exist_ok=True)
    os.makedirs(os.path.join(new_path_validation, category), exist_ok=True)

# Map category numbers to names
categories = {
    1: "glass",
    2: "paper",
    3: "cardboard",
    4: "plastic",
    5: "metal",
    6: "trash",
}

# Define paths to the text files
txt_test_path = "dataset_original/one-indexed-files-notrash_test.txt"
txt_train_path = "dataset_original/one-indexed-files-notrash_train.txt"
txt_validation_path = "dataset_original/one-indexed-files-notrash_val.txt"


# Helper function to copy files based on a split
def copy_files(txt_path, split_path):
    with open(txt_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.split()
            file_name = line[0]
            category = int(line[1])
            src = os.path.join(original_path, categories[category], file_name)
            dst = os.path.join(split_path, categories[category], file_name)
            shutil.copy(src, dst)


# Copy files to test, train, and validation folders
copy_files(txt_test_path, new_path_test)
copy_files(txt_train_path, new_path_train)
copy_files(txt_validation_path, new_path_validation)
