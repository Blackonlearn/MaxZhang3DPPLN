import bpy

# Set object and armature names
ObjectName = 'Cylinder.002'
ArmatureName = 'Armature'

def LocStrBoneToVG():
    """Assign location and stretch-to constraints to selected bones."""
    # Ensure objects exist
    if ObjectName not in bpy.data.objects or ArmatureName not in bpy.data.objects:
        print("Error: Object or Armature not found.")
        return
    
    # Get vertex groups from the target object
    VertexGroupINDEX = bpy.data.objects[ObjectName].vertex_groups
    
    # Loop through selected pose bones
    for i, bone in enumerate(bpy.context.selected_pose_bones):
        # Add Copy Location constraint
        CopyLocation = bone.constraints.new(type='COPY_LOCATION')
        CopyLocation.name = f"Copy Location Vertex {i}"
        CopyLocation.target = bpy.data.objects[ObjectName]
        CopyLocation.subtarget = VertexGroupINDEX[i].name
        
        # Add Stretch To constraint
        if i + 1 < len(VertexGroupINDEX):  # Ensure there's a next vertex group
            StretchTo = bone.constraints.new(type='STRETCH_TO')
            StretchTo.name = f"Stretch to Vertex {i+1}"
            StretchTo.target = bpy.data.objects[ObjectName]
            StretchTo.subtarget = VertexGroupINDEX[i+1].name
            StretchTo.volume = 'NO_VOLUME'

def SelectAndAssignVG():
    """Create vertex groups for selected vertices and assign them."""
    # Ensure the active object is a mesh
    obj = bpy.context.active_object
    if obj is None or obj.type != 'MESH':
        print("Error: Active object is not a mesh.")
        return
    
    # Get selected vertices
    selected_verts = [v for v in obj.data.vertices if v.select]
    if not selected_verts:
        print("Error: No vertices selected.")
        return
    
    # Create and assign vertex groups
    for i, vert in enumerate(selected_verts):
        # Create a new vertex group
        vg = obj.vertex_groups.new(name=f"Vertex_{i}")
        
        # Assign the vertex to the vertex group
        vg.add([vert.index], 1.0, 'REPLACE')

# Example usage
# Uncomment to execute
# SelectAndAssignVG()
LocStrBoneToVG()
