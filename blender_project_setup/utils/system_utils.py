import os
import json
import bpy

CONFIG_DIR = os.path.join(bpy.utils.user_resource('CONFIG'), "ProjectSetup")
LAST_PATH_FILE = os.path.join(CONFIG_DIR, "last_path.json")

class SystemUtils:
    @staticmethod
    def get_default_base_path():
        """Returns the default base path or the last saved path."""
        if os.path.exists(LAST_PATH_FILE):
            try:
                with open(LAST_PATH_FILE, "r") as f:
                    data = json.load(f)
                    return data.get("last_base_path", SystemUtils.get_fallback_path())
            except (json.JSONDecodeError, IOError):
                return SystemUtils.get_fallback_path()
        return SystemUtils.get_fallback_path()

    @staticmethod
    def save_last_base_path(path):
        """Saves the last selected base path to a file."""
        os.makedirs(CONFIG_DIR, exist_ok=True)
        with open(LAST_PATH_FILE, "w") as f:
            json.dump({"last_base_path": path}, f)

    @staticmethod
    def get_fallback_path():
        """Returns a fallback path based on the operating system."""
        return {
            "Windows": "C:/Projects",
            "Darwin": os.path.expanduser("~/Documents/Projects"),
            "Linux": os.path.expanduser("~/Projects")
        }.get(os.name, "C:/Projects")
