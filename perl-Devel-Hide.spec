#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Hide
Summary:	Devel::Hide - Forces the unavailability of specified Perl modules (for testing)
#Summary(pl.UTF-8):
Name:		perl-Devel-Hide
Version:	0.0008
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3b38c60feed1e922093f5f68dd6d5c20
URL:		http://search.cpan.org/dist/Devel-Hide/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Given a list of Perl modules/filenames, this module makes require and
use statements fail (no matter the specified files/modules are
installed or not).

They die with a message like:

Can't locate Module/ToHide.pm (hidden)

The original intent of this module is to allow Perl developers to test
for alternative behavior when some modules are not available. In a
Perl installation, where many modules are already installed, there is
a chance to screw things up because you take for granted things that
may not be there in other machines.

For example, to test if your distribution does the right thing when a
module is missing, you can do

# %description -l pl.UTF-8

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Devel/*.pm
%{_mandir}/man3/*
