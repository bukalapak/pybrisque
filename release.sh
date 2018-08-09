#!/bin/bash


echo "Have you updated changelog?"
echo "Have you updated the version in setup.py?"
echo "Have you updated README & Docs?"
read -sn 1 -p "Press any key to continue..."
echo

python setup.py sdist

if [ $1 == "test" ];
 then
    echo TEST RELEASE;
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
else
    echo PROD RELEASE;

    VERSION=`cat setup.py | grep version | grep -o "[0-9}*\.[0-9]*\.[0-9]*"`
    TAG_VERSION=`echo $VERSION| sed 's/\./_/g'`
    echo "Version: " $VERSION
    echo "Tag Version: " $TAG_VERSION
    git tag -s version-$TAG_VERSION -m "Version $VERSION"
    git push --tags origin version-$TAG_VERSION

    twine upload dist/*.tar.gz
fi
