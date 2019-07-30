Summary: Generates a map viewable with a webrowser.
Name: minecraft-overviewer
Version: 0.12
Release: 26%{?dist}
Source0: %{name}-%{version}.tar.gz
License: GNU General Public License v3
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Packager: Franz Dietrich <dietrich@teilgedanken.de>
Url: http://overviewer.org/
Requires: (python3-pillow or python36-pillow), (python3-numpy or python36-numpy)
BuildRequires: gcc, (python3-devel or python36-devel), (python3-pillow-devel or python36-pillow-devel), (python3-numpy or python36-numpy)
Provides: overviewer

%description
The Minecraft Overviewer is a command-line tool for rendering high-resolution
maps of Minecraft worlds. It generates a set of static html and image files and
uses the Leaflet viewer to display an interactive map.

%prep
%setup

%build
%py3_build

%install
%py3_install
ln -s %{_bindir}/overviewer.py %{buildroot}%{_bindir}/overviewer
rm -rf %{buildroot}%{_defaultdocdir}/minecraft-overviewer


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python3_sitearch}/Minecraft_Overviewer-*-*.egg-info
%{python3_sitearch}/overviewer_core
%{_bindir}/overviewer.py
%{_bindir}/overviewer
%doc README.rst COPYING.txt sample_config.py

%changelog
* Tue Jul 30 2019 Franz Dietrich <dietrich@teilgedanken.de> 0.12-26
- fix build on centos (dietrich@teilgedanken.de)

* Mon Jul 29 2019 Franz Dietrich <dietrich@teilgedanken.de> 0.12-25
- Fixing issue with building (dietrich@teilgedanken.de)

* Mon Jul 29 2019 Franz Dietrich <dietrich@teilgedanken.de> 0.12-24
- specfile changes (dietrich@teilgedanken.de)
- updated spec (dietrich@teilgedanken.de)

* Mon Jul 29 2019 Franz Dietrich <dietrich@teilgedanken.de> 0.12-23
- travis: use xenial after all because python 3.5 (ovdev@fratti.ch)
- observer: use == 0, not is 0 (ovdev@fratti.ch)
- travis: use bionic and test for 3.8-dev (ovdev@fratti.ch)
- docs/building: clarify Linux build instructions (ovdev@fratti.ch)
- world: fix rail orientations (ovdev@fratti.ch)
- test_world: disable broken test case (ovdev@fratti.ch)
- Get rid of config global state, improve tests (ovdev@fratti.ch)
- assetmanager: code style fixes (ovdev@fratti.ch)
- dispatcher: code style fixes (ovdev@fratti.ch)
- observer: code style fixes (ovdev@fratti.ch)
- remove vestigial python2 references (ovdev@fratti.ch)
- rename configParser to config_parser (ovdev@fratti.ch)
- configParser: code style and string changes (ovdev@fratti.ch)
- Implement some mossy blocks (ovdev@fratti.ch)
- Add force_writable argument to mirror_dir (ovdev@fratti.ch)
- add workstations: blastfurnace, smoker, lectern, loom, stonecutter and
  grindstone (programming18@verdunkelbar.de)
