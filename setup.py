import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


project_urls = {
    'Source Code':      'https://github.com/bicarlsen/easy-biologic',
    'Bug Tracker':      'https://github.com/bicarlsen/easy-biologic/issues'
}


setuptools.setup(
    name = "easy-biologic",
    version = "0.1.1",
    author = "Brian Carlsen",
    author_email = "carlsen.bri@gmail.com",
    description = "Controller class for communicating with BioLogic devices.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    keywords = [ 'biologic' ],
    url = "",
    project_urls = project_urls,
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    install_requires = [],
    package_data = {
        'easy_biologic': [
            'techniques/*'
        ]
    }
)