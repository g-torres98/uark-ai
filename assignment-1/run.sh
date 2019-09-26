#!/bin/sh

set -e
set -u

#python main.py
python bfs.py
python ucs.py
python astar.py
echo "Done."
