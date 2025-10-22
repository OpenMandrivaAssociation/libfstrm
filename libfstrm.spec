%define major 0
%define libname %mklibname fstrm
%define devname %mklibname fstrm -d

Name:		libfstrm
Version:	0.6.1
Release:	1
Source0:	https://dl.farsightsecurity.com/dist/fstrm/fstrm-%{version}.tar.gz
Summary:	C implementation of the Frame Streams data transport protocol
URL:		https://github.com/farsightsec/fstrm
License:	GPL
Group:		System/Libraries
BuildRequires:	autoconf automake slibtool
BuildRequires:	pkgconfig(libevent)
BuildSystem:	autotools

%description
C implementation of the Frame Streams data transport protocol

%package -n %{libname}
Summary:	C implementation of the Frame Streams data transport protocol
Group:		System/Libraries

%description -n %{libname}
C implementation of the Frame Streams data transport protocol

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%{name} is a C implementation of the Frame Streams data transport protocol

%prep -a
if [ -e autogen.sh ]; then ./autogen.sh; fi

%files
%{_bindir}/*
%{_mandir}/man1/*.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
