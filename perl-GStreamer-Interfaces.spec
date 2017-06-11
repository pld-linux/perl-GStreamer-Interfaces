#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	GStreamer
%define		pnam	Interfaces
Summary:	Perl gstreamer base plugins bindings
Summary(pl.UTF-8):	Wiązania podstawowych wtyczek gstreamera dla Perla
Name:		perl-GStreamer-Interfaces
Version:	0.06
Release:	10
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://downloads.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aa9583a484fa6829935b360887ecda45
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.9
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-GStreamer-devel >= 0.09
BuildRequires:	perl-Glib >= 1.180
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-GStreamer >= 0.09
Requires:	perl-Glib >= 1.180
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to gstreamer base plugins library.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do podstawowych wtyczek
gstreamera.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{perl_vendorarch}/GStreamer/Interfaces.pm
%dir %{perl_vendorarch}/GStreamer/Interfaces
%{perl_vendorarch}/GStreamer/Interfaces/Install
%dir %{perl_vendorarch}/auto/GStreamer/Interfaces
%attr(755,root,root) %{perl_vendorarch}/auto/GStreamer/Interfaces/Interfaces.so
%{_mandir}/man3/GStreamer::Interfaces*.3pm*
