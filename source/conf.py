import os
import sys
sys.path.insert(0, os.path.abspath('/home/lishiying/data6/01-interaction-v2/SPIDER/'))
print(sys.path)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'spider-st'
copyright = '2024, Li Shiying'
author = 'Li Shiying'
release = 'v0.0.2'



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',  # If you're using Google or NumPy style docstrings
    'recommonmark', 'sphinx_markdown_tables', "nbsphinx",
    "sphinx_gallery.load_style"]

templates_path = ['_templates']
exclude_patterns = []
nbsphinx_execute = 'never'




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_logo = "logo.png"
html_theme_options = {
    'logo_only': True,
    'style_nav_header_background': '#6a65d8',
}
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]