"""Sphinx configuration."""
project = "Hypermodern Python Test"
author = "Carlos Jourdan"
copyright = "2023, Carlos Jourdan"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
