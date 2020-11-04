import pandas as pd
import numpy as np
from selenium import webdriver
from bs4 import BeautifulSoup
import requests

df = pd.read_csv('mod_salary.csv')
first = []
second = []
third = []
subsidiary = []
skills = df['Skills in demand']
for x in skills:
    if len(x)>2:
        tmp1 = x[1:-1]
        tmp2 = tmp1.split(',')
        tmp2 = [i.lstrip() for i in tmp2]
        if len(tmp2)==1:
            first.append(tmp2[0][1:-1])
            second.append('')
            third.append('')
            subsidiary.append('')
        elif len(tmp2)==2:
            first.append(tmp2[0][1:-1])
            second.append(tmp2[1][1:-1])
            third.append('')
            subsidiary.append('')
        elif len(tmp2)==3:
            first.append(tmp2[0][1:-1])
            second.append(tmp2[1][1:-1])
            third.append(tmp2[2][1:-1])
            subsidiary.append('')
        else:
            first.append(tmp2[0][1:-1])
            second.append(tmp2[1][1:-1])
            third.append(tmp2[2][1:-1])
            tmp = []
            for i in range(3,len(tmp2)):
                tmp.append(tmp2[i][1:-1])
            subsidiary.append(tmp)
    else:
        first.append('')
        second.append('')
        third.append('')
        subsidiary.append('')

df['First'] = first
df['Second'] = second
df['Third'] = third
df['Subsidiary'] = subsidiary
df.to_csv('fin_salary.csv')


jobs = df['Job']
jobs = list(set(jobs))
dic4 = {'Design_Architect': 'Design Architect',
        'Business_Intelligence_(BI)_Developer': 'Busines Analyst',
        'iOS_Developer': 'iOS Developer',
        'Test_%2F_Quality_Assurance_(QA)_Engineer_(Computer_Software)': 'QA Engineer',
        'High_School_Teacher': 'High School Teacher', 'Web_Designer_%26_Developer': 'Web Designer',
        'Data_Scientist': 'Data Scientist',
        'Professor%2C_Postsecondary_%2F_Higher_Education': 'Professor',
        '.NET_Software_Developer_%2F_Programmer': '.NET SDE',
        'Lead_Software_Engineer': 'Lead Software Engineer', 'Senior_Java_Developer': 'Senior Java Developer',
        'Telecommunications_Engineer': 'Telecommunications Engineer', 'Accountant': 'Accountant',
        'Environmental_Engineer': 'Environmental Engineer',
        'Associate Professor%2C_Postsecondary_%2F_Higher_Education': 'Associate Professor',
        'Java_Developer': 'Java Developer', 'General_Manager': 'General Manager',
        'Financial_Analyst': 'Financial Analyst', 'Cyber_Security_Analyst': 'Cyber Security Analyst',
        'Project_Manager%2C_Information_Technology_(IT)': 'Project_Manager',
        'Network_Engineer': 'Network Engineer', 'Database_Administrator_(DBA)': 'Database Administrator',
        'Chartered_Accountant': 'Chartered Accountant', 'Senior_Project_Manager%2C_IT': 'Senior Project Manager',
        'Deputy_General_Manager': 'Deputy General Manager', 'Data_Engineer': 'Data Engineer',
        'ScrumMaster': 'ScrumMaster', 'Finance_Manager': 'Finance Manager', 'Web_Developer': 'Web Developer',
        'Primary_School_Teacher': 'Primary School Teacher', 'Software_Engineer': 'Software Engineer',
        'Front_End_Developer_%2F_Engineer': 'Front End Developer',
        'Assistant_General_Manager_(AGM)': 'AGM',
        'Secondary_School_Teacher': 'Secondary School Teacher', 'Application_Developer': 'Application Developer'}


df['Job'] = df['Job'].map(dic4)

cities = list(df['Cities'])
cities = list(set(cities))
lis = []
dic1 = {}
for x in cities:
    dic1[x] = x.split(',')[0]

