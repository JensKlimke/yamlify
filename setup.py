from setuptools import setup, find_packages

setup(
    name="yamlify",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["markdown", "pyyaml", "Jinja2"],
    entry_points={
        "console_scripts": [
            "yamlify=yamlify:main",
        ],
    },
)
