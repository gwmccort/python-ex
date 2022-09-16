
'''
src: https://stackoverflow.com/questions/19078170/python-how-would-you-save-a-simple-settings-config-file
doc: https://docs.python.org/2/library/configparser.html
'''

# %%
from configparser import ConfigParser
config = ConfigParser()

cs = '''
[DEFAULT]
var = one
[glen]
name = glen
'''
config.read_string(cs)


# %%

# config.read(['one', 'two'])

config.add_section('main')
config['main']['host'] = 'local host'
config.add_section('second')
config['second']['url'] = 'my url'

with open('x.cfg', 'w') as f:
    config.write(f)

# %%
for sect in config.sections():
    print(sect)

# %%
