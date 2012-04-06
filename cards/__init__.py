for plugin in ('images', 'core', 'mirkwood', 'osgiliath', 'khazaddum', 'dwarrowdelf'):
    try:
        exec('import {0}'.format(plugin))
    except ImportError:
        print('Plugin "cards/{0}.pyc" not found...'.format(plugin))