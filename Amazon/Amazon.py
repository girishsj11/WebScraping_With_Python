#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:35:29 2020

@author: giri
"""

import requests
import csv
from bs4 import BeautifulSoup



def csvwriter(results):
    with open(csvfile,'a+') as file:
        writer = csv.writer(file)
        writer.writerow(["item_description","price","stars","review_count"])
        for i in range(len(results)):
            print("------******"+str(i)+"*******------")
            element = results[i]
            
            #to get a each item title tag name 
            title = (element.h2.a).text.strip()
            
            try:
                price = element.find('span','a-price-whole').text
                #print(price)
            except:
                price = "Price is not available"
            
            try:
                star = element.find('span','a-icon-alt').text
                #star = item.i.text
                #print(star)
            except:
                star = "star rating is not available"
            
            
            try:
                review_count = element.find('span',{'class':'a-size-base','dir':'auto'}).text
                #print(review_count)
            except:
                review_count= "No reviews Yet!!"
                
            print()
            
            result = [title,price,star,review_count]
            
            writer.writerow(result)
        






def main(item):
    '''
    Generates a proper weblink to extract the items details from the amazon url

    Parameters
    ----------
    item : string
        which is favourite item entered by the user.

    Returns
    -------
    None.
    
    '''
    url = "https://www.amazon.in/s?k="+(item.replace(' ','+'))
    
    '''
    header is predefined ,The very first thing you need to take care 
    of is setting the user-agent. User Agent is a tool that works on behalf of the user and tells the server 
    about which web browser the user is using for visiting the website. '''
    
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    
    page = requests.get(url,headers=headers)
    
    print("Status code for webpage : 200-Sucessfull, otherthan-Error ",page.status_code)
    soup = BeautifulSoup(page.text,'html.parser')

    results = soup.find_all("div",{"data-component-type":"s-search-result"})
    print("Total items in the page is : ",len(results))
    
    
    
    #calling csvwriter function , so that each item details will write into csv file
    csvwriter(results)
    
    

if __name__ == "__main__" :
    item = str(input("Enter your favourite item to be search on Amazon.in : "))
    csvfile = "results.csv"
    
    main(item)
        
        