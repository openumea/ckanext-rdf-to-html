from setuptools import setup, find_packages

version = '1.0'

setup(
    name='ckanext-rdf-to-html',
    version=version,
    description="CKAN extension for the rdf-to-html plugin",
    long_description="""\
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Kim Nilsson',
    author_email='kim.nilsson@dohi.se',
    url='https://github.com/openumea/RDFtoHTML',
    license='EUPL v1.1',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.rdf_to_html'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
    ],
    entry_points=\
    """
        [ckan.plugins]
    # Add plugins here, eg
    rdf_to_html=ckanext.rdf_to_html.plugin:RDFToHTMLPlugin
    """,
)
