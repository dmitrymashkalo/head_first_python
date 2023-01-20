import pprint

people = {}
people['Ford'] = {
                'Name': 'Ford Perfect',
                'Gender': 'Male',
                'Occupation': 'Researcher',
                'Home Planet': 'Betelgeuse Seven'
                }
people['Arthur'] = {
                'Name': 'Arthur Dent',
                'Gender': 'Male',
                'Occupation': 'Sandwich-Maker',
                'Home Planet': 'Earth'
                }
people['Trillian'] = {
                'Name': 'Tricia McMillan',
                'Gender': 'Female',
                'Occupation': 'Mathematician',
                'Home Planet': 'Earth'
                }
people['Robot'] = {
                'Name': 'Marvin',
                'Gender': 'Unknow',
                'Occupation': 'Paranoid Android',
                'Home Planet': 'Unknow'
                }

pprint.pprint(people)