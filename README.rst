python-webcrawler
=================

Crawls HTML pages for prices and other pieces of data.

Installation
------------

This projects uses Gradle (at least version 3.3) as its build system
along with a Docker and docker-compose wrapper for continuous
development. On Debian Linux distributions Gradle can be installed with
the following commands:

.. code:: bash

    sudo apt-get install software-properties-common
    sudo add-apt-repository ppa:cwchien/gradle
    sudo apt-get update
    sudo apt-get install default-jdk gradle=3.4-0ubuntu1

If you prefer to install Docker and docker-compose (highly recommended)
refer to the `official
instructions <https://docs.docker.com/compose/install/>`__.

Usage
-----

To use the application get the sources and install its dependencies.

.. code:: bash

    git clone https://github.com/marcbperez/python-webcrawler
    cd python-webcrawler
    sudo gradle dependencies
    gradle install

The parser can retrieve the price of calling a landline in Canada,
Germany, Iceland, Pakistan, Singapore and South Africa.

.. code:: python

    from webcrawler.parser import Parser
    from webcrawler.parserhelper import ParserHelper

    helper = ParserHelper()
    parser = Parser(helper, 'utf-8')
    canada_landline_price = parser.landline_price(helper.CANADA())

Testing
-------

Tests will be executed by default every time the project is built. To
run them manually start a new build or use Gradle's test task. For a
complete list of tasks check ``gradle tasks --all``.

.. code:: bash

    gradle test

A continuous build cycle can be executed with ``gradle --continuous``
inside a virtual environment, or with Docker.

::

    sudo docker-compose up

Troubleshooting
---------------

The `issue
tracker <https://github.com/marcbperez/python-webcrawler/issues>`__ intends
to manage and compile bugs, enhancements, proposals and tasks. Reading
through its material or reporting to its contributors via the platform
is strongly recommended.

Contributing
------------

This project adheres to `Semantic Versioning <http://semver.org>`__ and
to certain syntax conventions defined in
`.editorconfig <.editorconfig>`__. To get a list of changes refer to the
`CHANGELOG <CHANGELOG.md>`__. Only branches prefixed by *feature-*,
*hotfix-*, or *release-* will be considered:

-  Fork the project.
-  Create your new branch:
   ``git checkout -b feature-my-feature develop``
-  Commit your changes: ``git commit -am 'Added my new feature.'``
-  Push the branch: ``git push origin feature-my-feature``
-  Submit a pull request.

Credits
-------

This project is created by `marcbperez <https://marcbperez.github.io>`__ and
maintained by its `author <https://marcbperez.github.io>`__ and contributors.

License
-------

This project is licensed under the `Apache License Version
2.0 <LICENSE>`__.
