LIB = timezones
SPEC = smartmet-${LIB}

# Installation directories

ifeq ($(origin PREFIX), undefined)
  PREFIX = /usr
else
  PREFIX = $(PREFIX)
endif

datadir = $(PREFIX)/share

# World timezone polygons from https://github.com/evansiroky/timezone-boundary-builder
# The release zip is stored unmodified, the unpacked shapefile would exceed
# the GitHub file size limit.

TZBB_RELEASE = 2026d
TZBB_ZIP = share/timezones-with-oceans-$(TZBB_RELEASE).shapefile.zip
TZBB_URL = https://github.com/evansiroky/timezone-boundary-builder/releases/download/$(TZBB_RELEASE)/timezones-with-oceans.shapefile.zip

# rpm variables

.PHONY: rpm download

# The rules

all:
	@echo Nothing to build, use make install or make rpm

rpm: $(SPEC).spec
	rm -f $(SPEC).tar.gz # Clean a possible leftover from previous attempt
	tar -czvf $(SPEC).tar.gz --transform "s,^,$(SPEC)/," *
	rpmbuild -tb $(SPEC).tar.gz
	rm -f $(SPEC).tar.gz

# Download a new release: make download TZBB_RELEASE=2026e, then update
# TZBB_RELEASE above, git rm the old zip and git add the new one.
download:
	curl -fL -o $(TZBB_ZIP) $(TZBB_URL)

install:
	mkdir -p $(datadir)/smartmet/$(LIB)
	rm -rf tmp-shapefile
	mkdir tmp-shapefile
	unzip -q -d tmp-shapefile $(TZBB_ZIP)
	for ext in shp shx dbf prj; do \
	  install -m 0644 tmp-shapefile/combined-shapefile-with-oceans.$$ext \
	    $(datadir)/smartmet/$(LIB)/timezones-with-oceans.$$ext; \
	done
	rm -rf tmp-shapefile

test:
	@echo Nothing to test.	
	@echo We should possibly test files for correctness.
