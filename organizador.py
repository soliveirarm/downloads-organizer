import os
from pathlib import Path

downloads = f"{Path.home()}/Downloads"
files = os.listdir(downloads)


def move_to_folder(filename, folder_name):
    if not os.path.exists(f"{downloads}/{folder_name}"):
        os.makedirs(f"{downloads}/{folder_name}")
    Path(f"{downloads}/{filename}").rename(f"{downloads}/{folder_name}/{filename}")


formats = {
    "Áudio": (".mp3", ".wav", ".m4a"),
    "Comprimidos": (".zip", ".rar", ".7z"),
    "Documentos": (
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
    "Executáveis": (".msi", ".exe"),
    "Imagens": (".png", ".jpg", ".jpeg", ".svg", ".gif", ".tif", ".tiff", ".jfif"),
    "Apresentações": (".odp", ".ppt", ".pptx"),
    "Vídeos": (".avi", ".mov", ".flv", ".mp4"),
}


for file in files:
    for key in formats:
        if file.endswith(formats[key]):
            move_to_folder(file, key)
