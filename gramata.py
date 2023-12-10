

import json


dotiedati=[
    {"nosaukums": "Dabas Stāsti", "autors": "John Smith", "žanrs": "daba", "izdošanas_gads": 2019},
    {"nosaukums": "Programmēšanas Pamati", "autors": "Alice Johnson", "žanrs": "tehnoloģijas", "izdošanas_gads": 2020},
    {"nosaukums": "Kriminālromāns", "autors": "John Smith", "žanrs": "kriminālromāns", "izdošanas_gads": 2018}
  ]

# pirmais uzdevums
gramatu_sk = len(dotiedati)
print(f"Grāmatu skaits ir: {gramatu_sk}")



autora_vards = input("Šeit ievadiet autora vārdu: ")
agrāmatas = [gramata for gramata in dotiedati 
             if gramata["autors"]==autora_vards]

if agrāmatas:
 print(f"{autora_vards} grāmatas: ")
 for gramata in agrāmatas:
  print(f"{gramata['nosaukums']} rakstīts {gramata['izdošanas_gads']}. gadā.")
else:
 print(f"{autora_vards} grāmata nav dotajā sarakstā.")

zanru_sk= {}

for i in dotiedati:
  zanri= i['žanrs']
  zanru_sk[zanri]= zanru_sk.get(zanri,0) +1

for zanri, sk in zanru_sk.items():
  print(f"Šajā žanrā '{zanri}' ir {sk} grāmatu!")