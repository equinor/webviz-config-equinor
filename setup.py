from setuptools import setup, find_packages

setup(
    name='webviz-config-equinor',
    version='0.1',
    description='Webviz config Equinor theme',
    url='https://github.com/equinor/webviz-config-equinor',
    author='R&T Equinor',
    packages=find_packages(exclude=['tests']),
    package_data={
        'webviz_config_equinor': [
            'assets/*'
        ]},
    entry_points={
        'webviz_config_themes': [
            'equinor_theme = webviz_config_equinor:equinor_theme'
        ]
    },
    zip_safe=False
)
