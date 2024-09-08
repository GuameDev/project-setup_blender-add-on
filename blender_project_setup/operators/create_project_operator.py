import bpy
from ..utils.template_manager import TemplateManager
from ..utils.project_manager import ProjectManager
import os

class CreateProjectFolderOperator(bpy.types.Operator):
    bl_idname = "object.create_project_folder"
    bl_label = "Create Project"
    bl_options = {'UNDO'}

    def execute(self, context):
        project_name = context.scene.my_project_name
        base_path = context.scene.my_base_path
        template_name = context.scene.my_template
        
        # Ensure base path is valid
        if not os.path.isdir(base_path):
            self.report({'ERROR'}, "Invalid base path. Please select a valid directory.")
            return {'CANCELLED'}
        
        # Ensure a valid template is selected
        if not template_name or template_name == 'NONE':
            self.report({'ERROR'}, "No template selected. Please select a valid template.")
            return {'CANCELLED'}
        
        template_manager = TemplateManager()
        project_manager = ProjectManager()

        try:
            template = template_manager.load_template(template_name)
            folder_structure = template.get("folders", [])
            
            # Create the project folder and subfolders
            project_path = project_manager.create_project(base_path, project_name, folder_structure)
            if not project_path:
                self.report({'ERROR'}, f"Project '{project_name}' already exists.")
                return {'CANCELLED'}
            
            self.report({'INFO'}, f"Project '{project_name}' created successfully.")
        except (FileNotFoundError, ValueError) as e:
            self.report({'ERROR'}, str(e))
            return {'CANCELLED'}
        
        return {'FINISHED'}
