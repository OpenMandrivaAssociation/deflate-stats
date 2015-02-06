Summary:	Apache mod_deflate logfile analyzer
Name:		deflate-stats
Version:	1.0
Release:	6
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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-5mdv2011.0
+ Revision: 617525
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2010.0
+ Revision: 427959
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2009.0
+ Revision: 244025
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.0-1mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2007.0
+ Revision: 101638
- Import deflate-stats

* Wed Aug 23 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2007.0
- initial Mandriva package

