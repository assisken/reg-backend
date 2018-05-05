#!/usr/bin/env bash
pass="$(mkpasswd $2)"

sudo useradd -p ${pass} -m -s /bin/bash $1

sudo edquota -p examplestudent $1