import unittest
import os
import sys
from unittest.mock import patch, mock_open, MagicMock

# Mock the bpy module to prevent it from loading during testing
sys.modules['bpy'] = MagicMock()

# Add the parent directory to sys.path so that Python can find the blender_project_setup module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from blender_project_setup.utils.template_manager import TemplateManager

class TestTemplateManager(unittest.TestCase):

    @patch("os.path.exists")
    @patch("os.listdir")
    def test_list_templates(self, mock_listdir, mock_exists):
        mock_exists.return_value = True
        mock_listdir.return_value = ['template1.json', 'template2.json']

        template_data = """
        {
            "template_name": "Test Template",
            "description": "A test template"
        }
        """
        with patch("builtins.open", mock_open(read_data=template_data)):
            manager = TemplateManager()
            templates = manager.list_templates()

            self.assertEqual(len(templates), 2)
            self.assertEqual(templates[0][0], "template1")
            self.assertEqual(templates[0][1], "Test Template")
            self.assertEqual(templates[0][2], "A test template")

    @patch("os.path.exists")
    @patch("os.listdir")
    def test_list_templates_no_templates(self, mock_listdir, mock_exists):
        mock_exists.return_value = True
        mock_listdir.return_value = []

        manager = TemplateManager()
        templates = manager.list_templates()

        self.assertEqual(len(templates), 1)
        self.assertEqual(templates[0][0], "NONE")
        self.assertEqual(templates[0][1], "No templates available")

    @patch("os.path.exists")
    def test_load_template(self, mock_exists):
        mock_exists.return_value = True
        template_data = """
        {
            "template_name": "Test Template",
            "description": "A test template",
            "folders": []
        }
        """
        with patch("builtins.open", mock_open(read_data=template_data)):
            manager = TemplateManager()
            template = manager.load_template("template1")

            self.assertEqual(template["template_name"], "Test Template")
            self.assertEqual(template["description"], "A test template")

    @patch("os.path.exists")
    def test_load_template_not_found(self, mock_exists):
        mock_exists.return_value = False
        manager = TemplateManager()

        with self.assertRaises(FileNotFoundError):
            manager.load_template("nonexistent_template")


if __name__ == '__main__':
    unittest.main()
