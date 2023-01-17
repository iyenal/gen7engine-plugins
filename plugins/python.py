
# This file is included in all local Gen7 Engine's setup builds
# Include here common code between projects, or code mandatory to plugins

# Your plugin Python code below




# Included plugins

def timeGetFPS():
    return 99

def showFPSScreen(text):
    createLog(str(text)+":"+str(timeGetFPS()))
    
