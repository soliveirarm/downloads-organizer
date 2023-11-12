import os
from pathlib import Path

downloads = f"{Path.home()}/Downloads"


def create_folder(folder_name):
    if not os.path.exists(f"{downloads}/{folder_name}"):
        os.makedirs(f"{downloads}/{folder_name}")


def move_to_folder(filename, folder_name):
    Path(f"{downloads}/{filename}").rename(f"{downloads}/{folder_name}/{filename}")


files = os.listdir(downloads)

image_ff = (".png", ".jpg", ".jpeg", ".svg", ".gif", ".tif", ".tiff")
audio_ff = (".mp3", ".wav", ".m4a")
compressed_ff = (".zip", ".rar", ".7z")
document_ff = (
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
)
video_ff = (".avi", ".mov", ".flv", ".mp4")
presentation_ff = (".odp", ".ppt", ".pptx")

for file in files:
    if file.endswith(image_ff):
        create_folder("Imagens")
        move_to_folder(file, "Imagens")
    if file.endswith(audio_ff):
        create_folder("Áudio")
        move_to_folder(file, "Áudio")
    if file.endswith(compressed_ff):
        create_folder("Comprimido")
        move_to_folder(file, "Comprimido")
    if file.endswith(video_ff):
        create_folder("Vídeo")
        move_to_folder(file, "Vídeo")
    if file.endswith(document_ff):
        create_folder("Documentos")
        move_to_folder(file, "Documentos")
    if file.endswith(presentation_ff):
        create_folder("Apresentações")
        move_to_folder(file, "Apresentações")
