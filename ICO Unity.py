#ICO Unity
import sys
import subprocess

if (len(sys.argv) != 2):
    print("Please provide the path to data.df")
    sys.exit()
print(sys.argv[1])
subprocess.call(["df-read2.exe",sys.argv[1]])

