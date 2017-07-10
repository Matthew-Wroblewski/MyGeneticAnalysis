# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import gedcom
import image
import time
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


if __name__ == "__main__":

    gedcomFile = gedcom.parse("Wainwright_Wroblewski.ged")

    names = []
    birthYear = []
    birthPlace = []
    i = 0
    k = 0
    lons, lats = (-500, -500)
    for person in gedcomFile.individuals:
        i = i + 1
        birthPlaces = person['BIRT']
        firstName, lastName = person.name
        personName = firstName + " " + lastName
        names.append(personName)
        birthYear.append(birthPlaces.date)
        birthPlace.append(birthPlaces.place)


    myMap = Basemap(llcrnrlat=0, llcrnrlon=-120, urcrnrlat=75, urcrnrlon=45, resolution='l')
    myMap.drawcoastlines()
    myMap.drawcountries(linewidth=1)
    myMap.drawstates(color='b')
    myMap.fillcontinents()

    # myMap.etopo()
    myMap.bluemarble()
    xs = []
    ys = []
    x = []
    y = []
    texts = ""

    xpt, ypt = myMap(x, y)

    xs.append(x)
    ys.append(y)

    myMap.plot(xpt, ypt, 'r.', markersize=35)
    plt.title("Birth Locations of Matt's Ancestors")

    point = myMap.plot(x, y, 'ro', markersize=20)[0]
    i = 0



    def init():
        point.set_data([], [])
        return point,

    # NJ[0] -74.4057, 40.0853  --- Ukraine[1] 31.1656, 49.3794 --- New York [2] -74.0059, 42.0, Trinidad [3] -61.2225, 10.6918 --- Bermuda [4] -64.7505, 32.3078 -- England[5] -1.4101,53.5598  ----
    #
    # animation function.  This is called sequentially
    def animate(i):
        global texts, k, birthPlace, lons, lats

        if k == len(birthPlace):
            return
        if  k > 0:
            texts.remove()

        if k <= len(birthPlace):
            if birthPlace[k] == "England":
                lons, lats = (-1.4101,53.5598)
                texts = plt.text(-52.00, 40.00, "Born in: " + birthPlace[k] + "\nBirth Date: " + birthYear[k] + "\nName: " + names[k] , color='red',
                                 bbox=dict(facecolor='white', edgecolor='red'), fontsize=14)

            elif birthPlace[k] == "New Jersey":
                lons, lats = (-74.4057, 40.0853)
                texts = plt.text(-52.00, 40.00,
                                 "Born in: " + birthPlace[k] + "\nBirth Date: " + birthYear[k] + "\nName: " + names[k], color='red',
                                 bbox=dict(facecolor='white', edgecolor='red'), fontsize=14)
            elif birthPlace[k] == "New York":
                lons, lats = (-74.4057, 42.0853)
                texts = plt.text(-52.00, 40.00,
                                 "Born in: " + birthPlace[k] + "\nBirth Date: " + birthYear[k] + "\nName: " + names[k], color='red',
                                 bbox=dict(facecolor='white', edgecolor='red'), fontsize=14)
            elif birthPlace[k] == "Ukraine":
                lons, lats = (31.1656, 49.3794)
                texts = plt.text(-52.00, 40.00,
                                 "Born in: " + birthPlace[k] + "\nBirth Date: " + birthYear[k] + "\nName: " + names[k], color='red',
                                 bbox=dict(facecolor='white', edgecolor='red'), fontsize=14)
            elif birthPlace[k] == "Trinidad":
                lons, lats = (-61.2225, 10.6918)
                texts = plt.text(-52.00, 40.00,
                                 "Born in: " + birthPlace[k] + "\nBirth Date: " + birthYear[k] + "\nName: " + names[k], color='red',
                                 bbox=dict(facecolor='white', edgecolor='red'), fontsize=14)
            elif birthPlace[k] == "Bermuda":
                lons, lats = (-64.7505, 32.3078)
                texts = plt.text(-52.00, 40.00,
                                 "Born in: " + birthPlace[k] + "\nBirth Date: " + birthYear[k] + "\nName: " + names[k], color='red',
                                 bbox = dict(facecolor='white', edgecolor='red'), fontsize = 14)
            else:
                lons, lats = (-500,-500)#locations[i]

        k = k + 1
        x, y = myMap(lons, lats)
        point.set_data(x, y)
        return point,

#    # call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(plt.gcf(), animate, init_func=init, frames=19, interval=1000, repeat = False, blit=False)
anim.save('mattsancestry.mp4', writer="ffmpeg")
plt.show()

