from setuptools import setup

setup(
    name="mkdocs-geometry-plugin",
    version="0.1.0",
    py_modules=["geometry_plugin"],
    install_requires=[
        "mkdocs>=1.0.0",
        "pythagoras==0.1.0",
    ],
    entry_points={
        "mkdocs.plugins": [
            "geometry = geometry_plugin:GeometryPlugin",
        ]
    },
)
