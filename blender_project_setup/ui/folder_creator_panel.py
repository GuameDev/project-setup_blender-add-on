import bpy
from ..utils.system_utils import SystemUtils


class FolderCreatorPanel(bpy.types.Panel):
    bl_label = "Project Folders"
    bl_idname = "OBJECT_PT_project_folders"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Project Setup'

    def draw(self, context):
        layout = self.layout
        scene = context.scene

        # Project Name input
        layout.prop(scene, "my_project_name")

        # Base Path - read-only, only accessible via the file browser operator
        row = layout.row()
        row.prop(scene, "my_base_path", text="Base Path")
        row.enabled = False  # Disables manual input
        
        # Button to select base path using file browser
        layout.operator("object.select_base_path", text="Select Base Path")
        
        # Template selection
        layout.prop(scene, "my_template", text="Template")
        
        # Button to create project folder
        layout.operator("object.create_project_folder", text="Create Project")
