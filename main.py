import os
import re


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def move_and_rename(source_folder, destination_folder_base, name):
  """
  Moves files from source_folder to subfolders within destination_folder_base
  based on density information in the filename and renames them to "cool.png".

  Args:
    source_folder: Path to the folder containing the files to move.
    destination_folder_base: Base path for the destination folders.
  """
  for filename in os.listdir(source_folder):
    # Check for .png extension
    if not filename.endswith(".png"):
        continue

    # Extract density information from filename
    match = re.search(r"@(\d+\.?\d*)x", filename)
    density = match.group(1) if match else None
    if density is None:
        density = "mdpi"
    if density == "1.5":
        density = "hdpi"
    elif density == "2":
        density = "xhdpi"
    elif density == "3":
        density = "xxhdpi"
    elif density == "4":
        density = "xxxhdpi"
    # Determine destination folder based on density
    destination_folder = os.path.join(destination_folder_base, f"drawable-{density}" if density else "drawable")

    # Create destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Move and rename file
    source_path = os.path.join(source_folder, filename)
    destination_path = os.path.join(destination_folder, name)
    os.rename(source_path, destination_path)
    print(f"Moved '{filename}' to '{destination_folder}' and renamed to {name}")

# Replace with your actual source and destination folder paths
source_folder = r"C:\Users\hti00036\Desktop\AHMI"
destination_folder_base = r"C:\Users\hti00036\Desktop\AHMI"
name = "error1.png"

move_and_rename(source_folder, destination_folder_base, name)
