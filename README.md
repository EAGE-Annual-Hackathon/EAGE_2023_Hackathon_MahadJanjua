# Introduction 

The **File Conversion Tool** is a Python-based tool to convert all .doc, .xls, and .ppt files into their respective .docx, .xlsx, and .pptx versions within a specified main directory.

Developed by: [Mahad Nadeem Janjua](mahad-nadeem.janjua@wintershalldea.com) (mahad-nadeem.janjua@wintershalldea.com)

### How it works: 
- The user defines variables for **path** (main directory), **old_file_dir_name** (name of folder for old files to be moved to), **only_file_count** (either set to True or False)
- The engine walks through all sub-directories within the specified main directory.
- If **only_file_count** is True, only a count of all files that ***can*** be converted will be provided.
- Otherwise, **only_file_count** is not True:
    - All specified file types (.ppt, .doc, .xls) within the main directory are converted to their corresponding formats (.pptx, .docx, .xlsx) in the same (sub-)directory as the original.
    - Additionally, the original .ppt, .doc, .xls files are then moved to a new folder (name can be defined by user) which is created in the same directory as where the file(s) are found. 

**Example**: file sample.doc found in /this/is/a/random/path/sample.doc will be moved to /this/is/a/random/path/old_files_folder/sample.doc, where old_files_folder is the name assumed given by the user. The converted file sample.docx will be found in /this/is/a/random/path/sample.docx, the same path as the original file.

--------------------------------------
-------------------------------------

# Requirements
- Recommended Python version 3.10.8
- Packages listed in requirements.txt file
    - xls2xlsx
    - openpyxl
    - python-docx
    - python-pptx

-------------------------------------
--------------------------------------

# Getting Started
- Create a virtual environment to localize Python package installations using the ``python -m venv .venv`` terminal command (**.venv** in this case is the name given to the virtual environment folder)
- Activate the virtual environment using the terminal command ``source .venv/bin/activate`` (for Mac) or ``.venv\Scripts\activate.bat`` (for Windows)
- With your virtual environment activated, install packages using ``pip install -r requirements.txt`` command in terminal 
- Define variables in code:
    - path (string input)
    - old_file_dir_name (string input)
    - only_file_count (boolean input - should be either True or False)  
- Run code using ``python file_conversion_tool.py`` command in terminal

--------------------------------------
--------------------------------------

# Feedback

In case you would like to ask questions, suggest improvements, or place your queries, please contact [Mahad Nadeem Janjua](mahad-nadeem.janjua@wintershalldea.com) (mahad-nadeem.janjua@wintershalldea.com)