dic2 = {'Canberra': '1,289.84A$', 'Brisbane': '1,356.69A$', 'Samara': '31,305.44руб', 'Düsseldorf': '789.44€',
        'Townsville': '0', 'Shanghai': '4,550.11¥', 'Delhi': '27,215.80₹', 'London': '832.77£',
        'St. Petersburg': '949.00$',
        'Hangzhou': '3,173.31¥', 'Adelaide': '1,173.85A$', 'Stuttgart': '790.04€', 'CHINA': '0', 'Chicago': '1,050.82$',
        'Melbourne': '1,313.23A$', 'Herzogenaurach': '0', 'San Diego': '978.92$', 'Charlotte': '1,003.46$',
        'RUSSIA': '0',
        'Edinburgh': '685.34£', 'Belfast': '574.61£', 'Vancouver': '1,184.47C$', 'Gold Coast': '1,272.43A$',
        'Nizhny Novgorod': '34,105.08руб', 'San Antonio': '832.19$', 'Ahmedabad': '24,995.23₹',
        'Minneapolis': '1,055.56$',
        'Columbus': '926.27$', 'Guangzhou': '3,718.69¥', 'New York': '1,307.65$', 'Frankfurt': '856.19€',
        'Bremen': '747.33€',
        'Austin': '836.05$', 'Kitchener': '1,090.68C$', 'Denver': '993.88$', 'Nuremberg': '792.69€',
        'Washington': '1,120.07$',
        'Phoenix': '874.55$', 'Bangalore': '26,220.74₹', 'Glasgow': '611.82£', 'Hamburg': '818.78€',
        'Atlanta': '993.89$',
        'Burnaby': '1,205.30C$', 'Seattle': '1,157.82$', 'Brampton': '1,167.56C$', "Bishop's Stortford": '0',
        'Munich': '861.20€', 'Halifax': '1,202.14C$', 'San Jose': '0', 'Aachen': '716.56€', 'Guildford': '739.72£',
        'Dallas': '880.98$', 'Portland': '1,024.28$', 'Montréal': '1,049.62C$', 'SWITZERLAND': '0',
        'Milwaukee': '1,019.37$',
        'NETHERLANDS': '0', 'Chennai': '24,516.72₹', 'San Francisco': '1,180.72$', 'Auckland': '1,444.93NZ$',
        'Novosibirsk': '31,516.79руб', 'Manchester': '654.73£', 'Sydney': '1,432.60A$', 'Victoria': '1,167.96C$',
        'Brighton': '761.09£', 'Los Angeles': '1,048.40$', 'New Delhi': '27,215.80₹', 'Winnipeg': '1,100.01C$',
        'Mississauga': '1,216.15C$', 'Beijing': '4,168.57¥', 'Frankfurt am Main': '0', 'Mumbai': '28,405.58₹',
        'Salt Lake City': '826.47$', 'Coimbatore': '21,991.09₹', 'Perth': '1,301.18A$', 'Philadelphia': '985.39$',
        'Noida': '28,141.60₹', 'Gurgaon': '31,134.26₹', 'Bristol': '711.87£', 'Leeds': '595.14£',
        'Huntsville': '770.67$',
        'Leicester': '631.56£', 'Newcastle-upon-Tyne': '611.32£', 'Tampa': '999.65$', 'Toronto': '1,240.32C$',
        'Kolkata': '24,500.09₹', 'Sheffield': '632.64£', 'York': '712.05£', 'Birmingham': '655.93£',
        'Shenzhen': '4,183.23¥',
        'Hyderabad': '24,588.30₹', 'Newcastle': '1,358.95A$', 'Cologne': '817.19€', 'SWEDEN': '0',
        'Ottawa': '1,141.33C$',
        'Surrey': '1,179.71C$', 'Tomsk': '30,259.29руб', 'Waterloo': '0', 'Mackay': '0', 'Baltimore': '962.55$',
        'Edmonton': '1,199.75C$', 'Berlin': '781.52€', 'Southampton': '642.72£', 'Houston': '856.44$',
        'Cairns': '1,334.62A$',
        'Bendigo': '0', 'Kelowna': '1,102.62C$', 'Liverpool': '635.40£', 'Miami': '1,070.96$', 'Norwich': '665.50£',
        'JAPAN': '0', 'Cardiff': '644.11£', 'Moscow': '41,984.51руб', 'DENMARK': '0', 'Cambridge': '712.98£',
        'Québec City': '1,026.54C$', 'GERMANY': '0', 'Johannesburg': '9,406.79R', 'Mannheim': '801.10€',
        'NEW ZEALND': '0',
        'Crawley': '0', 'Chengdu': '3,850.15¥', 'Karlsruhe': '704.14€', 'Oxford': '696.43£', 'Nottingham': '670.67£',
        'Hobart': '1,274.25A$', 'Calgary': '1,197.80C$', 'Boston': '1,147.98$', 'Hamilton': '1,088.68C$',
        'Cincinnati': '860.90$', 'Reading': '699.61£', 'Saskatoon': '1,160.65C$', 'Pune': '24,736.68₹'}

