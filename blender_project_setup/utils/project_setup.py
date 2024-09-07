import os
import json

# Get the main addon directory (one level up from the current file)
ADDON_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Define the path to the templates folder relative to the main addon directory
TEMPLATES_DIR = os.path.join(ADDON_DIR, 'templates')

MAX_DEPTH = 5

def create_project_directory(base_path, project_name):
    """
    Creates the main project directory and returns its path.
    """
    project_path = os.path.join(base_path, project_name)

    if os.path.exists(project_path):
        return None  # Project already exists
    os.makedirs(project_path)

    return project_path

def list_templates():
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
            with open(template_path, 'r') as json_file:
                template_data = json.load(json_file)
                templates.append((
                    filename[:-5],  # identifier (filename without .json)
                    template_data.get("template_name", "Unknown Template"),  # name
                    template_data.get("description", "No description available")  # description
                ))

    if not templates:
        return [('NONE', "No templates available", "No templates found.")]

    return templates


def create_subfolders(project_path, folder_structure, current_depth=0, created_folders=None):
    """
    Recursively creates subfolders based on a nested folder structure with a depth limit,
    and warns if duplicate folders are detected.
    """
    if created_folders is None:
        created_folders = set()

    if current_depth > MAX_DEPTH:
        print(f"Maximum folder depth of {MAX_DEPTH} reached. Skipping deeper folders.")
        return

    for folder in folder_structure:
        if isinstance(folder, dict):
            folder_name = folder["name"]
            subfolder_path = os.path.join(project_path, folder_name)
            
            if subfolder_path in created_folders:
                print(f"Warning: Duplicate folder '{subfolder_path}' found. Skipping...")
            else:
                os.makedirs(subfolder_path, exist_ok=True)
                created_folders.add(subfolder_path)

            if "subfolders" in folder:
                create_subfolders(subfolder_path, folder["subfolders"], current_depth + 1, created_folders)
        else:
            simple_folder_path = os.path.join(project_path, folder)
            if simple_folder_path in created_folders:
                print(f"Warning: Duplicate folder '{simple_folder_path}' found. Skipping...")
            else:
                os.makedirs(simple_folder_path, exist_ok=True)
                created_folders.add(simple_folder_path)

def get_default_base_path():
    """
    Determines the default project path based on the user's operating system.
    """
    import platform
    current_os = platform.system()

    if current_os == "Windows":
        return "C:/Projects"
    elif current_os == "Darwin":  # macOS
        return os.path.expanduser("~/Documents/Projects")
    elif current_os == "Linux":
        return os.path.expanduser("~/Projects")
    else:
        return "C:/Projects"  # Fallback for unknown OS
