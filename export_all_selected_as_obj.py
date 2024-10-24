
# export all selected objects to a folder based on their collection and the current project file location.

import bpy
import os

# variables
selected = bpy.context.selected_objects # list of all selected objects
for object in selected : object.select_set(False) # deselects all objects
path = bpy.data.filepath.rsplit('\\', 1)[0] # path to current project file

# loop through each selected object, exporting it as a .obj
for object in selected:
    object.select_set(True)
    # find path to export to based on parent collection of selected object
    export_path = (path +'\\'+ object.users_collection[0].name + '\\' + object.name + '.obj').replace('/', '\\')
    print('export path: ', export_path)
    # store the original location of the object
    original_position = object.matrix_world.translation 
    # move the object to the origin
    object.matrix_world.translation = (0, 0, 0)
    # export the object
    bpy.ops.wm.obj_export(
        filepath = export_path,
        export_selected_objects = True,
        export_triangulated_mesh = True,
        export_materials = False,
        forward_axis = 'NEGATIVE_Z',
        up_axis = 'Y',
    )
    # return the object to its original location
    object.location -= object.matrix_local.translation
    # deselect the object
    object.select_set(False)

# reselect the objects to avoid confusion
for object in selected : object.select_set(True)
