Summary: Generates large resolution images of a Minecraft map.
Name: minecraft-overviewer
Version: 0.12
Release: 3%{?dist}
Source0: %{name}-%{version}.tar.gz
License: GNU General Public License v3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Packager: Franz Dietrich <dietrich@teilgedanken.de>
Url: http://overviewer.org/
Requires: python-imaging, python2-numpy
BuildRequires: python2-devel, python-imaging-devel, python2-numpy
Provides: overviewer

%description
The Minecraft Overviewer is a command-line tool for rendering high-resolution
maps of Minecraft worlds. It generates a set of static html and image files and
uses the Google Maps API to display a nice interactive map.

%prep
%setup

%build
env CFLAGS="$RPM_OPT_FLAGS" %{__python2} setup.py build

%install
%{__python} setup.py install -O1 --root=%{buildroot}
ln -s %{_bindir}/overviewer.py %{buildroot}%{_bindir}/overviewer
ln -s %{_bindir}/overviewer.py %{buildroot}%{_bindir}/overviewer-2
ln -s %{_bindir}/overviewer.py %{buildroot}%{_bindir}/overviewer-2.7
rm -rf %{buildroot}%{_defaultdocdir}/minecraft-overviewer

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python2_sitearch}/Minecraft_Overviewer-*-*.egg-info
%{python2_sitearch}/overviewer_core
%{_bindir}/overviewer.py
%{_bindir}/overviewer
%{_bindir}/overviewer-2
%{_bindir}/overviewer-2.7
%doc README.rst COPYING.txt sample_config.py

%changelog
* Sun Apr 24 2016 Franz Dietrich <dietricf@informatik.uni-freiburg.de> 0.12-3
- new package built with tito

