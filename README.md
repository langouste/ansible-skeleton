Ansible skeleton
================

A code base for ansible projects that include :

* Vagrantfile
* Docker support
* Testinfra testing

Usage
-----

### 1. Install requirements

`Docker`, `Vagrant` and `Pip` have to be installed

Install python requirements :

```bash
$ python3 -m pip install virtualenv
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

This install virtualenv on your system and create an isolated environment with python requirements.

### 2. Run

Start a container and provision it with Ansible :

```bash
$ vagrant up
```

Launch tests :

```bash
py.test -v
```

### 3. Code

Code your infra and run playbooks with `vagrant provision`

Extra to this ansible-playbook command can be used directly : `ansible-playbook site.yml`.

Write assert in `*_test.py` files `py.test` will run them within the container using Testinfra's Ansible connection backend.

Ressources
----------

**Dockerfile** : [langouste/docker-vagrant-ready](https://github.com/langouste/docker-vagrant-ready/blob/master/Dockerfile)
