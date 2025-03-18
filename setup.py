from setuptools import setup

setup(
    name="secops-mcp",
    version="0.1.0",
    py_modules=["secops_mcp", "main"],  # Include both modules
    install_requires=[
        "mcp",
        "secops",
    ],
    entry_points={
        "console_scripts": [
            "secops-mcp=secops_mcp:main",
        ],
    },
) 