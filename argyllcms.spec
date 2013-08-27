Summary:	ICC compatible color management system
Summary(pl.UTF-8):	System zarządzania kolorami kompatybilny z ICC
Name:		argyllcms
Version:	1.6.0
Release:	1
License:	AGPL v3, MIT, GPL v2+, LGPL v2.1+, FDL v1.3
Group:		X11/Applications/Graphics
Source0:	http://people.freedesktop.org/~hughsient/releases/h%{name}-%{version}.tar.xz
# Source0-md5:	03d9d07e6551a72e4b5023df3821a663
URL:		http://www.argyllcms.com/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 1:1.4.2
BuildRequires:	libusb-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xz
BuildRequires:	yajl-devel
BuildRequires:	zlib-devel
Obsoletes:	udev-argyllcms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Argyll color management system supports accurate ICC profile
creation for acquisition devices, CMYK printers, film recorders and
calibration and profiling of displays.

Spectral sample data is supported, allowing a selection of illuminants
observer types, and paper fluorescent whitener additive compensation.
Profiles can also incorporate source specific gamut mappings for
perceptual and saturation intents. Gamut mapping and profile linking
uses the CIECAM02 appearance model, a unique gamut mapping algorithm,
and a wide selection of rendering intents. It also includes code for
the fastest portable 8 bit raster color conversion engine available
anywhere, as well as support for fast, fully accurate 16 bit
conversion. Device color gamuts can also be viewed and compared using
a VRML viewer.

%description -l pl.UTF-8
System zarządzania kolorami Argyll obsługuje tworzenie dokładnych
profili ICC dla urządzeń skanujących, drukarek CMYK i kamer oraz
kalibrację i profilowanie wyświetlaczy.

Obsługiwane są dane próbek widmowych, co pozwala na wybór typów
obserwatora oświetlenia oraz kompensację addytywną fluorescencyjnych
wybielaczy papieru. Profile mogą zawierać także zależne od źródła
odwzorowania podzbioru kolorów (gamut) pod kątem postrzegania i
nasycenia. Odwzorowanie kolorów i wiązanie profili wykorzystuje model
wyglądu kolorów CIECAM02, unikalny algorytm odwzorowania podzbioru
kolorów oraz szeroki wybór celu renderingu. Zawiera także kod
najszybszego dostępnego przenośnego 8-bitowego rastrowego silnika
konwersji kolorów, a także obsługę szybkiej, dokładniej 16-bitowej
konwersji. Podzbiór kolorów urządzeń można oglądać i porównywać przy
użyciu przeglądarki VRML.

%package doc
Summary:	Argyll CMS documentation
Summary(pl.UTF-8):	Dokumentacja systemu Argyll CMS
Group:		Documentation
# Does not really make sense without Argyll CMS itself
Requires:	%{name} = %{version}-%{release}

%description doc
The Argyll color management system supports accurate ICC profile
creation for acquisition devices, CMYK printers, film recorders and
calibration and profiling of displays.

This package contains the Argyll color management system
documentation.

%description doc -l pl.UTF-8
System zarządzania kolorami Argyll obsługuje tworzenie dokładnych
profili ICC dla urządzeń skanujących, drukarek CMYK i kamer oraz
kalibrację i profilowanie wyświetlaczy.

Ten pakiet zawiera dokumentację do systemu zarządzania kolorami
Argyll.

%prep
%setup -q -n h%{name}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# they shouldn't put Makefile.am to ref_DATA
%{__rm} $RPM_BUILD_ROOT%{_datadir}/color/argyll/ref/Makefile.am

# no -devel package (headers not exported)
%{__rm} $RPM_BUILD_ROOT%{_libdir}/lib*.{so,la}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/argyll

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS Readme.txt
%attr(755,root,root) %{_bindir}/applycal
%attr(755,root,root) %{_bindir}/average
%attr(755,root,root) %{_bindir}/cb2ti3
%attr(755,root,root) %{_bindir}/ccttest
%attr(755,root,root) %{_bindir}/ccxxmake
%attr(755,root,root) %{_bindir}/chartread
%attr(755,root,root) %{_bindir}/collink
%attr(755,root,root) %{_bindir}/colprof
%attr(755,root,root) %{_bindir}/dispcal
%attr(755,root,root) %{_bindir}/dispread
%attr(755,root,root) %{_bindir}/dispwin
%attr(755,root,root) %{_bindir}/extracticc
%attr(755,root,root) %{_bindir}/extractttag
%attr(755,root,root) %{_bindir}/fakeCMY
%attr(755,root,root) %{_bindir}/fakeread
%attr(755,root,root) %{_bindir}/iccdump
%attr(755,root,root) %{_bindir}/iccgamut
%attr(755,root,root) %{_bindir}/icclu
%attr(755,root,root) %{_bindir}/icctest
%attr(755,root,root) %{_bindir}/invprofcheck
%attr(755,root,root) %{_bindir}/kodak2ti3
%attr(755,root,root) %{_bindir}/mppcheck
%attr(755,root,root) %{_bindir}/mpplu
%attr(755,root,root) %{_bindir}/mppprof
%attr(755,root,root) %{_bindir}/oeminst
%attr(755,root,root) %{_bindir}/pathplot
%attr(755,root,root) %{_bindir}/printcal
%attr(755,root,root) %{_bindir}/printtarg
%attr(755,root,root) %{_bindir}/profcheck
%attr(755,root,root) %{_bindir}/refine
%attr(755,root,root) %{_bindir}/revfix
%attr(755,root,root) %{_bindir}/scanin
%attr(755,root,root) %{_bindir}/simpprof
%attr(755,root,root) %{_bindir}/spec2cie
%attr(755,root,root) %{_bindir}/specplot
%attr(755,root,root) %{_bindir}/splitti3
%attr(755,root,root) %{_bindir}/spotread
%attr(755,root,root) %{_bindir}/synthcal
%attr(755,root,root) %{_bindir}/synthread
%attr(755,root,root) %{_bindir}/targen
%attr(755,root,root) %{_bindir}/tiffgamut
%attr(755,root,root) %{_bindir}/txt2ti3
%attr(755,root,root) %{_bindir}/verify
%attr(755,root,root) %{_bindir}/viewgam
%attr(755,root,root) %{_bindir}/xicclu
%attr(755,root,root) %{_libdir}/libargyll.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libargyll.so.0
%attr(755,root,root) %{_libdir}/libargyllicc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libargyllicc.so.0
%dir %{_datadir}/color/argyll
%{_datadir}/color/argyll/ref

%files doc
%defattr(644,root,root,755)
%doc doc/*.html doc/*.jpg doc/*.txt
