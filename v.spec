# TODO:
# - fix build with current gcc
# - opt patch (RPM_OPT_FLAGS is not used)
# - review %files (*.so*)
Summary:	V C++ GUI Framework
Summary(pl):	V - biblioteka do tworzenia GUI dla C++
Name:		v
Version:	1.24a
Release:	2
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.objectcentral.com/%{name}-%{version}.tar.gz
# Source0-md5:	6336c1e2e9f7fa734cb021fffbfa0a95
Source1:	ftp://ftp.objectcentral.com/%{name}ref.pdf
# Source1-md5:	0ed281664d7cb0dedaf054aa890b6189
Patch0:		%{name}-config.fix
BuildRequires:	XFree86-devel >= 3.3.5
BuildRequires:	motif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
V is a free, multiple platform C++ graphical user interface framework
designed to make it the easiest way to write C++ GUI applications
available -- commercial, shareware, or freeware. V is available for X
Athena, X Motif/Lesstif, all Windows platforms, and now including
OS/2.

%description -l pl
V jest wieloplatformow± bibliotek± dla C++ do tworzenia GUI. Jest
dostêpna dla ¶rodowiska X-Window wraz z Ahtena Widgets,
Motifem/Lesstifem, wszystkich platform Windowsowych, a teraz tak¿e dla
OS/2.

%package devel
Summary:	V Development
Summary(pl):	Dla programistów V
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development for V library.

%description devel -l pl
Pliki nag³ówkowe dla biblioteki V.

%package static
Summary:	V static library
Summary(pl):	Biblioteka statyczna V
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
V static library.

%description static -l pl
Biblioteka statyczna V.

%package utils
Summary:	V library utilities
Summary(pl):	Narzêdzia dla biblioteki V
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description utils
V library utilities.

%description utils -l pl
Narzêdzia dla biblioteki V.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
# Make with Motif/Lesstif
cp -f Configs/ConfigM.mk Config.mk

# set HOMEV to %{_prefix}
# and ARCH to %{_ARCH} ?????
%{__make} all \
	HOMEV=`pwd` \
	Arch=linuxelf \
	RPM_OPT_FLAGS="%{rpmcflags}"

# run make again to create static libraries
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}"

install %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/v}

install lib/libV.so.* $RPM_BUILD_ROOT%{_libdir}
install lib/libVgl.so.* $RPM_BUILD_ROOT%{_libdir}

install lib/*.a $RPM_BUILD_ROOT%{_libdir}

install includex/v/*  $RPM_BUILD_ROOT%{_includedir}/v

rm -f bin/ThisIs
install bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/proto
%attr(755,root,root) %{_bindir}/tutapp
%attr(755,root,root) %{_bindir}/icondemo
%attr(755,root,root) %{_bindir}/vdrawex
%attr(755,root,root) %{_bindir}/vtestlib
%attr(755,root,root) %{_libdir}/libV*.so*

%files devel
%defattr(644,root,root,755)
%doc vref.pdf
%{_includedir}/v

%files static
%defattr(644,root,root,755)
%{_libdir}/libV*.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vgen
%attr(755,root,root) %{_bindir}/viconed
%attr(755,root,root) %{_bindir}/vdraw
%attr(755,root,root) %{_bindir}/b2v
%attr(755,root,root) %{_bindir}/vide
