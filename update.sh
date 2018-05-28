#!/usr/bin/env bash

git pull
python3 manage.py collectstatic
echo "Now do:"
echo "sudo systemctl stop stauth"
echo "sudo systemctl start stauth"