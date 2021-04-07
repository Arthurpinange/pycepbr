from setuptools import setup, find_packages

setup(name='pycepbr',
      version='1.0',
      description=' Consulta CEPs de todo território brasileiro',
      url='https://github.com/Arthurpinange/pycepbr',
      author='Arthur Pinangé',
      author_email='arthur.pinange@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)

install_requires = ['jsons', 'requests']

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)