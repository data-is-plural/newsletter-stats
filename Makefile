.PHONY: now charts all

default:

now:
	@echo $(shell date)

data/messages.csv: now
	tinystats messages data-is-plural | python scripts/reformat-csv.py > $@

charts:
	python scripts/make-charts.py

all: data/messages.csv charts
