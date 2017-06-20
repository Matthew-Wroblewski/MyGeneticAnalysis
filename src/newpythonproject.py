# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import gedcom
import image
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np



if __name__ == "__main__":
    # print("Hello World")

    myMap = Basemap(projection="mill", llcrnrlat = 0, llcrnrlon = -120, urcrnrlat = 75, urcrnrlon = 45, resolution='l')
    myMap.drawcoastlines()
    myMap.drawcountries(linewidth=1)
    myMap.drawstates(color='b')
    myMap.fillcontinents()

   # myMap.etopo()
    myMap.bluemarble()
    xs = []
    ys = []

    x = -79.0059
    y = 35.7127
    # NJ - 40.0583° N, 74.4057  --- Ukraine 48.3794° N, 31.1656° E ---

    locations = ((-74.4057, 40.0853),(31.1656,49.3794))
    print(locations[1][1])

    xpt, ypt = myMap(x,y)

    xs.append(x)
    ys.append(y)

    myMap.plot(xpt, ypt, 'r.', markersize=35)
    plt.title("Birth Locations of Matt's Ancestors")

    point = myMap.plot(x, y, 'ro', markersize=20)[0]


    def init():
        point.set_data([], [])
        return point,

    # animation function.  This is called sequentially
    def animate(i):
        lons, lats = locations[i]
        x, y = myMap(lons, lats)
        point.set_data(x, y)
        return point,


    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init,
                                   frames=2, interval=2000, blit=True)
    plt.show()


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
