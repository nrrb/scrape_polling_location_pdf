# Extracting Polling Locations from PDF for Chicago Mayoral Election 2015

## Background

The [Chicago Board of Election Commissioners website](http://www.chicagoelections.com/en/your-voter-information.html) has a search form where you can enter your home address and it will tell you your nearest polling location. I find this search form to be awkward to use, and I'd rather just see a map of all the polling locations at once.

They provide a list of all locations, but it's buried in a PDF which is a format that's notoriously difficult to copy structured information from. The PDF contains 2069 polling locations broken up over 50 pages with a lot of filler text between the locations making it harder to parse.

## Prerequisites

Install [pdftohtml](http://brewformulas.org/Pdftohtml) with homebrew:

```
brew install pdftohtml
```

## Procedure

1. Download [the list of polling locations as PDF](http://app.chicagoelections.com/documents/general/document_464.pdf) from the [Chicago Board of Election Commissioners website](http://www.chicagoelections.com/en/your-voter-information.html).

2. Convert the PDF file into HTML with `pdftohtml document_464.pdf`. This generates 3 separate HTML files for some reason, and the file we want is `document_464s.html`.

3. Extract the locations by running the script `python process_polling_locations_html.py document464s.html`. This will output to the files `polling_locations.csv` and `polling_locations-deduplicated.csv`. The first CSV file contains a location for each ward and precinct in the city. There are some locations that serve more than one ward/precinct, so the second CSV file contains a list of distinct polling locations with a compressed listing of the wards/precincts it represents.

## Output

Here's the first 10 lines of `polling_locations.csv`:

```csv
ward,precinct,name,address,accessible
1,1,Yates School,"1826 N Francisco Av, Chicago, IL",True
1,2,Iglesia De Dios,"1859 N Spaulding Av, Chicago, IL",False
1,3,Wells Community Academy,"936 N Ashland Av, Chicago, IL",True
1,4,Commercial Park,"1845 W Rice St, Chicago, IL",True
1,5,LaSalle II Magnet School,"1148 N Honore St, Chicago, IL",True
1,6,The Ogden Intrnl School/Chicago,"1250 W Erie St, Chicago, IL",True
1,7,Haas Park,"2402 N Washtenaw Av, Chicago, IL",True
1,8,Wicker Park Senior Housing,"2020 W Schiller St, Chicago, IL",True
1,9,Campbell Terrace Apartments,"2061 N Campbell Av, Chicago, IL",True
```

Here's the first 10 lines of `polling_locations-deduplicated.csv`:

```csv
name,address,accessible,wards_precincts
Calvary Lutheran Church,"6149 S Kenneth Av, Chicago, IL",False,"ward 13 precinct 14, ward 13 precinct 23"
Noble Square Cooperative,"1165 N Milwaukee Av, Chicago, IL",True,ward 27 precinct 13
Five Holy Martyrs,"4327 S Richmond St, Chicago, IL",False,ward 15 precinct 11
Senn Metro Academy,"5900 N Glenwood Av, Chicago, IL",True,"ward 48 precinct 1, ward 48 precinct 42"
Darwin School,"3116 W Belden Av, Chicago, IL",True,ward 32 precinct 20
Iglesia Cristiana De La Familia,"3053 N Linder Av, Chicago, IL",False,ward 31 precinct 31
Maple Park Missionary Bapt Church,"11759 S Ashland Av, Chicago, IL",True,ward 34 precinct 7
Newberry School,"700 W Willow St, Chicago, IL",True,"ward 43 precinct 5, ward 43 precinct 23"
Draper &amp; Kramer,"1360 N Lake Shore Dr, Chicago, IL",True,ward 43 precinct 28
```

`polling_locations.csv` is uploaded to Google Fusion Tables [here](https://www.google.com/fusiontables/DataSource?docid=1UeZgZMLEvcDi7YTEywlKzJhA3v38S2keo1XWXC7A).

`polling_locations-deduplicated.csv` is uploaded to Google Fusion Tables [here](https://www.google.com/fusiontables/DataSource?docid=1rlFA0vlbJwfR5SFSSQFE_AYcbitGRSPBJ93KAYtA).