%define SHORTNAME timezones
Name: smartmet-%{SHORTNAME}
Version: 22.12.13
Release: 1%{?dist}.fmi
Summary: SmartMet Timezone Database
Group: System Environment/Base
License: MIT
URL: https://github.com/fmidev/smartmet-timezones
Source0: smartmet-%{SHORTNAME}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: rpm-build
BuildRequires: make
BuildRequires: bash
BuildRequires: perl
#TestRequires: make
Provides: %{SHORTNAME}

%description
Timezone datafiles required by some Smartmet binaries.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n smartmet-%{SHORTNAME}

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0644,root,root,0775)
%{_datadir}/smartmet/%{SHORTNAME}/timezone.shz
%{_datadir}/smartmet/%{SHORTNAME}/date_time_zonespec.csv

%changelog
* Tue Dec 13 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.12.13-1.fmi
- Update to tzdata-2022g

* Fri Nov 25 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.11.25-1.fmi
- Update to tzdata-2022f

* Wed Oct 12 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.10.12-1.fmi
- Update to tzdata-2022d

* Tue Aug 30 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.8.30-1.fmi
- Update to tzdata-2022c

* Thu Mar 24 2022 Mika Heiskanen <mika.heiskanen@fmi.fi> - 22.3.24-1.fmi
- Update to tzdata-2022a

* Fri Oct 29 2021 Mika Heiskanen <mika.heiskanen@fmi.fi> - 21.10.29-1.fmi
- Update to tzdata-2021e

* Thu Oct 21 2021 Mika Heiskanen <mika.heiskanen@fmi.fi> - 21.10.21-1.fmi
- Update to tzdata-2021c

* Tue Feb  2 2021 Mika Heiskanen <mika.heiskanen@fmi.fi> - 21.2.2-1.fmi
- Update to tzdata-2021a

* Tue Jan  5 2021 Mika Heiskanen <mika.heiskanen@fmi.fi> - 21.1.5-1.fmi
- Update to tzdata-2020f

* Wed Oct 28 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.10.28-1.fmi
- Update to tzdata-2020d

* Wed Oct 21 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.10.21-1.fmi
- Update to tzdata-2020b

* Thu Oct 15 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.10.15-1.fmi
- Replaced Antarctica/Mirny and Antarctica/Central with Etc/GMT versions since Linux Olson database does not recognize the names

* Tue May  5 2020 Mika Heiskanen <mika.heiskanen@fmi.fi> - 20.5.5-1.fmi
- Update to tzdata-2020a

* Mon Jul 29 2019 Mika Heiskanen <mika.heiskanen@fmi.fi> - 19.7.29-1.fmi
- Update to tzdata-2019b

* Tue Apr  2 2019 Mika Heiskanen <mika.heiskanen@fmi.fi> - 19.4.2-1.fmi
- Update to tzdata-2019a

* Fri Jan 25 2019 Mika Heiskanen <mika.heiskanen@fmi.fi> - 19.1.25-1.fmi
- Fixed a bug in tzinfo which caused wrong output for example for Calcutta and Cairo

* Tue Jan 22 2019 Mika Heiskanen <mika.heiskanen@fmi.fi> - 19.1.22-1.fmi
- Update to tzdata-2018i

* Thu Nov  8 2018 Mika Heiskanen <mika.heiskanen@fmi.fi> - 18.11.8-1.fmi
- Update to tzdata-2018g

* Mon Sep 10 2018 Mika Heiskanen <mika.heiskanen@fmi.fi> - 18.9.10-1.fmi
- Improved accuracy for shapepack via shapetools improvements

* Wed May  9 2018 Mika Heiskanen <mika.heiskanen@fmi.fi> - 18.5.9-1.fmi
- Update to tzdata-2018e

* Tue Apr  3 2018 Mika Heiskanen <mika.heiskanen@fmi.fi> - 18.4.3-1.fmi
- Update to tzdata-2018d

* Wed Jan 31 2018 Mika Heiskanen <mika.heiskanen@fmi.fi> - 18.1.31-1.fmi
- Update to tzdata-2018c

* Thu Oct 26 2017 Mika Heiskanen <mika.heiskanen@fmi.fi> - 17.10.26-1.fmi
- Update to tzdata-2017c

* Wed Apr 12 2017 Mika Heiskanen <mika.heiskanen@fmi.fi> - 17.4.12-1.fmi
- Update to tzdata-2017b

* Mon Mar  6 2017 Mika Heiskanen <mika.heiskanen@fmi.fi> - 17.3.6-1.fmi
- Fixed file modes

* Wed Feb  1 2017 Mika Heiskanen <mika.heiskanen@fmi.fi> - 17.2.1-1.fmi
- Fixed date_time_zonespec.csv to include a CSV header row

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
