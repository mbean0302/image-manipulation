# IMPORTS
from PIL import Image
import os
import time
import sys

# GLOBAL VARIABLES
image_folder = 'JPG_Images/'
new_image_folder = 'PNG_Images/'

# CHECK / CREATE DIRECTORIES
try:
    if not os.path.exists(image_folder):
        os.mkdir(image_folder)
    if not os.path.exists(new_image_folder):
        os.mkdir(new_image_folder)
except FileNotFoundError as err:
    print('Please enter an EXISTING file for first argument.')
    print(f'File Not Found. {err}')

# DRAG AND DROP JPG FILES
print('Place the .JPG images you want to convert into the JPG_Images folder...')
time.sleep(.850)
os.startfile('JPG_Images')

# CONVERT CONFIRM
try:
    input('Press [ENTER] to convert files.')
except SyntaxError as syntax_err:
    print(f'Syntax Error: {syntax_err}')

# CHECK IF JPG AND IF ALREADY EXISTS
for img_file in os.listdir(image_folder):
    if img_file.endswith(".jpg"):
        if not os.path.exists(f'{img_file}'):
            # CONVERT THE FILE AND SAVE IN NEW DIRECTORY, IF PASSES ABOVE CHECKS
            if not os.path.exists(new_image_folder + img_file[0:-3] + 'png'):
                jpg_img = Image.open(image_folder + img_file)
                clean_name = os.path.splitext(img_file)[0]
                jpg_img.save(new_image_folder + clean_name + '.png', 'png')
                print('File Converted from JPG to PNG.')
            else:
                print('File already converted to PNG')
        else:
            # CHECKS FOR ANY JPG FILES IN CONVERTED IMAGE FOLDER
            print(f'File already exists in {new_image_folder} as a JPG. Move file to {image_folder} and then '
                  f'convert.')
time.sleep(.600)

# OPENS EXPLORER WINDOW TO SHOW NEWLY CONVERTED FILES
try:
    input('Press [ENTER] to display converted files.')
except SyntaxError as syntax_err:
    print(f'Syntax Error: {syntax_err}')
os.startfile('PNG_Images')
time.sleep(.850)

# OPTION TO DELETE ORIGINAL JPG FILES
check_delete = str.upper(input('Do you want to delete original JPG files? [Y/N]:  '))
if check_delete == 'Y':
    for img_file in os.listdir(image_folder):
        file_path = os.path.join(image_folder, img_file)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
        except Exception as except_err:
            print('Failed to delete %s. Reason: %s' % (file_path, except_err))
    input('Files deleted. Press [ENTER] to close program.')
    sys.exit()
if check_delete == 'N':
    time.sleep(.650)
    input('Press [ENTER] to close program.')
    sys.exit()
# END PROGRAM
