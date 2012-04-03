import subprocess


plugins = ('images', 'core', 'mirkwood', 'osgiliath', 'khazaddum', 'dwarrowdelf')

for plugin in plugins:
    subprocess.call(['pyrcc4', '-py3', '-no-compress', '{0}.qrc'.format(plugin), '-o', '{0}.py'.format(plugin)])
    print('{0}.qrc dumped'.format(plugin))

for plugin in plugins:
    print('Generating {0}.pyc...'.format(plugin))
    exec('import {0}'.format(plugin))  # this is quite time-consuming...