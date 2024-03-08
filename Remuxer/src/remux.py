import sys
import subprocess
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
    conversion_table = data["conversion_table"]["table"]
    location = data["output_location"]["location"]
    arguments = data["custom_remux_arguments"]["arguments"]
    if not location:
        location = "default"
    total = len(files)
    print(bcolors.WARNING + str(total) + " file(s) detected" + bcolors.ENDC)
    print("\n\nFrom your current file configuration, you will be converting: \n")
    
    supported_extensions = dict()
    for outputs, inputs in conversion_table.items():
        for extension in inputs:
            if extension not in supported_extensions.keys():
                supported_extensions.update({extension: outputs})
    
    files_to_remove = []
    for file in files:
        extension = os.path.splitext(file)[1][1:].strip().lower()
        if extension not in supported_extensions.keys():
            files_to_remove.append(file)
    
    for file in files_to_remove:
        files.remove(file)
        
    for outputs, inputs in conversion_table.items():
        count = 0
        zero_list = [0 for _ in inputs]
        old_count = dict(zip(inputs, zero_list))
        for file in files:
            extension = os.path.splitext(file)[1][1:].strip().lower()
            if extension in inputs:
                count += 1
                old_count[extension] += 1
        sub_list_str = [str(value) + " " + key for key, value in old_count.items()]
        if count == 0:
            print("Converting " + bcolors.FAIL + str(count) + bcolors.ENDC + " file(s) to " + bcolors.WARNING + "." + outputs + bcolors.ENDC + " (" + ", ".join(sub_list_str) + ")")
        else:
            print("Converting " + bcolors.OKGREEN + str(count) + bcolors.ENDC + " file(s) to " + bcolors.WARNING + "." + outputs + bcolors.ENDC + " (" + ", ".join(sub_list_str) + ")")
    
    print("\n")
    if files_to_remove:
        print(bcolors.FAIL + "ERROR: The following file(s) are not supported: Please check your config.json file." + bcolors.ENDC)
        for file in files_to_remove:
            print(bcolors.FAIL + "File " + file + " is not supported." + bcolors.ENDC)
        exit()
       
    print("\n")     
    ans = input("Do you want to proceed with remuxing? (y/n)")
    if (ans == 'y'):
        remux(files, total, conversion_table, location, arguments)
    else:
        print("Exiting...")
        sys.exit()
    
def remux(files: list, total: int, data: dict, location: str, arguments: list):
    os.system('cls')
    
    if len(files) == 0:
        print(bcolors.FAIL + "No files to remux" + bcolors.ENDC)
        sys.exit()
    count = 0
    errors = {}
    if location == "default":
        if not os.path.exists('Default Output'):
            os.makedirs('Default Output')
        location = os.path.join(os.getcwd(), 'Default Output')
    else:
        if not check_custom_output_folder(location):
            if not os.path.exists('Default Output'):
                os.makedirs('Default Output')
            location = os.path.join(os.getcwd(), 'Default Output')
        
    for file in files:
        count += 1
        for key, value in data.items():
            filename = os.path.basename(file).rsplit('.', 1)[0]
            extension = os.path.splitext(file)[1][1:].strip().lower()
            if extension in value:
                try:
                    print(bcolors.OKBLUE + "Remuxing " + file + " to " + os.path.join(location, filename) + "." + key + " (" + str(count) + "/" + str(total) + ")" + bcolors.ENDC)
                    call_args = ["ffmpeg", "-i", file]
                    for argument in arguments:
                        call_args.append(argument)
                    call_args.append(os.path.join(location, filename) + "." + key)
                    subprocess.call(call_args)
                    print(bcolors.OKGREEN + "\n\nRemuxed " + file + " to ." + key + bcolors.ENDC + "\n")
                except Exception as ex:
                    print(bcolors.FAIL + "\n\nError remuxing " + file + " due to: " + str(ex) + bcolors.ENDC + "\n")
                    errors[file] = str(ex)
                break
        
    print(bcolors.OKBLUE + "Remuxing complete. " + bcolors.ENDC + bcolors.OKGREEN + str(total-len(errors)) + bcolors.ENDC + " Successful, " + bcolors.FAIL + str(len(errors)) + bcolors.ENDC + " file(s) failed to remux.\n")
    if len(errors) > 0:
        print("\n")
        print(bcolors.FAIL + "Failed file(s): " + bcolors.ENDC)
    for key, value in errors.items():
        print(bcolors.FAIL + "Error remuxing " + key + " due to: " + value + bcolors.ENDC)
        
def check_custom_output_folder(output_path) -> bool:
    if not os.path.exists(output_path):
        print(bcolors.FAIL + "\nERROR: Output path " + output_path + " does not exist. Switching to default path.\n\n" + bcolors.ENDC)
        return False
    else:
        return True
        
def main():
    os.system('color')
    if len(sys.argv) == 1:
        print_ascii()
    else:
        pre_remux_checks(sys.argv[1:]) 
    

if __name__ == '__main__':
    main()
    