#!/usr/bin/env bash
PASS="$(mkpasswd $2)"
USER="$1"

useradd -p ${PASS} -m -g students -s /bin/bash ${USER}
#sudo edquota -p examplestudent ${USER}

mkdir -p /home/${USER}/www/${USER}.mati.su
chown -R ${USER}:students /home/${USER}
chmod -R 705 /home/${USER}