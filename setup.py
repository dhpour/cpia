from setuptools import setup, find_packages

VERSION = '2024.7.5' 
DESCRIPTION = 'Persian word analyzer'
LONG_DESCRIPTION = 'Inflectional anlyzer for contemporary Persian'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="cpia", 
        version=VERSION,
        author="Davood Heidarpour",
        author_email="<chandracar@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        #package_dir={"cpia": "fsts/*.fst"},
        package_data={"cpia": ["fsts/*.fst"]},
        install_requires=['fst-lookup>=2024.7.3'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['Persian', 'Farsi', 'Inflection', 'Analyzer'],
        classifiers= [
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Text Engineering",
            "Intended Audience :: NLP",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Operating System :: MacOS",
        ]
)