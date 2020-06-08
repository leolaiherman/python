def belts_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There area {num} {belt} belts')


#def ninja_intro(dictionary):
#    for key, val in dictionary.items():
#        print(f"I am {key} and I am {val} belt")

ninja_belts = {}

while True:
    ninja_name = input('input your ninja name:')
    ninja_belt = input('input your ninja belt:')
    ninja_belts [ninja_name] = ninja_belt

    another = input('any other? (y/n):')
    if another == 'y':
        continue
    else:
        break

#ninja_intro(ninja_belts)
belts_count(ninja_belts)