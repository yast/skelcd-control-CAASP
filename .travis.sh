#! /bin/bash

set -e -x

# validate the control file(s)
make -C control check

# build the package
# the "yast-travis-ruby" script is included in the base yastdevel/ruby image
# see https://github.com/yast/docker-yast-ruby/blob/master/yast-travis-ruby
yast-travis-ruby

