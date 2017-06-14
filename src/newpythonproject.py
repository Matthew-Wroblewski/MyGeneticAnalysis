# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import gedcom

if __name__ == "__main__":
    #print("Hello World")
    
    gedcomFile = gedcom.parse("Wainwright_Wroblewski.ged")
    for person in gedcomFile.individuals:
        firstname, lastname = person.name
        print ("{0} {1} is in the file".format(firstname, lastname))


