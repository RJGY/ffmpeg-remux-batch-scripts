import sys
import ffmpeg
import json
import os

def print_ascii():
    with open('./ascii.txt', 'r', encoding="utf8") as f:
        print(f.read())

    f.close()
    
def pre_remux_checks(files: list):
    json_str = open('config.json', 'r').read()
    data = json.loads(json_str)
    total = len(files)
    print(str(total) + " file(s) detected")
    print("From your current file configuration, you will be converting: ")
    for key, value in data.items():
        count = 0
        for file in files:
            extension = os.path.splitext(file)[1][1:].strip().lower()
            if extension in value:
                count += 1
        print("Converting " + str(count) + " file(s) to " + key)
            
    ans = input("Do you want to proceed with remuxing? (y/n)")
    if (ans == 'y'):
        remux(files, total, data)
    else:
        print("Exiting...")
        sys.exit()
    
def remux(files: list, total: int, data: dict):
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
                        print("Remuxing " + file + " to " + os.path.splitext(file)[0] + "." + key + " (" + str(count) + "/" + str(total) + ")")
                        stream = ffmpeg.input(file)
                        stream = ffmpeg.output(stream, os.path.splitext(file)[0] + "." + key, acodec='copy',vcodec='copy')
                    else:
                        print("Remuxing " + file + " to " + os.path.join(os.getcwd(), 'remuxed', filename) + "." + key + " (" + str(count) + "/" + str(total) + ")")
                        stream = ffmpeg.input(file)
                        stream = ffmpeg.output(stream, os.path.join(os.getcwd(), 'remuxed', filename) + "." + key, acodec='copy',vcodec='copy')
                    ffmpeg.run(stream, quiet=True)
                    print("Remuxed " + file + " to " + key)
                except Exception as ex:
                    print("Error remuxing " + file + " due to: " + str(ex))
                    errors[file] = str(ex)
                break
        
    print("Remuxing complete. " + str(total-len(errors)) + " Successful, " + str(len(errors)) + " file(s) failed to remux.")
    print("Failed file(s): ")
    for key, value in errors.items():
        print("Error remuxing " + key + " due to: " + value)
    
def check_output_folder():
    if not os.path.exists('remuxed'):
        os.makedirs('remuxed')
        
def main():
    if len(sys.argv) == 1:
        print_ascii()
    else:
        pre_remux_checks(sys.argv[1:]) 
    


if __name__ == '__main__':
    main()
    
    
    