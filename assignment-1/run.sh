#!/bin/sh

set -e
set -u

python bfs.py
echo ""
python ucs.py
echo ""
python astar.py
echo ""
echo "Done."
