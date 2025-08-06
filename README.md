DOWNLOAD ABOVE :P 

-
-
-



1. Prerequisites: Python 3
Check if Python 3 is already installed


Open Terminal (⌘+Space → type “Terminal” → Enter).


Run:

python3 --version

If you see something like Python 3.x.x, you’re ready to go.


Installing Python 3 (if needed)


Install Homebrew if you don’t have it:






/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"


brew install python


Verify:

python3 --version


2. Prepare the Script
Download or copy the blind_czi.py code (provided above) into a plain-text file.


Save it as blind_czi.py in a folder alongside your .czi files.


If you’re using TextEdit, switch to Format → Make Plain Text before saving.


Make sure the filename ends with .py, not .txt.



3. Running the Script
A. Navigate to your folder
In Finder, locate the folder containing your .czi files
Drag that folder onto the open Terminal window.


Terminal will automatically insert the full path, e.g.:

cd /Users/you/Library/Mobile\ Documents/com~apple~CloudDocs/MyCZI_Folder
Press Enter to change into that directory.


B. (Optional) Make the script executable

chmod +x blind_czi.py

C. Run the script
If executable:

./blind_czi.py


Otherwise:

python3 blind_czi.py

4. What You’ll Get
blinding_key.csv – a two-column spreadsheet mapping each Original Filename → Blinded Filename


blinded_files.zip – a ZIP archive containing only the blinded copies of your .czi files


(If you’ve used the variant that zips originals instead, you’ll see unblinded_files.zip.)




