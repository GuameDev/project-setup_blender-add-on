import bpy
import os
from ..utils.system_utils import SystemUtils

class SelectBasePathOperator(bpy.types.Operator):
    bl_idname = "object.select_base_path"
    bl_label = "Select Base Path"
    bl_description = "Select the base folder path for the project"

    directory: bpy.props.StringProperty(subtype="DIR_PATH")

    def execute(self, context):
        if not os.path.isdir(self.directory):
            self.report({'ERROR'}, f"Path '{self.directory}' does not exist.")
            return {'CANCELLED'}

        context.scene.my_base_path = self.directory
        self.report({'INFO'}, f"Base path set to: {self.directory}")
        return {'FINISHED'}

    def invoke(self, context, event):
        # Get the current base path from the context
        default_path = context.scene.my_base_path

        # Check if the path exists and is valid, otherwise use Blender's default path
        if not os.path.isdir(default_path):
            # Ensure the SystemUtils class is used properly
            system_utils = SystemUtils()
            default_path = system_utils.get_default_base_path()

        # Set the directory to open the file browser in
        self.directory = default_path
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}
