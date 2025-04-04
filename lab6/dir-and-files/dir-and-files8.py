import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            try:
                os.remove(file_path)
                print(f" File deleted: {file_path}")
            except Exception as e:
                print(f" Error while deleting the file: {e}")
        else:
            print(" No write permission for this file.")
    else:
        print(" File does not exist.")

file_to_delete = r"C:\Users\SystemX\Desktop\testpp2\delete.txt"
delete_file(file_to_delete)