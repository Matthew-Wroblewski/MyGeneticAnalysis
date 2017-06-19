# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import gedcom
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # print("Hello World")


    gedcomFile = gedcom.parse("Wainwright_Wroblewski.ged")

    me = gedcomFile.pointers['@P1@']
    mom = gedcomFile.pointers['@P3@']
    # print(me['BIRT'].place)
    # print(family)
    # print(mom)
    names = []
    birthYear = []
    i = 0
    for person in gedcomFile.individuals:
        i = i + 1
        birthPlaces = person['BIRT']
        firstName, lastName = person.name
        personName = firstName + " " + lastName
        names.append(personName)
        birthYear.append(birthPlaces.date)
        birthYear.append(birthPlaces.place)
        print(names)
        print(birthPlaces)
        #  print(names)
        #  print(birthYear)
        # print(firstName, lastName)
        ## print(birthPlaces.place)
        #    except IndexError:  # catch the error
        #    i = i +1
        #    names.append(personName)
        #    birthYear.append("Index Error")
        #    birthYear.append("Unknown Place")
        #    pass
        # except AttributeError:
        #     i = i + 1
        #    names.append(personName)
        #   birthYear.append("Attribute error")
        #  birthYear.append("Unknown Dt?")
        # pass
    print(i)
    print(len(names))
    print(len(birthYear))
    print(names)
    print(birthYear)
    # firstname, lastname = person.name
    # print ("{0} {1} is in the file".format(firstname, lastname))

    # print(len(gedcomFile.individuals))
