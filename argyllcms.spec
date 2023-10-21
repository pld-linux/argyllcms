Summary:	ICC compatible color management system
Summary(pl.UTF-8):	System zarządzania kolorami kompatybilny z ICC
Name:		argyllcms
Version:	3.0.1
Release:	1
License:	AGPL v3, MIT, GPL v2+, LGPL v2.1+, FDL v1.3
Group:		X11/Applications/Graphics
Source0:	https://www.argyllcms.com/Argyll_V%{version}_src.zip
# Source0-md5:	faf8673e2f493c66edf5b90f0925eac7
Patch0:		x32.patch
URL:		http://www.argyllcms.com/
BuildRequires:	jam
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	linux-libc-headers
BuildRequires:	openssl-devel
BuildRequires:	unzip
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	zlib-devel
Obsoletes:	udev-argyllcms < 1.5.1
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
%setup -q -n Argyll_V%{version}
%patch0 -p1

%build
export CC="%{__cc}"
export PREF_CCFLAGS="%{rpmcflags} %{rpmcppflags}"
export PREF_LINKFLAGS="%{rpmldflags}"
jam -fJambase %{_smp_mflags} -dx -sPREFIX="%{_prefix}" -sREFSUBDIR=share/color/argyll/ref  all

%install
rm -rf $RPM_BUILD_ROOT
jam -fJambase %{_smp_mflags} -dx -sPREFIX="%{_prefix}" -sDESTDIR=$RPM_BUILD_ROOT -sREFSUBDIR=share/color/argyll/ref  install

%{__rm} $RPM_BUILD_ROOT%{_prefix}/bin/License.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Readme.txt
%attr(755,root,root) %{_bindir}/applycal
%attr(755,root,root) %{_bindir}/average
%attr(755,root,root) %{_bindir}/cb2ti3
%attr(755,root,root) %{_bindir}/cctiff
%attr(755,root,root) %{_bindir}/ccxxmake
%attr(755,root,root) %{_bindir}/chartread
%attr(755,root,root) %{_bindir}/collink
%attr(755,root,root) %{_bindir}/colprof
%attr(755,root,root) %{_bindir}/colverify
%attr(755,root,root) %{_bindir}/cxf2ti3
%attr(755,root,root) %{_bindir}/dispcal
%attr(755,root,root) %{_bindir}/dispread
%attr(755,root,root) %{_bindir}/dispwin
%attr(755,root,root) %{_bindir}/extracticc
%attr(755,root,root) %{_bindir}/extractttag
%attr(755,root,root) %{_bindir}/fakeCMY
%attr(755,root,root) %{_bindir}/fakeread
%attr(755,root,root) %{_bindir}/greytiff
%attr(755,root,root) %{_bindir}/iccdump
%attr(755,root,root) %{_bindir}/iccgamut
%attr(755,root,root) %{_bindir}/icclu
%attr(755,root,root) %{_bindir}/iccvcgt
%attr(755,root,root) %{_bindir}/illumread
%attr(755,root,root) %{_bindir}/invprofcheck
%attr(755,root,root) %{_bindir}/kodak2ti3
%attr(755,root,root) %{_bindir}/ls2ti3
%attr(755,root,root) %{_bindir}/mppcheck
%attr(755,root,root) %{_bindir}/mpplu
%attr(755,root,root) %{_bindir}/mppprof
%attr(755,root,root) %{_bindir}/oeminst
%attr(755,root,root) %{_bindir}/printcal
%attr(755,root,root) %{_bindir}/printtarg
%attr(755,root,root) %{_bindir}/profcheck
%attr(755,root,root) %{_bindir}/refine
%attr(755,root,root) %{_bindir}/revfix
%attr(755,root,root) %{_bindir}/scanin
%attr(755,root,root) %{_bindir}/spec2cie
%attr(755,root,root) %{_bindir}/specplot
%attr(755,root,root) %{_bindir}/splitti3
%attr(755,root,root) %{_bindir}/spotread
%attr(755,root,root) %{_bindir}/synthcal
%attr(755,root,root) %{_bindir}/synthread
%attr(755,root,root) %{_bindir}/targen
%attr(755,root,root) %{_bindir}/tiffgamut
%attr(755,root,root) %{_bindir}/timage
%attr(755,root,root) %{_bindir}/txt2ti3
%attr(755,root,root) %{_bindir}/viewgam
%attr(755,root,root) %{_bindir}/xicclu
%dir %{_datadir}/color/argyll
%{_datadir}/color/argyll/ref

%files doc
%defattr(644,root,root,755)
%doc doc/*.html doc/*.jpg doc/*.txt
