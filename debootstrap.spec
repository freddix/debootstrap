Summary:	Bootstrap a basic Debian system
Name:		debootstrap
Version:	1.0.70
Release:	1
License:	MIT-like
Group:		Applications/File
Source0:	http://ftp.debian.org/debian/pool/main/d/debootstrap/%{name}_%{version}.tar.gz
# Source0-md5:	281c1bd46a4ccf3515e132b879460c19
Source1:	devices.tar.gz
BuildRequires:	sed >= 4.0
Requires:	binutils
Requires:	wget
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Debootstrap is used to create a Debian base system from scratch,
without requiring the availability of dpkg or apt. It does this by
downloading .deb files from a mirror site, and carefully unpacking
them into a directory which can eventually be chrooted into.

%prep
%setup -q

%{__sed} -i -e "s|@VERSION@|%{version}|g" debootstrap

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_datadir}/debootstrap}

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/debootstrap
install debootstrap $RPM_BUILD_ROOT%{_sbindir}/debootstrap
install debootstrap.8 $RPM_BUILD_ROOT%{_mandir}/man8/debootstrap.8
install functions $RPM_BUILD_ROOT%{_datadir}/debootstrap
cp -a scripts $RPM_BUILD_ROOT%{_datadir}/debootstrap/scripts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO debian/copyright debian/changelog
%attr(755,root,root) %{_sbindir}/debootstrap
%dir %{_datadir}/debootstrap
%{_datadir}/debootstrap/devices.tar.gz
%{_datadir}/debootstrap/functions
%{_datadir}/debootstrap/scripts
%{_mandir}/man8/debootstrap.8*

