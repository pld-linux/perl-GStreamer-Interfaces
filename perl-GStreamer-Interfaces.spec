#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	GStreamer
%define		pnam	Interfaces
Summary:	Perl gstreamer base plugins bindings
Summary(pl):	Wi�zania podstawowych wtyczek gstreamera dla Perla
Name:		perl-GStreamer-Interfaces
Version:	0.03
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0b72d9429ac1e270fa876f72de4bdd3c
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.9
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-GStreamer >= 0.09
BuildRequires:	perl-Glib >= 1.132
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Glib >= 1.132
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to gstreamer base plugins library.

%description -l pl
Ten modu� daje dost�p z poziomu Perla do podstawowych wtyczek
gstreamera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/GStreamer/Interfaces/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/GStreamer/Interfaces.pm
%dir %{perl_vendorarch}/GStreamer/Interfaces
%dir %{perl_vendorarch}/auto/GStreamer/Interfaces
%attr(755,root,root) %{perl_vendorarch}/auto/GStreamer/Interfaces/*.so
%{perl_vendorarch}/GStreamer/Interfaces/Install
%{perl_vendorarch}/auto/GStreamer/Interfaces/*.bs
%{_mandir}/man3/*
