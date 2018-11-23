#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Role-Tiny
Version  : 2.000006
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Role-Tiny-2.000006.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/H/HA/HAARG/Role-Tiny-2.000006.tar.gz
Summary  : 'Roles. Like a nouvelle cuisine portion size slice of Moose.'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
Role::Tiny - Roles. Like a nouvelle cuisine portion size slice of Moose.
SYNOPSIS
package Some::Role;

%package dev
Summary: dev components for the perl-Role-Tiny package.
Group: Development
Provides: perl-Role-Tiny-devel = %{version}-%{release}

%description dev
dev components for the perl-Role-Tiny package.


%prep
%setup -q -n Role-Tiny-2.000006

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.0/Role/Tiny.pm
/usr/lib/perl5/vendor_perl/5.28.0/Role/Tiny/With.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Role::Tiny.3
/usr/share/man/man3/Role::Tiny::With.3
