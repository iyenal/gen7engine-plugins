# Gen7 Engine's plugin for automatic exportation of collision cubes (in "Colliders" collection) to Gen7
# Licence: Public Domain (CC Zero)

import bpy

# generate camera: position accurate, FOV 80deg, 

collection = bpy.data.collections["Colliders"]

print("Exporting box colliders...")

collisionScript = 'createAssetCube("cube");\n'

for obj in collection.all_objects:
    print(obj.name)
    print(obj.location)
    print(obj.scale)
    
    px = str(round(obj.location.x,4))
    py = str(round(obj.location.y,4))
    pz = str(round(obj.location.z,4))
    sx = str(round(obj.scale.x,4))
    sy = str(round(obj.scale.y,4))
    sz = str(round(obj.scale.z,4))
    
    print(px+","+py+","+pz+","+sx+","+sy+","+sz)
    collisionScript+='createObjectwithScale("'+str(obj.name)+'", "cube",'+px+","+py+","+pz+","+sx+","+sy+","+sz+");\n"
    collisionScript+='addToCollision("'+str(obj.name)+'");\n'
    
print("\nUse this script to generate colliders for your scene:\n")

print(collisionScript)
bpy.context.window_manager.clipboard = collisionScript

print("\nScript pasted in clipboard too.\n")
print("Don't forget to set your player collider with setCollisionController")
