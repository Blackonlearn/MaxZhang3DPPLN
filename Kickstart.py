import bpy

C = bpy.context
D = bpy.data
ObjectName = 'BezierCurve'
ArmatureName = 'Armature'
VertexGroupINDEX = D.objects[ObjectName].vertex_groups

for i, j in enumerate(C.selected_pose_bones):
#    Add Copy Location Constraints
    CopyLocation = D.objects[ArmatureName].pose.bones[j.name].constraints.new(type='COPY_LOCATION')
    CopyLocation.name = f"Copy Location Vertex {i}"
    CopyLocation.target = D.objects[ObjectName]
    CopyLocation.subtarget = VertexGroupINDEX[i].name
    
#    Add Stretch Constraints
    StretchTo = D.objects[ArmatureName].pose.bones[j.name].constraints.new(type='STRETCH_TO')
    StretchTo.name = f"Stretch to Vertex {i+1}"
    StretchTo.target = D.objects[ObjectName]
    StretchTo.subtarget = VertexGroupINDEX[i+1].name
    StretchTo.volume = 'NO_VOLUME'
