%define upstream_name    Probe-Perl
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Information about the currently running perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Probe/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Config)
BuildRequires:	perl(Module::Build::Compat)
BuildRequires:	perl(Test)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
This module provides methods for obtaining information about the currently
running perl interpreter. It originally began life as code in the
'Module::Build' project, but has been externalized here for general use.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-4mdv2012.0
+ Revision: 765607
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.10.0-2
+ Revision: 654287
- rebuild for updated spec-helper

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 422795
- rebuild using %%perl_convert_version

* Mon Aug 31 2009 Jérôme Quelin <jquelin@mandriva.org> 0.01-2mdv2010.0
+ Revision: 422789
- rebuild

* Sat Aug 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.01-1mdv2009.0
+ Revision: 277669
- import perl-Probe-Perl


