Summary:	V C++ GUI Framework
Summary(pl):	V - biblioteka do tworzenia GUI dla C++
Name:		v
Version:	1.24a
Release:	2
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://ftp.objectcentral.com/%{name}-%{%{name}ersion}.tar.gz
Source1:	ftp://ftp.objectcentral.com/%{name}ref.pdf
Patch0:		%{name}-config.fix
BuildRequires:	XFree86-devel >= 3.3.5
BuildRequires:	motif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
V is a free, multiple platform C++ graphical user interface framework
designed to make it the easiest way to write C++ GUI applications
available -- commercial, shareware, or freeware. V is available for X
Athena, X Motif/Lesstif, all Windows platforms, and now including
OS/2.

%description -l pl
V jest wieloplatformow╠ bibliotek╠ dla C++ do tworzenia GUI. Jest
dostЙpna dla ╤rodowiska X-Window wraz z Ahtena Widgets,
Motifem/Lesstifem, wszystkich platform Windowsowych, a teraz tak©e dla
OS/2.

%package devel
Summary:	V Development
Summary(pl):	Dla programistСw V
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Development for V library.

%description devel -l pl
Pliki nagЁСwkowe dla biblioteki V.

%package static
Summary:	V static library
Summary(pl):	Biblioteka statyczna V
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
V static library.

%description static -l pl
Biblioteka statyczna V.

%package utils
Summary:	V library utilities
Summary(pl):	NarzЙdzia dla biblioteki V
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description utils
V library utilities.

%description utils -l pl
NarzЙdzia dla biblioteki V.

%prep
%setup -q -n %{name}

%patch -p0
%build
# Make with Motif/Lesstif 
cp -f Configs/ConfigM.mk Config.mk

# set HOMEV to %{_prefix}
# and ARCH to %{_ARCH} ?????
%{__make} HOMEV=`pwd` Arch=linuxelf RPM_OPT_FLAGS="%{rpmcflags}" all

# run make again to create static libraries
%{__make} RPM_OPT_FLAGS="%{rpmcflags}"
 
install %{SOURCE1} $RPM_BUILD_DIR/%{name}/

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
%attr(755,root,root) %{_libdir}/libV*.so*
%attr(755,root,root) %{_bindir}/proto
%attr(755,root,root) %{_bindir}/tutapp
%attr(755,root,root) %{_bindir}/icondemo
%attr(755,root,root) %{_bindir}/vdrawex
%attr(755,root,root) %{_bindir}/vtestlib

%files devel
%defattr(644,root,root,755)
%doc vref.pdf
%attr(644,root,root) %{_includedir}/v/*

%files static
%defattr(644,root,root,755)
%attr(644,root,root) %{_libdir}/libV*.a

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/vgen
%attr(755,root,root) %{_bindir}/viconed
%attr(755,root,root) %{_bindir}/vdraw
%attr(755,root,root) %{_bindir}/b2v
%attr(755,root,root) %{_bindir}/vide
	
