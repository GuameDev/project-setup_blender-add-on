import os

MAX_DEPTH = 5

class ProjectManager:
    """
    This class handles project creation and folder structure creation.
    """
    def create_project(self, base_path, project_name, folder_structure):
        """
        Creates the project folder and subfolders based on the template.
        """
        project_path = self.create_project_directory(base_path, project_name)
        if project_path:
            self.create_subfolders(project_path, folder_structure)
            return project_path
        return None

    def create_project_directory(self, base_path, project_name):
        """
        Creates the main project directory and returns its path.
        """
        project_path = os.path.join(base_path, project_name)

        if os.path.exists(project_path):
            return None  # Project already exists
        os.makedirs(project_path)

        return project_path

    def create_subfolders(self, project_path, folder_structure, current_depth=0, created_folders=None):
        """
        Recursively creates subfolders based on a nested folder structure with a depth limit.
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
                    self.create_subfolders(subfolder_path, folder["subfolders"], current_depth + 1, created_folders)
            else:
                simple_folder_path = os.path.join(project_path, folder)
                if simple_folder_path in created_folders:
                    print(f"Warning: Duplicate folder '{simple_folder_path}' found. Skipping...")
                else:
                    os.makedirs(simple_folder_path, exist_ok=True)
                    created_folders.add(simple_folder_path)
