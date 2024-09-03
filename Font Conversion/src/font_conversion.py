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
    
correct_formats = ["otf", "ttf", "woff", "woff2"]

def convert_font(input_files: list):
    for input_file in input_files:
        input_format = os.path.splitext(input_file)[1][1:].strip().lower()
        output_folder = os.path.dirname(input_file)
        output_format = input("Enter output format + " + str(correct_formats) + ": ")
        while output_format not in correct_formats or output_format == input_format:
            output_format = input("Format not recognized or is the same as the input. Enter output format " + str(correct_formats) + ": ")
        output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + "." + output_format)
        print("output file: " + output_file)
        print("input_format: " + input_format)
        print("output_format: " + output_format)
        if input_format == "otf":
            if output_format == "ttf":
                convert_otf_to_ttf(input_file)
            elif output_format == "woff":
                convert_otf_to_woff(input_file)
            elif output_format == "woff2":
                convert_otf_to_woff2(input_file)
        if input_format == "ttf":
            if output_format == "otf":
                convert_ttf_to_otf(input_file)
            elif output_format == "woff":
                convert_ttf_to_woff(input_file)
            elif output_format == "woff2":
                convert_ttf_to_woff2(input_file)
        if input_format == "woff":
            if output_format == "otf":
                convert_woff_to_otf(input_file)
            elif output_format == "ttf":
                convert_woff_to_ttf(input_file)
            elif output_format == "woff2":
                convert_woff_to_woff2(input_file)
        if input_format == "woff2":
            if output_format == "otf":
                convert_woff2_to_otf(input_file)
            elif output_format == "ttf":
                convert_woff2_to_ttf(input_file)
            elif output_format == "woff":
                convert_woff2_to_woff(input_file)
                

def convert_woff2_to_otf(input_file):
    woff2_font = TTFont(input_file)
    otf_file = input_file.replace('.woff2', '.otf')
    woff2_font.flavor = 'otf'
    woff2_font.save(otf_file)


def convert_woff2_to_ttf(input_file):
    woff2_font = TTFont(input_file)
    ttf_file = input_file.replace('.woff2', '.ttf')
    woff2_font.save(ttf_file)
                

def convert_woff2_to_woff(input_file):
    woff2_font = TTFont(input_file)
    woff_file = input_file.replace('.woff2', '.woff')
    woff2_font.flavor = 'woff'
    woff2_font.save(woff_file)
                
                
def convert_woff_to_woff2(input_file):
    woff_font = TTFont(input_file)
    woff2_file = input_file.replace('.woff', '.woff2')
    woff_font.flavor = 'woff2'
    woff_font.save(woff2_file)
                
                
def convert_woff_to_ttf(input_file):
    woff_font = TTFont(input_file)
    ttf_file = input_file.replace('.woff', '.ttf')
    woff_font.save(ttf_file)
    
                
def convert_woff_to_otf(input_file):
    woff_font = TTFont(input_file)
    otf_file = input_file.replace('.woff', '.otf')
    woff_font.flavor = 'otf'
    woff_font.save(otf_file)


def convert_ttf_to_otf(input_file):
    ttf_font = TTFont(input_file)
    otf_file = input_file.replace('.ttf', '.otf')
    ttf_font.flavor = 'otf'
    ttf_font.save(otf_file)
    

def convert_ttf_to_woff(input_file):
    ttf_font = TTFont(input_file)
    woff_file = input_file.replace('.ttf', '.woff')
    ttf_font.flavor = 'woff'
    ttf_font.save(woff_file)
    
    
def convert_ttf_to_woff2(input_file):
    ttf_font = TTFont(input_file)
    woff2_file = input_file.replace('.ttf', '.woff2')
    ttf_font.flavor = 'woff2'
    ttf_font.save(woff2_file)


def convert_otf_to_woff2(input_file):
    # Open the input OTF font file
    input_font = TTFont(input_file)

    # Get the base name of the input file without the extension
    base_name = os.path.splitext(input_file)[0]

    # Save the font as a WOFF2 file with the same base name
    output_file = base_name + '.woff2'
    input_font.flavor = 'woff2'
    input_font.save(output_file)
    
    
def convert_otf_to_woff(input_file):
    # Open the input OTF font file
    input_font = TTFont(input_file)

    # Get the base name of the input file without the extension
    base_name = os.path.splitext(input_file)[0]

    # Save the font as a WOFF file with the same base name
    output_file = base_name + '.woff'
    input_font.flavor = 'woff'
    input_font.save(output_file)
    
    
def convert_otf_to_ttf(input_file):
    # Open the input OTF font file
    input_font = TTFont(input_file)

    # Get the base name of the input file without the extension
    base_name = os.path.splitext(input_file)[0]

    # Save the font as a TTF file with the same base name
    output_file = base_name + '.ttf'
    input_font.save(output_file)
    
    
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