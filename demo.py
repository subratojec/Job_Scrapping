import requests 
from bs4 import BeautifulSoup
import time

print('Put some skill that you are not familiar with')
unfamiliar_skil = input('>')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python+&txtLocation=India&cboWorkExp1=3').text

    soup = BeautifulSoup(html_text,'html.parser')

    jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    for index,job in enumerate(jobs):
        published_date = job.find('span',class_= 'sim-posted').span.text
        if 'Posted' in published_date:
            company_name = job.find('h3',class_= 'joblist-comp-name').text 

            skills = job.find('span',class_='srp-skills').text.replace(' ','')

            more_info = job.header.h2.a['href']

            if unfamiliar_skil not in skills:

                with open(f'post/{index}.txt','w') as f:
                    f.write(f"Company Name: {company_name.strip()}\n")
                    f.write(f"Skills: {skills.strip()}\n")
                    f.write(f"More Info: {more_info}")

                print(f'File Saved:{index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting for {time_wait} minutes...")
        time.sleep(time_wait * 60 )




