import os

try:
    from ConfigParser import RawConfigParser, ConfigParser, SafeConfigParser  # noqa
except ImportError:
    from configparser import RawConfigParser, ConfigParser, SafeConfigParser  # nowa

config = RawConfigParser()

config.read(os.path.normpath(os.path.join(os.path.abspath(
    os.path.dirname(__file__)), './config.ex.ini')))

print(config.sections())

print(config.get('AD', 'enable'))
print(config.get('AD', 'string1'))

if config.get('AD', 'enable') == "true":
    print("AD-sync enable")
else:
    print("AD-sync disable")

try:
    print(config.get('AD', 'string2'))
except:
    print("No config: [AD][string2]")
