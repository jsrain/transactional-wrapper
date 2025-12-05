#
# spec file for package transactional-wrapper
#
# Copyright (c) 2024 SUSE LLC
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

# old location  was /etc/YaST2/licenses/, see jsc#SLE-3067

Name:           transactional-wrapper
Summary:        Generic wrapper for calling commands which need to run in transactional update transparently
License:        MIT
Group:          System/Base
Version:        0.0.1
Release:        0
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
install -m 755 %{SOURCE1} %{buildroot}/usr/sbin/transactional-alias
install -m 644 %{SOURCE2} %{buildroot}/usr/etc/transactional-wrapper.conf
mkdir -p %{buildroot}/usr/share/doc/packages/transactional-wrapper
install -m 644 %{SOURCE3} %{buildroot}/usr/share/doc/packages/transactional-wrapper/README
mkdir -p %{buildroot}/usr/share/transactional-wrapper/configs
install -m 644 %{SOURCE100} %{buildroot}/usr/share/transactional-wrapper/configs/zypper

%files
%defattr(644,root,root,755)
%dir /usr/share/doc/packages/transactional-wrapper
%dir /usr/share/transactional-wrapper
%dir /usr/share/transactional-wrapper/configs
%attr(755, root, root) /usr/sbin/transactional-wrapper
%attr(755, root, root) /usr/sbin/transactional-alias
/usr/etc/transactional-wrapper.conf
/usr/share/doc/packages/transactional-wrapper/README
/usr/share/transactional-wrapper/configs/zypper

%changelog
