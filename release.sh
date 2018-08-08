#!/bin/bash

echo "Have you updated changelog?"
echo "Have you updated the version in setup.py?"
echo "Have you updated README & Docs?"
read -sn 1 -p "Press any key to continue..."
echo

VERSION=`cat setup.py | grep version | grep -o "[0-9}*\.[0-9]*\.[0-9]*"`
TAG_VERSION=`echo $VERSION| sed 's/\./_/g'`
echo "Version: " $VERSION
echo "Tag Version: " $TAG_VERSION
git tag -s version-$TAG_VERSION -m "Version $VERSION"
git push --tags origin version-$TAG_VERSION

python setup.py sdist upload
