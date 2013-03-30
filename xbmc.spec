%define build_cec	1

Summary:	XBMC Media Center - media player and home entertainment system
Name:		xbmc
Version:	12.1
Release:	1
Group:		Video
# nosefart audio plugin and RSXS-0.9 based screensavers are GPLv2 only
# several eventclients are GPLv3+ (in subpackages)
# libhdhomerun is LGPLv3+ with an exception (always ok to link against it)
# the rest is GPLv2+
# both GPLv2+ and GPLv2 are mentioned because plugins are not part of core
# xbmc and therefore e.g. /usr/bin/xbmc is GPLv2+ with LGPLv3+ part
# as allowed by a license exception
License:	GPLv2+ and GPLv2 and (LGPLv3+ with exceptions)
URL:		http://xbmc.org/
Source0:	http://mirrors.xbmc.org/releases/source/%{name}-%{version}.tar.gz
# Hack to workaround upgrading from our old hack... see patch header for more
# details and an upstreaming plan.
Patch0:		0001-hack-workaround-for-old-incompatible-PVR-addon-datab.patch
Patch1:		xbmc-12.1-samba4.patch
BuildRequires:	afpclient-devel
BuildRequires:	avahi-common-devel
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	crystalhd-devel
BuildRequires:	cwiid-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	gettext-devel
BuildRequires:	jpeg-devel
BuildRequires:	liblzo2-devel
BuildRequires:	mysql-devel
BuildRequires:	python-devel
BuildRequires:	rtmp-devel
BuildRequires:	ssh-devel
BuildRequires:	tiff-devel
BuildRequires:	tinyxml-devel
BuildRequires:	yajl-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(avahi-client)
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(enca)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(fribidi)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(jasper)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libbluray)
BuildRequires:	pkgconfig(libcdio)
%if %{build_cec}
BuildRequires:	pkgconfig(libcec) >= 2:1:0
%else
BuildConflicts:	pkgconfig(libcec)
%endif
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libmicrohttpd)
BuildRequires:	pkgconfig(libmms)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpeg2)
BuildRequires:	pkgconfig(libnfs)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libplist)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libshairport)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(smbclient)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(wavpack)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xtst)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake
BuildRequires:	gperf
BuildRequires:	zip
%ifarch %{ix86}
BuildRequires:	nasm
%endif
Requires:	lsb-release
# for codegenrator
BuildRequires:	doxygen
BuildRequires:	java
BuildRequires:	swig

# dlopened (existence check required by rpm5 as it doesn't use stderr):
%define dlopenreq() %([ -e %{_libdir}/lib%{1}.so ] && rpm -qf --qf '%%{name}' $(readlink -f %{_libdir}/lib%{1}.so) 2>/dev/null || echo %{name})
Requires:	%dlopenreq curl
Requires:	%dlopenreq FLAC
Requires:	%dlopenreq mad
Requires:	%dlopenreq ogg
Requires:	%dlopenreq vorbis
Requires:	%dlopenreq vorbisenc
Requires:	%dlopenreq vorbisfile
Requires:	%dlopenreq modplug
Requires:	%dlopenreq rtmp
Requires:	%dlopenreq mpeg2
Requires:	%dlopenreq ass
Requires:	%dlopenreq bluray
Requires:	%dlopenreq nfs
Requires:	%dlopenreq afpclient
Requires:	%dlopenreq plist
Requires:	%dlopenreq shairport
%if %{build_cec}
Requires:	%dlopenreq cec
%endif
# not nearly as common as the above, so just suggest instead for now:
Suggests:	%dlopenreq crystalhd
# TODO: FEH.py is useless nowadays, drop it here and upstream.
# for FEH.py, to check current configuration is ok for xbmc:
Requires:	xdpyinfo
Requires:	glxinfo
# for FEH.py to allow it to give an error message (should be available already
# on most systems):
Requires:	pygtk2
# for xbmc python scripts:
Requires:	python-imaging
# Packages not shipped in core:
Suggests:	%{_lib}lame0
Suggests:	%{_lib}dvdcss2

%description
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

While XBMC functions very well as a standard media player application
for your computer, it has been designed to be the perfect companion
for your HTPC. Supporting an almost endless range of remote controls,
and combined with its beautiful interface and powerful skinning
engine, XBMC feels very natural to use from the couch and is the
ideal solution for your home theater.

