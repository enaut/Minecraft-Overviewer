Summary: Generates large resolution images of a Minecraft map.
Name: minecraft-overviewer
Version: 0.12
Release: 6%{?dist}
Source0: %{name}-%{version}.tar.gz
License: GNU General Public License v3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Packager: Franz Dietrich <dietrich@teilgedanken.de>
Url: http://overviewer.org/
Requires: python-imaging, numpy
BuildRequires: python2-devel, python-imaging-devel, numpy
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
rm -rf %{buildroot}%{_defaultdocdir}/minecraft-overviewer

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python2_sitearch}/Minecraft_Overviewer-*-*.egg-info
%{python2_sitearch}/overviewer_core
%{_bindir}/overviewer.py
%{_bindir}/overviewer
%doc README.rst COPYING.txt sample_config.py

%changelog
* Wed May 25 2016 Franz Dietrich <dietricf@informatik.uni-freiburg.de> 0.12-6
- Fix beetroots duplication (tazorax@gmail.com)
- Implement beetroot crops Conflicts:     overviewer_core/textures.py
  (tazorax@gmail.com)
- Tweak crop rendering (achin@eminence32.net)
- Add some missing pixel between blocks (Issue #992)
  (Socolin@users.noreply.github.com)
- fix typo (lotherex@gmail.com)
- add  frosted ice, structure_block (lotherex@gmail.com)
- fix  purpur pilar orientation (lotherex@gmail.com)
- add beetroot (lotherex@gmail.com)
- fix command block (lotherex@gmail.com)
- add end_gateway (lotherex@gmail.com)
- Implement path blocks (achin@eminence32.net)
- Bump mc version in travis and textures.py error msg.  also force rebuild
  (achin@eminence32.net)
- Add some new blocks for Minecraft 1.9 (achin@eminence32.net)
- Fix command block for Minecraft 1.9 (achin@eminence32.net)
- Fix redstone dust for Minecraft 1.9 (achin@eminence32.net)
- Remove inline for estimate_blocklevel (steef@steef389.eu)
- genpoi: Fix GzipFile closing on python 2.6 (ovdev@fratti.ch)
- rcon: Throw more helpful exception if proto error (ovdev@fratti.ch)
- genPOI: Use "with" statement to close gzip files (ovdev@fratti.ch)
- rcon: Wait for buffer to fill (ovdev@fratti.ch)
- Update README.rst (tcyrus@users.noreply.github.com)
- Use FileReplacer to manage the uuid cache file (achin@eminence32.net)
- JSObserver: Add missing string formatting param (achin@eminence32.net)
- genpoi UUID improvements (achin@eminence32.net)
- Catch TypeErrors as well when loading player dat files (achin@eminence32.net)
- More Travis whacking (ovdev@fratti.ch)
- Let's whack travis with a wrench for a bit (ovdev@fratti.ch)
- Add mingw-w64 build documentation (ovdev@fratti.ch)
- Fix mingw-w64 build (ovdev@fratti.ch)
- Don't call save_cache if running with --skip-players (achin@eminence32.net)
- Small documentation bug for StructureOverlay. (enaut.w@googlemail.com)
- Hopefully a better fix for the sdist problem. (achin@eminence32.net)
- Revert "Add c_overveiwer_includes to the list of source files"
  (achin@eminence32.net)
- Add c_overveiwer_includes to the list of source files (achin@eminence32.net)
- Update signs.rst (achin@eminence32.net)
- [webassets] Updated jQuery version (ovdev@fratti.ch)
- Convert filter generator to list before passing to handleEntities to fix
  repeated iteration. Fixes #1220 . (mark.fickett@gmail.com)
- equality != assignment... (aargri@gmail.com)
- get genpoi multiprocessing working on windows (aargri@gmail.com)
- [genPOI] sort list of imports (joker@someserver.de)
- [genPOI] fix generation of multiple players (joker@someserver.de)
- [genPOI] remove unnecessary second import of json (joker@someserver.de)
- [genPOI] pass filters as list to handleManualPOI (joker@someserver.de)
- [genPOI] Work around utter plebbery (ovdev@fratti.ch)
- [genPOI] Work around JSON signs (ovdev@fratti.ch)
- genPOI: don't ignore invalid polyline point (astronouth7303@gmail.com)
- genPOI: use more pythonic ways ... (astronouth7303@gmail.com)
- genPOI: add icon and createInfoWindow support for filters
  (astronouth7303@gmail.com)
- fix lighting for flowing water and ice (aargri@gmail.com)
- Explain importing for filter functions (tim@dierks.org)
- Explain ordered nature of renders dict (tim@dierks.org)
- Don't crash if no renders/regionsets are found (achin@eminence32.net)
- Skip missing dimensions in genPOI (gizmokid2005@gmail.com)
- Skip missing dimensions (gizmokid2005@gmail.com)
- nbt array lengths are unsigned (see issue #1190) (aargri@gmail.com)
- Added information about --skip-scan to the docs (caleb.sander@gmail.com)
- Allow worlds with a version of zero (temp fix for #1194)
  (achin@eminence32.net)
- Fixed rendering regions. genPOI.py: add new line to baseMakers.js; views.js:
  add polygons, with all the features that Google provides, polylines work
  fine; regions.js: example of usage (kiskoza@sch.bme.hu)
- genPOI: Resolve UUIDs for player spawns too (ovdev@fratti.ch)
- Fix east side large mushroom rendering (tswsl1989@sucs.org)
- Add warning if Overviewer is run as root (ovdev@fratti.ch)
- Add rollbacks to tile re-arrangements (ovdev@fratti.ch)
- optimizeimages: Add documentation for jpegoptim (ovdev@fratti.ch)
- optimizeimages: Add jpegoptim interface (ovdev@fratti.ch)
- Add documentation for RConObserver (ovdev@fratti.ch)
- Added RCon Observer (ovdev@fratti.ch)
- Adding StructureOverlay an overlay to color the map according to structures.
  (enaut.w@googlemail.com)
- Missing colon from else statement. (computertechie2@gmail.com)
- Added missing comma in function call for fence gate material definition.
  (computertechie2@gmail.com)
- Update C extension version number. (computertechie2@gmail.com)
- Might as well slip a tiny bit of clean up in. (computertechie2@gmail.com)
- Added definitions for the new fence gates. Hopefully I got the C side right.
  Close #1148 (computertechie2@gmail.com)
- Lighting fixes for red sandstone stairs and slabs (achin@eminence32.net)
- Forgot texture file extensions in a couple places.
  (computertechie2@gmail.com)
- Added definitions and support for all the various red sandstone blocks.
  (computertechie2@gmail.com)
- Forgot to bump version for travis (achin@eminence32.net)
- genPOI: use filter functions on the fly (joker@someserver.de)
- genPOI: generate marker's internal name only once (joker@someserver.de)
- genPOI: use a defaultdict for markers (joker@someserver.de)
- genPOI: unite for-loops with itertools (joker@someserver.de)
- genPOI: function for doubled code for marker creation (joker@someserver.de)
- genPOI: add option --skip-players (joker@someserver.de)
- Automatic commit of package [minecraft-overviewer] minor release [0.12-5].
  (dietricf@informatik.uni-freiburg.de)
- Removing symlinks (dietricf@informatik.uni-freiburg.de)
- Automatic commit of package [minecraft-overviewer] minor release [0.12-4].
  (dietricf@informatik.uni-freiburg.de)
- python2-numpy does not exist in F23 (dietricf@informatik.uni-freiburg.de)
- Automatic commit of package [minecraft-overviewer] minor release [0.12-3].
  (dietricf@informatik.uni-freiburg.de)
- Adding RPM spec file and initialize tito (dietricf@informatik.uni-
  freiburg.de)

* Wed May 25 2016 Franz Dietrich <dietricf@informatik.uni-freiburg.de> 0.12-5
- Removing symlinks (dietricf@informatik.uni-freiburg.de)

* Sun Apr 24 2016 Franz Dietrich <dietricf@informatik.uni-freiburg.de> 0.12-4
- python2-numpy does not exist in F23 (dietricf@informatik.uni-freiburg.de)

* Sun Apr 24 2016 Franz Dietrich <dietricf@informatik.uni-freiburg.de> 0.12-3
- new package built with tito

