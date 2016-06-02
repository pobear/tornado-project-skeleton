#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement
import sys
import os
from fabric.api import *

sys.path.insert(0, os.getcwd())
CMD_PYLINT = 'pylint'


@task
def vagrant():
    """Vagrant environment"""
    env.environment = 'local'
    env.user = 'vagrant'
    env.hosts = ['127.0.0.1:2222']
    result = local('vagrant ssh-config | grep IdentityFile', capture=True)
    env.key_filename = result.split()[1]


@task
def clean():
    """Remove temporary files."""
    for root, dirs, files in os.walk('.'):
        for name in files:
            if name.endswith('.pyc') or name.endswith('~'):
                os.remove(os.path.join(root, name))


@task
def devserver(port=8888, logging='debug'):
    """Start the server in development mode."""
    run('python run.py --port=%s --logging=%s' % (port, logging))


@task
def mo():
    pass


@task
def po():
    pass
