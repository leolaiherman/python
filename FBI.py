import time
Jon ={
    "Name" :"John Smith",
    'Age'  : 25,
    'Crime':'First Degree Murder'
}
Bil ={
    "Name" :"Billy Brock",
    'Age'  : 30,
    'Crime':'Stealing'
}
Ethan ={
    "Name" :'Ethan Travis',
    'Age'  : 20,
    'Crime':'Drug Dealing'
}
Ray ={
    "Name" :"Raymond Chris",
    'Age'  : 40,
    'Crime':'Second Degree Murder'
}
most_wanted =[Jon, Bil, Ethan, Ray]
total = 0

print('===================')
print('FBI MOST WANTED')
print('===================')

for x in range(3):
    for a in range(0,4,1):
        print('loading data' + a*'.')
        time.sleep (0.1)

#print('')
print(f'\n{len(most_wanted)} IDENTIFIED\n')
time.sleep(0.5)

for x in most_wanted:
    for key,val in x.items():
        print(f'{key}:{val}')
    print("")

for x in most_wanted:
    total += x['Age']
print(f'jumlah umur mereka adalah {total}')
