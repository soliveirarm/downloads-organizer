from os import listdir, makedirs, path
from pathlib import Path


downloads = f"{Path.home()}/Downloads"
files = listdir(downloads)


def move_to_folder(filename, folder_name):
    folder_path = f"{downloads}/{folder_name}"
    old_file_path = f"{downloads}/{filename}"
    new_file_path = f"{folder_path}/{filename}"

    if not path.exists(folder_path):
        makedirs(folder_path)

    Path(old_file_path).rename(new_file_path)


formats = {
    "Audio": (".mp3", ".wav", ".m4a"),
    "Compressed": (".zip", ".rar", ".7z"),
    "Documents": (
        ".txt",
        ".md",
        ".pdf",
        ".doc",
        ".docx",
        ".odt",
        ".epub",
        ".rtf",
        ".xls",
        ".xlsx",
    ),
    "Executables": (".msi", ".exe"),
    "Images": (".png", ".jpg", ".jpeg", ".svg", ".gif", ".tif", ".tiff", ".jfif"),
    "Presentation": (".odp", ".ppt", ".pptx"),
    "Video": (".avi", ".mov", ".flv", ".mp4", ".mkv", ".wmv", ".3gp"),
    "Coding": (
        ".js",
        ".py",
        ".cmd",
        ".c",
        ".bat",
        ".cs",
        ".coffee",
        ".fs",
        ".go",
        ".kt",
        ".lua",
        ".php",
        ".pyc",
        ".rb",
        ".sh",
        ".ts",
        ".tsx",
        ".jsx",
        ".vue",
    ),
    "Stylesheets": (".css", ".sass", ".scss", ".less"),
    "Encryption": (".ppk", ".pem"),
    "Data": (".json", ".csv"),
}


for file in files:
    for key, value in formats.items():
        if file.endswith(value) and file != "organize.py":
            move_to_folder(file, key)
