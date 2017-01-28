default:

now:
	@echo $(shell date)

data/messages.csv: now
	tinystats messages data-is-plural | python scripts/reformat-csv.py > $@

charts/subscribers.png: now
	python scripts/make-chart-subscribers.py < data/messages.csv > $@

charts/open-rate.png: now
	python scripts/make-chart-open-rate.py < data/messages.csv > $@

charts/unique-opens.png: now
	python scripts/make-chart-unique-opens.py < data/messages.csv > $@

charts: charts/subscribers.png charts/open-rate.png charts/unique-opens.png

all: data/messages.csv charts
