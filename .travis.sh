#! /bin/bash

set -e -x

if [ "$BUILD_FLAVOR" == "kubic" ]; then
  # build the file
  make -C control control.Kubic.xml
  # pretend we are running in an openSUSE Kubic build
  echo "%is_susecaasp 0" >> ~/.rpmmacros
elif [ "$BUILD_FLAVOR" == "caasp" ]; then
  # pretend we are running in a SUSE CaaSP build
  echo "%is_susecaasp 1" >> ~/.rpmmacros
else
  echo "Uknown BUILD_FLAVOR: $BUILD_FLAVOR"
  exit 1
fi

# validate the control file(s)
make -C control check

# build the package
# the "yast-travis-ruby" script is included in the base yastdevel/ruby image
# see https://github.com/yast/docker-yast-ruby/blob/master/yast-travis-ruby
yast-travis-ruby
