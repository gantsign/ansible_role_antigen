Ansible Role: Antigen
=======================

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-antigen/master/LICENSE)

Role to install the [Antigen](http://antigen.sharats.me/) plugin manger for Zsh
and use it to configure Zsh.

Requirements
------------

* Ansible >= 2.4

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Trusty (14.04)
            * Xenial (16.04)
            * Bionic (18.04)

    * RedHat Family

        * CentOS

            * 7

        * Fedora

            * 28

    * SUSE Family

        * OpenSUSE

            * 42.2

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role:

```yaml
# Antigen is installed per user so you need to specify the users to install it for
users:
  - username: # The username of the user to install Antigen for
    antigen_libraries:
      - name: # The name of the library (e.g. oh-my-zsh or prezto) must be unique
        url: # Optional. If you're using a custom library you must specify the Git URL
        args: # Optional. Command line arguments to pass to Antigen
          - '--exampleParam1'
          - 'paramValue1' # example with value passed as a separate arg
          - '--exampleParam2=paramValue2' # example with value passed in the same arg
        env: # Optional. Environnement variables to set
          EXAMPLE_ENV1: 'envValue1'
          EXAMPLE_ENV2: '"${HOME}/.example"' # the single quotes are for YAML the double quotes are for the shell
      # more libraries here
    antigen_theme:
      name: # The name of the library (e.g. one of the themes that come with Oh-My-Zsh)
      url: # Optional. If the theme doesn't come with Oh-My-Zsh you must specify the Git URL
      env: {} # Optional. Environnement variables to set
    antigen_bundles:
      - name: # The name of the Antigen bundle (e.g. one of the plugins that come with Oh-My-Zsh)
        url: # Optional. If the it's not one of the Oh-My-Zsh plugins you must specify the URL (use owner/repo shorthand for GitHub)
        location: # Optional. The directory in the repository containing the plugin
        branch: # Optional. Git branch to checkout.
        tag: # Optional. Git tag to checkout (takes preference over branch)
        args: [] # Optional. Command line arguments to pass to Antigen
        env: {} # Optional. Environnement variables to set
      # more bundles here
  # more users here
```

Example Playbooks
-----------------

The following achieves the same as the example in the Antigen
[README.mkd](https://github.com/zsh-users/antigen/blob/develop/README.mkd#usage).

```yaml
- hosts: servers
  roles:
    - role: gantsign.antigen
      users:
        - username: example
          antigen_libraries:
            - name: oh-my-zsh
          antigen_theme:
            name: robbyrussell
          antigen_bundles:
            # Bundles from the default repo (robbyrussell's oh-my-zsh).
            - name: git
            - name: heroku
            - name: pip
            - name: lein
            - name: command-not-found
            # Syntax highlighting bundle.
            - name: zsh-syntax-highlighting # `name` is required (any valid file name will do so long as it's unique for the bundles)
              url: zsh-users/zsh-syntax-highlighting
```

The following achieves the same as the example in the `gantsign.oh-my-zsh` role
[README.md](https://github.com/gantsign/ansible-role-oh-my-zsh/blob/master/README.md#example-playbook)

```yaml
- hosts: servers
  roles:
    - role: gantsign.antigen
      users:
        - username: example
          antigen_libraries:
            - name: oh-my-zsh
              env:
                DISABLE_AUTO_UPDATE: '"true"' # Optional (this was hard-coded in the .zshrc of the `gantsign.oh-my-zsh` role)
          antigen_theme:
            name: robbyrussell # This role has no default theme (unlike the `gantsign.oh-my-zsh` role)
          antigen_bundles:
            - name: git # This role has no default bundles/plugins (unlike the `gantsign.oh-my-zsh` role)
```


More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

To test this role run the following command from the project root:

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
