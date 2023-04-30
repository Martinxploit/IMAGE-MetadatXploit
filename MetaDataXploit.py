import exifread
import tkinter as tk
from tkinter import filedialog


print("""
 
 __  __      _        _____        _       __   __      _       _ _   
|  \/  |    | |      |  __ \      | |      \ \ / /     | |     (_) |  
| \  / | ___| |_ __ _| |  | | __ _| |_ __ _ \ V / _ __ | | ___  _| |_ 
| |\/| |/ _ \ __/ _` | |  | |/ _` | __/ _` | > < | '_ \| |/ _ \| | __|
| |  | |  __/ || (_| | |__| | (_| | || (_| |/ . \| |_) | | (_) | | |_ 
|_|  |_|\___|\__\__,_|_____/ \__,_|\__\__,_/_/ \_\ .__/|_|\___/|_|\__|
                                                 | |                  
                                                 |_|                  
                   
Created By - https://github.com/Martinxploit
    """)





# Open dialog box to select image file
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

# Open image file for reading in binary mode
with open(file_path, 'rb') as f:

    # Return Exif tags
    tags = exifread.process_file(f)

    # Open text file for writing
    with open('MetaDataXploit.txt', 'w') as output:

        # Loop through tags and write to file
        for tag in tags.keys():
            if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                output.write(f"{tag}: {tags[tag]}\n")
