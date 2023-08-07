import os
import zipfile
import shutil

def extract_all_zips_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".zip"):
            zip_file_path = os.path.join(folder_path, file_name)
            with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
            print(f"Extraiu {file_name}")

if __name__ == "__main__":
    folder_path = "/workspaces/codespaces-jupyter/RPISpider/downloads" 
    extract_all_zips_in_folder(folder_path)
