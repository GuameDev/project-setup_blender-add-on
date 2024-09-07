import bpy
import os
import platform

bl_info = {
    "name": "Blender Project Setup",
    "blender": (4, 2, 1),
    "category": "Object",
    "version": (1, 0),
    "author": "Your Name",
    "description": "Create a folder structure for new 3D projects in Blender",
}


def create_project_directory(base_path, project_name):
    """
    Creates the main project directory and returns its path.
    """
    project_path = os.path.join(base_path, project_name)

    if os.path.exists(project_path):
        return None  # Indicate that the project already exists
    else:
        os.makedirs(project_path)

    return project_path


def create_subfolders(project_path, folder_structure):
    """
    Creates subfolders for a project based on a given folder structure.
    """
    for folder in folder_structure:
        os.makedirs(os.path.join(project_path, folder), exist_ok=True)


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

        # Create project directory if it does not exist
        project_path = create_project_directory(base_path, project_name)
        if project_path:
            # Create subfolders
            create_subfolders(project_path, self.folder_structure)
            self.report({'INFO'}, f"Project '{project_name}' created successfully.")
        else:
            # Report to the user if the project already exists
            self.report({'WARNING'}, f"Project '{project_name}' already exists.")

        return {'FINISHED'}


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


class SelectBasePathOperator(bpy.types.Operator):
    bl_idname = "object.select_base_path"
    bl_label = "Select Base Path"
    bl_description = "Select the base folder path for the project"

    directory: bpy.props.StringProperty(subtype="DIR_PATH")

    def execute(self, context):
        context.scene.my_base_path = self.directory
        self.report({'INFO'}, f"Base path set to: {self.directory}")
        return {'FINISHED'}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}


def get_default_base_path():
    """
    Determines the default project path based on the user's operating system.
    """
    current_os = platform.system()

    if current_os == "Windows":
        return "C:/Projects"
    elif current_os == "Darwin":  # macOS
        return os.path.expanduser("~/Documents/Projects")
    elif current_os == "Linux":
        return os.path.expanduser("~/Projects")
    else:
        return "C:/Projects"  # Fallback for unknown OS


def register():
    bpy.utils.register_class(CreateProjectFolderOperator)
    bpy.utils.register_class(FolderCreatorPanel)
    bpy.utils.register_class(SelectBasePathOperator)

    # Set the default base path based on the OS
    bpy.types.Scene.my_project_name = bpy.props.StringProperty(
        name="Project Name",
        default="MyNew3DProject"
    )
    bpy.types.Scene.my_base_path = bpy.props.StringProperty(
        name="Base Path",
        default=get_default_base_path()
    )


def unregister():
    bpy.utils.unregister_class(CreateProjectFolderOperator)
    bpy.utils.unregister_class(FolderCreatorPanel)
    bpy.utils.unregister_class(SelectBasePathOperator)

    # Unregister custom properties
    del bpy.types.Scene.my_project_name
    del bpy.types.Scene.my_base_path


if __name__ == "__main__":
    register()
