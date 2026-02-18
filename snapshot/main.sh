!/bin/bash

{
echo "===== DATE ====="
date

echo "===== INSTALLED PACKAGES ====="
dpkg -l 2>/dev/null || rpm -qa

echo "===== ENVIRONMENT VARIABLES ====="
printenv | sort

echo "===== ACTIVE USERS ====="
who
} > snapshot_$(date +%F_%H-%M-%S).txt
