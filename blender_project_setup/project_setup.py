bl_info = {
    "name": "Blender Project Setup",
    "blender": (4, 2, 1),
    "category": "Object",
    "version": (1, 0),
    "author": "Your Name",
    "description": "Create a folder structure for new 3D projects in Blender",
}

import bpy
import os


def create_project_directory(base_path, project_name):
    """
    Creates the main project directory and returns its path.

    :param base_path: Root directory for projects
    :param project_name: Name of the project
    :return: The full path of the created project directory
    :raises OSError: If there is an error creating the directory
    """
    project_path = os.path.join(base_path, project_name)
    
    if os.path.exists(project_path):
        return None  # Indicate that the project already exists
    
    os.makedirs(project_path)
    return project_path


def create_subfolders(project_path, folder_structure):
    """
    Creates subfolders for a project based on a given folder structure.

    :param project_path: The main project directory path
    :param folder_structure: A list of subfolders to create
    :raises OSError: If there is an error creating a subfolder
    """
    for folder in folder_structure:
        os.makedirs(os.path.join(project_path, folder), exist_ok=True)


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


class CreateProjectFolderOperator(bpy.types.Operator):
    bl_idname = "object.create_project_folder"
    bl_label = "Create Project Folders"
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

    def invoke(self, context, event):
        # Get the input values from the scene (UI input)
        project_name = context.scene.my_project_name
        base_path = context.scene.my_base_path
        project_path = os.path.join(base_path, project_name)
        
        # Check if the directory already exists
        if os.path.exists(project_path):
            return context.window_manager.invoke_confirm(self, event)
        
        return self.execute(context)
    
    def execute(self, context):
        # Get the input values from the scene (UI input)
        project_name = context.scene.my_project_name
        base_path = context.scene.my_base_path

        try:
            # Create the project directory
            project_path = create_project_directory(base_path, project_name)
            if project_path:
                # Create the subfolders
                create_subfolders(project_path, self.folder_structure)
                self.report({'INFO'}, f"Project '{project_name}' created successfully.")
            else:
                self.report({'WARNING'}, f"Project '{project_name}' already exists.")
        except OSError as e:
            self.report({'ERROR'}, f"Error creating project: {str(e)}")
            return {'CANCELLED'}
        
        return {'FINISHED'}


class FolderCreatorPanel(bpy.types.Panel):
    bl_label = "Project Folder Creator"
    bl_idname = "OBJECT_PT_folder_creator"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Project Folders'
    
    def draw(self, context):
        layout = self.layout
        # Add input fields for project name
        layout.prop(context.scene, 'my_project_name')
        
        # Show current base path and a button to open the folder selection dialog
        layout.prop(context.scene, 'my_base_path')
        layout.operator("object.select_base_path", text="Select Base Path")
        
        # Add the "Create Project" button
        layout.operator("object.create_project_folder")


def register():
    bpy.utils.register_class(SelectBasePathOperator)
    bpy.utils.register_class(CreateProjectFolderOperator)
    bpy.utils.register_class(FolderCreatorPanel)
    
    # Register custom properties for user input
    bpy.types.Scene.my_project_name = bpy.props.StringProperty(
        name="Project Name",
        default="MyNew3DProject"
    )
    bpy.types.Scene.my_base_path = bpy.props.StringProperty(
        name="Base Path",
        default="C:/Projects"
    )


def unregister():
    bpy.utils.unregister_class(SelectBasePathOperator)
    bpy.utils.unregister_class(CreateProjectFolderOperator)
    bpy.utils.unregister_class(FolderCreatorPanel)
    
    # Unregister custom properties
    del bpy.types.Scene.my_project_name
    del bpy.types.Scene.my_base_path


if __name__ == "__main__":
    register()