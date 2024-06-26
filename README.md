### Set up steps - 
1. Create Dev Work Space
2. Import/Clone project from GIT - https://github.tools.sap/genai-certification-2024/certification_hub.git
    1. Set Runtime  - ">Runtime: Set Default"
    2. Create Python Environment - ">Python: Create Environment" - **Select ~/.asdf-inst/shims/python3**
    3. If you have already created the Python environment. Then select interpreter - ">Python: Select Interpreter" - then select Python virtual environment. **For example - Python 3.11.9 .venv**
3. Update your OPEN API KEY in the .env file to run the app on your local. You can also create a file - .env.local in the resources folder and add OPEN API KEY in it.
4. Create .env.development file in the resources folder and add OPEN API KEY for development server in this file. This will be required to deploy the application on BTP.

4. Every time you open workspace you might have to activate the virtual environment with the help of command - **source /home/user/projects/certification_hub/.venv/bin/activate**

### Debugging - 
1. To run python app on local - python3 ./src/server.py
2. To debug on local - Open server.py and start in debug mode. 
    1. Add breakpoint in the controller.
    2. For local testing, a sample certification_material.pdf is added in ./data folder.
    2. Refer to the CURL command in the requests.http.
    3. Open another terminal and run the curl command.
2. To check the BTP logs, use command - **cf logs certification_hub --recent**

### Important files - 
1. **manifest.yml** - This is required for BTP deployment. Minimum specifications to run the app on cloud foundary.
2. **Procfile** - Target python application
3. **runtime.txt** - Target python version
4. **requirements.txt** - Necessary python packages
5. **.cfignore** - ".venv" is unnecessary to run cf app, so list up the directory.
6. **.gitignore** - To ignore files from git commit
7. **requests.http** - This file contains the sample requests to test the APIs

### Initial GIT commands
1. git init
2. git add README.md
3. git commit -m "first commit"
4. git branch -M main
5. git remote add origin https://github.tools.sap/genai-certification-2024/certification_hub.git
6. git push -u origin main 