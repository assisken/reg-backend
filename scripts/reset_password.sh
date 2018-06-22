#!/usr/bin/env bash
PASS="$2"
USER="$1"

echo "${USER}:${PASS}" | chpasswd