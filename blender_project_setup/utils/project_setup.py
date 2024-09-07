import os

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
