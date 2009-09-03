Summary:	Apache mod_deflate logfile analyzer
Name:		deflate-stats
Version:	1.0
Release:	%mkrel 4
License:	BSD-like
Group:		Monitoring
URL:		http://prefetch.net/code/deflate-stats.html
Source0:	http://prefetch.net/code/deflate-stats.pl.bz2
Requires:	apache-mod_deflate
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
deflate-stats.pl is a Perl script that summarizes mod_deflate log data, and
provides detailed reports that include the amount of bandwidth saved, bytes not
sent, number of requestes deflated, and compresion ratios per URI.

%prep

%setup -q -c -T
bzcat %{SOURCE0} > %{name}

%build

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}


