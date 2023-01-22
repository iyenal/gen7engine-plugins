# This file is included in all local Gen7 Engine's setup builds
# Include here common code between projects, or code mandatory to plugins

import engine

# Your plugin Python code below




# Included plugins

def showFPSScreen(text):
    # Usage of Gen7 API: createLog for text display and timeGetFPS to get consolidated FPS
    createLog(str(text)+":"+str(timeGetFPS()))
    
