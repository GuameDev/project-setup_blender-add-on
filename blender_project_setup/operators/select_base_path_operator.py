import os
import bpy
from ..utils.system_utils import SystemUtils

class SelectBasePathOperator(bpy.types.Operator):
    bl_idname = "object.select_base_path"
    bl_label = "Select Base Path"
    bl_description = "Select the base folder path for the project"

    directory: bpy.props.StringProperty(subtype="DIR_PATH")

    def execute(self, context):
        # Ensure the directory exists
        if not os.path.isdir(self.directory):
            # If it doesn't exist, create it and report back
            os.makedirs(self.directory, exist_ok=True)
            self.report({'INFO'}, f"Folder '{self.directory}' did not exist, so it was created automatically.")
        else:
            # If it already exists, simply set the base path
            self.report({'INFO'}, f"Base path '{self.directory}' already exists.")

        # Update the base path in the scene
        context.scene.my_base_path = self.directory
        return {'FINISHED'}

    def invoke(self, context, event):
        # Get the current base path from the context
        default_path = context.scene.my_base_path

        # If the path doesn't exist, fall back to the system default
        if not os.path.isdir(default_path):
            system_utils = SystemUtils()
            default_path = system_utils.get_default_base_path()

        # Set the directory to open the file browser in
        self.directory = default_path
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
