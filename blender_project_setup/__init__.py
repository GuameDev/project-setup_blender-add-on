import bpy
from .operators.create_project_operator import CreateProjectFolderOperator
from .operators.select_base_path_operator import SelectBasePathOperator
from .ui.folder_creator_panel import FolderCreatorPanel
from .utils.project_setup import get_default_base_path

bl_info = {
    "name": "Blender Project Setup",
    "blender": (2, 80, 0),  # Minimum version of Blender
    "category": "Object",
    "version": (1, 0),
    "author": "Your Name",
    "description": "Create a folder structure for new 3D projects in Blender",
}

def register():
    bpy.utils.register_class(CreateProjectFolderOperator)
    bpy.utils.register_class(SelectBasePathOperator)
    bpy.utils.register_class(FolderCreatorPanel)

    # Register custom properties for user input
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
    bpy.utils.unregister_class(SelectBasePathOperator)
    bpy.utils.unregister_class(FolderCreatorPanel)

    # Unregister custom properties
    del bpy.types.Scene.my_project_name
    del bpy.types.Scene.my_base_path
