#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 16:45:28 2020

@author: giri
"""

import csv
import requests
from bs4 import BeautifulSoup

def csvwriter(results):
    with open(csvfile,'a+') as file:
        writer = csv.writer(file)
        for item in range(len(results)):
            print("------******"+str(item)+"******------")
            element = results[item]
                    
                #to get a each item title tag name 
            title = element.find('div','_4rR01T').text
            print(title)
                    
            try:
                    #to get a each item's price 
                price = element.find("div","_30jeq3 _1_WHN1").text
                print(price)
            except:
                price = "Price is not available"
                    
            try:
                    #to get a each item's star out of 5 
                star = element.find("div","_3LWZlK").text
                    #star = item.i.text
                print(star)
            except:
                star = "star rating is not available"
                    
                    
            try:
                    #to get a each item's review count 
                review_count = element.find("span","_2_R_DZ").text
                print(review_count)
            except:
                review_count= "No reviews Yet!!"
                        
            print()
                    
            result = [title,price,star,review_count]
                    
            writer.writerow(result)   


def extract_data(new_url):
    '''
    header is predefined ,The very first thing you need to take care 
    of is setting the user-agent. User Agent is a tool that works on behalf of the user and tells the server 
    about which web browser the user is using for visiting the website. 
    '''
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    
    #loading the url pages to the request module with headers variable data to make the browser accessing by the user not by BOT
    page = requests.get(url=new_url,headers=headers)
    
    if(page.status_code != 200):
        print("Check your internet connections & Retry once !! ")
    
    #passing the contents of url to beautiful soup package to parse it with html language
    soup = BeautifulSoup(page.text,'html.parser')
        
    results = soup.find_all("div",{"class":"_2kHMtA"})
    print("Total items in the page is : ",len(results))
    
    #passing the results of each to csvwriter funtion to write it on csv file
    
    csvwriter(results)

def get_url(item,url):
    item = item.replace(' ','+')
    page=1
    while(page):
        new_url = url+item+'&page='+str(page)
        extract_data(new_url)
        print("Page : {} details were stored in csv file ".format(page))
        if("Yes" == str(input("Enter Yes to get the data for next page :"))):
            page+=1
            if(page==6):
                print("As user has entered hi/her limit , so program will terminate here !")
                break
            else:
                continue
        else:
            break
    
    print("Users Option is No , so program will terminates here !!")

def main():
    item = str(input("Enter your favourite item to be seacrh on FlipKart.com : "))
    url = "https://www.flipkart.com/search?q="
    
    get_url(item,url)
    
    


if __name__ == "__main__":
    
    csvfile = "results.csv"
    with open(csvfile,'a+') as file:
        writer = csv.writer(file)
        writer.writerow(["Tag_name","Price in INR","Stars","Rating & Reviews Count"])
    
    main()