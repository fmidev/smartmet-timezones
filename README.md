# SmartMet Server timezone files
The SmartMet server requires two separate time zone files: date_time_zonespec.csv needed by the Boost.Date_Time library and timezone.shz, a packed 1 km resolution version of timezone.shp to resolve the timezone for any coordinate.

# Boost.Date_Time timezone database

The Boost.Date_Time timezone database does not support past timezones and hence needs to be regularly updated. To ease the maintenance of the database the smartmet-timezones package includes a Makefile and a Perl script which creates the database automatically from the system timezone database in /usr/share/zoneinfo.

# Packed global timezone information

The shapefile included in the package is a merge of two different timezone shapes:
* http://efele.net/maps/tz/world/ defines timezones for land areas including DST information
* http://www.naturalearthdata.com/downloads/10m-cultural-vectors/timezones/ defines timezones for marine areas but does not include DST information
The merged shape covers the entire globe and includes DST information.

The SmartMet server does not use the shapefile directly. Instead, the shapepack program in https://github.com/fmidev/smartmet-shapetools is used to render the shapefile in roughly 1 kilometer accuracy. The raster image is then run length encoded one raster line at a time to provide fast access to the timezone for any coordinate.

The packed shape can be read and used with the WorldTimeZones class in https://github.com/fmidev/smartmet-library-macgyver. The class is used in the SmartMet Server by https://github.com/fmidev/smartmet-engine-geonames.

![Image of world timezones rendered by QGis](/images/timezone.png)
