### Reference - 


### Commands - 
1. Create Dev Work Space
2. Import/Clone project from GIT - <link>
3. Open Command Pallete
    1. Set Runtime  - ">Runtime: Set Default"
    2. Create Python Environment - ">Python: Create Environment" - **Select ~/.asdf-inst/shims/python3**
    3. If you have already created the Python environment. Then select interpreter - ">Python: Select Interpreter" - then select Python virtual environment. **For example - Python 3.11.9 .venv**

4. Every time you open workspace you might have to activate the virtual environment with the help of command - **source /home/user/projects/certification_hub/.venv/bin/activate**

### Debugging - 
1. To check the logg, use command - **cf logs certification_hub --recent**


### Important files - 
1. **manifest.yml** - This is required for BTP deployment. Minimum specifications to run the app on cloud foundary.
2. **Procfile** - Target python application
3. **runtime.txt** - Target python version
4. **requirements.txt** - Necessary python packages
5. **.cfignore** - ".venv" is unnecessary to run cf app, so list up the directory.
6. **.gitignore** - To ignore files from git commit
7. **requests.http** - This file contains the sample requests to test the APIs
