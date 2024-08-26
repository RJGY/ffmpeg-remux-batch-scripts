from fontTools.ttLib import TTFont
import os
import sys

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
    
correct_formats = ["otf", "ttf", "woff", "woff2", "eot"]

def convert_font(input_files: list):
    for input_file in input_files:
        input_font = TTFont(input_file)
        output_folder = os.path.dirname(input_file)
        output_format = input("Enter output format + " + correct_formats + ": ")
        while output_format not in correct_formats:
            output_format = input("Format not recognized. Enter output format " + correct_formats + ": ")
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + "." + output_format)
        input_font.save(output_file, format=output_format)
        
        """ this doesnt work rn, i porobs have to make a different script for each font type"""
        """ so like 4 + 3 + 2 + 1 functions * 2 for each different type of conversion """
        """ so basically 20 fucking funcitons its litttttttttttttttttttttttt"""
    
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