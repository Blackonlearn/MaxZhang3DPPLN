import bpy

#This simple code is mine, and it has already been pushed to github repo as my archive:https://github.com/Blackonlearn/MaxZhang3DPPLN

C = bpy.context
D = bpy.data
ObjectName = 'BezierCurve'
ArmatureName = 'Armature'

def LocStrBoneToVG():
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

def SelectAndAssignVG():
    selected_verts = [v for v in C.active_object.data.vertices if v.select]
    
    # Get the active object
    obj = bpy.context.active_object
    
    # Ensure the object is a mesh
    if obj and obj.type == 'MESH':
        # Create a new vertex group for each vertex
        for vert_index in range(len(obj.data.vertices)):
            # Create a new vertex group
            vg = obj.vertex_groups.new(name=f"Vertex_{vert_index}")
            
            # Assign the vertex to the vertex group
            vg.add([vert_index], 1.0, 'REPLACE')
