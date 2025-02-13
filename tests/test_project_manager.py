import unittest
import os
import sys
from unittest.mock import patch, mock_open, MagicMock

# Mock the bpy module to prevent Blender dependency issues during testing
sys.modules["bpy"] = MagicMock()

# Add the parent directory to sys.path so that Python can find the module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from blender_project_setup.project_manager import ProjectManager

class TestProjectManager(unittest.TestCase):
    
    @patch("os.makedirs")
    @patch("os.path.exists")
    def test_create_project_directory(self, mock_exists, mock_makedirs):
        manager = ProjectManager()
        base_path = "/mock/path"
        project_name = "TestProject"
        project_path = os.path.join(base_path, project_name)

        # Case 1: Project already exists
        mock_exists.return_value = True
        result = manager.create_project_directory(base_path, project_name)
        self.assertIsNone(result)  # Should return None if project exists

        # Case 2: Project does not exist
        mock_exists.return_value = False
        result = manager.create_project_directory(base_path, project_name)
        self.assertEqual(result, project_path)
        mock_makedirs.assert_called_once_with(project_path)  # Ensure directory was created

    @patch("os.makedirs")
    @patch("os.path.exists")
    def test_create_subfolders(self, mock_exists, mock_makedirs):
        manager = ProjectManager()
        base_path = "/mock/path"
        project_name = "TestProject"
        project_path = os.path.join(base_path, project_name)

        mock_exists.return_value = False

        folder_structure = [
            {"name": "Models", "order": 2, "subfolders": [
                {"name": "Blockout", "order": 1, "create_blend": True, "initial_blend": True},
                {"name": "High_Poly", "order": 2, "create_blend": True}
            ]},
            {"name": "Textures", "order": 3, "subfolders": [
                {"name": "UV_Maps", "order": 1}
            ]}
        ]

        with patch.object(manager, "create_blend_file") as mock_create_blend:
            manager.create_subfolders(project_path, folder_structure, project_name)

            # Check folder creation calls
            mock_makedirs.assert_any_call(os.path.join(project_path, "02_Models"), exist_ok=True)
            mock_makedirs.assert_any_call(os.path.join(project_path, "02_Models", "01_Blockout"), exist_ok=True)
            mock_makedirs.assert_any_call(os.path.join(project_path, "02_Models", "02_High_Poly"), exist_ok=True)
            mock_makedirs.assert_any_call(os.path.join(project_path, "03_Textures"), exist_ok=True)
            mock_makedirs.assert_any_call(os.path.join(project_path, "03_Textures", "01_UV_Maps"), exist_ok=True)

            # Ensure blend file creation is called correctly
            mock_create_blend.assert_any_call(
                os.path.join(project_path, "02_Models", "01_Blockout"), project_name, 1, "Blockout", True
            )
            mock_create_blend.assert_any_call(
                os.path.join(project_path, "02_Models", "02_High_Poly"), project_name, 2, "High_Poly", False
            )

    @patch("bpy.ops.wm.save_mainfile")
    @patch("bpy.ops.wm.save_as_mainfile")
    def test_create_blend_file(self, mock_save_as_mainfile, mock_save_mainfile):
        manager = ProjectManager()
        folder_path = "/mock/path/Models/Blockout"
        project_name = "TestProject"
        folder_order = 1
        folder_name = "Blockout"

        # Case 1: Initial Blend File
        manager.create_blend_file(folder_path, project_name, folder_order, folder_name, is_initial=True)
        blend_filename = "01-TestProject-Blockout-v0.1.blend"
        blend_filepath = os.path.join(folder_path, blend_filename)
        mock_save_mainfile.assert_called_once_with(filepath=blend_filepath)

        # Case 2: Empty Blend File
        mock_save_mainfile.reset_mock()
        manager.create_blend_file(folder_path, project_name, folder_order, folder_name, is_initial=False)
        mock_save_as_mainfile.assert_called_once_with(filepath=blend_filepath, copy=True)

if __name__ == "__main__":
    unittest.main()
