import requests
from bs4 import BeautifulSoup

url = "https://iftp.chinamoney.com.cn/english/bdInfo/"
params = {"bondType": "Treasury Bond", "issueYear": "2023"}

response = requests.get(url, params=params)
html = response.content

soup = BeautifulSoup(html, "html.parser")

table = soup.find("table", attrs={"class": "dm-table-data"})

with open("treasury_bonds_2023.csv", "w") as f:
    f.write("ISIN,Bond Code,Issuer,Bond Type,Issue Date,Latest Rating\n")

    rows = table.find_all("tr")
    for row in rows[1:]: 
        cells = row.find_all("td")
        isin = cells[0].text.strip()
        bond_code = cells[1].text.strip()
        issuer = cells[2].text.strip()
        bond_type = cells[3].text.strip()
        issue_date = cells[4].text.strip()
        latest_rating = cells[5].text.strip()
        f.write(f"{isin},{bond_code},{issuer},{bond_type},{issue_date},{latest_rating}\n")