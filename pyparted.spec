Summary: Python module for GNU parted
Name:    pyparted
Version: 3.10
Release: 1
License: GPLv2+
Group:   Development/Python
URL:     http://fedorahosted.org/pyparted

Source0: https://fedorahosted.org/releases/p/y/pyparted/%{name}-%{version}.tar.gz


BuildRequires: python-devel
BuildRequires: parted-devel >= 3.0-6
BuildRequires: pkgconfig
Obsoletes:	python-parted

%description
Python module for the parted library.  It is used for manipulating
partition tables.

%prep
%setup -q

%build
%make

%install
%makeinstall_std

%files
%doc AUTHORS BUGS COPYING ChangeLog NEWS README TODO
%{python_sitearch}/_pedmodule.so
%{python_sitearch}/parted
%{python_sitearch}/%{name}-%{version}-*.egg-info

