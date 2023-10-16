class facebook:
    def __init__(self, name, surname, gender, date_of_birth, date_today, location):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = date_today - date_of_birth
        self.resindence = location
    def getmemberfullname(self):
        return self.name
    
member1 = facebook(name="Batuhan",surname="Yüksel", gender="Male",date_of_birth=1996, date_today=2023, location="Türkiye")

print(member1.getmemberfullname)
print(member1.getmemberfullname())