#7.1
#years_list = [1997, 1998, 1999, 2000, 2001, 2002]

#7.2
#years3 = years_list[3]
#print(years3)

#7.3
#years_list = [1997, 1998, 1999, 2000, 2001, 2002]
#years_max = max(years_list)
#print(years_max)
#or
#print(years_list[-1])

#7.4
#things = ['mozarella', 'cinderella', 'salmonela']
#7.5
#things[1] = things[1].capitalize()  
#7.6
#things[0] = things[0].upper()
#7.7
#del things[2]
#print(things)

#7.8
#surprise = ['Groucho', 'Chico', 'Harpo']
#7.9
#surprise[2] = surprise[2].lower()
#surprise[2] = surprise[2][ : :-1]  
#surprise[2] = surprise[2].capitalize()
#print(surprise[2])
#7.10
#even =[number for number in range(10) if number %2 == 0]
#7.11
start1 = ['fee', 'fie', 'foe']
rhymes = [
    ('flop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call the judge'),
    ('fat', 'pet the cat'),
    ('fog', 'pet the dog'),
    ("fun", "say we're done")
]
start2 = 'someone better'
start1_caps = " ".join([word.capitalize() + '!' for word in start1])
for first, second in rhymes:
    print(f'{start1_caps} {first.capitalize()}!')
    print(f'{start2} {second}.')