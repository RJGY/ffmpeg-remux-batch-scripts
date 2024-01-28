import sys
import ffmpeg
import json
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_ascii():
    with open('./src/ascii.txt', 'r', encoding="utf8") as f:
        print(f.read())

    f.close()
    
def pre_remux_checks(files: list):
    json_str = open('src/config.json', 'r').read()
    data = json.loads(json_str)
    total = len(files)
    print(bcolors.WARNING + str(total) + " file(s) detected" + bcolors.ENDC)
    print("\n")
    print("From your current file configuration, you will be converting: \n")
    
    supported_extensions = dict()
    for key, value in data.items():
        for extension in value:
            if extension not in supported_extensions.keys():
                supported_extensions.update({extension: key})
    
    files_to_remove = []
    for file in files:
        extension = os.path.splitext(file)[1][1:].strip().lower()
        if extension not in supported_extensions.keys():
            files_to_remove.append(file)
    
    for file in files_to_remove:
        files.remove(file)
        
        
    for key, value in data.items():
        count = 0
        zero_list = [0 for key, value in data.items()]
        old_count = dict(zip(value, zero_list))
        for file in files:
            extension = os.path.splitext(file)[1][1:].strip().lower()
            if extension in value:
                count += 1
                old_count[extension] += 1
        sub_list_str = [str(value) + " " + key for key, value in old_count.items()]
        if count == 0:
            print("Converting " + bcolors.FAIL + str(count) + bcolors.ENDC + " file(s) to " + bcolors.WARNING + "." + key + bcolors.ENDC + " (" + ", ".join(sub_list_str) + ")")
        else:
            print("Converting " + bcolors.OKGREEN + str(count) + bcolors.ENDC + " file(s) to " + bcolors.WARNING + "." + key + bcolors.ENDC + " (" + ", ".join(sub_list_str) + ")")
    
    print("\n")
    print(bcolors.FAIL + "ERROR: The following file(s) are not supported: Please check your config.json file." + bcolors.ENDC)
    for file in files_to_remove:
        print(bcolors.FAIL + "File " + file + " is not supported." + bcolors.ENDC)
       
    print("\n")     
    ans = input("Do you want to proceed with remuxing? (y/n)")
    if (ans == 'y'):
        remux(files, total, data)
    else:
        print("Exiting...")
        sys.exit()
    
def remux(files: list, total: int, data: dict):
    os.system('cls')
    
    if len(files) == 0:
        print(bcolors.FAIL + "No files to remux" + bcolors.ENDC)
        sys.exit()
    count = 0
    errors = {}
    if total > 1:
        check_output_folder()
    for file in files:
        count += 1
        for key, value in data.items():
            filename = os.path.basename(file).rsplit('.', 1)[0]
            extension = os.path.splitext(file)[1][1:].strip().lower()
            if extension in value:
                try:
                    if total == 1:
                        print(bcolors.OKBLUE + "Remuxing " + file + " to " + os.path.splitext(file)[0] + "." + key + " (" + str(count) + "/" + str(total) + ")" + bcolors.ENDC)
                        stream = ffmpeg.input(file)
                        stream = ffmpeg.output(stream, os.path.splitext(file)[0] + "." + key, acodec='copy',vcodec='copy')
                    else:
                        print(bcolors.OKBLUE + "Remuxing " + file + " to " + os.path.join(os.getcwd(), 'remuxed', filename) + "." + key + " (" + str(count) + "/" + str(total) + ")" + bcolors.ENDC)
                        stream = ffmpeg.input(file)
                        stream = ffmpeg.output(stream, os.path.join(os.getcwd(), 'remuxed', filename) + "." + key, acodec='copy',vcodec='copy')
                    ffmpeg.run(stream, quiet=False)
                    print("Remuxed " + file + " to " + key)
                except Exception as ex:
                    print(bcolors.FAIL + "Error remuxing " + file + " due to: " + str(ex) + bcolors.ENDC)
                    errors[file] = str(ex)
                break
        
    print(bcolors.OKBLUE + "Remuxing complete. " + bcolors.ENDC + bcolors.OKGREEN + str(total-len(errors)) + bcolors.ENDC + " Successful, " + bcolors.FAIL + str(len(errors)) + bcolors.ENDC + " file(s) failed to remux.")
    if len(errors) > 0:
        print("\n")
        print(bcolors.FAIL + "Failed file(s): " + bcolors.ENDC)
    for key, value in errors.items():
        print(bcolors.FAIL + "Error remuxing " + key + " due to: " + value + bcolors.ENDC)
    
def check_output_folder():
    if not os.path.exists('remuxed'):
        os.makedirs('remuxed')
        
def main():
    os.system('color')
    if len(sys.argv) == 1:
        print_ascii()
    else:
        pre_remux_checks(sys.argv[1:]) 
    


if __name__ == '__main__':
    main()
    