from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pyomopcdm",
    description="OHDSI OMOP Common Data Model (Version 5.3, 5.4, 6.0) ORM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://github.com/DZD-eV-Diabetes-Research/pyomopcdm-docs/",####
        "Source": "https://github.com/DZD-eV-Diabetes-Research/pyomopcdm",
    },
    url="https://dzd-ev.github.io/dict2graph-docs/",
    author="Yaroslav Zdravomyslov",
    author_email="yaroslav.zdravomyslov@helmholtz-munich.de",
    license="MIT",
    packages=["pyomopcdm"],
    install_requires=[
        "sqlalchemy",
    ],
    extras_require={
        "tests": ["pytest", "deepdiff"],
        "docs": [
            "mkdocs",
            "mkdocstrings[python]",
            "mkdocs-autorefs",
            "mkdocs-material",
        ],
    },
    python_requires=">=3.9",
    zip_safe=False,
    include_package_data=True,
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        # "local_scheme": "node-and-timestamp"
        "local_scheme": "no-local-version",
        "write_to": "version.py",
    },
    setup_requires=["setuptools_scm"],
)
