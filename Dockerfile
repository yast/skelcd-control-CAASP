# FIXME: switch to yastdevel/cpp:caasp-1_0 when available to avoid running
# useless Ruby checks
FROM yastdevel/ruby:caasp-1_0
COPY . /usr/src/app
