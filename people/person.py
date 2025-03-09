class Person:
    def __init__(self,firstname,lastname,age,nationality,occupation):
        self.__firstname= firstname
        self.__lastname = lastname
        self.__age = age
        self.__nationality = nationality
        self.__occupation = occupation

    def get_first_name(self):
        return self.__firstname

    def get_age(self):
        return self.__age

    def set_first_name(self, first_name):
        if str(first_name).isupper():
            self.__firstname = first_name
        else:
            raise ValueError("First name must be alphabetical")

    def set_age(self,age):
        if int(age)>16:
            self.__age= age
        else:
            raise TypeError("Age must be over 16")

aiman_profile = Person('Aiman','Ahmed',23,'British','Operations Specialist')
print(aiman_profile)

aiman_profile.get_first_name()
print(aiman_profile.get_first_name())

aiman_profile.set_first_name("PRABLEEN")
print(aiman_profile.get_first_name())

aiman_profile.get_age()
print(aiman_profile.get_age())

aiman_profile.set_age(12)
print(aiman_profile.get_age())