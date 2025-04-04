import os
import string

def generate_26_files(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for letter in string.ascii_uppercase:
        file_path = os.path.join(directory, f"{letter}.txt")
        with open(file_path, 'w') as file:
            pass

generate_test = r"C:\Users\SystemX\Desktop\testpp2\letters"
generate_26_files(generate_test)