#!/bin/sh

module purge
module load gompic/2016.03
module=OpenMPI
version=2.0.0
module load $module/$version

if [ $? != 0 ]; then
	echo "unable to load module $module/$version"
	exit 1
fi

mpic++ -v
if [ $? != 0 ]; then
	echo "Unable to run mpic++ -v"
	exit 1
fi