dic3 = {'Los Angeles, California': '1,048.40$', 'Nottingham, England: Nottinghamshire': '670.67£',
        'Denver, Colorado': '993.88$', 'Berlin, Berlin': '781.52€', 'Gurgaon, Haryana': '31,134.26₹',
        'Shenzhen, Guangdong': '4,183.23¥', 'DENMARK': '0', 'Delhi, Delhi': '27,215.80₹',
        'Mississauga, Ontario': '1,216.15C$', 'Leicester, England: Leicestershire': '631.56£',
        'Québec City, Québec': '1,026.54C$', 'Saskatoon, Saskatchewan': '1,160.65C$',
        'Coimbatore, Tamil Nadu': '21,991.09₹', 'Reading, England: Berkshire': '699.61£',
        'Philadelphia, Pennsylvania': '985.39$', 'Frankfurt, Hessen': '856.19€', 'Hangzhou, Zhejiang': '3,173.31¥',
        'Canberra, Australian Capital Territory (ACT)': '1,289.84A$', 'Johannesburg, California': '9,406.79R',
        'Düsseldorf, Nordrhein-Westfalen (North Rhine-Westphalia)': '789.44€', 'Dallas, Texas': '880.98$',
        'Norwich, England: Norfolk': '665.50£', 'Bendigo, Victoria': '0', 'Brighton, England: East Sussex': '761.09£',
        'Winnipeg, Manitoba': '1,100.01C$', 'Pune, Maharashtra': '24,736.68₹',
        'Cambridge, England: Cambridgeshire': '712.98£', 'Sydney, New South Wales': '1,432.60A$',
        'Ottawa, Ontario': '1,141.33C$', 'Hamburg, Hamburg': '818.78€', 'GERMANY': '0',
        'Sheffield, England: South Yorkshire': '632.64£', 'Edmonton, Alberta': '1,199.75C$',
        'Chengdu, Sichuan': '3,850.15¥', 'St. Petersburg, Sankt-Peterburg (Saint Petersburg)': '949.00$',
        'Bremen, Bremen': '747.33€', 'Perth, Western Australia': '1,301.18A$', 'Leeds, England: Leeds': '595.14£',
        'London, England: London': '832.77£', 'Manchester, England: Manchester': '654.73£',
        'Novosibirsk, Novosibirskaya': '31,516.79руб', 'Delhi, New York': '27,215.80₹',
        'Adelaide, South Australia': '1,173.85A$', 'San Antonio, Texas': '832.19$',
        'Cardiff, Wales: Cardiff': '644.11£', 'Herzogenaurach, Bavaria (Bayern)': '0',
        'Hyderabad, Andhra Pradesh': '24,588.30₹', 'Frankfurt am Main, Hessen': '856.19€',
        'Huntsville, Alabama': '770.67$', 'New Delhi, Delhi': '27,215.80₹', 'Columbus, Ohio': '926.27$',
        'Hobart, Tasmania': '1,274.25A$', 'Crawley, England: West Sussex': '0', 'Hamilton, Ontario': '1,088.68C$',
        'Ahmedabad, Gujarat': '24,995.23₹', 'Cambridge, Cambridgeshire': '712.98£', 'SWITZERLAND': '0',
        'San Francisco, California': '1,180.72$', 'Nizhny Novgorod, Nizhegorodskaya': '34,105.08руб',
        'Calgary, Alberta': '1,197.80C$', 'London, Ontario': '1,024.76C$', 'Glasgow, Scotland: Glasgow': '611.82£',
        'San Diego, California': '978.92$', 'Kitchener, Ontario': '1,090.68C$', 'Brampton, Ontario': '1,167.56C$',
        'Austin, Texas': '836.05$', 'Moscow, Moskva (Moscow)': '41,984.51руб',
        'Cologne, Nordrhein-Westfalen (North Rhine-Westphalia)': '817.19€', 'Houston, Texas': '856.44$',
        'New York, New York': '1,307.65$', 'Portland, Oregon': '1,024.28$', 'Nuremberg, Bavaria (Bayern)': '792.69€',
        'Edinburgh, Scotland: Edinburgh': '685.34£', 'Canberra, Australian Capital Territory': '1,289.84A$',
        'Guildford, England: Surrey': '739.72£', 'Samara, Samarskaya': '31,305.44руб', 'Baltimore, Maryland': '962.55$',
        'Liverpool, England: Liverpool': '635.40£', 'NEW ZEALND': '0', 'Gold Coast, Queensland': '1,272.43A$',
        'Vancouver, British Columbia': '1,184.47C$', 'Shanghai, Shanghai': '4,550.11¥',
        'Auckland, Auckland': '1,444.93NZ$', 'Leeds, England: West Yorkshire': '595.14£',
        'Kolkata, West Bengal': '24,500.09₹', 'Kelowna, British Columbia': '1,102.62C$', 'Cincinnati, Ohio': '860.90$',
        'Victoria, British Columbia': '1,167.96C$', 'Munich, Bavaria (Bayern)': '861.20€', 'RUSSIA': '0',
        'Washington, District of Columbia': '1,120.07$', 'CHINA': '0', 'Milwaukee, Wisconsin': '1,019.37$',
        'Noida, Uttar Pradesh': '28,141.60₹', 'Burnaby, British Columbia': '1,205.30C$',
        'Charlotte, North Carolina': '1,003.46$', 'Tampa, Florida': '999.65$', 'NETHERLANDS': '0',
        'Guangzhou, Guangdong': '3,718.69¥', 'Minneapolis, Minnesota': '1,055.56$', 'Toronto, Ontario': '1,240.32C$',
        'Brisbane, Queensland': '1,356.69A$', 'Mumbai, Maharashtra': '28,405.58₹',
        'Birmingham, England: Birmingham': '655.93£', 'Mackay, Queensland': '0', 'JAPAN': '0', 'SWEDEN': '0',
        'Mannheim, Baden-Wuerttemberg': '801.10€', 'Miami, Florida': '1,070.96$',
        'Oxford, England: Oxfordshire': '696.43£', 'Tomsk, Tomskaya': '30,259.29руб', 'Salt Lake City, Utah': '826.47$',
        'Atlanta, Georgia': '993.89$', 'Boston, Massachusetts': '1,147.98$', 'Halifax, Nova Scotia': '1,202.14C$',
        'Newcastle, New South Wales': '1,358.95A$', 'Beijing, Beijing': '4,168.57¥',
        'Surrey, British Columbia': '1,179.71C$', 'Townsville, Queensland': '0', 'San Jose, California': '1,008.58$',
        'Birmingham, England: West Midlands': '655.93£', 'Seattle, Washington': '1,157.82$',
        'Southampton, England: Hampshire': '642.72£', 'Waterloo, Ontario': '0', 'Melbourne, Victoria': '1,313.23A$',
        "Bishop's Stortford, England: Hertfordshire": '0', 'Karlsruhe, Baden-Wuerttemberg': '704.14€',
        'Stuttgart, Baden-Wuerttemberg': '790.04€', 'Wollongong, New South Wales': '0',
        'Bangalore, Karnataka': '26,220.74₹', 'Chennai, Tamil Nadu': '24,516.72₹', 'Cairns, Queensland': '1,334.62A$',
        'Phoenix, Arizona': '874.55$', 'Aachen, Nordrhein-Westfalen (North Rhine-Westphalia)': '716.56€',
        'Bristol, England: Bristol': '711.87£', 'Montréal, Québec': '1,049.62C$',
        'Belfast, Northern Ireland: Belfast': '574.61£', 'Chicago, Illinois': '1,050.82$',
        'Newcastle-upon-Tyne, England: Tyne and Wear': '611.32£', 'London, England': '832.77£',
        'York, England: North Yorkshire': '712.05£'}

df['Cost of living pm'] = df['Cities'].map(dic3)

# 1,024.76C$ london ontario
# 1,008.58$ san jose
# 856.19€ frankfurt
cnt = 1
for x in dic1.values():
    url = 'https://www.numbeo.com/cost-of-living/in/' + x
    if x == 'Wollongong':
        continue
    print(cnt)
    print(url)
    print(dic2)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(
        class_='seeding-call table_color summary limit_size_ad_right padding_lower other_highlight_color')
    if results:
        avg = results.find_all('span', class_='emp_number')
        if avg:
            if len(avg[1].text.split(' ')) > 1:
                txt = avg[1].text.split(' ')[1]
                dic2[x] = txt[txt.find("(") + 1:txt.find(")")]
            else:
                dic2[x] = avg[1].text.split(' ')[0]
        else:
            dic2[x] = '0'
    else:
        dic2[x] = '0'
    cnt += 1

lis.remove('DENMARK')
lis.remove('JAPAN')
lis.remove('SWITZERLAND')
lis.remove('RUSSIA')
lis.remove('GERMANY')
lis.remove('NETHERLANDS')
lis.remove('CHINA')


df['Cities'] = df['Cities'].apply(lambda x: x.split(',')[0])
df.to_csv('fin_salary.csv')
