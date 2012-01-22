%define upstream_name    Probe-Perl
%define upstream_version 0.01

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 4

Summary:    Information about the currently running perl
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Probe/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Config)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl(Test)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides methods for obtaining information about the currently
running perl interpreter. It originally began life as code in the
'Module::Build' project, but has been externalized here for general use.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
