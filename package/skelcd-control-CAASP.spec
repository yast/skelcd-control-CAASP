#
# spec file for package skelcd-control-CAASP
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


######################################################################
#
# IMPORTANT: Please do not change the control file or this spec file
#   in build service directly, use
#   https://github.com/yast/skelcd-control-CAASP repository
#
#   See https://github.com/yast/skelcd-control-CAASP/blob/master/CONTRIBUTING.md
#   for more details.
#
######################################################################

Name:           skelcd-control-CAASP
# xmllint (for validation)
BuildRequires:  libxml2-tools
# RNG validation schema
BuildRequires:  yast2-installation-control >= 4.0.0

%if !0%{?is_susecaasp}
# xsltproc - for building control.Kubic.xml from control.CAASP.xml
BuildRequires:  libxslt-tools
BuildRequires:  diffutils
# we need to copy some parts from the openSUSE control.xml to Kubic
BuildRequires:  skelcd-control-openSUSE
%endif

######################################################################
#
# Here is the list of Yast packages which are needed in the
# installation system (inst-sys) for the Yast installer
#

# SLES specific Yast packages needed in the inst-sys
# to provide the functionality needed by this control file
Requires:       yast2-registration
%if 0%{?is_susecaasp}
Requires:       yast2-theme-SLE
%else
Requires:       yast2-branding-openSUSE
Requires:       yast2-qt-branding-openSUSE
%endif

# the CaaSP specific packages
Requires:       yast2-caasp

# Generic Yast packages needed for the installer
Requires:       autoyast2
Requires:       yast2-add-on
Requires:       yast2-buildtools
Requires:       yast2-devtools
Requires:       yast2-fcoe-client
# For creating the AutoYast profile at the end of installation (bnc#887406)
Requires:       yast2-firewall
# instsys_cleanup
Requires:       yast2-installation >= 3.1.217.9
Requires:       yast2-iscsi-client
Requires:       yast2-kdump
Requires:       yast2-multipath
Requires:       yast2-network >= 3.1.42
Requires:       yast2-nfs-client
Requires:       yast2-ntp-client
Requires:       yast2-proxy
Requires:       yast2-services-manager
Requires:       yast2-slp
Requires:       yast2-trans-stats
Requires:       yast2-tune
Requires:       yast2-update
Requires:       yast2-users
Requires:       yast2-x11
# Ruby debugger in the inst-sys (FATE#318421)
Requires:       rubygem(%{rb_default_ruby_abi}:byebug)
# Install and enable xrdp by default (FATE#320363)
Requires:       yast2-rdp

# Ensure no two skelcd-control-* packages can be installed in the same time,
# an OBS check reports a file conflict for the /CD1/control.xml file from
# the other packages.
Conflicts:      product_control
Provides:       product_control

# Architecture specific packages
#
%ifarch s390 s390x
Requires:       yast2-reipl >= 3.1.4
Requires:       yast2-s390
%endif

%ifarch %ix86 x86_64
Requires:       yast2-vm
%endif

#
######################################################################

Url:            https://github.com/yast/skelcd-control-CAASP
AutoReqProv:    off
Version:        15.0.6
Release:        0
Summary:        The CaaSP control file needed for installation
License:        MIT
Group:          Metapackages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.bz2

%description
The package contains the CaaSP control file needed for installation.

%prep

%setup -n %{name}-%{version}

%if !0%{?is_susecaasp}
%build
# build control.Kubic.xml from control.CAASP.xml
make -C control control.Kubic.xml
# display the changes (just for easier debugging)
# don't fail, a difference is expected
diff -u control/control.CAASP.xml control/control.Kubic.xml || :
%endif

%check
#
# Verify syntax
#
make -C control check

%install
#
# Add control file 
#
%if 0%{?is_susecaasp}
mkdir -p $RPM_BUILD_ROOT/usr/lib/skelcd/CD1
install -m 644 control/control.CAASP.xml $RPM_BUILD_ROOT/usr/lib/skelcd/CD1/control.xml
%else
mkdir -p $RPM_BUILD_ROOT/CD1
install -m 644 control/control.Kubic.xml $RPM_BUILD_ROOT/CD1/control.xml
%endif

# install LICENSE (required by build service check)
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/doc/packages/%{name}
install -m 644 LICENSE $RPM_BUILD_ROOT/%{_prefix}/share/doc/packages/%{name}

%files
%defattr(644,root,root,755)
%if 0%{?is_susecaasp}
%dir /usr/lib/skelcd
/usr/lib/skelcd/CD1
%else
/CD1
%endif
%doc %dir %{_prefix}/share/doc/packages/%{name}
%doc %{_prefix}/share/doc/packages/%{name}/LICENSE

%changelog
