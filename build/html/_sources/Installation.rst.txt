Installation
=====================================

SPIDER requires Python version over 3.7 to run.

Prerequisite
----------------

.. code-block:: console

    conda create -n spider python=3.8
    conda activate spider
    conda install -c conda-forge somoclu fa2

Make sure you have scgco installed with 

.. code-block:: console
   
    pip install Cython
    SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=TRUE \ 
        pip install sklearn
    pip install scgco

If you have problem installing the pygco package required by scgco, try clone the pygco repo, in which you need to change the name in the setup function in setup.py from gco-wrapper to pygco, and install pygco with setup.py

.. code-block:: console
   
    git clone https://github.com/Borda/pyGCO.git
    cd pyGCO
    <!-- change name in setup.py from gco-wrapper to pygco -->
    pip install -r requirements.txt
    python setup.py install

To also use the R packages in SPIDER, you need to first install:

.. code-block:: r
    
    if (!require("BiocManager", quietly = TRUE))
        install.packages("BiocManager")
    BiocManager::install("SpatialExperiment")
    BiocManager::install("scran")
    BiocManager::install("nnSVG")

    install.packages('devtools')
    devtools::install_github('xzhoulab/SPARK')
    devtools::install_github('linxihui/NNLM')
    devtools::install_github('ZJUFanLab/SpaTalk')

PyPI
----------------
SPIDER is availabel on PyPI:

.. code-block:: python

    pip install spider-st