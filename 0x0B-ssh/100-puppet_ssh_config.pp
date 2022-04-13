#!/usr/bin/env bash
# Using Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d
# like you to set up your client SSH configuration file so
# that you can connect to a server without typing a
# password.

ssh -i ~/.ssh/school -oBatchMode=yes
