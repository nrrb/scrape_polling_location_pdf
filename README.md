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

3. Extract the locations by running the script `python process_polling_locations_html.py document464s.html`. This will output to the file `polling_locations.csv`.

## Output

Here's the first 10 lines of the CSV output file:

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