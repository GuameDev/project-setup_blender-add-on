import os
import bpy

MAX_DEPTH = 5

class ProjectManager:
    def create_project(self, base_path, project_name, folder_structure):
        """
        Creates the project folder and subfolders based on the template.
        """
        project_path = self.create_project_directory(base_path, project_name)
        if project_path:
            # Sort folders by order before creating them
            sorted_folders = sorted(folder_structure, key=lambda f: f.get("order", 999))
            self.create_subfolders(project_path, sorted_folders, project_name)
            return project_path
        return None

    def create_project_directory(self, base_path, project_name):
        """
        Creates the main project directory and returns its path.
        """
        project_path = os.path.join(base_path, project_name)
        if os.path.exists(project_path):
            print("⚠ The project already exists.")
            return None  # Project already exists
        os.makedirs(project_path)
        return project_path

    def create_subfolders(self, project_path, folder_structure, project_name, current_depth=0, created_folders=None):
        """
        Recursively creates subfolders and `.blend` files based on a template.
        """
        if created_folders is None:
            created_folders = set()

        if current_depth > MAX_DEPTH:
            print(f"⚠ Maximum folder depth of {MAX_DEPTH} reached. Skipping deeper folders.")
            return

        # Sort folders by order
        sorted_folders = sorted(folder_structure, key=lambda f: f.get("order", 999))

        # Track if we have saved the initial blend file
        initial_blend_saved = False

        for folder in sorted_folders:
            if isinstance(folder, dict):
                folder_name = folder["name"]
                folder_order = folder.get("order", 999)
                ordered_folder_name = f"{folder_order:02d}_{folder_name}"
                subfolder_path = os.path.join(project_path, ordered_folder_name)

                if subfolder_path in created_folders:
                    print(f"⚠ Warning: Duplicate folder '{subfolder_path}' found. Skipping...")
                else:
                    os.makedirs(subfolder_path, exist_ok=True)
                    created_folders.add(subfolder_path)

                    # Check if the template specifies to create a .blend file
                    if folder.get("create_blend", False):
                        is_initial = folder.get("initial_blend", False) and not initial_blend_saved
                        if is_initial:
                            initial_blend_saved = True  # Ensure only one gets the saved project

                        self.create_blend_file(subfolder_path, project_name, folder_order, folder_name, is_initial)

                if "subfolders" in folder:
                    sorted_subfolders = sorted(folder["subfolders"], key=lambda f: f.get("order", 999))
                    self.create_subfolders(subfolder_path, sorted_subfolders, project_name, current_depth + 1, created_folders)

    def create_blend_file(self, folder_path, project_name, folder_order, folder_name, is_initial=False):
        """
        Creates a Blender project file (.blend) inside the specified folder.
        If is_initial=True, the current Blender session is saved in this file.
        Otherwise, an empty Blender project is created.
        """
        blend_filename = f"{folder_order:02d}-{project_name}-{folder_name}-v0.1.blend"
        blend_filepath = os.path.join(folder_path, blend_filename)

        if is_initial:
            bpy.ops.wm.save_mainfile(filepath=blend_filepath)
            print(f"✅ Saved current Blender project as: {blend_filepath}")
        else:
            bpy.ops.wm.save_as_mainfile(filepath=blend_filepath, copy=True)
            print(f"🆕 Created empty Blender file: {blend_filepath}")
