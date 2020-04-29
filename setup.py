from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

tests_require = ["black"]

setup(
    name="webviz-config-equinor",
    description="Webviz config Equinor theme",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/equinor/webviz-config-equinor",
    author="R&T Equinor",
    packages=find_packages(exclude=["tests"]),
    package_data={"webviz_config_equinor": ["assets/*"]},
    entry_points={
        "webviz_config_themes": ["equinor_theme = webviz_config_equinor:equinor_theme"]
    },
    install_requires=["webviz-config>=0.0.48"],
    tests_require=tests_require,
    extras_require={"tests": tests_require},
    setup_requires=["setuptools_scm~=3.2"],
    python_requires="~=3.6",
    use_scm_version=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: Other/Proprietary License",
    ],
)
