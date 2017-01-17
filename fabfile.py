#coding=utf-8
from __future__ import with_statement
from fabric.api import local, env, settings, abort, run, cd, lcd
from fabric.contrib.console import confirm
import time

# env.use_ssh_config = True
env.hosts = ['git@github.com:CG0323/jobboard.git']
env.user = 'git'
env.key_filename = 'C:\Users\mac\Documents\id_rsa_mopyfish'

def push():
    local('git add .')
    local('git commit')
    local('git push')
	
def deploy():
	push()

	
