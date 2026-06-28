import os
import sys

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DataClassBase'
copyright = '2026, Josef Mayr'
author = 'Josef Mayr'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary']

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# change this to the respective sphinx template (original was 'alabaster')
# note that pydata requires `pip install pydata-sphinx-theme`. If you change the theme, change the
# `.github/workflows/py_lint_test.yml` step for the theme setup accordingly
html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

sys.path.insert(0, os.path.abspath('../..'))
