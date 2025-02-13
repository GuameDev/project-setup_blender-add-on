import bpy
from .operators import CreateProjectFolderOperator, SelectBasePathOperator
from .ui import FolderCreatorPanel
from .utils import SystemUtils, TemplateManager

bl_info = {
    "name": "Project Setup",
    "blender": (2, 80, 0),  # Minimum version of Blender
    "category": "Object",
    "version": (1, 2),
    "author": "Pablo Muñoz",
    "description": "Create a folder structure for new 3D projects in Blender",
}

def get_template_items(self, context):
    manager = TemplateManager()
    return manager.list_templates()

def register():
    bpy.utils.register_class(SelectBasePathOperator)
    bpy.utils.register_class(CreateProjectFolderOperator)
    bpy.utils.register_class(FolderCreatorPanel)

    # Load last saved base path
    default_path = SystemUtils.get_default_base_path()

    bpy.types.Scene.my_project_name = bpy.props.StringProperty(
        name="Project Name",
        default="MyNew3DProject"
    )

    bpy.types.Scene.my_base_path = bpy.props.StringProperty(
        name="Base Path",
        default=default_path
    )

    bpy.types.Scene.my_template = bpy.props.EnumProperty(
        name="Template",
        description="Choose a template for the folder structure",
        items=get_template_items,
        default=0
    )

def unregister():
    bpy.utils.unregister_class(SelectBasePathOperator)
    bpy.utils.unregister_class(CreateProjectFolderOperator)
    bpy.utils.unregister_class(FolderCreatorPanel)

    del bpy.types.Scene.my_project_name
    del bpy.types.Scene.my_base_path
    del bpy.types.Scene.my_template

if __name__ == "__main__":
    register()