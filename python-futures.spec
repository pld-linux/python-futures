#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Backport of the concurrent.futures package from Python 3.2
Summary(pl.UTF-8):	Backport pakietu concurrent.futures z Pythona 3.2
Name:		python-futures
Version:	3.2.0
Release:	1
License:	PSF v2
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/futures/
Source0:	https://files.pythonhosted.org/packages/source/f/futures/futures-%{version}.tar.gz
# Source0-md5:	d1b299a06b96ccb59f70324716dc0016
URL:		https://github.com/agronholm/pythonfutures
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The concurrent.futures module provides a high-level interface for
asynchronously executing callables.

%description -l pl.UTF-8
Moduł concurrent.futures udostępnia wysokopoziomowy interfejs do
asynchronicznego wykonywania procedur.

%package apidocs
Summary:	API documentation for Python concurrent.futures module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona concurrent.futures
Group:		Documentation

%description apidocs
API documentation for Python concurrent.futures module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona concurrent.futures.

%prep
%setup -q -n futures-%{version}

%build
%py_build

%if %{with tests}
%{__python} test_futures.py
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py_sitescriptdir}/concurrent
%{py_sitescriptdir}/futures-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
