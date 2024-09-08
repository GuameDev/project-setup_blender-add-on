import unittest
import os
import sys
from unittest.mock import patch, MagicMock

# Add the parent directory to sys.path so that Python can find the blender_project_setup module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock the bpy module to prevent it from loading during testing
sys.modules['bpy'] = MagicMock()

from blender_project_setup.utils.system_utils import SystemUtils  # Now this should import without the bpy issue

class TestSystemUtils(unittest.TestCase):
    @patch('platform.system')
    def test_get_default_base_path_windows(self, mock_platform):
        mock_platform.return_value = 'Windows'
        utils = SystemUtils()
        expected_path = "C:/Projects"
        self.assertEqual(utils.get_default_base_path(), expected_path)

    @patch('platform.system')
    def test_get_default_base_path_mac(self, mock_platform):
        mock_platform.return_value = 'Darwin'
        utils = SystemUtils()
        expected_path = os.path.expanduser("~/Documents/Projects")
        self.assertEqual(utils.get_default_base_path(), expected_path)

    @patch('platform.system')
    def test_get_default_base_path_linux(self, mock_platform):
        mock_platform.return_value = 'Linux'
        utils = SystemUtils()
        expected_path = os.path.expanduser("~/Projects")
        self.assertEqual(utils.get_default_base_path(), expected_path)

    @patch('platform.system')
    def test_get_default_base_path_unknown(self, mock_platform):
        mock_platform.return_value = 'UnknownOS'
        utils = SystemUtils()
        expected_path = "C:/Projects"  # Fallback path
        self.assertEqual(utils.get_default_base_path(), expected_path)

if __name__ == '__main__':
    unittest.main()
