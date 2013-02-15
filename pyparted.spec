Summary: Python module for GNU parted
Name:    pyparted
Version: 3.8
Release: 7
License: GPLv2+
Group:   Development/Python
URL:     http://fedorahosted.org/pyparted

Source0: http://fedorahosted.org/releases/p/y/%{name}/%{name}-%{version}.tar.gz

Patch1: 0001-Add-support-for-new-disk-flag-PED_DISK_GPT_PMBR_BOOT.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(id -u -n)
BuildRequires: python-devel
BuildRequires: parted-devel >= 3.0-6
BuildRequires: pkgconfig
Obsoletes:	python-parted

%description
Python module for the parted library.  It is used for manipulating
partition tables.

%prep
%setup -q
%patch1 -p1

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{python_sitearch}/_pedmodule.so
%{python_sitearch}/parted
%{python_sitearch}/%{name}-%{version}-*.egg-info

%changelog
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
