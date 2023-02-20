people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'},
          3: {'Name': ['Rafa','Rafa2'], 'Age': '15', 'Sex': 'Female'}}

size =  len(people.items())

if 'Rafa' in people[3]['Name'][0]:
    print("bien")
else:
    print("mal")

    
