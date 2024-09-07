import os
import platform

class SystemUtils:
    def get_default_base_path(self):
        current_os = platform.system()

        if current_os == "Windows":
            return "C:/Projects"
        elif current_os == "Darwin":  # macOS
            return os.path.expanduser("~/Documents/Projects")
        elif current_os == "Linux":
            return os.path.expanduser("~/Projects")
        else:
            return "C:/Projects"  # Fallback for unknown OS
