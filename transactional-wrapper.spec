#
# spec file for package transactional-wrapper
#
# Copyright (c) 2026 SUSE LLC
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


Name:           transactional-wrapper
Summary:        Wrapper for easing to port commands to transactional systems
License:        MIT
Group:          System/Base
Version:        0.0.1
Release:        0
BuildArch:      noarch
Url:		https://github.com/jsrain/transactional-wrapper/
Requires:	transactional-update

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Source0:	transactional-wrapper
Source1:	transactional-alias
Source2:	transactional-wrapper.conf
Source3:	README
Source100:	zypper


%description
Generic wrapper for calling commands which need to run in transactional update transparently

%prep

%build

%install
mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/etc
install -m 755 %{SOURCE0} %{buildroot}/usr/sbin/transactional-wrapper
%if 0%{?with_alias}
install -m 755 %{SOURCE1} %{buildroot}/usr/sbin/transactional-alias
%endif
install -m 644 %{SOURCE2} %{buildroot}/usr/etc/transactional-wrapper.conf
mkdir -p %{buildroot}/usr/share/doc/packages/transactional-wrapper
install -m 644 %{SOURCE3} %{buildroot}/usr/share/doc/packages/transactional-wrapper/README
mkdir -p %{buildroot}/usr/share/transactional-wrapper/configs
%if 0%{?with_configs}
install -m 644 %{SOURCE100} %{buildroot}/usr/share/transactional-wrapper/configs/zypper
%endif

%files
%defattr(644,root,root,755)
%dir /usr/share/doc/packages/transactional-wrapper
%dir /usr/share/transactional-wrapper
%attr(755, root, root) /usr/sbin/transactional-wrapper
%if 0%{?with_alias}
%attr(755, root, root) /usr/sbin/transactional-alias
%endif
/usr/etc/transactional-wrapper.conf
/usr/share/doc/packages/transactional-wrapper/README
%dir /usr/share/transactional-wrapper/configs
%if 0%{?with_configs}
/usr/share/transactional-wrapper/configs/zypper
%endif

%changelog
