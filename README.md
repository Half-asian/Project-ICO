# Project-ICO

Welcome to Project Ico tools.

Usage:
Have Python 3 installed.
Mount the Ico game ISO.
Open cmd, type "python main.py X:DFDATAS\DATA.DF", where X: is the drive you mounted Ico to.
All game files will be extracted into the data folder.
Model files (.p2o and .p2c) will be converted into .obj and .mtl files.
Texture files (.tm2) will be converted into .png files.

Notes:
Some textures fail to convert. This is usually because the resolution hasn't been programmed in texture_export.py.
Model normals are broken. Enabling backface-culling will make 50% of the models polygons invisible.
Terrain is upside-down. (Might be all .p2o models)

Todo:
Better aglorithm for texture exporting, such that only one algorithm is needed for all texture resolutions.
Figure out if it's possible to get correct normals.
Figure out structure of other file types.
Cleanup of code.

Thanks:
majo33 for the creation of df-read2 https://github.com/majo33/df-read2
ps23dformat.wikispaces.com (Archive.org only) for hosting valuable information on Ico's file structures. It is sad that the website is defunct as they had information on dozens of games, which you can find almost nowhere else.

Hopes and dreams:
People will make cool stuff with the Ico content. Also, full debug symbols for the Ico binary are literaly included on the European version of the disc. They are just waiting to be reverse engineered.
