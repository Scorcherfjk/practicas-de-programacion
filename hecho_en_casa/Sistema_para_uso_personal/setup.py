from setuptools import setup

setup(name="Inventario",  # Nombre
      version="0.1",  # Versión de desarrollo
      description="modulo de inventario",  # Descripción del funcionamiento
      author="Francisco De Freitas",  # Nombre del autor
      author_email='franjavikale@gmail.com',  # Email del autor
      license="GPL",  # Licencia: MIT, GPL, GPL 2.0...
      url="https://bit.ly/2jjjUX2",  # Página oficial (si la hay)
      packages=['inventario'],  #paquetes
      install_requires=[i.strip() for i in open("requirements.txt").readlines() ],  #dependencia si las hay
      test_suite="tests",  #carpeta contenedora de los unittest
)