#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires X server)
#
%define		pdir	GStreamer
%define		pnam	Interfaces
Summary:	Perl gstreamer base plugins bindings
Summary(pl.UTF-8):	Wiązania podstawowych wtyczek gstreamera dla Perla
Name:		perl-GStreamer-Interfaces
Version:	0.07
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	https://downloads.sourceforge.net/gtk2-perl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ccb354c9e6f05a25d825e439b3e04c01
URL:		http://gtk2-perl.sourceforge.net/
BuildRequires:	gstreamer0.10-plugins-base-devel >= 0.10.9
BuildRequires:	perl-ExtUtils-Depends >= 0.205
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.07
BuildRequires:	perl-GStreamer-devel >= 0.09
BuildRequires:	perl-Glib-devel >= 1.180
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
Requires:	perl-GStreamer >= 0.09
Requires:	perl-Glib >= 1.180
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides Perl access to GStreamer base plugins library.

Note: this module is deprecated and no longer maintained.

%description -l pl.UTF-8
Ten moduł daje dostęp z poziomu Perla do podstawowych wtyczek
GStreamera.

Uwaga: ten moduł jest przestarzały i nie jest już utrzymywany.

%package devel
Summary:	Development files for Perl GStreamer-Interfaces bindings
Summary(pl.UTF-8):	Pliki programistyczne wiązań GStreamer-Interfaces dla Perla
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer0.10-plugins-base-devel >= 0.10.9
BuildRequires:	perl-GStreamer-devel >= 0.09
BuildRequires:	perl-Glib-devel >= 1.180

%description devel
Development files for Perl GStreamer-Interfaces bindings.

%description devel -l pl.UTF-8
Pliki programistyczne wiązań GStreamer-Interfaces dla Perla.

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
%dir %{perl_vendorarch}/auto/GStreamer/Interfaces
%attr(755,root,root) %{perl_vendorarch}/auto/GStreamer/Interfaces/Interfaces.so
%{_mandir}/man3/GStreamer::Interfaces*.3pm*

%files devel
%defattr(644,root,root,755)
%{perl_vendorarch}/GStreamer/Interfaces/Install
