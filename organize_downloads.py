from os import listdir
from pathlib import Path

DOWNLOADS = f"{Path.home()}/Downloads"

formats = {
    "Audio": (".mp3", ".wav", ".m4a"),
    "Compressed": (".zip", ".rar", ".7z"),
    "Docs": (".doc", ".docx", ".odt"),
    "Spreadsheets": (".xls", ".xlsx", ".ods"),
    "Text": (".txt", ".md", ".epub", ".rtf"),
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
    "PDFs": (".pdf",),
}


def move_to_folder(filename, sorting_folder):
    folder_path = f"{DOWNLOADS}/{sorting_folder}"
    old_file_path = f"{DOWNLOADS}/{filename}"
    new_file_path = f"{folder_path}/{filename}"

    Path(folder_path).mkdir(exist_ok=True)

    if not Path(new_file_path).is_file():
        Path(old_file_path).rename(new_file_path)


def organize_downloads():
    files = listdir(DOWNLOADS)
    for file in files:
        for key, value in formats.items():
            if file.endswith(value) and file != "organize_downloads.py":
                move_to_folder(file, key)


if __name__ == "__main__":
    organize_downloads()
