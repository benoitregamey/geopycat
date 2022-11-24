import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="geopycat",
    version="0.1.0",
    author="Benoit G. Regamey",
    author_email="benoit.regamey@swisstopo.ch",
    description="Manage metadata and data of geocat.ch - a geonetwork instance for Switzerland",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests >=2.25.1',
        'urllib3 >=1.26.6',
        'python-dotenv >=0.20.0',
        'psycopg2 >= 2.9.3'
      ]
)