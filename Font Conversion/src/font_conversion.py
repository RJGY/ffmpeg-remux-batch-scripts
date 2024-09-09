from fontTools.ttLib import TTFont
import os
import sys
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
    
correct_formats = ["otf", "ttf", "woff", "woff2"]

def convert_font(input_files: list):
    json_str = open('src/config.json', 'r').read()
    config = json.loads(json_str)
    for input_file in input_files:
        input_format = os.path.splitext(input_file)[1][1:].strip().lower()
        output_folder = config["output_location"]["location"]
        output_format = str(config["output_format"]["format"])
        if output_format not in correct_formats:
            print("Output format not supported. Please use one of the following: " + str(correct_formats))
            return
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + "." + output_format)
        print("output file: " + output_file)
        print("input_format: " + input_format)
        print("output_format: " + output_format)
        conversion(input_file, output_format, output_file)
                
def conversion(input_file, output_format, output_file):
    font = TTFont(input_file)
    if output_format != "ttf":
        font.flavor = output_format
    if output_format == "otf":
        font.flavor = 'woff2'
    font.save(output_file)
    
    
def print_ascii():
    with open('./src/ascii.txt', 'r', encoding="utf8") as f:
        print(f.read())

    f.close()
    

if __name__ == '__main__':
    os.system('color')
    if len(sys.argv) == 1:
        print_ascii()
    else:
        convert_font(sys.argv[1:])