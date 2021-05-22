#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Role-Tiny
Version  : 2.002004
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Role-Tiny-2.002004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Role-Tiny-2.002004.tar.gz
Summary  : 'Roles: a nouvelle cuisine portion size slice of Moose'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Role-Tiny-license = %{version}-%{release}
Requires: perl-Role-Tiny-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Role::Tiny - Roles: a nouvelle cuisine portion size slice of Moose
SYNOPSIS
package Some::Role;

%package dev
Summary: dev components for the perl-Role-Tiny package.
Group: Development
Provides: perl-Role-Tiny-devel = %{version}-%{release}
Requires: perl-Role-Tiny = %{version}-%{release}

%description dev
dev components for the perl-Role-Tiny package.


%package license
Summary: license components for the perl-Role-Tiny package.
Group: Default

%description license
license components for the perl-Role-Tiny package.


%package perl
Summary: perl components for the perl-Role-Tiny package.
Group: Default
Requires: perl-Role-Tiny = %{version}-%{release}

%description perl
perl components for the perl-Role-Tiny package.


%prep
%setup -q -n Role-Tiny-2.002004
cd %{_builddir}/Role-Tiny-2.002004

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Role-Tiny
cp %{_builddir}/Role-Tiny-2.002004/LICENSE %{buildroot}/usr/share/package-licenses/perl-Role-Tiny/f7f18487ddc4af5caae4b3d4bce309474c8e2915
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Role::Tiny.3
/usr/share/man/man3/Role::Tiny::With.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Role-Tiny/f7f18487ddc4af5caae4b3d4bce309474c8e2915

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Role/Tiny.pm
/usr/lib/perl5/vendor_perl/5.34.0/Role/Tiny/With.pm
