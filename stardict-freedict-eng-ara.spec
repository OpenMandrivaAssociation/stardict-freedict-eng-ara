%define	version	2.4.2
%define release	%mkrel 5
%define dict_format_version	2.4.2

Summary:	English -> Arabic Freedict dictionary for StarDict 2
Name:		stardict-freedict-eng-ara
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Databases
URL:		http://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-dictd_www.freedict.de_eng-ara-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
English -> Arabic Freedict dictionary in StarDict 2 format

%prep
%setup -q -n stardict-dictd_www.freedict.de_eng-ara-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stardict/dic
install -m 0644 * $RPM_BUILD_ROOT%{_datadir}/stardict/dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*



%changelog
* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-5mdv2009.0
+ Revision: 242734
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-3mdv2008.0
+ Revision: 67661
- use %%mkrel


* Sat Oct 01 2005 Abel Cheung <deaddog@mandriva.org> 2.4.2-3mdk
- Rebuild

* Tue Jun 01 2004 Abel Cheung <deaddog@deaddog.org> 2.4.2-2mdk
- Dictionaries require main program as well

* Fri Nov 28 2003 Abel Cheung <deaddog@deaddog.org> 2.4.2-1mdk
- First Mandrake package

