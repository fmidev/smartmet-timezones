# SmartMet Server timezone files

Part of [SmartMet Server](https://github.com/fmidev/smartmet-server). See the [SmartMet Server documentation](https://github.com/fmidev/smartmet-server) for an overview of the ecosystem.

The package contains `timezones-with-oceans.shp`, the timezone polygons of the entire globe, used to resolve the timezone of any coordinate. The timezone rules themselves come from the system tzdata package.

# Global timezone polygons

The recommended source of timezone polygons is [timezone-boundary-builder](https://github.com/evansiroky/timezone-boundary-builder), which post-processes OpenStreetMap boundary data into polygons for every IANA timezone. The package installs its "with-oceans" release, which covers the entire globe:

```
/usr/share/smartmet/timezones/timezones-with-oceans.shp  (.shx, .dbf, .prj)
```

This shapefile is the default data source of `Fmi::TimeZoneFinder` in [smartmet-library-gis](https://github.com/fmidev/smartmet-library-gis), which the [geonames engine](https://github.com/fmidev/smartmet-engine-geonames) and `qdpoint` in [smartmet-qdtools](https://github.com/fmidev/smartmet-qdtools) use to resolve the timezone of a coordinate. The geonames engine can alternatively read the same data from PostGIS.

Some things to know about the data:

* Land zones include the territorial waters (12 nautical miles). Beyond them the zones are the nautical `Etc/GMT±N` bands, which are 15 degrees wide and have no daylight saving time.
* Some zones overlap on purpose in disputed areas, for example `Asia/Shanghai` and `Asia/Urumqi` in Xinjiang.
* The full "with-oceans" variant keeps every IANA zone. The "now" and "1970" variants merge zones with identical rules since the given time, which loses historical information.
* All coordinates are OpenStreetMap coordinates with 7 decimals.

See the [timezone documentation](https://github.com/fmidev/smartmet-library-gis/blob/master/docs/gis-timezones.md) of smartmet-library-gis for details.

## Updating the polygons

The release zip is stored in `share/` unmodified. The unpacked shapefile (about 130 MB) would exceed the GitHub file size limit, so `make install` unpacks it. To update to a new release:

```
make download TZBB_RELEASE=2026e
git rm share/timezones-with-oceans-2026d.shapefile.zip
git add share/timezones-with-oceans-2026e.shapefile.zip
```

Then update `TZBB_RELEASE` in the `Makefile`. New releases may add timezones, so the system tzdata should be at least as new as the polygons.

## Removed data

Earlier versions of the package also contained:

* `timezone.shz`, a 1 km resolution raster made from a merge of the efele.net land zones and the Natural Earth marine zones. It gave wrong answers near borders, for example in towns on both sides of a border.
* `date_time_zonespec.csv`, the timezone rules for Boost.Date_Time. SmartMet now uses the system tzdata through the date library in smartmet-library-macgyver.
