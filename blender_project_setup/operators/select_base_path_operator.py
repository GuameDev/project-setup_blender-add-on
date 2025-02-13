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
            os.makedirs(self.directory, exist_ok=True)
            self.report({'INFO'}, f"Folder '{self.directory}' did not exist, so it was created automatically.")
        else:
            self.report({'INFO'}, f"Base path '{self.directory}' already exists.")

        # Update the base path in the scene
        context.scene.my_base_path = self.directory

        # Save the selected path in JSON
        SystemUtils.save_last_base_path(self.directory)

        return {'FINISHED'}

    def invoke(self, context, event):
        # Get last used path from JSON
        self.directory = SystemUtils.get_default_base_path()
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
