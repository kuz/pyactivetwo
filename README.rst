==================================================================
pyactivetwo: Python library for reading signal from BioSemi ActiveTwo EEG device
==================================================================


Installation
------------

The easiest way to install is via ``easy_install`` or ``pip``::

    $ easy_install pyactivetwo

Usage
-----

Turn on the BioSemi ActiveTwo device.
Start BioSemi ActiView and configure sampling rate and other important parameters to your liking. Pay special attention to the "TCP Server" tab. The parameters should correspond with the parameters you inialize `ActiveTwo` object with.
Have a look at the ``examples/example.py`` for the minimal usage example.
