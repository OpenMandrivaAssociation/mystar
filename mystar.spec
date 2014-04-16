Summary:	A 802.1x auth client for Ruijie
Name:		mystar
Version:	2.56
Release:	7
License:	GPLv2+
Group:		System/Servers
Url:		http://gf.cs.hit.edu.cn/projects/mystar/
Source0:	http://gf.cs.hit.edu.cn/frs/download.php/253/%{name}_for_starV%{version}.tar.gz
# fwang: We don't need static linking libraries
Patch0:		%{name}-2.56-Makefile.patch
# fwang: conf file should be put into /etc
Patch1:		%{name}-2.56-conf-path.patch
BuildRequires:	libnet-devel
BuildRequires:	libpcap-devel

%description
mystar is a 802.1x auth client for Rujie and other compatible network.

%files
%doc Readme.txt
%{_sbindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}_for_%{version}
%patch0 -p0
%patch1 -p0

%build
make Flags="%{optflags}"

%install
mkdir -p %{buildroot}%{_sbindir}
install -m 755 mystar %{buildroot}%{_sbindir}

mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 mystar.conf %{buildroot}%{_sysconfdir}

