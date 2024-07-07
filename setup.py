from setuptools import setup, find_packages
from pathlib import Path
this_directory = Path(__file__).parent

VERSION = '2024.7.8' 
DESCRIPTION = 'Contemporary Persian word analyzer'
LONG_DESCRIPTION = (this_directory / "README.md").read_text(encoding='utf-8')

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="cpia", 
        version=VERSION,
        author="Davood Heidarpour",
        author_email="<chandracar@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        project_urls = {
            'Homepage': "https://github.com/lingwndr/cpia",
            "Repository": "https://github.com/lingwndr/cpia"
        },
        packages=find_packages(),
        #package_dir={"cpia": "fsts/*.fst"},
        package_data={"cpia": ["fsts/*.fst", "streats/*"]},
        install_requires=['fst-lookup>=2024.7.3'], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['Persian', 'Farsi', 'Inflection', 'Analyzer', 'Inormal', 'Formal', 'Lemmatizer', 'Converter'],
        classifiers= [
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Topic :: Software Development",
            "Topic :: Scientific/Engineering",
            "Topic :: Text Processing :: Linguistic",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: Unix",
            "Operating System :: MacOS",
        ]
)