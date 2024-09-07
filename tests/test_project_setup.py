import unittest
import tempfile
import os
from unittest.mock import patch, MagicMock

# Mock bpy before importing anything else
bpy_mock = MagicMock()
modules = {'bpy': bpy_mock}
patcher = patch.dict('sys.modules', modules)
patcher.start()

# Import the module AFTER mocking bpy
from blender_project_setup.project_setup import create_project_directory, create_subfolders, get_default_base_path

class TestProjectSetup(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory before each test
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        # Cleanup temporary directory after each test
        self.temp_dir.cleanup()

    # Test for creating a project directory
    def test_create_project_directory(self):
        project_name = "TestProject"
        project_path = create_project_directory(self.temp_dir.name, project_name)

        # Check if the project path exists
        self.assertIsNotNone(project_path)
        self.assertTrue(os.path.exists(project_path))

    # Test for trying to create a directory that already exists
    def test_create_project_directory_already_exists(self):
        project_name = "TestProject"
        os.makedirs(os.path.join(self.temp_dir.name, project_name))

        # Try to create it again, expect None
        project_path = create_project_directory(self.temp_dir.name, project_name)
        self.assertIsNone(project_path)

    # Test creating subfolders
    def test_create_subfolders(self):
        project_name = "TestProject"
        project_path = create_project_directory(self.temp_dir.name, project_name)
        folder_structure = ["folder1", "folder2"]

        # Create subfolders
        create_subfolders(project_path, folder_structure)

        # Verify that the subfolders exist
        for folder in folder_structure:
            self.assertTrue(os.path.exists(os.path.join(project_path, folder)))

    # Test OS-specific paths with mocked OS detection
    @patch('platform.system')
    def test_get_default_base_path_windows(self, mock_platform):
        mock_platform.return_value = "Windows"
        self.assertEqual(get_default_base_path(), "C:/Projects")

    @patch('platform.system')
    def test_get_default_base_path_mac(self, mock_platform):
        mock_platform.return_value = "Darwin"  # macOS
        self.assertEqual(get_default_base_path(), os.path.expanduser("~/Documents/Projects"))

    @patch('platform.system')
    def test_get_default_base_path_linux(self, mock_platform):
        mock_platform.return_value = "Linux"
        self.assertEqual(get_default_base_path(), os.path.expanduser("~/Projects"))

if __name__ == "__main__":
    unittest.main()
