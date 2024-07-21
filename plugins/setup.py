from setuptools import setup, find_packages

setup(
    name='mkdocs-publications-sort',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'publications-sort = publications_sort.plugin:PublicationsSortPlugin'
        ]
    },
    install_requires=[
        'mkdocs>=1.0.4',
        'beautifulsoup4',
        'multisort'
    ]
)
