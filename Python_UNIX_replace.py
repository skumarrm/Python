import os
import subprocess

def update_env2(script):
    #pipe1 = subprocess.Popen(". %s; env -0" % script, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")
    pipe1 = subprocess.Popen(". %s; env" % script, stdout=subprocess.PIPE, shell=True, executable="/bin/bash")

    output = pipe1.communicate()[0]
    #env = dict((line.split("=", 1) for line in output.splitlines()))
    env = dict((line.split("=", 1) for line in output.split('\0')))

    os.environ.update(env)

update_env2("C:\\Users\\smallisudarsan@paypal.com\\Documents\\env_test.sh")
