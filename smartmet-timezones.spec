%define NAME timezones
Name: smartmet-%{NAME}
Version: 17.1.28
Release: 1%{?dist}.fmi
Summary: SmartMet Timezone Database
Group: System Environment/Base
License: MIT
URL: https://github.com/fmidev/smartmet-timezones
Source0: %{NAME}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: bash
BuildRequires: perl
Provides: %{NAME}

%description
Timezone datafiles required by some Smartmet binaries.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{NAME}

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,root)
%{_datadir}/smartmet/%{NAME}/timezone.shz
%{_datadir}/smartmet/%{NAME}/date_time_zonespec.csv

%changelog
* Sat Jan 28 2017 Mika Heiskanen <mika.heiskanen@fmi.fi> - 17.1.28-1.fmi
- Updated using the latest TZ data

* Sat Jan 21 2017 Mika Heiskanen <mika.heiskanen@fmi.fi> - 17.1.21-1.fmi
- Updated using the latest timezone shapefile

* Mon Nov 14 2016 Mika Heiskanen <mika.heiskanen@fmi.fi> - 16.11.14-1.fmi
- Updated using the latest TZ data

* Fri Jul 29 2016 Mika Heiskanen <mika.heiskanen@fmi.fi> - 16.7.29-1.fmi
- Updated using the latest TZ data

* Tue Jun 14 2016 Mika Heiskanen <mika.heiskanen@fmi.fi> - 16.6.14-1.fmi
- Updated using the latest TZ data

* Tue May 10 2016 Mika Heiskanen <mika.heiskanen@fmi.fi> - 16.5.10-1.fmi
- Updated using the latest TZ data

* Mon Mar 21 2016 Mika Heiskanen <mika.heiskanen@fmi.fi> - 16.3.21-1.fmi
- Added scripts for creating date_time_zonespec.csv automatically from system zoneinfo files.

* Mon Oct  5 2015 Mika Heiskanen <mika.heiskanen@fmi.fi> - 15.10.5-1.fmi
- Russia no longer obeys daylight savings rules. Asia/Srednekolymnsk was also missing.

* Fri Aug 21 2015 Tuomo Lauri <tuomo.lauri@fmi.fi> - 15.8.21-1.fmi
- Added Lower_Princes timezone

* Fri Aug  7 2015 Tuomo Lauri <tuomo.lauri@fmi.fi> - 15.8.7-1.fmi
- Fixed typo in 'Kralendijk'

* Thu Aug  6 2015 Tuomo Lauri <tuomo.lauri@fmi.fi> - 15.8.6-1.fmi
- Added Kralendjik timezone

* Fri Feb 13 2015 Mika Heiskanen <mika.heiskanen@fmi.fi> - 15.2.13-1.fmi
- Quintana Roo changed its timezone in 14.1.2015

* Fri Jan 23 2015 Mika Heiskanen <mheiskan@laila.fmi.fi> - 15.1.23-1.fmi
- Updated Asia/Colombo with the 2006 changes
- Samoa moved across the dateline boundary in 2011 and started to follow DST rules. Fixed Pacific/Pago_Pago and Pacific/Apia definitions by copying the rules from Pacific/Auckland and by adjusting things by one hour where necessary (change DST one hour later, and shift UTC+13 instead of +12).

* Tue Oct 22 2013 Mika Heiskanen <mika.heiskanen@fmi.fi> - 13.10.22-1.fmi
- Updated Pacific/Auckland with the 2007 changes

* Tue Aug 13 2013 Mika Heiskanen <mika.heiskanen@fmi.fi> - 13.8.13-1.fmi
- Added timezone.shz
- Added date_time_zonespec.csv
