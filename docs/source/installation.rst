Installing Python
=================

This guide explains how to install Python on Windows.


Installing Python on Windows
----------------------------

The current Python documentation recommends the Python Install Manager
for installations obtained directly from the Python project.

#. Open the Python downloads page:

   `Download Python <https://www.python.org/downloads/>`_

#. Download the Python Install Manager.

#. Open the downloaded installation file.

#. Follow the installation instructions.

#. Open a new Command Prompt or PowerShell window.

#. Verify the installation:

   .. code-block:: powershell

      python --version

#. Check that the Python launcher is available:

   .. code-block:: powershell

      py --version

If both commands are available, prefer ``python`` in the examples in
this documentation.

Getting Started
------------------

This course uses `uv` to manage Python packages and environments.

Start by going to the directory where you want to create your course environment.

```{tip}
   You can open a terminal in the desired directory by holding down the **Shift** key, right-clicking in the folder, and selecting **Open PowerShell window here**. Or by typing `cmd` in the address bar of the folder and pressing **Enter**.
```

Then, install `uv` by running the following command in your terminal or command prompt:
```bash
pip install uv
```

Once `uv` is installed, you can create a new environment by navigating to the course directory and running the following command:
```bash
uv venv .venv
```

Once the environment has been created we will install the required packages for this course, including Jupyter Lab, by running:
```bash
uv pip install jupyterlab gwrefpy pastas tqdm ipywidgets tornado==6.4.2
```

After installation, active the environment by running:
```bash
".venv/Scripts/activate"
```

```{note}
   If you are using PowerShell, you may not need the quotes around the command can can use `.\.venv\Scripts\activate` instead.
```

and start Jupyter Lab by running:
```bash
jupyter lab
```
An instance of Jupyter Lab will open in your default web browser, where you can create new notebooks or open existing ones.

Additional information on installing and using Jupyter Lab can be found in the [official documentation](https://jupyter.org/install).


Continue to :doc:`jupyter_notebooks` to run Python interactively, execute
scripts, and create a virtual environment.