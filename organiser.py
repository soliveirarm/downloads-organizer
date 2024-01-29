import os
from pathlib import Path

downloads = f"{Path.home()}/Downloads"
files = os.listdir(downloads)


def move_to_folder(filename, folder_name):
    if not os.path.exists(f"{downloads}/{folder_name}"):
        os.makedirs(f"{downloads}/{folder_name}")
    Path(f"{downloads}/{filename}").rename(f"{downloads}/{folder_name}/{filename}")


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
    "Video": (".avi", ".mov", ".flv", ".mp4"),
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
}


for file in files:
    for key in formats:
        if file.endswith(formats[key]):
            move_to_folder(file, key)
