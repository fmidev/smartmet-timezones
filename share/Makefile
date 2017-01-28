all: timezone.shz

# World timezones in 1km resolution

timezone.shz: timezone.shp
	shapepack -v -a TZID -s timezone -o timezone.shz -W 40000
	# shapepack -v -a TZID -s timezone -o test.shz -W 2000 -p test.png

