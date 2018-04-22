%define modname	Probe-Perl
%define modver	0.03

Summary:	Information about the currently running perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/K/KW/KWILLIAMS/Probe-Perl-%{modver}.tar.gz
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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

