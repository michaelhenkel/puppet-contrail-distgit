%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-contrail
%global commit c0f7cde686c20ce139c184c688e9f7d13dcd0743
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-contrail
Version:        1.0.0
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module for Juniper OpenContrail
License:        Apache-2.0

URL:            https://github.com/redhat-cip/puppet-contrail

Source0:        https://github.com/redhat-cip/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       puppet-inifile
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for Juniper OpenContrail

%prep
%setup -q -n %{name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/contrail/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/contrail/



%files
%{_datadir}/openstack-puppet/modules/contrail/


%changelog
* Tue Sep 20 2016 Haikel Guemar <hguemar@fedoraproject.org> - 1.0.0-1.c0f7cde.git
- Newton update 1.0.0 (c0f7cde686c20ce139c184c688e9f7d13dcd0743)


