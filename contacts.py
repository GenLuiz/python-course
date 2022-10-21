contacts = {"number": 4,
           "students":
               [
                   {"name": "Sarah", "email": "sarah@example.com"},
                   {"name": "Harry", "email": "harry@example.com"},
                   {"name": "Hermione", "email": "hermione@example.com"},
                   {"name": "Ron", "email": "ron@example.com"}
               ]
           }

for student in contacts['students']:
    print(student["email"])