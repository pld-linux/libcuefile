#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
%define		rev	475
Summary:	Library for working with Cue Sheet (cue) and Table of Contents (toc) files
Summary(pl.UTF-8):	Biblioteka do pracy z plikami Cue Sheet (cue) oraz Table of Contents (toc)
Name:		libcuefile
Version:	0.0.1.r%{rev}
Release:	2
License:	GPL v2+
Group:		Libraries
#Source0Download: https://www.musepack.net/index.php?pg=src
Source0:	https://files.musepack.net/source/%{name}_r%{rev}.tar.gz
# Source0-md5:	1a6ac52e1080fd54f0f59372345f1e4e
URL:		https://www.musepack.net/
BuildRequires:	cmake >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for working with Cue Sheet (cue) and Table of Contents (toc)
files.

%description -l pl.UTF-8
Biblioteka do pracy z plikami list ścieżek cue (Cue Sheet) oraz toc
(Table of Contents).

%package devel
Summary:	Header files for CUE File library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki CUE File
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for CUE File library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki CUE File.

%package static
Summary:	Static version of the CUE File library
Summary(pl.UTF-8):	Statyczna wersja biblioteki CUE File
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of the CUE File library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki CUE File.

%prep
%setup -q -n libcuefile_r%{rev}

%build
%cmake

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}
%{__cp} -r include/cuetools $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libcuefile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcuefile.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcuefile.so
%{_includedir}/cuetools

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libcuefile.a
%endif
