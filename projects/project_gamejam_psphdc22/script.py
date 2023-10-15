from engine import *
enableRenderTexture()
setCamera(0,0,0,0,0,0)

# This file is included in all local Gen7 Engine's setup builds
# Include here common code between projects, or code mandatory to plugins

# Your plugin Python code below




# Included plugins

def timeGetFPS():
    return 99

def showFPSScreen(text):
    createLog(str(text)+":"+str(timeGetFPS()))
    

import math
import urandom

# GameJam Entry

SCENE_STEP = -1
fps = 25 #25 PSP
setTargetFPS(40) # Rendering and script framerate
player_name = "Player"
TPVController = False

#various vars
time_diff = 0
boss = ["BossSkin","BossSkinPlus","BossMisc"]
cranes_unused = ["Crane.001","Crane.002","Crane.003","Crane.004","Crane.005","Crane.006", "Crane.007", "Crane.008"]
cranes_used = []

def setCameraLeg(x, y, z, a, b, c):
  # Transform the old camera pos/rot calculation to the new format (Blender norm)
  setCamera(x, y, z, -(b-90), -a, -c)


def start():

  #setCameraLeg(0,-2,2,21,0,0)
  # Scene Sand
  
  createAssetCube("cube")
  createAssetModel("title", "title.obj")

  createAssetTexture("sky","sky.png")
  createSprite("sky_sand", "sky", 0, 0, 640, 480, -1)
  disableObject("sky_sand")

  createAssetTexture("lives","lives.png")
  createSprite("lives", "lives", 30, 400, 128, 64, 0)
  disableObject("lives")

  createAssetTexture("msg1","msg1.png")
  createSprite("msg_box", "msg1", 0, 0, 640, 200, 1)
  disableObject("msg_box")

  # setCameraLeg(0,0,2,0,0,0)
  # setCameraLeg(x,y,z,90,0,0)

def orbitAroundPoint(ox, oy, deg):
  global SCENE_STEP
  global player_name

  # x and z to orbit
  px = getObjectPX(player_name)
  pz = getObjectPY(player_name)+3
  rad = math.radians(-deg-180)
  qx = ox + math.cos(rad) * (px - ox) - math.sin(rad) * (pz - oy)
  qz = oy + math.sin(rad) * (px - ox) + math.cos(rad) * (pz - oy)
  if(SCENE_STEP<2):
    setCameraLeg(qx, qz, 0, 25, 0, deg) #deg
  else:
    setCameraLeg(qx, qz, 2, 20, 0, deg) #deg

def updateTerrainSand():
  sin = math.sin(math.radians(((getObjectPY(player_name)*360)/80)+180))
  setObject(player_name, getObjectPX(player_name), getObjectPY(player_name),  sin*4)
  setCameraLeg(getCameraPX(),getCameraPY(), sin*4+3, 20,0,getCameraRZ())

def updateTerrainNight():
  player_x = getObjectPX(player_name)
  player_y = getObjectPY(player_name)

  # Upper zone
  if(player_y >= 14.6 and getObjectPZ(player_name)>0.5):
    setObject(player_name, getObjectPX(player_name), getObjectPY(player_name), 2.06)
    setCameraLeg(getCameraPX(),getCameraPY(), 2.06+2, 0,0,getCameraRZ())

  # Stairs
  elif(player_y > 10 and player_x > -6 and player_x < -3.4 and player_y < 14.6):
    pz = ((player_y-10)*2.06)/(14.6-10)
    setObject(player_name, getObjectPX(player_name), getObjectPY(player_name),  pz)
    setCameraLeg(getCameraPX(),getCameraPY(), pz+2, 0,0,getCameraRZ())

  # Below
  elif(player_y > 13 and getObjectPZ(player_name)<0.5):
    moveObjectwithRotationScale(player_name, 0,-0.01,0, 0,0,0, 0,0,0)



def getDistanceObj(obj1, obj2):
  return abs(abs(getObjectPX(obj2)-getObjectPX(obj1))+abs(getObjectPY(obj2)-getObjectPY(obj1)))

