#!/bin/sh
# CSCE 4613 Artificial Intelligence Assignment 1
# Manuel Serna-Aguilera, Guadalupe Torres
#
# Execute this script to perform the below three searches on the same graph.

set -e
set -u

python bfs.py
echo ""
python ucs.py
echo ""
python astar.py
echo ""
echo "Done."
