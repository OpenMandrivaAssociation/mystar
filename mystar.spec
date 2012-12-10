
%define version 2.56
%define release %mkrel 6

Summary:	A 802.1x auth client for Ruijie
Name:		mystar
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Servers
URL:		http://gf.cs.hit.edu.cn/projects/mystar/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://gf.cs.hit.edu.cn/frs/download.php/253/%{name}_for_starV%{version}.tar.gz
# fwang: We don't need static linking libraries
Patch0:		%{name}-2.56-Makefile.patch
# fwang: conf file should be put into /etc
Patch1:		%{name}-2.56-conf-path.patch
BuildRequires:	net-devel >= 1.1.3
BuildRequires:	libpcap-devel

%description
mystar is a 802.1x auth client for Rujie and other compatible network.

%prep
%setup -q -n %{name}_for_%{version}
%patch0 -p0
%patch1 -p0

%build
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_sbindir}
install -m 755 mystar %{buildroot}%{_sbindir}

mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 mystar.conf %{buildroot}%{_sysconfdir}

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Readme.txt
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.56-6mdv2011.0
+ Revision: 620427
- the mass rebuild of 2010.0 packages

* Thu Jun 04 2009 Oden Eriksson <oeriksson@mandriva.com> 2.56-5mdv2010.0
+ Revision: 382718
- rebuilt against libnet 1.1.3

* Wed Oct 29 2008 Oden Eriksson <oeriksson@mandriva.com> 2.56-4mdv2009.1
+ Revision: 298275
- rebuilt against libpcap-1.0.0

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.56-3mdv2009.0
+ Revision: 241053
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Apr 18 2007 Funda Wang <fwang@mandriva.org> 2.56-1mdv2008.0
+ Revision: 14875
- no more changelog needed.
- import the SOURCES and SPECS for mystar
- Created package structure for mystar.

