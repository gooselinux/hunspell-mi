Name: hunspell-mi
Summary: Maori hunspell dictionaries
%define upstreamid 20080630
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://packages.papakupu.maori.nz/hunspell/hunspell-mi-0.1.%{upstreamid}-beta.tar.gz
Group: Applications/Text
URL: http://papakupu.maori.nz/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv3+
BuildArch: noarch

Requires: hunspell

%description
Maori hunspell dictionaries.

%prep
%setup -q -c -n hunspell-mi-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p mi.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/mi_NZ.aff
cp -p mi.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/mi_NZ.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc mi.AUTHORS mi.LICENSE mi.README
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20080630-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080630-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20080630-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 29 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080630-1
- initial version
