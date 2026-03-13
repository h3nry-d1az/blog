from setuptools import setup

setup(
    name="mkdocs-geometry-plugin",
    version="0.1.0",
    py_modules=["geometry_plugin"],
    install_requires=[
        "mkdocs>=1.0.0",
        "pythagoras @ git+https://github.com/h3nry-d1az/pythagoras.git@main",
    ],
    entry_points={
        "mkdocs.plugins": [
            "geometry = geometry_plugin:GeometryPlugin",
        ]
    },
)
