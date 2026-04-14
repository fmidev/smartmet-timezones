# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

`smartmet-timezones` is a data-only package (noarch RPM) providing two timezone data files used by SmartMet Server:

- **`date_time_zonespec.csv`** — Boost.Date_Time timezone database, auto-generated from the system `/usr/share/zoneinfo` files
- **`timezone.shz`** — Run-length encoded 1km-resolution raster of global timezone boundaries, packed from a shapefile using `shapepack` from smartmet-shapetools

These are consumed by `smartmet-library-macgyver` (WorldTimeZones class) via `smartmet-engine-geonames`.

## Build Commands

```bash
make          # Regenerates share/date_time_zonespec.csv from system zoneinfo
make rpm      # Build noarch RPM
make install  # Install data files to $PREFIX/share/smartmet/timezones/
make test     # No tests currently (placeholder)
```

## Regenerating timezone.shz

The packed shapefile is built separately via `share/Makefile`:
```bash
make -C share timezone.shz   # Requires shapepack from smartmet-shapetools
```
This renders `timezone.shp` at ~1km resolution using attribute `TZID`.

## How the CSV Generation Works

`bin/create_date_time_zoneinfo` (shell) iterates all zoneinfo files, calling `bin/tzinfo` (Perl) on each. The Perl script parses raw TZif binary files to extract current-year DST transition rules and emits one CSV row per timezone in Boost.Date_Time format:

```
"ID","STD ABBR","STD NAME","DST ABBR","DST NAME","GMT offset","DST adjustment","DST Start Date rule","Start time","DST End date rule","End time"
```

DST rules use `week;day;month` format (week=-1 means last week, day 0=Sunday).

## Update Workflow

When new `tzdata` is released:
1. Ensure the system `tzdata` package is updated
2. Run `make` to regenerate the CSV
3. Review changes with `git diff share/date_time_zonespec.csv`
4. Update version in `smartmet-timezones.spec` and add a changelog entry
