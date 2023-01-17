import bpy

collection = bpy.data.collections["Colliders"]

print("Exporting box colliders...")

collisionScript = 'createAssetCube("cube")\n'

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
    collisionScript+='createObjectwithScale("'+str(obj.name)+'", cube,'+px+","+py+","+pz+","+sx+","+sy+","+sz+")\n"
    collisionScript+='addToCollision("'+str(obj.name)+'")\n'
    
print("\nUse this script to generate colliders for your scene:\n")

print(collisionScript)
bpy.context.window_manager.clipboard = collisionScript

createAssetCube("cube")
createObjectwithScale("Cube.004", cube,2.8671,2.2938,0.0,1.0,1.0,1.0)
addToCollision("Cube.004")
createObjectwithScale("Cube.003", cube,4.6241,-3.8397,0.0,2.1784,0.4529,1.0)
addToCollision("Cube.003")
