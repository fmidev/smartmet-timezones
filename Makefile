LIB = timezones
SPEC = smartmet-${LIB}

# Installation directories

ifeq ($(origin PREFIX), undefined)
  PREFIX = /usr
else
  PREFIX = $(PREFIX)
endif

datadir = $(PREFIX)/share

# rpm variables

.PHONY: rpm

# The rules

all: csv

csv: 
	@echo "Updating share/date_time_zonespec.csv..."
	@PATH=${PWD}/bin:${PATH} create_date_time_zoneinfo > share/date_time_zonespec.csv
	@echo Use git diff share/date_time_zonespec.csv to inspect differences

rpm:
	@if [ -e $(SPEC).spec ]; \
	then \
	  tar -czvf $(LIB).tar.gz --transform "s,^,$(LIB)/," * ; \
	  TAR_OPTIONS=--wildcards rpmbuild -v -ta $(LIB).tar.gz ; \
	  rm -f $(LIB).tar.gz; \
	else \
	  echo $(SPEC).spec missing; \
	fi;

install:
	mkdir -p $(datadir)/smartmet/$(LIB)
	install -m 0644 share/date_time_zonespec.csv $(datadir)/smartmet/$(LIB)/
	install -m 0644 share/timezone.shz           $(datadir)/smartmet/$(LIB)/
