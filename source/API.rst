API Documentation
=================

This section provides an overview of the API, including the main class and its associated functions.

Class SPIDER
------------------
- **Description**: Main functions of SPIDER.
- **Methods**: See the members listed above.

.. autoclass:: spider.SPIDER
   :members:

Module preprocess.py
-------------------------
- **Description**: Functions for data preparation and processing.
- **Functions**: See `idata_construct` and other available functions in the module.

.. currentmodule:: spider.preprocess
.. autofunction:: idata_construct
.. autofunction:: power_tri_init
.. autofunction:: find_interfaces
.. autofunction:: score_ot

Module svi.py
------------------
- **Description**: Functions for TF correlation and spatial variance candidate calling.

.. currentmodule:: spider.svi
.. autofunction:: tf_corr
.. autofunction:: combine_SVI