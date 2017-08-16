Summary: Generates large resolution images of a Minecraft map.
Name: minecraft-overviewer
Version: 0.12
Release: 12%{?dist}
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
* Wed Aug 16 2017 Franz Dietrich <dietrich@teilgedanken.de> 0.12-12
- docs: various small updates to build instructions (ovdev@fratti.ch)
- docs: Clarify Ubuntu/Debian install instructions (ovdev@fratti.ch)
- Update minecraft version in gitlay-ci.yml to 1.12 (merten.fermont@gmail.com)
- Change forgotten 1.11 to 1.12 in documentation (merten.fermont@gmail.com)
- travis: Update MC version (ovdev@fratti.ch)
- textures.py: Fix beds for 1.12 (ovdev@fratti.ch)
- Update strings to 1.12 (ovdev@fratti.ch)
- docs: add a section about how to contribute (ovdev@fratti.ch)
- setup.py: remove workaround for CentOS 5 (ovdev@fratti.ch)
- readme: add API key note, small fixes (ovdev@fratti.ch)
- settingsValidators: clean up checkBadEscapes (ovdev@fratti.ch)
- Remove unused imports (ovdev@fratti.ch)
- docs: update copyright year to 2017 (ovdev@fratti.ch)
- docs: optimise PNGs (ovdev@fratti.ch)
- docs: fix two warnings during docs building (ovdev@fratti.ch)
- docs: fix code block in signs.rst (ovdev@fratti.ch)
- docs: add link to Twitter account to index.rst (ovdev@fratti.ch)
- docs: Change some http:// URLs to https:// (ovdev@fratti.ch)
- docs: remove remaining references to CentOS 5 (ovdev@fratti.ch)
- Copy el6 rpms into a better home (achin@eminence32.net)
- docs: remove CentOS 5 build instructions (ovdev@fratti.ch)
- Re-enable render CI job in master branch (achin@eminence32.net)
- Build and test rpm and deb repos during CI (achin@eminence32.net)
- genpoi: query fs caps before using FileReplacer (ovdev@fratti.ch)
- rcon: code style fixes (ovdev@fratti.ch)
- logger: reduce pillow verbosity (ovdev@fratti.ch)
- docs: fix oxipng formatting (ovdev@fratti.ch)
- world: remove redundant hashing (ovdev@fratti.ch)
- travis: stop testing for 2.6 (ovdev@fratti.ch)
- optimizeimages: add oxipng support (ovdev@fratti.ch)
- optimizeimages: code style fixes (ovdev@fratti.ch)
- Remove memcached support (ovdev@fratti.ch)
- Be more consistant in build artifact naming (achin@eminence32.net)
- Add support for concrete powder (ovdev@fratti.ch)
- Fix deprecated NumPy API warnings (ovdev@fratti.ch)
- Add terracotta and concrete blocks (ovdev@fratti.ch)
- Do an apt-get update during debian verification (achin@eminence32.net)
- More work on gitlab CI (achin@eminence32.net)
- Allow debug import (achin@eminence32.net)
- Work on windows build with gitlab CI (achin@eminence32.net)
- Replace `python` with `python2` (achin@eminence32.net)

* Thu Dec 29 2016 Franz Dietrich <dietrich@teilgedanken.de> 0.12-11
- Apply same only/except tags to `remove_render` (achin@eminence32.net)
- Improved gitlab CI which will remove renders when a branch is deleted
  (achin@eminence32.net)
- Some minor changes based on github comment feedback (achin@eminence32.net)
- Be sure to exit with a non-zero code on build error (achin@eminence32.net)
- Need to catch CorruptNBTError in both paths (tswsl1989@sucs.org)
- Added some explanatory text about corrupt worlds (achin@eminence32.net)
- Better error handling of errors when a world fails to open.
  (achin@eminence32.net)
- Updating linux build docs (achin@eminence32.net)

* Thu Dec 15 2016 Franz Dietrich <enaut.w@googlemail.com> 0.12-10
- Enable gitlab CI (achin@eminence32.net)
- optimizeimages: support pngnq-s9 (ovdev@fratti.ch)
- genPOI: expose uuid value for filter functions (ovdev@fratti.ch)
- genPOI/docs: Handle new sign id values (ovdev@fratti.ch)
- Change shebang to python2 instead of python (ovdev@fratti.ch)
- Update strings and items to 1.11 (mvndrstl@gmail.com)
- Add new 1.11 blocks (mvndrstl@gmail.com)

* Sat Aug 13 2016 Franz Dietrich <dietrich@teilgedanken.de> 0.12-9
- Update text for 1.10 (code@manuelgu.eu)

* Thu Jul 21 2016 Franz Dietrich <dietrich@teilgedanken.de> 0.12-8
- Update CONTRIBUTORS.rst information (ovdev@fratti.ch)
- Update docs version and copyright year (ovdev@fratti.ch)
- Make command line option docs more complete (ovdev@fratti.ch)
- Add -q alias for --quiet to genPOI (ovdev@fratti.ch)
- Update client jar version in documentation (ovdev@fratti.ch)

* Sun Jun 12 2016 Franz Dietrich <enaut.w@googlemail.com> 0.12-7
- bump overviewer.h version, textures.py version (aargri@gmail.com)
- fixed typo in biomes.h (aargri@gmail.com)
- update to 1.10 (dan@seattle.codeexception.com)
- Revert temp & humidity changes and add missing biomes (dbergl@outlook.com)
- Add new 1.7.2 biomes and update colors temp/humnidity was calculated so it
  matched the pixel at the start of each biome as shown in the color template
  (http://minecraft.gamepedia.com/File:Biomes1.7.2.png) TODO: switch to using
  coordinates in the image instead of temp/humidity (dbergl@hotmail.com)
- add new 1.10 blocks (dbergl@outlook.com)
- Fix chorus plants (tazorax@gmail.com)
- Add chorus plants and chorus flowers (tazorax@gmail.com)
- Add missing pixels between slabs (Socolin@users.noreply.github.com)
- Fix render when using rotation and crop (Socolin@users.noreply.github.com)
- create filter identifiers from render name instead of region set
  (kevin@kevinwchang.com)
- Add region directory to corruption warnings (ovdev@fratti.ch)
- fix typo from last commit, should work now (mc@680x0.com)
- add support for advpng to optimizeimages.py (mc@680x0.com)

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

