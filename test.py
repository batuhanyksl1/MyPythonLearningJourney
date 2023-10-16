#trial of writing a class and a method to return it.
class adressbook:
    def __init__(self,name,surname,phone_number,contact_id):
        self.name=name
        self.surname=surname
        self.phone_number=phone_number
        self.contact_id= 0
    def get_contacts(self,name,surname):
        return self.name,self.surname


#nasıl getireceğimi bilmiyorum.
user1=adressbook("Baturalp","Yüksel",5345241548,2)


"silmeme izin vermiyor ama başka ekletme yaptırıyor."