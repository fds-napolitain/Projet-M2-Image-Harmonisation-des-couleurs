import cv2
import random
import math
from imgTools import *


#trouve la meilleurs harmonisation et effectue la modification de l'image
def findBestHarmonieCompl(histoHSV, imgHSV, verbose = True):
    #le mode correspond a un p
    #mode = couleur, occurance 
    mode = (0,0)
    ite = 0
    for key, value in histoHSV.items():
        ite+=1
        color = key #teinte de la couleur
      #  print(color)
        #calcul des couleurs triadique
        colort1 = (color+60)%180
        colort2 = (color+120)%180
        #on prend en compte aussi les voisines
        #somme =sommeVoisine(histoHSV,color) + sommeVoisine(histoHSV, colorCompl)
        somme = sommeVoisinHSV(histoHSV, color)+ sommeVoisinHSV(histoHSV, colort1)+sommeVoisinHSV(histoHSV, colort2)

        if somme > mode[1]:
            mode = (color, somme)
        if verbose:
            verbosePourcent(ite, len(histoHSV))

    modet1 =  (mode[0]+60)%180
    modet2 =  (mode[0]+120)%180
    print("mode = ",mode[0])
    print("t1 = ", modet1)
    print("t2 = ", modet2)
    tupleTeinte = [int(modet1),int(mode[0]),int(modet2)]
    #on harmonise les couleur de l'image
    for i in range(0,imgHSV.shape[0]):
        for j in range(0,imgHSV.shape[1]):
            colorcurr = (imgHSV[i,j])
            imgHSV.itemset((i,j,0),   getColor_Degrader(tupleTeinte,colorcurr ))
    couleurs = vignette([mode[0],modet1,modet2])
    cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_Triadique_converge_Vignette.jpg", couleurs)

            



#### ATTENTION: ####
# OPENCV utilise le format BGR (bleu, vert, rouge)
# pensez a rectifier si nécessaire pour les calculs
####

filename = "tulipes"
img = cv2.imread ("../Images/Inputs/"+filename+".jpg")
#ImgIndex = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


histoHSV = getHistoHSV(img)


hsvImage = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#print("couleur   : ",hsvImage[0,0])
#print("couleur   : ",hsvImage[0,0])

findBestHarmonieCompl(histoHSV, hsvImage)
#findBestHarmonieTriad(histo, img)

img = cv2.cvtColor(hsvImage, cv2.COLOR_HSV2BGR)
#cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_TriadiqueHSV.jpg", hsvImage)
cv2.imwrite("../Images/Outputs/"+filename+"/"+filename+"_Triadique_converge.jpg", img)








