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

rpm: $(SPEC).spec
	rm -f $(SPEC).tar.gz # Clean a possible leftover from previous attempt
	tar -czvf $(SPEC).tar.gz --transform "s,^,$(SPEC)/," *
	rpmbuild -ta $(SPEC).tar.gz
	rm -f $(SPEC).tar.gz

install:
	mkdir -p $(datadir)/smartmet/$(LIB)
	install -m 0644 share/date_time_zonespec.csv $(datadir)/smartmet/$(LIB)/
	install -m 0644 share/timezone.shz           $(datadir)/smartmet/$(LIB)/
