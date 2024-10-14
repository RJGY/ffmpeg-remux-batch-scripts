import sys
import os
import subprocess
import json

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
        
def main():
    os.system('color')
    if len(sys.argv) == 1:
        print_ascii()
    else:
        upscale(sys.argv[1:])

def upscale(input_files: list):
    json_str = open('src/config.json', 'r').read()
    config = json.loads(json_str)
    location = config["output_location"]["location"]
    for input_file in input_files:
        output_filename = os.path.basename(input_file)
        output_path = os.path.join(location, output_filename)
        
        #Construct ffmpeg command
        command = [
            'ffmpeg',
            '-i', input_file,
            '-vf', f"scale={config['scale']['scale']}:flags={config['interpolation_type']['type']}",  #Use config for scale, maintain aspect ratio
            '-c:v', config['codec']['codec'],  #Use libx264 encoder (you can change this)
            '-crf', config['quality']['crf'], # Constant Rate Factor (adjust for quality, lower is better)
            '-preset', config['preset']['preset'], # Encoding speed (slower presets give better quality)
            output_path
        ]

        try:
            subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            print(f"{bcolors.OKGREEN}Successfully upscaled {input_file} to {output_path}{bcolors.ENDC}")
        except subprocess.CalledProcessError as e:
            print(f"{bcolors.FAIL}Error upscaling {input_file}: {e.stderr.decode()}{bcolors.ENDC}")
        
    

if __name__ == '__main__':
    main()
    