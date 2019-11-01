## Geonet Earthquake Data  

I've manually downloaded this from Geonet's quake search: https://quakesearch.geonet.org.nz/  

We've extracted data from 1 Aug 2019 - 1 Nov 2019. Each search has the following format: `https://quakesearch.geonet.org.nz/csv?region=aucklandnorthland&startdate=2019-08-01T1:00:00&enddate=2019-11-1T2:00:00`. It would be easy enough to query this programatically if I want to update these data.

There is a basic data dictionary here: https://www.geonet.org.nz/data/types/eq_catalogue

**Note about missing data** (https://wfs.geonet.org.nz/)  
DEPTHS AND MAGNITUDES  
  - Two earthquakes in our catalogue have an unknown depth represented by -9 km.  
  - Many earthquakes have undetermined magnitudes represented by -9.0. This is either because:  
  - No reliable estimate can be made from these pre-instrumental events, though they will have been felt; or  
  - Insufficient stations calibrated for magnitude recorded the earthquake.  

Massive thanks to Geonet for making these data so easily available. 