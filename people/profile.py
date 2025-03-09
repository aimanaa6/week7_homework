from people.person import Person

# person
aiman_profile = Person('Aiman','Ahmed',23,'British','Operations Specialist')
print(aiman_profile)

aiman_profile.get_first_name()
print(aiman_profile.get_first_name())

aiman_profile.set_first_name("PRABLEEN")
print(aiman_profile.get_first_name())

aiman_profile.get_age()
print(aiman_profile.get_age())

aiman_profile.set_age(18)
print(aiman_profile.get_age())