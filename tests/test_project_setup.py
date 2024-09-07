import unittest
import tempfile
import os
from unittest.mock import MagicMock, patch

# Patching bpy to mock Blender's API during tests
with patch.dict('sys.modules', bpy=MagicMock()):

    from blender_project_setup.project_setup import create_project_directory, create_subfolders

class TestProjectSetup(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory before each test
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        # Cleanup temporary directory after each test
        self.temp_dir.cleanup()

    def test_create_project_directory(self):
        project_name = "TestProject"
        project_path = create_project_directory(self.temp_dir.name, project_name)
        
        # Check if the project path exists
        self.assertIsNotNone(project_path)
        self.assertTrue(os.path.exists(project_path))

    def test_create_project_directory_already_exists(self):
        project_name = "TestProject"
        # Create the directory manually
        os.makedirs(os.path.join(self.temp_dir.name, project_name))

        # Try to create it again
        project_path = create_project_directory(self.temp_dir.name, project_name)
        
        # Assert that the directory already exists (function returns None)
        self.assertIsNone(project_path)

    def test_create_subfolders(self):
        project_name = "TestProject"
        project_path = create_project_directory(self.temp_dir.name, project_name)
        folder_structure = ["folder1", "folder2"]

        # Create subfolders
        create_subfolders(project_path, folder_structure)

        # Check if the subfolders were created
        for folder in folder_structure:
            self.assertTrue(os.path.exists(os.path.join(project_path, folder)))

if __name__ == "__main__":
    unittest.main()