- overviewer_core/__init__: code style fixes (ovdev@fratti.ch)
- signals: whitespace fixes (ovdev@fratti.ch)
- observer: don't divide by zero in RConObserver (ovdev@fratti.ch)
- util.js: actually run the ready queue (ovdev@fratti.ch)
- Catch KeyboardInterrupt so we don't barf a trace (ovdev@fratti.ch)
- util.js: remove some obsolete stuff (ovdev@fratti.ch)
- util.js: don't specify a map minzoom of 0 (ovdev@fratti.ch)
- world: add __lt__ to RegionSetWrapper for genPOI (ovdev@fratti.ch)
- genPOI: respect crop option (ovdev@fratti.ch)
- Bump C extension version to 68 (ovdev@fratti.ch)
- Fix GCC signed-unsigned and pointer-warnings (#1608) (wunkolo@gmail.com)
- Bump C extension version to 67 (ovdev@fratti.ch)
- world: remove redundant stride 1 in iteration (ovdev@fratti.ch)
- world: use numpy.empty instead of numpy.zeros (ovdev@fratti.ch)
- world: optimise bad block translation code (ovdev@fratti.ch)
- textures: fix texturepath option not being used (ovdev@fratti.ch)
- rcon: fix for python 3 (ovdev@fratti.ch)
- nbt: catch EOFError because of gzip streams (ovdev@fratti.ch)
- textures: implement proper fallback loading (ovdev@fratti.ch)
- src/primitives/base: don't try to free nullpointer (ovdev@fratti.ch)
- world: fix those pesky poi warnings (ovdev@fratti.ch)
- Add "center" config option (ovdev@fratti.ch)
- textures: greatly simplify find_file and friends (ovdev@fratti.ch)
- textures: cache when a texture couldn't be found (ovdev@fratti.ch)
- textures: try more than the most recent Minecraft (ovdev@fratti.ch)
- genPOI: hopefully fix binary string nonsense (ovdev@fratti.ch)
- Implement straggler standard integer types (Wunkolo@gmail.com)
- Implement standard C boolean type (Wunkolo@gmail.com)
- Propagate block, bool, standard integer types across codebase
  (Wunkolo@gmail.com)
- web_assets: update leaflet to 1.5.1 (ovdev@fratti.ch)
- world: add __lt__ method to RegionSet (ovdev@fratti.ch)
- observer: use bytes fp for JSObserver (ovdev@fratti.ch)
- Update observer import examples for Py3 (tswsl1989@sucs.org)
- Add .clang_format (Wunkolo@gmail.com)
- another version bump, to test out new builder (aargri@gmail.com)
- bump extension version (aargri@gmail.com)
- Fixes for WindowsOutputStream (achin@eminence32.net)
- Fix for reading worlds from local dir (achin@eminence32.net)
- Bumped extension version. (aargri@gmail.com)
- updated gitignore to ignore new python3 products (aargri@gmail.com)
- docs/installing: remove CentOS 6 section (ovdev@fratti.ch)
- decode Popen stdout bytes to utf-8 (steadmanben1@gmail.com)
- docs/installing: update CenturyOldOS instructions (ovdev@fratti.ch)
- remove deleted contrib scripts (steadmanben1@gmail.com)
- logger.warn->logger.warning (steadmanben1@gmail.com)
- use adjacency dictionary for graph equality (steadmanben1@gmail.com)
- python3.5 minimum (steadmanben1@gmail.com)
- pip install networkx in travis (steadmanben1@gmail.com)
- testRender.py tests (steadmanben1@gmail.com)
- testRender.py Python3 refactor (steadmanben1@gmail.com)
- # This is a combination of 7 commits. # This is the 1st commit message:
  (steadmanben1@gmail.com)
- python3 shebang lines (steadmanben1@gmail.com)
- regionTrimmer.py tests (steadmanben1@gmail.com)
- regionTrimmer.py Python3 refactor (steadmanben1@gmail.com)
- deltete deprecated/unused scripts (steadmanben1@gmail.com)
- playerInspect.py Python3 refactor (steadmanben1@gmail.com)
- gallery.py Python3 refactor (steadmanben1@gmail.com)
- cyrillic_convert.py Python3 refactor (steadmanben1@gmail.com)
- contributors.py Python3 refactor (steadmanben1@gmail.com)
- contributors.py Python3 refactor (steadmanben1@gmail.com)
- docs/building.rst: clean up macOS instructions (ovdev@fratti.ch)
- docs: move last mentions of Python 2 to Python 3 (ovdev@fratti.ch)
- docs: update mingw build instructions (untested) (ovdev@fratti.ch)
- docs: update Linux build instructions for Python 3 (ovdev@fratti.ch)
- genPOI: replace optparse with argparse (ovdev@fratti.ch)
- travis: switch to xenial and test for python 3.7 (ovdev@fratti.ch)
- docs: update optimizeimages instructions for py3 (ovdev@fratti.ch)
- genPOI: port to Python 3 (ovdev@fratti.ch)
- overviewer: fix shell quoting check in edge case (ovdev@fratti.ch)
- contribManager: Python 3 compatibility (ovdev@fratti.ch)
- world: fix reading old biomes (ovdev@fratti.ch)
- travis: move to Python 3 (ovdev@fratti.ch)
- Initial Python 3 port (ovdev@fratti.ch)
- contrib/playerInspect: add usage output (ovdev@fratti.ch)
- contrib/playerInspect: fix code style (ovdev@fratti.ch)
- contribManager: fix imports, use print_function (ovdev@fratti.ch)
- contribManager: fix code style (ovdev@fratti.ch)

* Thu Jun 06 2019 Franz Dietrich <dietrich@teilgedanken.de> 0.12-22
- overviewer: add warning for CentOS/RHEL 6 (ovdev@fratti.ch)
- Ensure coordinates are properly converted when changing views (#1571)
  (23699979+mircokroon@users.noreply.github.com)
- world: remove lit chunk check (ovdev@fratti.ch)
- world: make the chunk populated code even uglier (ovdev@fratti.ch)
- world: fix snowy grass check (ovdev@fratti.ch)
- world: fix rendering of 1.13 worlds (ovdev@fratti.ch)
- world: only render fully formed and lit chunks (ovdev@fratti.ch)
- .gitignore: add the docs build dir to ignore (ovdev@fratti.ch)
- Add fletching, cartography and smithing tables (ovdev@fratti.ch)
- added new 1.14 slabs, referencing issue #1560 (programming18@verdunkelbar.de)
- docs/running: update texture install instructions (ovdev@fratti.ch)
- travis: test with 1.14 assets (ovdev@fratti.ch)
- textures: fix stone slabs for 1.14 (ovdev@fratti.ch)
- world: ignore poi directory in world dir (ovdev@fratti.ch)
- world: fix for chunk parsing for 1.14 (ovdev@fratti.ch)
- Revert "web: fix goToHash on layer change" (ovdev@fratti.ch)
- primitives: misc char -> short fixes (ovdev@fratti.ch)
- world: space comments correctly (ovdev@fratti.ch)
- textures: set prismarine slabs to transparent (ovdev@fratti.ch)
- reorder code in world.py (programming18@verdunkelbar.de)
- double slab fix (programming18@verdunkelbar.de)
- activated red_sandstone_slab, for only half implemented
  (programming18@verdunkelbar.de)
- fix upper/lower slab issue for more slab types
  (programming18@verdunkelbar.de)
- added: prismarine_brick_stairs, prismarine_slab, dark_prismarine_slab,
  prismarine_brick_slab (programming18@verdunkelbar.de)
- fix prismarine stairs (ovdev@fratti.ch)

* Sat Mar 30 2019 Franz Dietrich <dietrich@teilgedanken.de> 0.12-21
- docs/signs.rst: fix filter function ids for 1.13 (ovdev@fratti.ch)
- web: fix goToHash on layer change (aheadley@waysaboutstuff.com)
- world: fix stair orientations (ovdev@fratti.ch)
- world: bandaid fix for double stone brick slabs (ovdev@fratti.ch)
- added cut_red_sandstone and chiseled_red_sandstone
  (programming18@verdunkelbar.de)
- mailmap: more adding of myself, sheesh (ovdev@fratti.ch)
- mailmap: add myself (ovdev@fratti.ch)
- Implement style fixes (Wunkolo@gmail.com)
- Fix block_class_is_subset linkage (Wunkolo@gmail.com)
- Increment extension version (Wunkolo@gmail.com)
- Fix implicit declaration (Wunkolo@gmail.com)
- Collapse special case logic to block_class_is_subset (Wunkolo@gmail.com)
- Convert case switch to block_class_is_subset (Wunkolo@gmail.com)
- block_class_is_subset implementation pass (Wunkolo@gmail.com)
- Implement block_class header (Wunkolo@gmail.com)
- Increment overviewer extension version (Wunkolo@gmail.com)
- Block ID enum pass (Wunkolo@gmail.com)
- Block ID to mc_id replacement pass (Wunkolo@gmail.com)
- First pass mc_id enum implementation (Wunkolo@gmail.com)
- world: fix potatoes and carrots growth stages (ovdev@fratti.ch)
- world: fix seed growth stages (ovdev@fratti.ch)
- world: fix mossy cobblestone block/wall rendering (ovdev@fratti.ch)
- world: fix petrified_oak_slab rendering (ovdev@fratti.ch)
- settingsValidators: fix code style, adjust strings (ovdev@fratti.ch)
- overviewer: use print_function (ovdev@fratti.ch)
- Replaced OSX with macOS (admin@tomtamaira.com)
- contrib/png-it: allow saving to stdout with - (ovdev@fratti.ch)
- contrib/png-it: use the print function (ovdev@fratti.ch)
- contrib/png-it: switch from optparse to argparse (ovdev@fratti.ch)
- contrib/png-it: clean up code, grammar (ovdev@fratti.ch)
- Updated macOS Build Instructions (#1530) (admin@tomtamaira.com)
- contribManager: get rid of removed scripts (ovdev@fratti.ch)
- Simplified finding spawn Y (jeroensmienk@icloud.com)
- contrib: delete scripts that are no longer useful (ovdev@fratti.ch)
- genPOI: fix code style (ovdev@fratti.ch)
- overviewer: warn about shell quoting issues (ovdev@fratti.ch)
- overviewer: replace optparse with argparse (ovdev@fratti.ch)
- overviewer: fix git hash being after line break (ovdev@fratti.ch)
- overviewer: misc style fixes (ovdev@fratti.ch)
- optimizeimages: fix code style (ovdev@fratti.ch)
- util: fix code style (ovdev@fratti.ch)
- cache: fix code style (ovdev@fratti.ch)
- logger: code style fixes (ovdev@fratti.ch)
- overviewer: code style and consistency fixes (ovdev@fratti.ch)
- Add WebP image format support (ovdev@fratti.ch)
- tileset: drastic code style fixes (ovdev@fratti.ch)
- docs: update copyright year, version, release (ovdev@fratti.ch)
- nbt: code style fixes (ovdev@fratti.ch)
- observer: drastic code style fixes (ovdev@fratti.ch)

* Fri Mar 01 2019 Franz Dietrich <dietrich@teilgedanken.de> 0.12-20
- progressbar: actually flush the fd on update (ovdev@fratti.ch)
- web: add layer fallback to goToHash (ovdev@fratti.ch)
- web: fix overlays showing up for all base layers (ovdev@fratti.ch)
- do block state unpacking with numpy slices, not loops (aargri@gmail.com)
- Fix C extension build warnings the painful way (ovdev@fratti.ch)
- block states with 9, 10, 11, and 12 bits per value now unpack correctly
  (aargri@gmail.com)
- Revert "Fix C extension build warnings" (aargri@gmail.com)
- web: fix white rectangle behind markers (ovdev@fratti.ch)
- web: reimplement marker groups default checking (ovdev@fratti.ch)
- docs: actually fix chestFilter example (ovdev@fratti.ch)
- docs: fix chestFilter example (ovdev@fratti.ch)
- Fix C extension build warnings (ovdev@fratti.ch)
- Fix marker icon position properly. Closes #1481. (willemmaster@hotmail.com)
- removed strong tags in coordination box (marc@marc.tv)
- trapdoor orientation non-oak trapdoors dried kelp blocks
  (jvaskonen@gmail.com)
- non-oak buttons buttons on top of blocks (jvaskonen@gmail.com)
- bone block orientation smooth stone blocks coral and dead coral blocks blue
  ice (jvaskonen@gmail.com)
- Wood and stripped wood (jvaskonen@gmail.com)
- Stripped logs (jvaskonen@gmail.com)
- non-oak pressure plates (jvaskonen@gmail.com)
- Uncarved pumpkin textures (jvaskonen@gmail.com)
- One more infested block (jvaskonen@gmail.com)
- Fix light grey terracotta and glazed terracotta orientation.
  (jvaskonen@gmail.com)
- When adding quartz pillar orientation, I assumed the top orientation was
  correct, when it was actually the side. (jvaskonen@gmail.com)
- Fixing top textures of non-vertically oriented quartz pillars.
  (jvaskonen@gmail.com)
- Added note blocks, carved pumkin, non-oak pressure plates (oak texture), more
  infested stone bricks and melons. (jvaskonen@gmail.com)
- Adds chiseled quartz and quartz pillars (jvaskonen@gmail.com)
- Adding mappings for damaged anvils. Add handling for sign and anvil
  orientation. (jvaskonen@gmail.com)
- Potted plants still not rendering, but I figure this is better than an error
  message. (jvaskonen@gmail.com)
- Fixes big mushrooms (jvaskonen@gmail.com)
- Fixing handling of torches/redstone torches on walls (jvaskonen@gmail.com)
- genpoi: Also fix missing nbt keys if processes > 1 (ovdev@fratti.ch)
- genPOI: catch ChunkDoesntExist when processes > 1 (ovdev@fratti.ch)
- genpoi: fix uncaught KeyErrors on some MC data (ovdev@fratti.ch)
- web: fix createInfoWindow not having any effect (ovdev@fratti.ch)
- web: fix marker icon position (ovdev@fratti.ch)
- Make JSObserver work with Leaflet. Fixes #1451. (willemmaster@hotmail.com)
- Use cached center for initial view. Fixes #1453. (willemmaster@hotmail.com)
- remove print (admin@redsparr0w.com)
- furnace orientation (admin@redsparr0w.com)
- dispenser, dropper orientation (admin@redsparr0w.com)
- add/update comments (admin@redsparr0w.com)
- fix piston orientation (admin@redsparr0w.com)
- fix gate orientation (admin@redsparr0w.com)
- fix rail, powered rail orientation + powered state (admin@redsparr0w.com)
- add oak button (admin@redsparr0w.com)
- fix shulker, observer orientation (admin@redsparr0w.com)
- fix slab top/bottom slab (admin@redsparr0w.com)
- fix repeate, comparator orientation + powered state (admin@redsparr0w.com)
- fix restone torch, torch orientations + lit state (admin@redsparr0w.com)
- fix ladder, chest, ender chest, trapped chest + orientation
  (admin@redsparr0w.com)
- Add more blocks (admin@redsparr0w.com)
- add banners, rearrange colored blocks by id (admin@redsparr0w.com)
- update block properties (admin@redsparr0w.com)
- update 1.13 underwater blocks to be water instead of air
  (admin@redsparr0w.com)
- remove items (not blocks) (admin@redsparr0w.com)
- add & fix some blocks (admin@redsparr0w.com)
- remove extra whitespace (admin@redsparr0w.com)
- Disable IRC notifications from travis (achin@eminence32.net)
- Fixed behaviour of 'defaultZoom' property. (leightheduck@gmail.com)
- NBT: Use a replacement strategy to deal with undecodable data.
  (achin@eminence32.net)
- Add concrete powder and other misc. blocks (#4) (jspanos@gmail.com)
- do not render internal faces for water (aargri@gmail.com)
- Forward compatibility (gmcnew@gmail.com)
- Reenable support for old 1.12-era chunks (gmcnew@gmail.com)
- More blocks added (softer@lin.in.ua)
- ignore "decorated" chunks (achin@eminence32.net)
- Always interpret long_array as 64-bit (aargri@gmail.com)
- Misc fixes (gmcnew@gmail.com)
- More blocks... (softer@lin.in.ua)
- Yet another attempt to get travis working (achin@eminence32.net)
- Use hard-coded 1.13 client jar URL in travis config (achin@eminence32.net)
- Update travis to use 1.13 textures (achin@eminence32.net)
- Add puCharm directory to .gitignore (softer@lin.in.ua)
- A 1.13-compatible texture pack is required (gmcnew@gmail.com)
- Add support for remaining palette sizes. (gmcnew@gmail.com)
- Support 9-bit palettes. (gmcnew@gmail.com)
- More block mappings! (gmcnew@gmail.com)
- Lots more block mappings (gmcnew@gmail.com)
- Translate to old map format (gmcnew@gmail.com)
- Allow new NBT type 12 (long array) to be read (gmcnew@gmail.com)
- Finish updating texture names (gmcnew@gmail.com)
- Minor texture fixes (gmcnew@gmail.com)
- Reverse version-check logic (gmcnew@gmail.com)
- Partial texture path fixes (gmcnew@gmail.com)

* Fri Mar 01 2019 Franz Dietrich <dietrich@teilgedanken.de>
- progressbar: actually flush the fd on update (ovdev@fratti.ch)
- web: add layer fallback to goToHash (ovdev@fratti.ch)
- web: fix overlays showing up for all base layers (ovdev@fratti.ch)
- do block state unpacking with numpy slices, not loops (aargri@gmail.com)
- Fix C extension build warnings the painful way (ovdev@fratti.ch)
- block states with 9, 10, 11, and 12 bits per value now unpack correctly
  (aargri@gmail.com)
- Revert "Fix C extension build warnings" (aargri@gmail.com)
- web: fix white rectangle behind markers (ovdev@fratti.ch)
- web: reimplement marker groups default checking (ovdev@fratti.ch)
- docs: actually fix chestFilter example (ovdev@fratti.ch)
- docs: fix chestFilter example (ovdev@fratti.ch)
- Fix C extension build warnings (ovdev@fratti.ch)
- Fix marker icon position properly. Closes #1481. (willemmaster@hotmail.com)
- removed strong tags in coordination box (marc@marc.tv)
- trapdoor orientation non-oak trapdoors dried kelp blocks
  (jvaskonen@gmail.com)
- non-oak buttons buttons on top of blocks (jvaskonen@gmail.com)
- bone block orientation smooth stone blocks coral and dead coral blocks blue
  ice (jvaskonen@gmail.com)
- Wood and stripped wood (jvaskonen@gmail.com)
- Stripped logs (jvaskonen@gmail.com)
- non-oak pressure plates (jvaskonen@gmail.com)
- Uncarved pumpkin textures (jvaskonen@gmail.com)
- One more infested block (jvaskonen@gmail.com)
- Fix light grey terracotta and glazed terracotta orientation.
  (jvaskonen@gmail.com)
- When adding quartz pillar orientation, I assumed the top orientation was
  correct, when it was actually the side. (jvaskonen@gmail.com)
- Fixing top textures of non-vertically oriented quartz pillars.
  (jvaskonen@gmail.com)
- Added note blocks, carved pumkin, non-oak pressure plates (oak texture), more
  infested stone bricks and melons. (jvaskonen@gmail.com)
- Adds chiseled quartz and quartz pillars (jvaskonen@gmail.com)
- Adding mappings for damaged anvils. Add handling for sign and anvil
  orientation. (jvaskonen@gmail.com)
- Potted plants still not rendering, but I figure this is better than an error
  message. (jvaskonen@gmail.com)
- Fixes big mushrooms (jvaskonen@gmail.com)
- Fixing handling of torches/redstone torches on walls (jvaskonen@gmail.com)
- genpoi: Also fix missing nbt keys if processes > 1 (ovdev@fratti.ch)
- genPOI: catch ChunkDoesntExist when processes > 1 (ovdev@fratti.ch)
- genpoi: fix uncaught KeyErrors on some MC data (ovdev@fratti.ch)
- web: fix createInfoWindow not having any effect (ovdev@fratti.ch)
- web: fix marker icon position (ovdev@fratti.ch)
- Make JSObserver work with Leaflet. Fixes #1451. (willemmaster@hotmail.com)
- Use cached center for initial view. Fixes #1453. (willemmaster@hotmail.com)
- remove print (admin@redsparr0w.com)
- furnace orientation (admin@redsparr0w.com)
- dispenser, dropper orientation (admin@redsparr0w.com)
- add/update comments (admin@redsparr0w.com)
- fix piston orientation (admin@redsparr0w.com)
- fix gate orientation (admin@redsparr0w.com)
- fix rail, powered rail orientation + powered state (admin@redsparr0w.com)
- add oak button (admin@redsparr0w.com)
- fix shulker, observer orientation (admin@redsparr0w.com)
- fix slab top/bottom slab (admin@redsparr0w.com)
- fix repeate, comparator orientation + powered state (admin@redsparr0w.com)
- fix restone torch, torch orientations + lit state (admin@redsparr0w.com)
- fix ladder, chest, ender chest, trapped chest + orientation
  (admin@redsparr0w.com)
- Add more blocks (admin@redsparr0w.com)
- add banners, rearrange colored blocks by id (admin@redsparr0w.com)
- update block properties (admin@redsparr0w.com)
- update 1.13 underwater blocks to be water instead of air
  (admin@redsparr0w.com)
- remove items (not blocks) (admin@redsparr0w.com)
- add & fix some blocks (admin@redsparr0w.com)
- remove extra whitespace (admin@redsparr0w.com)
- Disable IRC notifications from travis (achin@eminence32.net)
- Fixed behaviour of 'defaultZoom' property. (leightheduck@gmail.com)
- NBT: Use a replacement strategy to deal with undecodable data.
  (achin@eminence32.net)
- Add concrete powder and other misc. blocks (#4) (jspanos@gmail.com)
- do not render internal faces for water (aargri@gmail.com)
- Forward compatibility (gmcnew@gmail.com)
- Reenable support for old 1.12-era chunks (gmcnew@gmail.com)
- More blocks added (softer@lin.in.ua)
- ignore "decorated" chunks (achin@eminence32.net)
- Always interpret long_array as 64-bit (aargri@gmail.com)
- Misc fixes (gmcnew@gmail.com)
- More blocks... (softer@lin.in.ua)
- Yet another attempt to get travis working (achin@eminence32.net)
- Use hard-coded 1.13 client jar URL in travis config (achin@eminence32.net)
- Update travis to use 1.13 textures (achin@eminence32.net)
- Add puCharm directory to .gitignore (softer@lin.in.ua)
- A 1.13-compatible texture pack is required (gmcnew@gmail.com)
- Add support for remaining palette sizes. (gmcnew@gmail.com)
- Support 9-bit palettes. (gmcnew@gmail.com)
- More block mappings! (gmcnew@gmail.com)
- Lots more block mappings (gmcnew@gmail.com)
- Translate to old map format (gmcnew@gmail.com)
- Allow new NBT type 12 (long array) to be read (gmcnew@gmail.com)
- Finish updating texture names (gmcnew@gmail.com)
- Minor texture fixes (gmcnew@gmail.com)
- Reverse version-check logic (gmcnew@gmail.com)
- Partial texture path fixes (gmcnew@gmail.com)

* Mon Aug 27 2018 Franz Dietrich <dietrich@teilgedanken.de> 0.12-17
- using python2 instead of python (dietrich@teilgedanken.de)
- simple change (dietrich@teilgedanken.de)

* Mon Aug 27 2018 Franz Dietrich <dietrich@teilgedanken.de> 0.12-16
- changing to leaflet (dietrich@teilgedanken.de)

* Mon Aug 27 2018 Franz Dietrich <dietrich@teilgedanken.de> 0.12-15
- adding gcc to build depends (dietrich@teilgedanken.de)

* Mon Aug 27 2018 Franz Dietrich <dietrich@teilgedanken.de> 0.12-14
- Fix missing titles for markers (cl0ne@mithril.org.ua)
- Remove trailing whitespaces (r15ch13+git@gmail.com)
- Remove jQuery and underscore dependencies (r15ch13+git@gmail.com)
- Use <noscript> to display message when JavaScript is disabled
  (r15ch13+git@gmail.com)
- issues-1411: Block Addition: Add inverted daylight sensor.
  (karl.kuhn@hmhco.com)

* Wed May 23 2018 Franz Dietrich <dietrich@teilgedanken.de> 0.12-13
- Remove broken marker centreing code (ovdev@fratti.ch)
- Fix custom icons not showing up properly (ovdev@fratti.ch)
- Increase the Overviewer C extension version (ovdev@fratti.ch)
- Add 3 more touch-up points for smooth lighting (skaggsm333@gmail.com)
- world: Don't call sys.exit here, raise something (ovdev@fratti.ch)
- Fixes and improvements to leaflet marker support (achin@eminence32.net)
- Set the attribution prefix (ovdev@fratti.ch)
- Don't collapse marker group control (ovdev@fratti.ch)
- Update leaflet to 1.3.1 (ovdev@fratti.ch)
- Assume 32x32 marker size so they get centred (ovdev@fratti.ch)
- Show marker group display names (ovdev@fratti.ch)
- I don't make typos, no sir I don't (achin@eminence32.net)
- Rename package to pkg in gitlab ci steps (achin@eminence32.net)
- Updated to new gitlab registry URL (achin@eminence32.net)
- Add testrepo step for ubuntu:artful (achin@eminence32.net)
- During windows CI builds, use a specific Pillow (achin@eminence32.net)
- Use sys.exit(1) to exit rather than throwing a ValueError
  (supermarioryan@gmail.com)
- Throw an error if the overviewer is running on a world saved on versions of
  Minecraft newer than snapshot 17w47a (supermarioryan@gmail.com)
- Fix gitlab CI (achin@eminence32.net)
- travis: additionally fetch ImagingUtils.h (kevin@kevinwchang.com)
- update Pillow header URLs in .travis.yml (kevin@kevinwchang.com)
- fix pillow no longer allowing RGBA JPEG (kevin@kevinwchang.com)
- Removing deprecated option in index.html : ?sensor=false (srumeu@manymore.fr)
- Terracotta texture rotation fix (kenisis@hotmail.com)
- Modernize Windows build instructions (kenisis@hotmail.com)
- Fix slime algo by using integer for chunk coordinates. (dev.lyknode@cilg.org)
- Added expiration of uuidcache entries (3db@3decibels.net)
- leaflet: Reimplement coordinate box on bottom left (ovdev@fratti.ch)
- Protect against optional marker variable (achin@eminence32.net)
- Actually add the high-dpi icons, durr (ovdev@fratti.ch)
- Remove old junk in web_assets (ovdev@fratti.ch)
- Carpet-bombing code style fixes (ovdev@fratti.ch)
- Re-implement map compass (ovdev@fratti.ch)
- Move icon anchor to tip of icons (ovdev@fratti.ch)
- Add retina size icons for spawn and location (ovdev@fratti.ch)
- Centre map view on spawn marker if left-clicked (ovdev@fratti.ch)
- Re-implement location marker (ovdev@fratti.ch)
- WIP marker stuff (achin@eminence32.net)
- Fix for IE11 (achin@eminence32.net)
- Style fixes for the world selector control (achin@eminence32.net)
- Update to latest version of leaflet 1.0.2 (achin@eminence32.net)
- Initial reimplementation of url hash updating (achin@eminence32.net)
- Re-implement configurable bgcolor (ovdev@fratti.ch)
- Fix errorTileUrl for JPEG tilesets (ovdev@fratti.ch)
- Get rid of overviewer.gmap, move code into util (ovdev@fratti.ch)
- Add tset config to leaflet layer, refactor marker (ovdev@fratti.ch)
- Re-implement spawn marker (ovdev@fratti.ch)
- Set errorTileUrl to blank.png (ovdev@fratti.ch)
- Replace mentions of Google Maps in documentation (ovdev@fratti.ch)
- Misc leaflet fixes (achin@eminence32.net)
- Add replacement for the location marker (ovdev@fratti.ch)
- Add replacement for home marker, add icon_src dir (ovdev@fratti.ch)
- Added world switcher control (achin@eminence32.net)
- Include licnese information into jquery and leafjet js files
  (achin@eminence32.net)
- Adjust README.rst to remove mentions of GMaps API (ovdev@fratti.ch)
- Initial commit to drop gmaps and to add support for leaflet
  (achin@eminence32.net)

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
