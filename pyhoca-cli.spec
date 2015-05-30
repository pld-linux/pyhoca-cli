Summary:	Command line X2Go client written in Python
Name:		pyhoca-cli
Version:	0.5.0.2
Release:	1
License:	AGPLv3+
Group:		Applications/Communications
Source0:	http://code.x2go.org/releases/source/pyhoca-cli/%{name}-%{version}.tar.gz
# Source0-md5:	fe00e243dddd20f5fdb68a521fd92a54
URL:		http://www.x2go.org/
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
Requires:	python-argparse
Requires:	python-setproctitle
Requires:	python-x2go
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X2Go is a server based computing environment with:
- session resuming
- low bandwidth support
- LDAP support
- client side mass storage mounting support
- client side printing support
- audio support
- authentication by smartcard and USB stick

PyHoca-CLI provides a simple and flexible command line client written
in Python that allows you to control X2Go client sessions on desktops
and thin clients.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}}
cp -p %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a man/* $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{py_sitescriptdir}/pyhoca
%dir %{py_sitescriptdir}/pyhoca/cli
%{py_sitescriptdir}/pyhoca/cli/*.py[co]
%{py_sitescriptdir}/PyHoca_CLI-%{version}-py*.egg-info
%{py_sitescriptdir}/PyHoca_CLI-%{version}-py*-nspkg.pth
%{_mandir}/man1/%{name}.1*
