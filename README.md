# AA-treasure-map
Hello all this is a private repository for privileged OnlyFans members only. Normies, Pride, CMB can kindly fuck off.

## Instructions
### Pre-requisites
This application is optimized for Windows only.
You will also need to install python which can be found at https://www.python.org/downloads/

### Installing
Press the green "Code" button on the top right of this page and then click "Download ZIP"
Unzip the file anywhere on your computer

### Using the map
In the root directory, simply double click on index.html to open the map application
There are three ways to add markers:
* You can input the coordinates directly using the textboxes at the top of the web application
* You can right click on the map to directly place a marker on your cursor
* You can create bulk number of markers by editing the json_markers.json. Read the README inside the json_markers.json to understand the format you have to input coordinates in

### Using the coordinates auto-capturing script
To use the coordinates capturing script, you need to further install the python dependencies for it.

You need to do the following installation steps only once:
1. Open your command prompt (type "CMD" into the search box")
1. Change your current directory to the place where you unzipped the .zip file and then inside coordsgen using "cd <path\to\your\unzippedfolder\coordsgen>"
1. Type "py -m pip install --user virtualenv" to install virtual environment
1. Type "py -m venv venv" to create the virtual environment
1. Once done type "venv\Scripts\activate"
1. Type "pip3 install -r requirements.txt". Make sure you have a internet connection.
1. You also need to install tesserract at https://github.com/UB-Mannheim/tesseract/wiki, you can install this to the same directory as this application
1. Open main.py with notepad, change pt.pytesseract.tesseract_cmd = r'C:\Users\User\Desktop\GitRepos\tesseract\tesseract.exe'to pt.pytesseract.tesseract_cmd = r'<path\to\where\you\installed\tesseract\tesseract.exe'
1. You can also change your delay between captures.

To run the auto capturing script (after you install):
1. Make sure your Archeage is on full-screen and it is on monitor 1
1. Change your current directory to the place where you unzipped the .zip file and then inside coordsgen using "cd <path\to\your\unzippedfolder\coordsgen>"
1. Type "venv\Scripts\activate"
1. Type "python main.py"
1. Now it should be capturing your screen on monitor 1, switch to Archeage and start hovering over the treasure maps in your inventory. If it successfully captures a coordinate, you should hear a "Ding" sound. For best accuracy, use the script while in Ahnimar.
1. Once you're done with capturing the coordinates of all your maps, go to the command prompt and hold Ctrl+F to stop capturing
1. Look into the output subdirectory to retrieve the .json file. Rename it to json_markers.json and replace the copy in the root directory. Next, simply open index.html and click on "Mark from JSON"
