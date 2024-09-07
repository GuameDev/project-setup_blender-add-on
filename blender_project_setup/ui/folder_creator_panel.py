import bpy

class FolderCreatorPanel(bpy.types.Panel):
    bl_label = "Project Folder Creator"
    bl_idname = "OBJECT_PT_folder_creator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Project Folders'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, 'my_project_name')
        layout.prop(context.scene, 'my_base_path')
        layout.operator("object.select_base_path", text="Select Base Path")
        layout.operator("object.create_project_folder", text="Create Project")
