Summary:	V C++ GUI Framework
Summary(pl):	V biblioteka do tworzenia GUI dla C++
Name:		v
Version:	1.22
Release:	1
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://objectcentra.com/%{name}-%{version}.tar.gz
Patch:		v-config.fix
#BuildRequires:	Athena-devel
Buildroot: /tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
V is a free, multiple platform C++ graphical user interface framework designed
to make it the easiest way to write C++ GUI applications available -- 
commercial, shareware, or freeware.
V is available for X Athena, X Motif/Lesstif, all Windows platforms, and now including OS/2. 

%description -l pl
V jest wieloplatformow± bibliotek± dla C++ do tworzenia GUI.
Jest dostêpna dla ¶rodowiska X-Window wraz z Ahtena Widgets, Motif/Lesstif.
Wszystkich platform Windowsowych, a teraz tak¿e dla OS/2.

%package	devel
Summary:	V Development
Summary(pl):	V Development
Group:		Libraries/Development
Group(pl):	Biblioteki/Programowanie

%description devel
Development for V library.

%description -l pl devel
Pliki nag³ówkowe dla biblioteki V.

%prep
%setup -q -n %{name}

%patch -p0
%build
# Make with Motif/Lesstif 
cp Configs/ConfigM.mk Config.mk

# set HOMEV to %{_prefix}
# and ARCH to %{_ARCH} ?????
make HOMEV=`pwd` Arch=linuxelf RPM_OPT_FLAGS="$RPM_OPT_FLAGS" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_bindir},%{_includedir}/v}

install lib/libV.so.1.22 $RPM_BUILD_ROOT%{_libdir}
install lib/libVgl.so.1.22 $RPM_BUILD_ROOT%{_libdir}

install includex/v/*  $RPM_BUILD_ROOT%{_includedir}/v

rm bin/ThisIs
install -s bin/* $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc
%attr(755,root,root) %{_libdir}/libV*.so.1.22
%attr(755,root,root) %{_bindir}/*

%files devel
%defattr(644, root, root, 755)
%doc
%attr(644,root,root) %{_includedir}/v/*

%changelog
* Thu Oct  7 1999 Wojciech "Sas" Ciêciwa <cieciwa@alpha.zarz.agh.edu.pl>
-build RPM.
