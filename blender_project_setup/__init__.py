import bpy
from .operators import CreateProjectFolderOperator, SelectBasePathOperator
from .ui import FolderCreatorPanel
from .utils import SystemUtils, TemplateManager

bl_info = {
    "name": "Project Setup",
    "blender": (2, 80, 0),  # Minimum version of Blender
    "category": "Object",
    "version": (1, 0),
    "author": "Pablo Muñoz",
    "description": "Create a folder structure for new 3D projects in Blender",
}

def get_template_items(self, context):
    manager = TemplateManager()
    return manager.list_templates()

def register():
    bpy.utils.register_class(CreateProjectFolderOperator)
    bpy.utils.register_class(SelectBasePathOperator)
    bpy.utils.register_class(FolderCreatorPanel)

    # Register custom properties for user input
    bpy.types.Scene.my_project_name = bpy.props.StringProperty(
        name="Project Name",
        default="MyNew3DProject"
    )

    system_utils = SystemUtils()
    bpy.types.Scene.my_base_path = bpy.props.StringProperty(
        name="Base Path",
        default=system_utils.get_default_base_path()
    )

    # Register the template selection property with valid function for items
    bpy.types.Scene.my_template = bpy.props.EnumProperty(
        name="Template",
        description="Choose a template for the folder structure",
        items=get_template_items,
        default=0
    )

def unregister():
    # Only unregister if it has been registered to prevent errors
    if hasattr(bpy.types.Scene, 'my_project_name'):
        del bpy.types.Scene.my_project_name
    if hasattr(bpy.types.Scene, 'my_base_path'):
        del bpy.types.Scene.my_base_path
    if hasattr(bpy.types.Scene, 'my_template'):
        del bpy.types.Scene.my_template

    bpy.utils.unregister_class(CreateProjectFolderOperator)
    bpy.utils.unregister_class(SelectBasePathOperator)
    bpy.utils.unregister_class(FolderCreatorPanel)

if __name__ == "__main__":
    register()
