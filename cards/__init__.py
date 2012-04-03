import glob
import os

_suffix = '.pyc'
_pluginList = glob.glob('cards/*{0}'.format(_suffix))

for (i, filePath) in enumerate(_pluginList):
    filePath = filePath.replace('cards', '')
    filePath = filePath.replace('/', '')
    filePath = filePath.replace('\\', '')
    _pluginList[i] = filePath


for plugin in ('images', 'core', 'mirkwood', 'osgiliath', 'khazaddum', 'dwarrowdelf'):
    if plugin + _suffix in _pluginList:
        exec('import {0}'.format(plugin))