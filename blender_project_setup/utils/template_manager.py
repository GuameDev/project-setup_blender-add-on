import os
import json

# Define the path to the templates folder relative to the main addon directory
TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'templates')

class TemplateManager:
    """
    This class handles loading and listing templates for folder structures.
    """
    def list_templates(self):
        """
        List all available JSON templates in the templates folder.
        """
        templates = []
        if not os.path.exists(TEMPLATES_DIR):
            print(f"Templates directory not found: {TEMPLATES_DIR}")
            return [('NONE', "No templates available", "No templates found.")]

        for filename in os.listdir(TEMPLATES_DIR):
            if filename.endswith('.json'):
                template_path = os.path.join(TEMPLATES_DIR, filename)
                try:
                    with open(template_path, 'r') as json_file:
                        template_data = json.load(json_file)
                        templates.append((
                            filename[:-5],  # identifier (filename without .json)
                            template_data.get("template_name", "Unknown Template"),  # name
                            template_data.get("description", "No description available")  # description
                        ))
                except json.JSONDecodeError:
                    print(f"Error reading template: {filename}. Skipping it.")
        
        if not templates:
            return [('NONE', "No templates available", "No templates found.")]

        return templates

    def load_template(self, template_name):
        """
        Load a template by its name from the templates folder.
        :param template_name: Name of the template JSON file (without extension)
        :return: Dictionary containing the template data
        """
        template_path = os.path.join(TEMPLATES_DIR, f"{template_name}.json")
        
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template '{template_name}' not found.")

        with open(template_path, 'r') as json_file:
            return json.load(json_file)
