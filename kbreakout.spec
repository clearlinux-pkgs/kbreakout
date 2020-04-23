#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kbreakout
Version  : 20.04.0
Release  : 19
URL      : https://download.kde.org/stable/release-service/20.04.0/src/kbreakout-20.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.0/src/kbreakout-20.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.0/src/kbreakout-20.04.0.tar.xz.sig
Summary  : A Breakout-like game
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kbreakout-bin = %{version}-%{release}
Requires: kbreakout-data = %{version}-%{release}
Requires: kbreakout-license = %{version}-%{release}
Requires: kbreakout-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package bin
Summary: bin components for the kbreakout package.
Group: Binaries
Requires: kbreakout-data = %{version}-%{release}
Requires: kbreakout-license = %{version}-%{release}

%description bin
bin components for the kbreakout package.


%package data
Summary: data components for the kbreakout package.
Group: Data

%description data
data components for the kbreakout package.


%package doc
Summary: doc components for the kbreakout package.
Group: Documentation

%description doc
doc components for the kbreakout package.


%package license
Summary: license components for the kbreakout package.
Group: Default

%description license
license components for the kbreakout package.


%package locales
Summary: locales components for the kbreakout package.
Group: Default

%description locales
locales components for the kbreakout package.


%prep
%setup -q -n kbreakout-20.04.0
cd %{_builddir}/kbreakout-20.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587677546
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1587677546
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kbreakout
cp %{_builddir}/kbreakout-20.04.0/COPYING %{buildroot}/usr/share/package-licenses/kbreakout/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kbreakout-20.04.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/kbreakout/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang kbreakout

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kbreakout

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kbreakout.desktop
/usr/share/icons/hicolor/128x128/apps/kbreakout.png
/usr/share/icons/hicolor/16x16/apps/kbreakout.png
/usr/share/icons/hicolor/22x22/apps/kbreakout.png
/usr/share/icons/hicolor/32x32/apps/kbreakout.png
/usr/share/icons/hicolor/48x48/apps/kbreakout.png
/usr/share/icons/hicolor/64x64/apps/kbreakout.png
/usr/share/icons/hicolor/scalable/apps/kbreakout.svg
/usr/share/kbreakout/levelsets/default.levelset
/usr/share/kbreakout/qml/Ball.qml
/usr/share/kbreakout/qml/Bar.qml
/usr/share/kbreakout/qml/Brick.qml
/usr/share/kbreakout/qml/CanvasItem.qml
/usr/share/kbreakout/qml/Gift.qml
/usr/share/kbreakout/qml/Singleshot.qml
/usr/share/kbreakout/qml/TextItem.qml
/usr/share/kbreakout/qml/globals.js
/usr/share/kbreakout/qml/logic.js
/usr/share/kbreakout/qml/main.qml
/usr/share/kbreakout/themes/IceWorld.desktop
/usr/share/kbreakout/themes/IceWorld.svgz
/usr/share/kbreakout/themes/IceWorld_preview.png
/usr/share/kbreakout/themes/alien_preview.png
/usr/share/kbreakout/themes/alienbreakout.desktop
/usr/share/kbreakout/themes/alienbreakout.svgz
/usr/share/kbreakout/themes/crystal.desktop
/usr/share/kbreakout/themes/crystal.svgz
/usr/share/kbreakout/themes/crystal_preview.png
/usr/share/kbreakout/themes/default.desktop
/usr/share/kbreakout/themes/egyptian_breakout_preview.png
/usr/share/kbreakout/themes/egyptianbreakout.svgz
/usr/share/kbreakout/themes/simple.desktop
/usr/share/kbreakout/themes/simple.svgz
/usr/share/kbreakout/themes/simple_preview.png
/usr/share/kbreakout/themes/web20.desktop
/usr/share/kbreakout/themes/web20.svgz
/usr/share/kbreakout/themes/web20_preview.png
/usr/share/metainfo/org.kde.kbreakout.appdata.xml
/usr/share/qlogging-categories5/kbreakout.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kbreakout/index.cache.bz2
/usr/share/doc/HTML/de/kbreakout/index.docbook
/usr/share/doc/HTML/en/kbreakout/BreakableBrick.png
/usr/share/doc/HTML/en/kbreakout/ExplodingBrick.png
/usr/share/doc/HTML/en/kbreakout/Gift1000Points.png
/usr/share/doc/HTML/en/kbreakout/GiftAddBall.png
/usr/share/doc/HTML/en/kbreakout/GiftAddLife.png
/usr/share/doc/HTML/en/kbreakout/GiftBurningBall.png
/usr/share/doc/HTML/en/kbreakout/GiftDecreaseSpeed.png
/usr/share/doc/HTML/en/kbreakout/GiftEnlargeBar.png
/usr/share/doc/HTML/en/kbreakout/GiftIncreaseSpeed.png
/usr/share/doc/HTML/en/kbreakout/GiftLoseLife.png
/usr/share/doc/HTML/en/kbreakout/GiftMagicEye.png
/usr/share/doc/HTML/en/kbreakout/GiftMagicWand.png
/usr/share/doc/HTML/en/kbreakout/GiftMoreExplosion.png
/usr/share/doc/HTML/en/kbreakout/GiftNextLevel.png
/usr/share/doc/HTML/en/kbreakout/GiftShrinkBar.png
/usr/share/doc/HTML/en/kbreakout/GiftSplitBall.png
/usr/share/doc/HTML/en/kbreakout/GiftStickyBar.png
/usr/share/doc/HTML/en/kbreakout/GiftUnstoppableBall.png
/usr/share/doc/HTML/en/kbreakout/HiddenBrick.png
/usr/share/doc/HTML/en/kbreakout/MultipleBrick3.png
/usr/share/doc/HTML/en/kbreakout/PlainBrick1.png
/usr/share/doc/HTML/en/kbreakout/UnbreakableBrick.png
/usr/share/doc/HTML/en/kbreakout/gameboard.png
/usr/share/doc/HTML/en/kbreakout/index.cache.bz2
/usr/share/doc/HTML/en/kbreakout/index.docbook
/usr/share/doc/HTML/es/kbreakout/index.cache.bz2
/usr/share/doc/HTML/es/kbreakout/index.docbook
/usr/share/doc/HTML/et/kbreakout/index.cache.bz2
/usr/share/doc/HTML/et/kbreakout/index.docbook
/usr/share/doc/HTML/fr/kbreakout/index.cache.bz2
/usr/share/doc/HTML/fr/kbreakout/index.docbook
/usr/share/doc/HTML/it/kbreakout/index.cache.bz2
/usr/share/doc/HTML/it/kbreakout/index.docbook
/usr/share/doc/HTML/nl/kbreakout/index.cache.bz2
/usr/share/doc/HTML/nl/kbreakout/index.docbook
/usr/share/doc/HTML/pl/kbreakout/index.cache.bz2
/usr/share/doc/HTML/pl/kbreakout/index.docbook
/usr/share/doc/HTML/pt/kbreakout/index.cache.bz2
/usr/share/doc/HTML/pt/kbreakout/index.docbook
/usr/share/doc/HTML/pt_BR/kbreakout/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kbreakout/index.docbook
/usr/share/doc/HTML/sv/kbreakout/index.cache.bz2
/usr/share/doc/HTML/sv/kbreakout/index.docbook
/usr/share/doc/HTML/uk/kbreakout/gameboard.png
/usr/share/doc/HTML/uk/kbreakout/index.cache.bz2
/usr/share/doc/HTML/uk/kbreakout/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kbreakout/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kbreakout/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kbreakout.lang
%defattr(-,root,root,-)

