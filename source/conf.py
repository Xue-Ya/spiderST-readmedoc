# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'spider-st'
copyright = '2023, Li Shiying'
author = 'Li Shiying'
release = 'v0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['recommonmark', 'sphinx_markdown_tables', "nbsphinx",
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