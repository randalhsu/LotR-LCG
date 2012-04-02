'''run pylupdate4 to extract translation strings, then run lrelease to compile *.qm files.'''
'''qt_*.qm files are from PyQt 4.9.1'''
import glob
import subprocess


# dump all source file paths
s = 'SOURCES += ../../Launcher.py '
sourceList = glob.glob('../../LotRLCG/*.py')
for sourcePath in sourceList:
    sourcePath = sourcePath.replace('\\', '/')
    s += ' ' + sourcePath

s += '\nTRANSLATIONS +='
languages = ('zh_TW', 'zh_CN')
for language in languages:
    s += ' {0}.ts'.format(language)

s += '\n\nCODECFORTR = UTF-8\nCODECFORSRC = UTF-8'

projectFilePath = 'LotRLCG.pro'
with open(projectFilePath, 'w') as f:
    f.write(s)

subprocess.call(['pylupdate4', '-verbose', '-noobsolete', projectFilePath])
subprocess.call(['lrelease', projectFilePath])