
import os

def get_static_file_path(filename, folder):
    return os.path.join(os.path.dirname(__file__), folder, filename)