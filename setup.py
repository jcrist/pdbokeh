from setuptools import setup

setup(name='pdbokeh',
      version='0.0.1',
      description='Pandas plotting accessor using bokeh',
      url='http://github.com/jcrist/pdbokeh/',
      maintainer='Jim Crist',
      maintainer_email='jiminy.crist@gmail.com',
      license='BSD',
      packages=['pdbokeh'],
      requires=['bokeh', 'pandas'],
      zip_safe=False)
