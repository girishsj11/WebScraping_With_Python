# WebScraping_With_Python
## Webscrape

### ***Amazon***

**Program motive :-**   
   ***Amazon.py***
         Storing the user favourite items details from the first page  into csv file.
   ***Amazon_updated.py***
         Storing the user favourite items details from minimum 5 pages into csv file.
            if user wants to increase the count of page , he/she can edit the python program where (if page==6).

**Pre-requisite things :**
   - pip install bs4
   - pip install csv
   - pip install requests
   - Good internet connection
 
**Program execution :** 
   - loading the webpage url with item name entered by user to the main program
   - taking out the contents of webpage by request module & passing it into BeautifullSoup module to get prettify results
   - calling csv writer function for each item's details to be carried into the csv file
