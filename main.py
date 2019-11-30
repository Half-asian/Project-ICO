#ICO Unity
import sys
import os
import subprocess
import texture_export
import model_export


if (len(sys.argv) != 2):
    print("Please provide the path to data.df")
    sys.exit()
print(sys.argv[1])
subprocess.call(["df-read2.exe",sys.argv[1]])

path = 'data'

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.p2c' in file or '.p2o' in file:
            files.append(os.path.join(r, file))

for f in files:
    print("Exporting:", f)
    try:
        model_export.main(f)
    except:
        print("Failed.")

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.tm2' in file:
            files.append(os.path.join(r, file))

for f in files:
    print("Exporting:", f)
    try:
        texture_export.main(f)
    except Exception:
        print("ERROR")


    
print("Finished!")