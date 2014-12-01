from zipfile import ZipFile
import os
import sys

SRC_DIR = 'src'
EXCLUDE = ()
PACKAGE_FILENAME = 'FixASP.sublime-package'

with ZipFile(PACKAGE_FILENAME, 'w') as sublime_package:
    for filename in os.listdir(SRC_DIR):
        if filename not in EXCLUDE:
            zip_name = os.path.join(SRC_DIR, filename)
            sublime_package.write(zip_name, filename)

print('\nPackage created: ' + PACKAGE_FILENAME)