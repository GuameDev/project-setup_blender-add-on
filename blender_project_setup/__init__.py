import bpy
from .operators.create_project_operator import CreateProjectFolderOperator
from .operators.select_base_path_operator import SelectBasePathOperator
from .ui.folder_creator_panel import FolderCreatorPanel
from .utils.system_utils import SystemUtils
from .utils.template_manager import TemplateManager

bl_info = {
    "name": "Blender Project Setup",
    "blender": (2, 80, 0),  # Minimum version of Blender
    "category": "Object",
    "version": (1, 0),
    "author": "Your Name",
    "description": "Create a folder structure for new 3D projects in Blender",
}

# Function to dynamically get the list of templates
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

    # Register the template selection property
    bpy.types.Scene.my_template = bpy.props.EnumProperty(
        name="Template",
        description="Choose a template for the folder structure",
        items=get_template_items,  # Dynamically populate the dropdown
        default=0  # Set default to the first available template
    )

def unregister():
    bpy.utils.unregister_class(CreateProjectFolderOperator)
    bpy.utils.unregister_class(SelectBasePathOperator)
    bpy.utils.unregister_class(FolderCreatorPanel)

    # Unregister custom properties
    del bpy.types.Scene.my_project_name
    del bpy.types.Scene.my_base_path
    del bpy.types.Scene.my_template

if __name__ == "__main__":
    register()
