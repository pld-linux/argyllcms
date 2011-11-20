%define		alphatag	20100201
%define		rel			0.3
Summary:	ICC compatible color management system
Name:		argyllcms
Version:	1.1.0
Release:	0.2.%{alphatag}git.%{rel}
License:	GPL v3 and MIT
Group:		X11
URL:		http://github.com/hughsie/hargyllcms
#Source0:   http://people.freedesktop.org/~hughsient/releases/hargyllcms-%{version}-%{?alphatag}.tar.gz
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/argyllcms/h%{name}-%{version}-%{alphatag}.tar.gz/59cdfbefa1c905967b0848634c2fb509/hargyllcms-%{version}-%{alphatag}.tar.gz
# Source0-md5:	59cdfbefa1c905967b0848634c2fb509
BuildRequires:	libtiff-devel
BuildRequires:	libusb-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires:	udev-core
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

%package doc
Summary:	Argyll CMS documentation
Group:		Documentation
# Does not really make sense without Argyll CMS itself
Requires:	%{name} = %{version}-%{release}

%description doc
The Argyll color management system supports accurate ICC profile
creation for acquisition devices, CMYK printers, film recorders and
calibration and profiling of displays.

This package contains the Argyll color management system
documentation.

%prep
#%setup -q -n hargyllcms-%{version}
%setup -q -n h%{name}-%{?version}-%{?alphatag}

# we're not allowed to refer to acquisition devices as scanners
./legal.sh

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# they shouldn't put Makefile.am to ref_DATA
%{__rm} $RPM_BUILD_ROOT%{_datadir}/color/argyll/ref/Makefile.am

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/color/argyll
%{_datadir}/color/argyll/ref
/lib/udev/rules.d/55-Argyll.rules

%exclude %{_datadir}/doc/argyll

%files doc
%defattr(644,root,root,755)
%doc doc/*.html doc/*.jpg doc/*.txt
