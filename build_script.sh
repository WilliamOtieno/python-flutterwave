#!/bin/sh

rm -rf dist/
rm -rf *.egg-info

python -m build
