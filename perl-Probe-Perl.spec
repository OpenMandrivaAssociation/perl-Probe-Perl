%define modname	Probe-Perl

Summary:	Information about the currently running perl
Name:		perl-%{modname}
Version:	0.03
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Probe::Perl
Source0:	http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Probe-Perl-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Config)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl-devel
# For tests
BuildRequires:	perl(Test)
BuildRequires:	perl(Test::More)

%description
This module provides methods for obtaining information about the currently
running perl interpreter. It originally began life as code in the
'Module::Build' project, but has been externalized here for general use.

%prep
%setup -qn %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*
