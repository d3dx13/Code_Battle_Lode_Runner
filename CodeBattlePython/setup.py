from distutils.core import setup

setup(name='loderunnerclient',
      version='1.0',
      description='Loderunner Dojo game client',
      author='',
      author_email='',
      packages=['loderunnerclient'],
      install_requires=['websocket-client', 'click', 'xmltodict', 'keyboard'],
      entry_points={
          'console_scripts': ['loderunnerclient=loderunnerclient.Main:main']
      }
)
