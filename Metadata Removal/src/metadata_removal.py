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
    
    
def convert_metadata(files: list):
    json_str = open('src/config.json', 'r').read()
    data = json.loads(json_str)
    location = data["output_location"]["location"]
    arguments = data["custom_metadata_removal_arguments"]["arguments"]
    
    for file in files:   
        output_filename = os.path.basename(file)
        call_args = ["ffmpeg", "-i", file, "-map_metadata", "-1", "-c:v", "copy", "-c:a", "copy", "-fflags", "+bitexact", "-flags:v", "+bitexact", "-flags:a", "+bitexact"]
        for argument in arguments:
            call_args.append(argument)
        call_args.append(os.path.join(location, output_filename))
        subprocess.check_call(call_args)

def print_ascii():
    with open('./src/ascii.txt', 'r', encoding="utf8") as f:
        print(f.read())

    f.close()
        
def main():
    os.system('color')
    if len(sys.argv) == 1:
        print_ascii()
    else:
        convert_metadata(sys.argv[1:]) 
    

if __name__ == '__main__':
    main()
    