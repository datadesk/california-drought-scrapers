droughtmonitordata:
	pipenv run jupyter execute drought-monitor/drought-monitor.ipynb

precipitationdata:
	pipenv run jupyter execute precipitation/daily-precipitation.ipynb
	pipenv run jupyter execute precipitation/precipitation.ipynb

reservoirsdata:
	pipenv run jupyter execute reservoirs/download/01-statewide.ipynb
	pipenv run jupyter execute reservoirs/download/01-dwr.ipynb
	pipenv run jupyter execute reservoirs/download/01-colorado-bor.ipynb
	pipenv run jupyter execute reservoirs/process/01-statewide.ipynb
	pipenv run jupyter execute reservoirs/process/01-dwr.ipynb
	pipenv run jupyter execute reservoirs/process/01-colorado.ipynb

snowpackdata:
	pipenv run jupyter execute snowpack/download-timeseries.ipynb

urbanwaterusedata:
	$(call python,urban-water-use/scrape.py)
	pipenv run jupyter execute urban-water-use/r-gpcd.ipynb
