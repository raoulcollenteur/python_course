Installing Python
=================

This guide explains how to install Python on Windows, macOS, and Linux.

Before installing Python
------------------------

Check whether Python is already installed by opening a terminal and
running:

.. code-block:: bash

   python --version

If that command does not work, try:

.. code-block:: bash

   python3 --version

A successful command prints a version number similar to:

.. code-block:: text

   Python 3.x.y

The exact version number may be different.

.. important::

   Make sure to install Python version **3.11** or later. Some packages may not support older versions.

If Python is not installed, follow the instructions below for your operating system.

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


Continue to :doc:`running_python` to run Python interactively, execute
scripts, and create a virtual environment.