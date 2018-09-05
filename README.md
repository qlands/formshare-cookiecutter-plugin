# FormShare Plugins Template

A Cookiecutter (project template) for creating FormShare plugins.

Requirements
------------

* Python 3.6
* [FormShare](https://github.com/qlands/formshare)
* [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

Usage
-----

1. Generate a FormShare plugin project, following the prompts from the command
    ```sh
    $ cookiecutter https://github.com/qlands/formshare-cookiecutter-plugin
    ```
2. Finish configuring the plugin by creating a virtual environment and installing your new project. 
    ```sh
    $ . ./formshare_virtual_env/bin/activate
    $ cd myFormSharePlugin
    $ python setup.py develop
```
    Add the plugin to the FormShare list of plugins by editing the following line in development.ini or production.ini
    ```
        #formshare.plugins = examplePlugin
        formshare.plugins = myformshareplugin
    ```
3. Run your FormShare
