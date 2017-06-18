# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import gedcom

if __name__ == "__main__":
    #print("Hello World")
    

    gedcomFile = gedcom.parse("Wainwright_Wroblewski.ged")

    me = gedcomFile.pointers['@P1@']
    family = gedcomFile.pointers['@F82@']
    mom = gedcomFile.pointers['@P3@']
   # print(me['BIRT'].place)
   # print(family)
    #print(mom)
    for person in gedcomFile.individuals:
        try:
            birthPlaces = person['BIRT']
            print (birthPlaces.date)
            print(birthPlaces.place)
        except IndexError:  # catch the error
            pass
        except AttributeError:
            pass


      #  for attr, value in stuff:
          #  print (attr, value)



    # firstname, lastname = person.name
    # print ("{0} {1} is in the file".format(firstname, lastname))

    # print(len(gedcomFile.individuals))




