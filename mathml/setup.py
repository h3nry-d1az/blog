from setuptools import setup

setup(
    name="mkdocs-mathml-plugin",
    version="0.1.0",
    py_modules=["mathml_plugin"],
    install_requires=["mkdocs>=1.0.0", "latex2mathml>=3.0.0"],
    entry_points={
        "mkdocs.plugins": [
            "mathml = mathml_plugin:MathMLPlugin",
        ]
    },
)
