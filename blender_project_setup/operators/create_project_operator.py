import bpy
from ..utils.project_setup import create_project_directory, create_subfolders

class CreateProjectFolderOperator(bpy.types.Operator):
    bl_idname = "object.create_project_folder"
    bl_label = "Create Project"
    bl_options = {'UNDO'}

    folder_structure = [
        "01_Concept/References", "01_Concept/Sketches",
        "02_Models/Base_Meshes", "02_Models/Sculpted_Models", "02_Models/Retopology",
        "03_Textures/UV_Maps", "03_Textures/Baked_Textures", "03_Textures/Hand_Painted",
        "04_Rigs/Bones", "04_Rigs/Controllers",
        "05_Animations/Walk_Cycles", "05_Animations/Facial_Expressions",
        "06_Render/Preview", "06_Render/Final",
        "07_Backups/Old_Versions", "07_Backups/Auto_Saves"
    ]

    def execute(self, context):
        project_name = context.scene.my_project_name
        base_path = context.scene.my_base_path

        project_path = create_project_directory(base_path, project_name)
        if project_path:
            create_subfolders(project_path, self.folder_structure)
            self.report({'INFO'}, f"Project '{project_name}' created successfully.")
        else:
            self.report({'WARNING'}, f"Project '{project_name}' already exists.")
        return {'FINISHED'}
