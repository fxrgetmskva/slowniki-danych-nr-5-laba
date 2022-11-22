sample_dict = {
 "name": "Kelly",
 "surname": "Jones",
 "age": 25,
 "salary": 8000,
 "city": "New york"}

for key, value in sample_dict.items():
 print(f'{key:<10} : {value:>10}')

 
for key in sample_dict.keys():
 print(key, sample_dict[key])