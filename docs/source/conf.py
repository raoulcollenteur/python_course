# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Python, gwrepy and pastas"
copyright = "2026, SGF"
author = "Erik Toller, Anders Retzner, and Raoul Collenteur"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx_design",
    "myst_nb",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "navigation_depth": 4,
    "collapse_navigation": False,
    "sticky_navigation": True,
}

# -- Zip the notebook files for download ------------------------------------------------
# This will create a zip file of the notebook files so that they can be downloaded from the documentation.
from pathlib import Path
import zipfile

HERE = Path(__file__).parent

download_dir = HERE / "downloads"
download_dir.mkdir(parents=True, exist_ok=True)

notebooks_zip = download_dir / "notebooks.zip"

with zipfile.ZipFile(notebooks_zip, "w", zipfile.ZIP_DEFLATED) as zf:
    for notebook in HERE.rglob("*.ipynb"):
        if "downloads" not in notebook.parts:
            zf.write(notebook, arcname=notebook.name)

html_extra_path = ["downloads"]