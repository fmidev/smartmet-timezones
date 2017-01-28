LIB = timezones
SPEC = smartmet-${LIB}

# rpm variables

rpmsourcedir = /tmp/$(shell whoami)/rpmbuild

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
	  tar -C ../ -cf $(rpmsourcedir)/$(LIB).tar $(LIB) ; \
	  gzip -f $(rpmsourcedir)/$(LIB).tar ; \
	  TAR_OPTIONS=--wildcards rpmbuild -v -ta $(rpmsourcedir)/$(LIB).tar.gz ; \
	else \
	  echo $(SPEC).spec missing; \
	fi;

install:
	mkdir -p $(datadir)/smartmet/$(LIB)
	install -m 0644 share/date_time_zonespec.csv $(datadir)/smartmet/$(LIB)/
	install -m 0440 share/timezone.shz           $(datadir)/smartmet/$(LIB)/