Support for RAR files is not included due to license issues.

%package	eventclients-common
Summary:	Common files for XBMC eventclients
Group:		Video
License:	GPLv2+
%py_requires

%description	eventclients-common
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains common files for eventclients.

%package	eventclients-devel
Summary:	Development files for XBMC eventclients
Group:		Development/C
License:	GPLv2+

%description	eventclients-devel
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains files needed to build eventclients.

%package	eventclient-wiiremote
Summary:	Wii Remote eventclient for XBMC
Group:		Video
License:	GPLv3+
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-wiiremote
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the Wii Remote eventclient.

%package	eventclient-j2me
Summary:	J2ME eventclient for XBMC
Group:		Video
License:	GPLv2+
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-j2me
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the J2ME eventclient, providing a bluetooth
server that can communicate with a mobile tool supporting J2ME.

%package	eventclient-ps3
Summary:	PS3 eventclients for XBMC
Group:		Video
License:	GPLv2+
Requires:	python-pybluez
Requires:	%{name}-eventclients-common = %{version}-%{release}
# requires via zeroconf.py, only used by xbmc-ps3d:
Requires:	python-gobject avahi-python python-dbus

%description	eventclient-ps3
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the PS3 remote and sixaxis eventclients.

%package	eventclient-xbmc-send
Summary:	PS3 eventclient for XBMC
Group:		Video
License:	GPLv2+
Requires:	%{name}-eventclients-common = %{version}-%{release}

%description	eventclient-xbmc-send
XBMC is an award-winning free and open source software media player
and entertainment hub for digital media.

This package contains the xbmc-send eventclient.

%prep
%setup -q
%patch0 -p1
# Support for Samba 4
%if %{mdvver} >= 201300
%patch1 -p1
%endif

# otherwise backups end up in binary rpms
find -type f \( -name '*.00??' -o -name '*.00??~' \) -print -delete

# remove prebuilt libraries
find -type f \( -iname '*.so' -o -iname '*.dll' -o -iname '*.exe' \) -delete

# GPLv2 only
rm -r lib/cmyth/Win32/include/mysql
# BSD 4-clause
rm -r xbmc/cores/DllLoader/exports/emu_socket

# win32 only
rm -rf system/players/dvdplayer/etc/fonts

%build
export GIT_REV="tarball"
./bootstrap

# due to xbmc modules that use symbols from xbmc binary
# and are not using libtool
%define _disable_ld_no_undefined 1

# Workaround configure using git to override GIT_REV (TODO: fix it properly)
export ac_cv_prog_HAVE_GIT="no"

%configure2_5x \
	--disable-debug \
	--disable-ccache \
%ifarch %arm
	--enable-neon	\
%endif
	--enable-external-libraries \
	--disable-non-free \
	--disable-dvdcss \
	--enable-goom \
	--enable-pulse \
	--with-lirc-device=/var/run/lirc/lircd

# non-free = unrar
# dvdcss is handled via dlopen when disabled

%make
%make -C tools/EventClients wiimote

%install
%makeinstall_std
%makeinstall_std -C tools/EventClients

# unused
rm %{buildroot}%{_datadir}/xsessions/XBMC.desktop
# our version of the above:
install -d -m755 %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat > %{buildroot}%{_sysconfdir}/X11/wmsession.d/15XBMC <<EOF
NAME=XBMC
ICON=xbmc.png
DESC=XBMC Media Center
EXEC=%{_bindir}/xbmc-standalone
SCRIPT:
exec %{_bindir}/xbmc-standalone
EOF

# unused files, TODO fix this upstream:
find %{buildroot}%{_datadir}/xbmc/addons/skin.*/media -name '*.png' -delete

