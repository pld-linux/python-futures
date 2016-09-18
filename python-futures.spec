Summary:	Backport of the concurrent.futures package from Python 3.2
Name:		python-futures
Version:	3.0.4
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/f/futures/futures-%{version}.tar.gz
# Source0-md5:	27f0941502b3852ac78f3384e94f544e
URL:		https://github.com/agronholm/pythonfutures
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The concurrent.futures module provides a high-level interface for
asynchronously executing callables.

%prep
%setup -q -n futures-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE
%{py_sitescriptdir}/concurrent
%{py_sitescriptdir}/futures-%{version}-py*.egg-info
