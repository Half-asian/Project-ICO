import sys
import os
import subprocess
import texture_export

path = 'data'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.tm2' in file:
            files.append(os.path.join(r, file))

for f in files:
    print("Exporting:", f)
    texture_export.main(f)
    
for r, d, f in os.walk(path):
    for file in f:
        if '.p2c' in file or '.p2o' in file or '.p2s':
            files.append(os.path.join(r, file))

for f in files:
    print("Exporting:", f)
    model_export.main(f)


