all: timezone.shz

# World timezones in 1km resolution

timezone.shz: timezone.shp
	shapepack -v -a TZID -s timezone -o timezone.shz -W 40000

timezone.png:
	shapepack -v -a TZID -s timezone -o /dev/null -W 800 -p timezone.png
