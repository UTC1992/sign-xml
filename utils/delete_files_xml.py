import os

def delete_files(path_directory: str, extension: str):
    # iterate over all files in the directory
    for filename in os.listdir(path_directory):
        # check if the file is an XML document
        if filename.endswith(extension):
            filepath = os.path.join(path_directory, filename)
            # delete the file
            os.remove(filepath)
            print(f"{filepath} has been deleted.")
