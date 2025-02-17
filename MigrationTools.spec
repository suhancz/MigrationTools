Summary: Migration scripts for LDAP
Name:      migrationtools
Version:   42
Release:   2
Source: https://github.com/suhancz/MigrationTools/archive/refs/heads/master.zip
URL:       http://www.padl.com/
License: BSD
Group: Networking/Utilities
BuildRoot: /tmp/rpm-%{name}-root
Prefix: /usr/local

%description
The MigrationTools are a set of Perl scripts for migrating users, groups,
aliases, hosts, netgroups, networks, protocols, RPCs, and services from 
existing nameservices (flat files, NIS, and NetInfo) to LDAP. 

%prep
export RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/%{name}
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/%{name}

%setup

%build

%install
export RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local/%{name}
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/%{name}
cp -a migrate_* $RPM_BUILD_ROOT/usr/local/%{name}
cp -a README.md $RPM_BUILD_ROOT/usr/share/doc/%{name}/README

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/local/%{name}

%doc README
