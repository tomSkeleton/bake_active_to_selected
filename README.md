# bake_active_to_selected
Blender script that lets you bake textures from the active object onto a material held by the selected objects.

## Glossary
- Scene Collection \: The list of everything important, by default shown on the side of the main window.
- Objects \: An object in blender is one entry that appears in the 'Scene Collection'.
- Active Object \: The object which blender is 'focusing on'. By default the active object will have its name written in yellow font in the Scene Collection.
- Selected Object \: An object which blender can work on, but is not active. By default a selecetd object will have its name written in orange font in the Scene Collection.

## Requirments
- Your selected objects must have a single material with the same name as your active object.  
- All of the relevant objects must be visible, and all other objects must be hidden.

## Using the Script
- Load the script into your blender project. By default you can use the tabs in the top-center of the window to open the scripting workspace. Then use the 'open' button to open the script.
- Select all of the objects you want to be involved. By default you can do this by holding shift and left-clicking on the top and bottom of them in the scene view. Alternativley you can hold alt and left-click each object one at a time.
- Hold alt and left-click the object you want to be the active object.
- Run the script from the scripting tab. By default you can do this by pressing the 'arrow' \/ 'play' button.
- Check your outputs.
