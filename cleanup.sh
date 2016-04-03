#!/bin/bash

#------------------------------------------#
# Этот файл является частью CMS Cirno v9.0 #
# © 2016 https://github.com/WST            #
# Распространяется на условиях MIT License #
#-------------------------------------------

find . -type f -name '*.pyc' -delete
find . -name '__pycache__' -type d -delete
echo "done"
