import bpy
from .operators import CreateProjectFolderOperator, SelectBasePathOperator
from .ui import FolderCreatorPanel
from .utils import SystemUtils, TemplateManager

bl_info = {
    "name": "Project Setup",
    "author": "GuameDev",
    "version": (1, 3, 0),
    "blender": (4, 3, 0),
    "location": "File > Project Setup",
    "description": "Automates the creation of a structured folder system for new 3D projects.",
    "category": "System",
}


def get_template_items(self, context):
    manager = TemplateManager()
    return manager.list_templates()

def register():
    from bpy.types import Scene
    from bpy.props import StringProperty, EnumProperty

    bpy.utils.register_class(SelectBasePathOperator)
    bpy.utils.register_class(CreateProjectFolderOperator)
    bpy.utils.register_class(FolderCreatorPanel)

    default_path = SystemUtils.get_default_base_path()

    Scene.my_project_name = StringProperty(
        name="Project Name",
        default="MyNew3DProject"
    )

    Scene.my_base_path = StringProperty(
        name="Base Path",
        default=default_path,
        subtype='DIR_PATH'
    )

    Scene.my_template = EnumProperty(
        name="Template",
        description="Choose a template for the folder structure",
        items=get_template_items
    )

def unregister():
    from bpy.types import Scene

    bpy.utils.unregister_class(SelectBasePathOperator)
    bpy.utils.unregister_class(CreateProjectFolderOperator)
    bpy.utils.unregister_class(FolderCreatorPanel)

    del Scene.my_project_name
    del Scene.my_base_path
    del Scene.my_template

if __name__ == "__main__":
    register()
