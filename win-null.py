# Author: m33k
# Date: 2017-09-16
# Description: Create a /dev/null like file for windows and delete contents in it
# Environment: For Windows 7

import os
import shutil

# Create null file if it doesn't exists
nullFile = ('C:\\Users\\Public\\null')
if not os.path.isdir(nullFile):
  os.makedirs(nullFile)
  print("Creating win null file at" ,nullFile)

# Recursively delete files, but leave parent directory.
for file in os.listdir(nullFile):
  filePath =  os.path.join(nullFile, file)
  try:
    if os.path.isfile(filePath):
      os.unlink(filePath)
    elif os.path.isdir(filePath): shutil.rmtree(filePath)
  except Exception as e:
    print(e)
