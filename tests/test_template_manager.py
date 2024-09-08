import unittest
import os
import sys
import json
from unittest.mock import patch, mock_open, MagicMock

# Mock the bpy module to prevent it from loading during testing
sys.modules['bpy'] = MagicMock()

# Add the parent directory to sys.path so that Python can find the blender_project_setup module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from blender_project_setup.utils.template_manager import TemplateManager, TEMPLATES_DIR

class TestTemplateManager(unittest.TestCase):

    @patch('os.path.exists')
    @patch('os.listdir')
    def test_list_templates_with_templates(self, mock_listdir, mock_exists):
        mock_exists.return_value = True
        mock_listdir.return_value = ['template1.json', 'template2.json']

        mock_template_data = json.dumps({
            "template_name": "Test Template",
            "description": "A test template"
        })

        with patch('builtins.open', mock_open(read_data=mock_template_data)):
            manager = TemplateManager()
            templates = manager.list_templates()

        expected = [
            ('template1', 'Test Template', 'A test template'),
            ('template2', 'Test Template', 'A test template')
        ]
        self.assertEqual(templates, expected)

    @patch('os.path.exists')
    def test_list_templates_no_templates(self, mock_exists):
        mock_exists.return_value = False

        manager = TemplateManager()
        templates = manager.list_templates()

        self.assertEqual(templates, [('NONE', "No templates available", "No templates found.")])

    @patch('os.path.exists')
    @patch('os.listdir')
    def test_list_templates_invalid_json(self, mock_listdir, mock_exists):
        mock_exists.return_value = True
        mock_listdir.return_value = ['template1.json']

        with patch('builtins.open', mock_open(read_data="INVALID_JSON")):
            with patch('builtins.print') as mock_print:
                manager = TemplateManager()
                templates = manager.list_templates()

                mock_print.assert_called_once_with("Error reading template: template1.json. Skipping it.")
                self.assertEqual(templates, [('NONE', "No templates available", "No templates found.")])

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open, read_data='{"folders": []}')
    def test_load_template_valid(self, mock_open_file, mock_exists):
        mock_exists.return_value = True

        manager = TemplateManager()
        template = manager.load_template("template1")

        mock_open_file.assert_called_once_with(os.path.join(TEMPLATES_DIR, "template1.json"), 'r')
        self.assertEqual(template, {"folders": []})

    @patch('os.path.exists')
    def test_load_template_not_found(self, mock_exists):
        mock_exists.return_value = False

        manager = TemplateManager()
        with self.assertRaises(FileNotFoundError):
            manager.load_template("nonexistent_template")

if __name__ == '__main__':
    unittest.main()
