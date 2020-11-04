from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

# driver = webdriver.Chrome('bin/chromedriver.exe')
countryToCodeMap = {'INDIA': 'IN', 'AUSTRALIA': 'AU', 'RUSSIA': 'RU', 'UNITED STATES': 'US', 'SWITZERLAND': 'CH',
                    'UNITED KINGDOM': 'UK', 'CANADA': 'CA', 'JAPAN': 'JP', 'CHINA': 'CN', 'NETHERLANDS': 'NL',
                    'GERMANY': 'DE', 'SWEDEN': 'SE', 'DENMARK': 'DK', 'NEW ZEALAND': 'NZ'}
job_profiles = ['Assistant_General_Manager_(AGM)', 'Data_Scientist', 'Software_Engineer', 'Primary_School_Teacher',
                'Secondary_School_Teacher',
                'High_School_Teacher', 'Accountant', 'Finance_Manager', 'Chartered_Accountant', 'Financial_Analyst',
                'Design_Architect', 'Environmental_Engineer', 'Professor%2C_Postsecondary_%2F_Higher_Education',
                'Associate_Professor%2C_Postsecondary_%2F_Higher_Education', 'General_Manager',
                'Deputy_General_Manager', 'Network_Engineer',
                'Database_Administrator_(DBA)', 'Data_Engineer',
                'Test_%2F_Quality_Assurance_(QA)_Engineer_(Computer_Software)', 'Lead_Software_Engineer',
                'Web_Developer', 'Front_End_Developer_%2F_Engineer', '.NET_Software_Developer_%2F_Programmer',
                'Project_Manager%2C_Information_Technology_(IT)', 'Senior_Project_Manager%2C_IT', 'Java_Developer',
                'Senior_Java_Developer', 'Senior_Java_Developer', 'Business_Intelligence_(BI)_Developer',
                'iOS_Developer', 'Cyber_Security_Analyst', 'Application_Developer', 'Web_Designer_%26_Developer',
                'ScrumMaster', 'Telecommunications_Engineer']

countries = []
code = []
avgSal = []
minSal = []
maxSal = []
city = []


diff = []
job = []
skill = []
maleR = []
femaleR = []

for a, b in countryToCodeMap.items():
    for z in job_profiles:
        url = 'https://www.payscale.com/research/' + b + '/Job=' + z + '/Salary'
        print(url)
        skillset = []
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='__next')
        if results:
            avg = results.find('div', class_='spotlight__value')
            minmax = results.find('div', class_='sidebar')
            tmp = results.find('div', class_='pay-diff-by-dimension diff-table--location')
            ss = results.find('div', class_='pay-diff-by-dimension diff-table--skills')

            name = []
            val = []

            for x in results.find_all('div', class_='pie-chart__labels'):
                for y in x.find_all('div', class_='pie-chart__name'):
                    name.append(y.text)
                for q in x.find_all('div', class_='pie-chart__value'):
                    val.append(q.text)
            male, female = 0, 0
            for i in range(len(name)):
                if name[i] == 'Male':
                    male = val[i]
                if name[i] == 'Female':
                    female = val[i]

            if ss:
                for x in ss.find_all('div', class_='name'):
                    skillset.append(x.text)

            if tmp:
                for x in tmp.find_all('div', class_='name'):
                    countries.append(a)
                    code.append(b)
                    avgSal.append(avg.text)
                    minSal.append(minmax.strong.text.split('-')[0])
                    maxSal.append(minmax.strong.text.split('-')[1])
                    city.append(x.text)
                    job.append(z)
                    skill.append(skillset)
                    maleR.append(male)
                    femaleR.append(female)
                # 9650-up  9660-down
                for x in tmp.find_all('div', class_='arrow'):
                    if ord((x.text)[0]) == 9650:
                        diff.append('+' + (x.text)[1:])
                    else:
                        diff.append('-' + (x.text)[1:])
            else:
                countries.append(a)
                code.append(b)
                avgSal.append(avg.text)
                minSal.append(minmax.strong.text.split('-')[0])
                maxSal.append(minmax.strong.text.split('-')[1])
                city.append(a)
                job.append(z)
                skill.append(skillset)
                maleR.append(male)
                femaleR.append(female)
                diff.append(0)

df = pd.DataFrame({'Country': countries, 'Country code': code, 'Job': job, 'Avg. salary': avgSal, 'Min. salary': minSal,
                   'Max. salary': maxSal, 'Cities': city, 'Variation': diff, 'Male percent': maleR,
                   'Female percent': femaleR, 'Skills in demand': skill})
df.to_csv('salary.csv')