( # for IFS and +x
# Check for issues in ELF binaries
undefined=
fhserr=
echo Silencing output of undefined symbol and FHS conformance checks
set +x
IFS=$'\n'
for file in $(find %{buildroot} -type f); do
	type="$(file "$file")"
	echo "$type" | grep -q "ELF" || continue

	# Check that a binary file is not in datadir:
	echo "$file" | grep -q "%{_datadir}" && fhserr="${fhserr}$file\n"

	# check for undefined symbols in XBMC modules
	echo "$type" | grep -q "shared object" || continue
	for symbol in $(LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir} ldd -r "$file" 2>&1 | grep undefined | awk '{ print $3 }'); do
		# undefined symbols may also be provided by XBMC:
		nm -f posix -D --no-demangle --defined-only %{buildroot}%{_libdir}/xbmc/xbmc.bin | grep -q "^$symbol " && continue
		# The symbol was not provided by XBMC.
		# Check if it is available through its dependencies:
		for filename in $(objdump -p %{buildroot}%{_libdir}/xbmc/xbmc.bin | grep NEEDED | awk '{ print $2 }'); do
			depfile="/%{_lib}/$filename"
			[ -e "$depfile" ] || depfile="%{_libdir}/$filename"
			nm -f posix -D --no-demangle --defined-only $depfile | grep -q "^$symbol " && continue 2
		done
		# Euphoria references rsxs PNG class, but it is never used at runtime,
		# so it results in no errors due to RTLD_LAZY being used by xbmc module loader.
		case $file:$symbol in */Euphoria.xbs:_ZN3PNG*) continue; esac
		# the symbol was not found
		undefined="${undefined}$file: $symbol\n"
	done
done
ok=1
[ -n "$undefined" ] && echo -e "$undefined" && echo "Undefined symbols!" && ok=
[ -n "$fhserr" ] && echo -e "$fhserr" && echo "Binaries in datadir!" && ok=
[ -n "$ok" ]
)

%files
%doc %{_docdir}/xbmc
%{_sysconfdir}/X11/wmsession.d/15XBMC
%{_bindir}/xbmc
%{_bindir}/xbmc-standalone
%dir %{_libdir}/xbmc
%dir %{_libdir}/xbmc/addons
%dir %{_libdir}/xbmc/system
%dir %{_libdir}/xbmc/system/players
%dir %{_libdir}/xbmc/system/players/dvdplayer
%dir %{_libdir}/xbmc/system/players/paplayer
%{_libdir}/xbmc/xbmc.bin
%{_libdir}/xbmc/xbmc-xrandr
%dir %{_libdir}/xbmc/addons/*
%{_libdir}/xbmc/addons/*/*.so
%{_libdir}/xbmc/addons/*/*.vis
%{_libdir}/xbmc/addons/*/*.xbs
%{_libdir}/xbmc/system/ImageLib-*.so
%{_libdir}/xbmc/system/hdhomerun-*.so
%{_libdir}/xbmc/system/libcmyth-*.so
%{_libdir}/xbmc/system/libcpluff-*.so
%{_libdir}/xbmc/system/libexif-*.so
%{_libdir}/xbmc/system/players/dvdplayer/libdvdnav-*.so
%{_libdir}/xbmc/system/players/paplayer/adpcm-*.so
%{_libdir}/xbmc/system/players/paplayer/libsidplay2-*.so
%{_libdir}/xbmc/system/players/paplayer/nosefart-*.so
%{_libdir}/xbmc/system/players/paplayer/stsoundlibrary-*.so
%{_libdir}/xbmc/system/players/paplayer/timidity-*.so
%{_libdir}/xbmc/system/players/paplayer/vgmstream-*.so
%ifarch %{ix86}
%{_libdir}/xbmc/system/players/paplayer/SNESAPU-*.so
%endif
%dir %{_datadir}/xbmc
%{_datadir}/xbmc/addons
%{_datadir}/xbmc/FEH.py
%{_datadir}/xbmc/language
%{_datadir}/xbmc/media
%{_datadir}/xbmc/sounds
%{_datadir}/xbmc/system
%{_datadir}/xbmc/userdata
%{_datadir}/applications/xbmc.desktop
%{_iconsdir}/hicolor/*/apps/xbmc.png

%files eventclients-common
%{python_sitelib}/xbmc
%dir %{_datadir}/pixmaps/xbmc
%{_datadir}/pixmaps/xbmc/*.png

%files eventclients-devel
%dir %{_includedir}/xbmc
%{_includedir}/xbmc/xbmcclient.h

%files eventclient-j2me
%{_bindir}/xbmc-j2meremote

%files eventclient-ps3
%{_bindir}/xbmc-ps3d
%{_bindir}/xbmc-ps3remote

%files eventclient-xbmc-send
%{_bindir}/xbmc-send

%files eventclient-wiiremote
%{_bindir}/xbmc-wiiremote

