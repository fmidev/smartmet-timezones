# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

`smartmet-timezones` is a data-only package (noarch RPM) providing the global timezone polygons used by SmartMet:

- **`timezones-with-oceans.shp`** (+ `.shx`, `.dbf`, `.prj`) — global timezone polygons from [timezone-boundary-builder](https://github.com/evansiroky/timezone-boundary-builder) (OpenStreetMap based), stored as the unmodified release zip `share/timezones-with-oceans-<release>.shapefile.zip` and unpacked by `make install`

The shapefile is the default source of `Fmi::TimeZoneFinder` in `smartmet-library-gis`, used by `smartmet-engine-geonames` and `qdpoint` in `smartmet-qdtools`. Timezone rules come from the system tzdata, not from this package.

## Build Commands

```bash
make rpm      # Build noarch RPM
make install  # Unpack and install the shapefile to $PREFIX/share/smartmet/timezones/
```

## Updating the timezone polygons

```bash
make download TZBB_RELEASE=2026e   # fetch the release zip into share/
```
Then `git rm` the old zip, `git add` the new one, update `TZBB_RELEASE` in the `Makefile`, and bump the spec. The unpacked `.shp` (~130 MB) exceeds the GitHub file size limit, which is why only the zip is committed.
