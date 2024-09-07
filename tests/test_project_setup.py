import sys
import unittest
from unittest.mock import patch
import os

# Mock bpy globally to avoid ModuleNotFoundError
sys.modules['bpy'] = unittest.mock.MagicMock()

# Import only the domain logic (utils)
from blender_project_setup.utils.project_setup import create_project_directory, create_subfolders, get_default_base_path

class TestProjectSetup(unittest.TestCase):

    @patch('os.makedirs')
    @patch('os.path.exists', return_value=False)
    def test_create_project_directory(self, mock_exists, mock_makedirs):
        project_name = "TestProject"
        base_path = "/path/to/base"
        expected_path = os.path.join(base_path, project_name)
        result = create_project_directory(base_path, project_name)
        
        self.assertEqual(result, expected_path)
        mock_makedirs.assert_called_once()

    @patch('os.path.exists', return_value=True)
    def test_create_project_directory_already_exists(self, mock_exists):
        project_name = "TestProject"
        base_path = "/path/to/base"
        result = create_project_directory(base_path, project_name)
        
        self.assertIsNone(result)  # None is returned if project already exists

    @patch('os.makedirs')
    def test_create_subfolders(self, mock_makedirs):
        project_path = "/path/to/project"
        folder_structure = ["folder1", "folder2"]

        create_subfolders(project_path, folder_structure)

        # Ensure os.makedirs was called twice (for each folder)
        self.assertEqual(mock_makedirs.call_count, 2)
        mock_makedirs.assert_any_call(os.path.join(project_path, "folder1"), exist_ok=True)
        mock_makedirs.assert_any_call(os.path.join(project_path, "folder2"), exist_ok=True)

    @patch('platform.system', return_value="Windows")
    def test_get_default_base_path_windows(self, mock_system):
        base_path = get_default_base_path()
        self.assertEqual(base_path, "C:/Projects")

    @patch('platform.system', return_value="Darwin")
    def test_get_default_base_path_mac(self, mock_system):
        base_path = get_default_base_path()
        self.assertEqual(base_path, os.path.expanduser("~/Documents/Projects"))

    @patch('platform.system', return_value="Linux")
    def test_get_default_base_path_linux(self, mock_system):
        base_path = get_default_base_path()
        self.assertEqual(base_path, os.path.expanduser("~/Projects"))

if __name__ == '__main__':
    unittest.main()
