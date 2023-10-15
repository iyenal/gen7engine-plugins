
import math

# Complex Visual Programming: Lists!

# we put here our variables used by both start and update
list2 = []

deg = 0
camx = 0
camz = 2

def start():

  # setCamera(0,2,4,27,0,0)
  # creating all our objects
  createAssetModel("fire", "scene.obj")
  # createAssetPlane("cube")
  # setObject("002-1-2", 0, 0, 0)
  moveObjectwithRotationScale("Material.001", 0,0,0,0,0,0,0,0,0)
  # createObjectwithRotationScale("player", "cube", 0, 0, -9, 20, 45, 0, 0.1, 0.1, 0.1)
  # createSprite('bgs','bg',0,0,640,480,(-1))
  # createSprite('bob','bobsprite',100,200,100,100,0)

def orbitAroundPoint(ox, oy, dist, deg):
  global camx
  global camz
  # x and z to orbit
  px = camx
  pz = camz
  rad = math.radians(deg)
  qx = ox + math.cos(rad) * (px - ox) - math.sin(rad) * (pz - oy)
  qz = oy + math.sin(rad) * (px - ox) + math.cos(rad) * (pz - oy)
  setCamera(qx, 2, qz, 35, deg, 0)

player_name = "Material.001"

def update():
  global player_name
  global deg
  global camx
  global camz

  # check input
  if (isButtonRight()):
    # createLog("R")
    rad = math.radians(-getObjectRY(player_name))
    d = 0.01
    nx = (d * math.cos(rad))
    ny = (d * math.sin(rad))
    moveObjectwithRotationScale(player_name, nx,0,ny, 0,0,0,0,0,0)
    moveCamera(nx,0, ny, 0,0,0)
    camx += nx
    camz += ny

  if (isButtonLeft()):
    #createLog("L")
    rad = math.radians(-getObjectRY(player_name)+180)
    d = 0.01
    nx = (d * math.cos(rad))
    ny = (d * math.sin(rad))
    moveObjectwithRotationScale(player_name, nx,0,ny, 0,0,0,0,0,0)
    moveCamera(nx,0, ny, 0,0,0)
    camx += nx
    camz += ny

  if (isButtonDown()):
    #createLog("U")
    rad = math.radians(-getObjectRY(player_name)+90)
    d = 0.01
    nx = (d * math.cos(rad))
    ny = (d * math.sin(rad))
    moveObjectwithRotationScale(player_name, nx,0,ny, 0,0,0,0,0,0)
    moveCamera(nx,0, ny, 0,0,0)
    camx += nx
    camz += ny

  if (isButtonUp()):
    #createLog("D")
    #moveObjectwithRotationScale(player_name, 0,0, -0.1, 0,0,0,0,0,0)
    #moveCamera(0,0, -0.1, 0,0,0)

    rad = math.radians(-getObjectRY(player_name)-90)
    d = 0.01
    nx = (d * math.cos(rad))
    ny = (d * math.sin(rad))
    moveObjectwithRotationScale(player_name, nx,0,ny, 0,0,0,0,0,0)
    moveCamera(nx,0, ny, 0,0,0)
    camx += nx
    camz += ny

  if (isButtonX()):
    # createLog("T")
    moveObjectwithRotationScale(player_name, 0,0,0, 0,1,0, 0,0,0)
    orbitAroundPoint(getObjectPX(player_name), getObjectPZ(player_name), 3, -getObjectRY(player_name))

  if (isButtonY()):
    # createLog("B")
    moveObjectwithRotationScale(player_name, 0,0,0, 0,-1,0, 0,0,0)
    orbitAroundPoint(getObjectPX(player_name), getObjectPZ(player_name), 3, -getObjectRY(player_name))



