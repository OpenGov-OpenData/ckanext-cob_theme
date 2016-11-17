=============
ckanext-cob_theme
=============

.. Put a description of your extension here:
   What does it do? What features does it have?
   Consider including some screenshots or embedding a video!


------------
Requirements
------------

Compatible with CKAN 2.3+

Install the ckanext-showcase extension


------------
Development Installation
------------

To install ckanext-cob_theme:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Download the ckanext-cob_theme github repository::

     cd /usr/lib/ckan/default/src
     git clone https://github.com/Ontodia/ckanext-cob_theme.git

3. Install the extension into your virtual environment::

     cd ckanext-cob_theme
     python setup.py develop

4. Add ``cob_theme`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

5. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


---------------
Config Settings
---------------

Document any optional config settings here. For example::

    # The minimum number of hours to wait before re-checking a resource
    # (optional, default: 24).
    ckanext.cob_theme.some_setting = some_default_value
