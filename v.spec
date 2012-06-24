Summary:	V C++ GUI Framework
Summary(pl):	V biblioteka do tworzenia GUI dla C++
Name:		v
Version:	1.24a
Release:	1
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source0:	ftp://ftp.objectcentral.com/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.objectcentral.com/vref.pdf
Patch:		v-config.fix
#BuildRequires:	Athena-devel
BuildRequires:	XFree86-devel >= 3.3.5
BuildRequires:	lesstif-devel >= 0.88
Buildroot: /tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
V is a free, multiple platform C++ graphical user interface framework designed
to make it the easiest way to write C++ GUI applications available -- 
commercial, shareware, or freeware.
V is available for X Athena, X Motif/Lesstif, all Windows platforms, and now including OS/2. 

%description -l pl
V jest wieloplatformow� bibliotek� dla C++ do tworzenia GUI.
Jest dost�pna dla �rodowiska X-Window wraz z Ahtena Widgets, Motif/Lesstif.
Wszystkich platform Windowsowych, a teraz tak�e dla OS/2.

%package	devel
Summary:	V Development
Summary(pl):	V Development
Group:		Libraries/Development
Group(pl):	Biblioteki/Programowanie

%description devel
Development for V library.

%description -l pl devel
Pliki nag��wkowe dla biblioteki V.

%package	static
Summary:	V static library.
Summary(pl):	V static library.
Group:		Libraries/Development
Group(pl):	Biblioteki/Programowanie
Requires:	%{name}-devel = %{version}

%description static
%description -l pl static

%package utils
Summary:	V library utilities
Summary(pl):	Narz�dzia dla biblioteki V.
Group:		Libraries/Development
Group(pl):	Biblioteki/Programowanie
Requires:	%{name} = %{version}

%description utils
%description -l pl utils

%prep
%setup -q -n %{name}

%patch -p0
%build
# Make with Motif/Lesstif 
cp Configs/ConfigM.mk Config.mk

# set HOMEV to %{_prefix}
# and ARCH to %{_ARCH} ?????
make HOMEV=`pwd` Arch=linuxelf RPM_OPT_FLAGS="$RPM_OPT_FLAGS" all

# run make again to create static libraries
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
 
install %{SOURCE1} $RPM_BUILD_DIR/%{name}/

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/v}

install lib/libV.so.* $RPM_BUILD_ROOT%{_libdir}
install lib/libVgl.so.* $RPM_BUILD_ROOT%{_libdir}

install lib/*.a $RPM_BUILD_ROOT%{_libdir}

install includex/v/*  $RPM_BUILD_ROOT%{_includedir}/v

rm bin/ThisIs
install -s bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%attr(755,root,root) %{_libdir}/libV*.so*
%attr(755,root,root) %{_bindir}/proto
%attr(755,root,root) %{_bindir}/tutapp
%attr(755,root,root) %{_bindir}/icondemo
%attr(755,root,root) %{_bindir}/vdrawex
%attr(755,root,root) %{_bindir}/vtestlib

%files devel
%defattr(644, root, root, 755)
%doc vref.pdf
%attr(644,root,root) %{_includedir}/v/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/libV*.a

%files utils
%defattr(644,root,root,755)
%attr(644,root,root) %{_bindir}/vgen
%attr(644,root,root) %{_bindir}/viconed
%attr(644,root,root) %{_bindir}/vdraw
%attr(644,root,root) %{_bindir}/b2v
%attr(644,root,root) %{_bindir}/vide
	