def update():
  global SCENE_STEP
  global player_name
  global TPVController
  global time_diff
  global cranes_unused
  global cranes_used

  speed = 0.01*fps

  if(TPVController):

    # check input
    if (isButtonRight()):
      # createLog("R")
      rad = math.radians(-getObjectRZ(player_name))
      nx = (speed * math.cos(rad))
      ny = (speed * math.sin(rad))
      moveObjectwithRotationScale(player_name, nx,ny,0, 0,0,0,0,0,0)

    if (isButtonLeft()):
      #createLog("L")
      rad = math.radians(-getObjectRZ(player_name)+180)
      nx = (speed * math.cos(rad))
      ny = (speed * math.sin(rad))
      moveObjectwithRotationScale(player_name, nx,ny,0, 0,0,0,0,0,0)
      # orbitAroundPoint(getObjectPX(player_name), getObjectPY(player_name), -getObjectRZ(player_name))

    if (isButtonDown()):
      #createLog("U")
      rad = math.radians(-getObjectRZ(player_name)-90)
      nx = (speed * math.cos(rad))
      ny = (speed * math.sin(rad))
      moveObjectwithRotationScale(player_name, nx,ny,0, 0,0,0,0,0,0)

    if (isButtonUp()):
      #createLog("U")
      rad = math.radians(getObjectRZ(player_name)+90)
      nx = (speed * math.cos(rad))
      ny = (speed * math.sin(rad))
      moveObjectwithRotationScale(player_name, nx,ny,0, 0,0,0,0,0,0)

    if (isButtonX()):
      # createLog("T")
      moveObjectwithRotationScale(player_name, 0,0,0, 0,0,speed*10, 0,0,0)

    if (isButtonY()):
      # createLog("B")
      moveObjectwithRotationScale(player_name, 0,0,0, 0,0,-speed*10, 0,0,0)

    orbitAroundPoint(getObjectPX(player_name), getObjectPY(player_name), -getObjectRZ(player_name))

  # -------------- SCENE MANAGEMENT --------------------

  if(SCENE_STEP == -1):

    if(isTriggerA()):
      createAssetModel("fire", "scene.obj")
      createObjectwithRotationScale("coll_camel", "cube", -2.4, 20, -3.5, 0, 0, 0, 1, 1, 0.15)
      createObjectwithRotationScale("coll_tornado", "cube", -0.5, 94, -2.7, 0, 0, 0, 3, 3, 0.15)
      hideObject("coll_camel")
      hideObject("coll_tornado")
      enableObject("sky_sand")
      TPVController = True
      SCENE_STEP = 0


  if(SCENE_STEP < 2):
    updateTerrainSand()

  if(SCENE_STEP == 0):
    enableObject("lives")
    if(isCollisionBox(player_name, "coll_camel")):
      setCameraLeg(-5,19,-2,21,0,66)
      TPVController = False
      enableObject("msg_box")

      if(isTriggerA()):
        disableObject("msg_box")
        TPVController = True
        SCENE_STEP = 1

  if((SCENE_STEP == 1) and isCollisionBox(player_name, "coll_tornado")):
    SCENE_STEP = 2






  if(SCENE_STEP == 2):
    TPVController = True
    enableObject("lives")
    # Reset player position and setup new scene
    createAssetTexture("sky_night","sky_night.png")
    updateSprite("sky_sand","sky_night")
    createAssetModel("sand","night.obj")

    setObjectwithRotationScale(player_name, 0,0,0, 0,0,0,0,0,0)
    setCameraLeg(0,-2,2,12,0,0)
    createObjectwithRotationScale("coll_nightdoor", "cube", -4.65, 23.75, 1.75, 0, 0, 0, 1, 1, 2)
    setObjectwithRotationScale("Ghost_White", -0.56, 2.9, 0.93, 0,0,20, 0,0,0)
    hideObject("coll_nightdoor")
    SCENE_STEP = 3

  if(SCENE_STEP == 3):
    # print("dist: " + str(getDistanceObj(player_name, "Ghost White")))
    if(getDistanceObj(player_name, "Ghost_White") < 1.2):
      SCENE_STEP = 4
  
  if(SCENE_STEP == 4):
    TPVController = False
    moveObjectwithRotationScale(player_name, -0.7,-0.2,0, 0,0,0, 0,0,0)
    setCameraLeg(1,1.5,1,7,0,-70)
    createAssetTexture("msg2","msg2.png")
    enableObject("msg_box")
    updateSprite("msg_box","msg2")
    SCENE_STEP = 5

  if(SCENE_STEP == 5 and isTriggerA()):
    disableObject("msg_box")
    setObject("Ghost_White", 5.7, 4, 1)
    TPVController = True
    SCENE_STEP = 6

  # Three locations: (-3.5, 7), (2.5, 10.5), (5.7, 4)

  if(SCENE_STEP == 6):
    #print(str(timeSinceStartup()))

    time_trigger = timeSinceStartup()
    if(time_trigger%2 == 0 and time_diff != time_trigger):
      loc = urandom.randrange(0, 3, 1)
      if(loc == 0):
        setObject("Ghost_White", -3.5, 7, 1)
      elif(loc == 1):
        setObject("Ghost_White", 2.5, 10.5, 1)
      else:
        setObject("Ghost_White", 5.7, 4, 1)
      time_diff = time_trigger

    if(getDistanceObj(player_name, "Ghost_White") < 0.6):
      # createLog ow you already found me...
      # okay, here's my boss
      createAssetTexture("msg3","msg3.png")
      enableObject("msg_box")
      updateSprite("msg_box","msg3")
      TPVController = False
      setCameraLeg(getObjectPX("Ghost_White")+1.3,getObjectPY("Ghost_White")-1,1.2,7,0,-70)
      setObjectwithRotationScale(player_name, getObjectPX("Ghost_White")-0.5,getObjectPY("Ghost_White")-1,0, 0,0,0, 0,0,0)
      SCENE_STEP = 7

  if(SCENE_STEP == 7 and isTriggerA()):
    disableObject("msg_box")
    SCENE_STEP = 8

  if(SCENE_STEP == 8):
    TPVController = True
    updateTerrainNight()

    if(isCollisionBox(player_name, "coll_nightdoor")):
      TPVController = False
      SCENE_STEP = 9









  if(SCENE_STEP == 9):
    TPVController = False
    enableObject("lives")
    createAssetModel("boss", "boss.obj")
    # Hide unused cranes
    for cranes in cranes_unused:
      setObjectwithRotationScale(cranes, 0,-10,0, 0,0,0, 0,0,0)
    # Set position boss
    for boss_ in boss:
      setObjectwithRotationScale(boss_, 0,17,2, 0,0,0, 0,0,0)
    setObjectwithRotationScale(player_name, 0,0,0, 0,0,0,0,0,0)
    #setCameraLeg(0,-2.5,2,12,0,0)

    createAssetTexture("msg4","msg4.png")
    enableObject("msg_box")
    updateSprite("msg_box","msg4")
    setCameraLeg(-2,6.5,4,5,0,15)
    SCENE_STEP = 10

  if(SCENE_STEP == 10):
    if(isTriggerA()):
      disableObject("msg_box")
      setCameraLeg(0,-2.5,2,12,0,0)
      SCENE_STEP = 11


  if(SCENE_STEP == 11):

    #----------- ENEMY GENERATION ---------------
    time_trigger = timeSinceStartup()
    spawn_len = 1
    
    if(time_trigger%spawn_len == 0 and time_diff != time_trigger):
  
      # Spawn cranes
      if(len(cranes_unused) > 0):
        crane_spawn = cranes_unused.pop()
        #print("spawn "+crane_spawn)

        spawn_cr = urandom.randrange(-2, 3, 2)

        for boss_ in boss:
          setObjectwithRotationScale(boss_, spawn_cr,getObjectPY(boss_),getObjectPZ(boss_), 0,0,0, 0,0,0)

        setObjectwithRotationScale(crane_spawn, spawn_cr,getObjectPY("BossSkin")-5,0.4, 0,0,0,0,0,0)
        cranes_used.insert(0, crane_spawn)
      
    time_diff = time_trigger
    
    # -------- Move and remove cranes ---------------
    for crane in cranes_used:

      # Remove because too far
      if(getObjectPY(crane) < getObjectPY(player_name)-2):
        # put it in cranes unused
        moveObjectwithRotationScale(crane, 0, -100 ,0, 0,0,0, 0,0,0)
        cranes_unused.insert(0, crane)
        cranes_used.remove(crane)
        continue

      # Remove because hurt
      if( abs(getObjectPX(crane)-getObjectPX(player_name))<0.1 and abs(getObjectPY(crane)-getObjectPY(player_name))<0.1):
        # Awww got hurt
        moveObjectwithRotationScale(player_name, 0, -2 ,0, 0,0,0, 0,0,0)
        moveCamera(0, -2, 0, 0,0,0)
        # Remove crane
        moveObjectwithRotationScale(crane, 0, -100 ,0, 0,0,0, 0,0,0)
        cranes_unused.insert(0, crane)
        cranes_used.remove(crane)
        continue

      moveObjectwithRotationScale(crane, 0, -speed ,0, 0,0,0, 0,0,0)

    # Move player towards boss
    moveObjectwithRotationScale(player_name, 0, speed*1.1, 0, 0,0,0, 0,0,0)
    moveCamera(0, speed*1.1, 0, 0,0,0)
    # Move boss
    for boss_ in boss:
      moveObjectwithRotationScale(boss_, 0, speed, 0, 0,0,0, 0,0,0)

    # Control Player
    if(isTriggerRight()):
      moveObjectwithRotationScale(player_name, 2,0,0, 0,0,0, 0,0,0)
      if(getObjectPX(player_name)>2):
        setObjectwithRotationScale(player_name, 2,getObjectPY(player_name),getObjectPZ(player_name), 0,0,0, 0,0,0)
    if(isTriggerLeft()):
      moveObjectwithRotationScale(player_name, -2,0,0, 0,0,0, 0,0,0)
      if(getObjectPX(player_name)>2):
        setObjectwithRotationScale(player_name, -2,getObjectPY(player_name),getObjectPZ(player_name), 0,0,0, 0,0,0)

    if(getDistanceObj(player_name, boss[0])<7):
      SCENE_STEP=12


  if(SCENE_STEP == 12):
    disableObject("lives")
    setCameraLeg(-2,6.5+(getObjectPY(boss[0])-17),4+getObjectPZ(boss[0]),5,0,15)
    createAssetTexture("msg5","msg5.png")
    enableObject("msg_box")
    updateSprite("msg_box","msg5")
    SCENE_STEP = 13








