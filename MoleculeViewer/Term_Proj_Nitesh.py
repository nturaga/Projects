# Nitesh Turaga

# AMINO ACID EXPLORER/ MOLECULE VIEWER

# andrew id : nturaga


# AMINO ACID EXPLORER
#   Features-- Structures of amino acids 
#           
#           -- Best part--Everything in 3D with animations and rotatable
#               views.
#           -- GUI buttons used to navigate the Amino acids
#INSTRCTIONS#
#   Use the dropdown box to select the different amino acids

import os

    
import tkMessageBox
import tkSimpleDialog

from visual import*

from Tkinter import*

# First stage is build amino acids in different

# Build the amino acids using visual python first
# and then integrate with Tkinter.

# Amino acid rules : All carbons are in Yellow

##   NH 2(green edge),COOH(light blue edge) will not be
#   explicitly shown but dipicted.

##   H atoms attached to the primary carbon are considered
#   trivial-yellow edge.


# Getting a larger display for the amino acid structures

aminoDisplay = display(title='Amino Acid',
     x=0, y=0, width=800, height=800,
     center=(0,0,0), background=(1,1,1))
                            
def glycine():
    visibility= canvas.data.vGly
    for drawn in canvas.data.drawnGlycine:
        drawn.visible = visibility
    
def glycineVisibility():
    pCarbon= sphere(pos=vector(0,0,0),radius= 1, color=color.yellow, opacity=1)
        # C-NH2 green edge
    NH2=cylinder(pos=vector(0.8,-0.4,0),
                 axis=(2,-2,0), radius=0.2 , color=color.green)   
    # C-COOH edge 
    COOH= cylinder(pos=vector(-0.8,-0.4,0),
                   axis=(-2,-2,0), radius=0.2 ,color=color.cyan)
    #H bonds to the C atom
    hAtom1= cylinder(pos= vector(0.5,0.8,0),
                     axis= (1.5,1.5,0), radius=0.1, color= color.red)
    hAtom2= cylinder(pos= vector(-0.5,0.8,0),
                     axis= (-1.5,1.5,0), radius=0.1, color= color.red)
    canvas.data.drawnGlycine = [COOH, NH2, hAtom1,hAtom2,pCarbon]
    for i in xrange(len(canvas.data.drawnGlycine)):
        canvas.data.drawnGlycine[i].visible=False

def alanine():
    visibility= canvas.data.vAla
    for drawn in canvas.data.drawnAlanine:
        drawn.visible = visibility
        
def alanineVisibility():
    #Central carbon
    pCarbon_1= sphere(pos=vector(0,-0.5,0),
                    radius= 0.6, color=color.yellow, opacity=1)
    # C-C bond between the pCarbon and rCarbon
    ccBond_1= cylinder(pos= vector(0,0,0),
                     axis= (0,1,0), radius=0.1, color= color.yellow)
    ### C-H3 group
    rCarbon_1= sphere(pos=vector(0,1.5,0),
                    radius=0.5, color= color.yellow, opacity=1)
    hAtom1_1= cylinder(pos= vector(0.5,1.5,0),
                     axis= (1,0,0), radius=0.1, color= color.red)
    hAtom2_1= cylinder(pos= vector(-0.5,1.5,0),
                     axis= (-1,0,0), radius=0.1, color= color.red)
    hAtom3_1= cylinder(pos= vector(0,1.5,0.5),
                     axis= (0,0,1), radius=0.1, color= color.red)
    # C-NH2 green edge
    NH2_1=cylinder(pos=vector(0.4,-0.8,0),
                 axis=(2,-1.5,0), radius=0.2 , color=color.green)   
    # C-COOH edge 
    COOH_1= cylinder(pos=vector(-0.4,-0.8,0),
                   axis=(-2,-1.5,0), radius=0.2 ,color=color.cyan)
    canvas.data.drawnAlanine=[pCarbon_1,NH2_1,COOH_1,
                              hAtom1_1,hAtom2_1,hAtom3_1,
                              rCarbon_1,ccBond_1]
    for i in xrange(len(canvas.data.drawnAlanine)):
        canvas.data.drawnAlanine[i].visible = False

#alanine()

# Helper function CH3 used to call in multiple amino acids
# Takes in position vector, axis vector and radius
#(px,py,pz,ax,ay,az,radius)
# Color is according to the legend followed by the program
def CH3(px,py,pz,rad):
    #primary carbon
    #rad is radius
    rad=float( rad)
    rCarbon= sphere(pos=vector(px,py,pz),
                    radius=rad, color= color.yellow, opacity=1)
    #hydrogen atoms to balance the valency
    hAtom1= cylinder(pos= vector(px+rad,py,pz),
                     axis= (rad,0,0), radius=rad/5, color= color.red)
    
    hAtom2= cylinder(pos= vector(px-rad,py,pz),
                     axis= (-rad,0,0), radius=rad/5, color= color.red)

    hAtom3= cylinder(pos= vector(px,py,pz+rad),
                     axis= (0,0,rad), radius=rad/5, color= color.red)
    canvas.data.drawnCH3=[hAtom1,hAtom2,hAtom3,rCarbon]
    return canvas.data.drawnCH3

# The C-C bond which is also used in a lot of amino acids is
# used as a helper function
def ccBond(px,py,pz,ax,ay,az,rad):
    rad=float (rad)
    canvas.data.bond=cylinder(pos= vector(px,py,pz),
                     axis= (ax,ay,az), radius=rad, color= color.yellow)
    return canvas.data.bond

def valineVisibility():
    # primary carbon
    pCarbonVal= sphere(pos=vector(0,-0.7,0),
                    radius= 0.4, color=color.yellow, opacity=1)
    #rCarbon1 
    rCarbonVal= sphere(pos=vector(0,0.5,0),
                    radius= 0.4, color=color.yellow, opacity=1)
    #C-C--Bond between C-C
    bond1=ccBond(0,-0.3,0,0,0.4,0,0.05)
    #Bond C-1CH3
    bond2=ccBond(-0.3,0.7,0,-0.5,0.5,0,0.05)
    #Bond C-2CH3
    bond3=ccBond(0.3,0.7,0,0.5,0.5,0,0.05)
    #rCarbon2
    CH3_1=CH3(-1,1.5,0,0.4)
    #rCarbon3
    CH3_2 = CH3(1,1.5,0,0.4)
        
    NH2Val=cylinder(pos=vector(0.3,-0.9,0),
                 axis=(1.5,-1.0,0), radius=0.1 , color=color.green)   
    # C-COOH blue edge 
    COOHVal= cylinder(pos=vector(-0.3,-0.9,0),
                   axis=(-1.5,-1,0), radius=0.1 ,color=color.cyan)

    canvas.data.drawnValine = [pCarbonVal,rCarbonVal,bond1,bond2
                               ,bond3,NH2Val,COOHVal]
    canvas.data.drawnValine+=CH3_1
    canvas.data.drawnValine+=CH3_2
    for drawn in canvas.data.drawnValine:
        drawn.visible= False

def valine():
    visibility= canvas.data.vVal
    for drawn in canvas.data.drawnValine:
        drawn.visible=visibility

# Helper Function for Serine and Threonine
# and any other amino acid which requires text
# to identify the functional groups.

def cBondResidue(px,py,pz,rad,residueName):
    # Carbon atom
    rad= float (rad)
    rCarbon_cbr= sphere(pos=vector(px,py,pz),
                    radius= rad, color=color.yellow, opacity=1)    
    # connected to text--Functional group
    bond_cbr= cylinder(pos = vector(px+ rad/2,py+rad/2,pz),
                   axis= (2*rad,2*rad,0), radius= rad/5, color=color.red)
    # name of the residue
    residue_cbr= text (text= residueName, align= 'left',
                   pos= vector( px+2.5*rad,py+ 2.7*rad,pz), depth=0.1,
                   color=color.blue, height= rad)
    canvas.data.cBondResidue= [rCarbon_cbr,bond_cbr,residue_cbr]
    return canvas.data.cBondResidue                    

def serineVisibility():
    # primary carbon
    pCarbon= sphere(pos=vector(0,-0.7,0),
                    radius= 0.4, color=color.yellow, opacity=0.5)
    # C-NH2 green edge
    NH2=cylinder(pos=vector(0.3,-0.9,0),
                 axis=(1.5,-1.0,0), radius=0.1 , color=color.green)   
    # C-COOH blue edge 
    COOH= cylinder(pos=vector(-0.3,-0.9,0),
                   axis=(-1.5,-1,0), radius=0.1 ,color=color.cyan)    
    # bond between primary carbon and residual carbon
    bond=ccBond(0,-0.3,0,0,0.9,0,0.05)
    
    # OH residue and rCarbon atom 
    resList=cBondResidue(0,1,0,0.4,'OH')
    canvas.data.drawnSerine= [pCarbon,NH2,COOH,bond]
    canvas.data.drawnSerine+=resList
    for drawn in canvas.data.drawnSerine:
        drawn.visible=False
    
def serine():
    visibility= canvas.data.vSer
    for drawn in canvas.data.drawnSerine:
        drawn.visible=visibility

def threonineVisibility():

    # primary carbon
    pCarbon= sphere(pos=vector(0,-0.7,0),
                    radius= 0.4, color=color.yellow, opacity=0.5)
    
    # C-NH2 green edge
    NH2=cylinder(pos=vector(0.3,-0.9,0),
                 axis=(1.5,-1.0,0), radius=0.1 , color=color.green)   
    # C-COOH blue edge 
    COOH= cylinder(pos=vector(-0.3,-0.9,0),
                   axis=(-1.5,-1,0), radius=0.1 ,color=color.cyan)    
    # bond between primary carbon and residual carbon
    bond1=ccBond(0,-0.3,0,0,0.9,0,0.05)
    # OH residue and rCarbon atom
    resList=cBondResidue(0,1,0,0.4,'OH')
    # CH3 bonded to the rCarbon
    CH3_1=CH3(-1.5,2,0,0.4)
    # Bond between CH3 and rCarbon
    bond2=ccBond(-0.3,1.1,0,-1.2,1,0,0.05)
    canvas.data.drawnThreonine=[pCarbon,NH2,COOH,bond1,bond2]
    canvas.data.drawnThreonine+=resList
    canvas.data.drawnThreonine+=CH3_1
    for drawn in canvas.data.drawnThreonine:
        drawn.visible = False

def threonine():
    visibility= canvas.data.vThr
    for drawn in canvas.data.drawnThreonine:
        drawn.visible=visibility

def cysteineVisibility():

    # primary carbon
    pCarbon= sphere(pos=vector(0,-0.7,0),
                    radius= 0.4, color=color.yellow, opacity=0.5)
    
    # C-NH2 green edge
    NH2=cylinder(pos=vector(0.3,-0.9,0),
                 axis=(1.5,-1.0,0), radius=0.1 , color=color.green)   
    # C-COOH blue edge 
    COOH= cylinder(pos=vector(-0.3,-0.9,0),
                   axis=(-1.5,-1,0), radius=0.1 ,color=color.cyan)    
    # bond between primary carbon and residual carbon
    bond1=ccBond(0,-0.3,0,0,0.9,0,0.05)
    
    # OH residue and rCarbon atom 
    resList=cBondResidue(0,1,0,0.4,'SH')
    canvas.data.drawnCysteine= [pCarbon,NH2,COOH,bond1]
    canvas.data.drawnCysteine+=resList
    for drawn in canvas.data.drawnCysteine:
        drawn.visible= False

def cysteine():
    visibility= canvas.data.vCys
    for drawn in canvas.data.drawnCysteine:
        drawn.visible=visibility

# holds NH2 and COOH
def genericForm(px,py,pz,rad):
    rad= float (rad)
    margin=rad/2
    # primary carbon
    pCarbon= sphere(pos=vector(px,py,pz),
                    radius= rad, color=color.yellow, opacity=0.5)
    
    # C-NH2 green edge
    NH2=cylinder(pos=vector(px+(rad-rad/4),py-rad/2,pz),
                 axis=(rad*3,-rad*2,0), radius=rad/4 , color=color.green)   
    # C-COOH blue edge 
    COOH= cylinder(pos=vector(px-(rad-rad/4),py-rad/2,pz),
                   axis=(-rad*3,-rad*2,0), radius=rad/4 ,color=color.cyan)  
    # bond in between residual carbons
    bond1=ccBond(px,py+(rad-rad/4),pz,pz,-(py)/2,pz,rad/4)
    # rCarbon atom
    rCarbon1= sphere(pos=vector(px,py+(3.5*rad),pz),
                    radius= rad ,color=color.yellow, opacity=0.5)
    # 
    bond2=ccBond(px+(rad-rad/4)-margin/2,(py+(4*rad)+rad/4)-margin/2,pz,
           rad*2,rad*2,pz,rad/4)

    rCarbon2=sphere(pos= vector(px+(rad*3),
             (py+(3.5*rad)+(rad*3)),pz),radius= rad,
                       color=color.yellow,opacity=0.5)
    canvas.data.drawnGenericForm=[pCarbon,NH2,COOH,bond1,bond2,rCarbon1,
                                  rCarbon2]
    return canvas.data.drawnGenericForm


def leucineVisibility():
    # Calling th base structure from the generic form
    # of the amino acids.
    basic_amino=genericForm(-0.5,-0.8,0,0.2)
    # Drawing the rest of Leucine
    bond1_leu=ccBond(0.1,0.65,0,0,0.5,0,0.05)
    # second C-cbond in leucine
    bond2_leu=ccBond(0.2,0.4,0,0.4,-0.4,0,0.05)
    # CH3 groups at the end of the C-C bonds
    CH3_1=CH3(0.1,1,0,0.2)
    CH3_2=CH3(0.5,0.1,0,0.2)
    canvas.data.drawnLeucine=[bond1_leu,bond2_leu]
    canvas.data.drawnLeucine+=CH3_1
    canvas.data.drawnLeucine+=CH3_2
    canvas.data.drawnLeucine+=basic_amino
    for drawn in canvas.data.drawnLeucine:
        drawn.visible=False

def leucine():
    visibility= canvas.data.vLeu
    for drawn in canvas.data.drawnLeucine:
        drawn.visible=visibility

def isoLeucineVisibility():
    # Calling the base structure from the generic form
    # of the amino acids.
    basic_amino=genericForm(0,-0.8,0,0.2)
    # Drawing the rest of isoLeucine
    bond1=ccBond(0.6,0.65,0,0,0.5,0,0.05)
    # second C-cbond in isoleucine
    bond2=ccBond(-0.5,0.4,0,0.4,-0.4,0,0.05)
    # CH3 groups at the end of the C-C bonds
    CH3_1=CH3(0.6,1,0,0.2)
    CH3_2=CH3(-0.4,0.4,0,0.2)
    canvas.data.drawnIsoLeu= [bond1,bond2]
    canvas.data.drawnIsoLeu+=basic_amino
    canvas.data.drawnIsoLeu+=CH3_1
    canvas.data.drawnIsoLeu+=CH3_2
    for drawn in canvas.data.drawnIsoLeu:
        drawn.visible =False

def isoLeucine():
    visibility= canvas.data.vIle
    for drawn in canvas.data.drawnIsoLeu:
        drawn.visible=visibility


def asparticAcidVisibility():
    # Calling th base structure from the generic form
    # of the amino acids.
    basic_amino=genericForm(-0.5,-0.8,0,0.2)
    # Drawing the rest of aspartic Acid(O)
    resList=cBondResidue(0.1,0.5,0,0.2,'O')
    # second C-cbond in aspartic acid(OH)
    
    bond2=cylinder(pos= vector(0.2,0.4,0),
                     axis= (0.4,-0.4,0),
             radius=0.04, color= color.red)
    name=text (text='OH', align= 'left',
                   pos= vector(0.65,-0.15,0), depth=0.1,
                   color=color.blue, height= 0.2)
    canvas.data.drawnAsp=[bond2,name]
    canvas.data.drawnAsp += resList
    canvas.data.drawnAsp+=basic_amino
    for drawn in canvas.data.drawnAsp:
        drawn.visible= False

def asparticAcid():
    visibility= canvas.data.vAsp
    for drawn in canvas.data.drawnAsp:
        drawn.visible=visibility

def glutamicAcidVisibility():
    # Calling th base structure from the generic form
    # of the amino acids.
    basic_amino=genericForm(0,-0.8,0,0.2)
    # Drawing the rest of glutamic acid
    bond1=ccBond(0.6,0.65,0,0,0.5,0,0.05)
    #OH residue with carbon atom
    resList=cBondResidue(0.6,1.1,0,0.2,'OH')
    # second C-cbond in glutamic acid(O)
    bond2=cylinder(pos= vector(0.45,1.1,0),
                     axis= (-0.4,0.4,0),
             radius=0.04, color= color.red)
    name=text (text='O', align= 'left',
                   pos= vector(-0.1,1.5,0), depth=0.1,
                   color=color.blue, height= 0.2)
    canvas.data.drawnGlu=[bond1,bond2,name]
    canvas.data.drawnGlu+=resList
    canvas.data.drawnGlu+=basic_amino
    for drawn in canvas.data.drawnGlu:
        drawn.visible = False

def glutamicAcid():
    visibility= canvas.data.vGlu
    for drawn in canvas.data.drawnGlu:
        drawn.visible=visibility


def aspargineVisibility():
    # Calling th base structure from the generic form
    # of the amino acids.
    basic_amino=genericForm(-0.5,-0.8,0,0.2)
    # Drawing the rest of aspargine(O)
    resList=cBondResidue(0.1,0.5,0,0.2,'O')
    # second C-cbond in aspargine(NH2)
    
    bond2=cylinder(pos= vector(0.2,0.4,0),
                     axis= (0.4,-0.4,0),
             radius=0.04, color= color.red)
    name=text (text='NH2', align= 'left',
                   pos= vector(0.65,-0.15,0), depth=0.1,
                   color=color.blue, height= 0.2)
    canvas.data.drawnAsn=[bond2,name]
    canvas.data.drawnAsn+=resList
    canvas.data.drawnAsn+=basic_amino
    for drawn in canvas.data.drawnAsn:
        drawn.visible= False
        
def aspargine():
    visibility= canvas.data.vAsn
    for drawn in canvas.data.drawnAsn:
        drawn.visible=visibility


def glutamineVisibility():
    # Calling th base structure from the generic form
    # of the amino acids.
    basic_amino=genericForm(0,-0.8,0,0.2)
    # Drawing the rest of glutamine
    bond1=ccBond(0.6,0.65,0,0,0.5,0,0.05)
    #OH residue with carbon atom
    resList=cBondResidue(0.6,1.1,0,0.2,'NH2')
    # second C-cbond in glutamine(NH2)
    bond2=cylinder(pos= vector(0.45,1.1,0),
                     axis= (-0.4,0.4,0),
             radius=0.04, color= color.red)
    name=text (text='O', align= 'left',
                   pos= vector(-0.1,1.5,0), depth=0.1,
                   color=color.blue, height= 0.2)
    canvas.data.drawnGln= [bond1,bond2,name]
    canvas.data.drawnGln+=resList
    canvas.data.drawnGln+=basic_amino
    for drawn in canvas.data.drawnGln:
        drawn.visible = False
    
def glutamine():
    visibility= canvas.data.vGln
    for drawn in canvas.data.drawnGln:
        drawn.visible=visibility



def polygon(px,py,pz,rad,sides=6):
    # making the ring
    radius= float(rad)
    distance=rad*3
    carbon1= sphere( pos=vector(px,py,pz), radius= rad,
                     color= color.yellow, opacity=1)
    bond1=ccBond(px,py,pz,px,distance,pz,rad/4)
    carbon2= sphere( pos =vector(px,py+distance,pz),radius= rad,
                     color= color.red, opacity=1)
    bond2=ccBond(px,py+distance,pz,px+distance,py+distance,pz,rad/4)
    carbon3=sphere( pos = vector (px+distance, py+2*distance,pz),radius= rad,
                    color=color.yellow, opacity=1)
    bond3=ccBond(px+distance,py+2*distance,pz,px+distance,py-distance,pz,rad/4)
    carbon4= sphere(pos = vector(px+2*distance, py+distance,pz),radius= rad,
                    color=color.red, opacity=1)
    bond4=ccBond(px+2*distance, py+distance,pz,px,py-distance,pz,rad/4)
    carbon5=sphere(pos =vector( px+2*distance,py,pz),radius= rad,
                    color=color.yellow, opacity=1)
    if sides==6:
        carbon6= sphere(pos=vector(px+distance,py-distance,pz),radius= rad,
                    color=color.red, opacity=1)
        bond5=ccBond(px+2*distance,py,pz,px-distance,py-distance,pz,rad/4)
        
        bond6=ccBond(px+distance,py-distance,pz,px-distance,py+distance,pz,rad/4)
        canvas.data.drawnPolygon=[carbon1,bond1,carbon2,bond2,carbon3,
                              bond3,carbon4,bond4,carbon5,bond5,carbon6,
                              bond6]
    
    else:
        bond7=ccBond(px+2*distance,py,pz,px-2*distance,py,pz,rad/4)
        canvas.data.drawnPolygon=[carbon1,bond1,carbon2,bond2,carbon3,
                              bond3,carbon4,bond4,carbon5,bond7]
    return canvas.data.drawnPolygon
    
def phenylAlanineVisibility():
    basic_amino= genericForm(-.6,-1.3,0,0.2)
    basicPoly = polygon(0,0,0,0.2,6)
    canvas.data.drawnPhe=[]
    canvas.data.drawnPhe+= basic_amino
    canvas.data.drawnPhe+= basicPoly
    for drawn in canvas.data.drawnPhe:
        drawn.visible = False

def phenylAlanine():
    visibility= canvas.data.vPhe
    for drawn in canvas.data.drawnPhe:
        drawn.visible= visibility

def histidineVisibility():
    basic_amino = genericForm(-0.6,-1.3,0,0.2)
    basicPoly= polygon(0,0,0,0.2,5)
    canvas.data.drawnHis=[]
    canvas.data.drawnHis+= basic_amino
    canvas.data.drawnHis+= basicPoly
    for drawn in canvas.data.drawnHis:
        drawn.visible = False

def histidine():
    visibility= canvas.data.vHis
    for drawn in canvas.data.drawnHis:
        drawn.visible= visibility

###################################################################
    
def mousePressed(event):
    xLeft=20
    xRight=320
    yOffset=80
    boxHeight=30
    boxDiff=60
    #print canvas.data.popupList1
    if (event.x>xLeft and event.x<xRight\
        and event.y>yOffset and event.y<(yOffset+boxHeight)):
      
        if canvas.data.popupList2==False and canvas.data.popupList3==False:
            if canvas.data.popupList1  == False:
                canvas.data.popupList1  = True 
            else:
                canvas.data.popupList1=False
    # drop down for polar
    elif ((event.x>xLeft and event.x<xRight and event.y>(yOffset+boxDiff)
        and event.y<(yOffset+boxDiff+boxHeight))
        and canvas.data.popupList1 == False):
       
        if canvas.data.popupList1==False and canvas.data.popupList3==False:
            if canvas.data.popupList2  ==False :
                canvas.data.popupList2  = True
            else:
                canvas.data.popupList2= False
    # drop down for electrically charged
    elif ((event.x>xLeft and event.x<xRight and\
            event.y>(yOffset+(2*boxDiff))\
            and event.y<(yOffset+(2*boxDiff)+boxHeight))
            and canvas.data.popupList1==False and
            canvas.data.popupList2 == False):
       
        if canvas.data.popupList1==False and canvas.data.popupList2==False:       
            if canvas.data.popupList3  == False:
                canvas.data.popupList3  = True
            else:
                canvas.data.popupList3=False
    elif canvas.data.popupList1 == True:
        pressNonPolar(event)
    elif canvas.data.popupList2 == True:
        pressPolar(event)
    elif canvas.data.popupList3 == True:
        pressElectric(event)
    else:
        button1Pressed(event)  
    redrawAll()
 


import math
# Mouse Pressed for non polar amino acids
def pressNonPolar(event):
    yOffset=80
    boxHeight=30
    nonPolarDict= {1:glycine,2:alanine,3:valine,4:leucine,5:isoLeucine,
                   6:phenylAlanine}
                   
    dictKey = -1  
                   #()}#(6,methionine),
                  #(8,tryptophan),(9,proline)}              
    if (event.x>20 and event.x<320 and event.y>30+yOffset and event.y<290):
        dictKey= int(math.floor(float(event.y-yOffset)/boxHeight))
        if dictKey == 1:
            canvas.data.vGly = not canvas.data.vGly
        elif dictKey == 2:
            canvas.data.vAla = not canvas.data.vAla
        elif dictKey == 3:
            canvas.data.vVal = not canvas.data.vVal
        elif dictKey == 4:
            canvas.data.vLeu = not canvas.data.vLeu
        elif dictKey ==5:
            canvas.data.vIle= not canvas.data.vIle
        elif dictKey == 6:
            canvas.data.vPhe= not canvas.data.vPhe
        nonPolarDict[dictKey]()
    
def pressPolar(event):
    yOffset=140
    boxHeight = 30
    polarDict = {1:serine,2:threonine,3:cysteine,4:aspargine,5:glutamine}
                # 4:tyrosine,
    dictKey= -1
    if (event.x>20 and event.x<320 and event.y>30+yOffset and event.y<320):
        dictKey= int(math.floor(float(event.y-yOffset)/boxHeight))
        
        if dictKey ==1:
            canvas.data.vSer = not canvas.data.vSer
        elif dictKey==2:
            canvas.data.vThr = not canvas.data.vThr
        elif dictKey==3:
            canvas.data.vCys = not canvas.data.vCys
        elif dictKey ==4:
            canvas.data.vAsn = not canvas.data.vAsn
        elif dictKey ==5:
            canvas.data.vGln = not canvas.data.vGln
        polarDict[dictKey]()
    
           
def pressElectric(event):
    yOffset=200
    boxHeight = 30
    dictKey=-1
    electricDict = {1:asparticAcid , 2:glutamicAcid,3:histidine}#,# 3:lysine,
                 #4:arginine,5:histidine}
    if (event.x>20 and event.x<320 and event.y>30+yOffset and event.y<320):
        dictKey= int(math.floor(float(event.y-yOffset)/boxHeight))
        
        if dictKey == 1:
            canvas.data.vAsp = not canvas.data.vAsp
        elif dictKey ==2:
            canvas.data.vGlu = not canvas.data.vGlu
        elif dictKey ==3:
            canvas.data.vHis = not canvas.data.vHis
        electricDict[dictKey]()
    
           
                
                
    
##########################################################################
def nonPolarList(left,top,w,h):
    npList=["Glycine - Gly","Alanine - Ala","Valine - Val",
            "Leucine - Leu","Isoleucine - Ile",
            "Phenylalanine - Phe"]
            #"Tryptophan - Trp","Proline - Pro",,"Methionine - Met"]
     # Serine
    margin=7
    for i in xrange(len(npList)):
        newTop=top + h*i
        canvas.create_rectangle(left,newTop,left+w,newTop+h,
                                fill='grey',width=2)
        canvas.create_text(left+(left/2), newTop+margin,
                           text= npList[i],font= 'Times 14',
                           anchor=NW)

# Polar amino acids list for GUI
def polarList(left,top,w,h):
    pList=['Serine - Ser','Threonine - Thr','Cysteine - Cys'
           ,'Aspargine - Asn','Glutamine - Gln']
     #'Tyrosine - Tyr',
    margin=7
    for i in xrange(len(pList)):
        newTop=top + h*i
        canvas.create_rectangle(left,newTop,left+w,newTop+h,
                                fill='grey',width=2)
        canvas.create_text(left+(left/2), newTop+margin,
                           text= pList[i],font= 'Times 14',
                           anchor=NW)

# Electrically charged amino acids
def electricAminoList(left,top,w,h):
    # Serine
    margin=7
    elecList=["Aspartic Acid - Asp","Glutamic Acid - Glu","Histidine - His"]
              #,"Arginine - Arg","Lysine-Lys"]
    for i in xrange(len(elecList)):
        newTop=top + h*i
        canvas.create_rectangle(left,newTop,left+w,newTop+h,
                                fill='grey',width=2)
        canvas.create_text(left+(left/2), newTop+margin,
                           text= elecList[i],font= 'Times 14',
                           anchor=NW)

########################################################################    

    
def keyPressed(event):
    redrawAll()

def timerFired():
    redrawAll()
    delay = 250 # milliseconds
    canvas.after(delay, timerFired) # pause, then call timerFired again


class MyDialog(tkSimpleDialog.Dialog):
    def body(self, master):
        canvas.data.modalResult = None
        Label(master, text="Enter file name").grid(row=0)
        self.e1 = Entry(master)
        self.e1.grid(row=0, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        global canvas
        canvas.data.modalResult = (first)

def showDialog():
    global canvas
    MyDialog(canvas)
    return canvas.data.modalResult

def button1Pressed(event):
    # defining button pressed for pdb file view
    if (event.x>canvas.data.width*1/4 and event.x<canvas.data.width*3/4
        and event.y>canvas.data.height*3/4
        and event.y<(canvas.data.height*3/4)+30 ):
        filename = "" + str(showDialog())
        # And update and redraw our canvas
        canvas.data.filename = filename
        try:
            if filename== "": print "enter wrong filename"
            filePath= getDesktopPath(canvas.data.filename)
            #print "1"
            fileExists(filePath)
            #print "2"
            makeMolecule(readTextFile(filePath))
            #print "3"    
        except AttributeError:
            print "enter a filename"
    redrawAll()

##########################################################

import os

def getDesktopPath(filename = ""):
    # next line is odd, but works in Windows/Mac/Linux
    homepath = os.getenv('USERPROFILE') or os.getenv('HOME')
    return homepath + os.sep + "Desktop" + os.sep + filename

def fileExists(filename):
    return os.path.exists(filename)

def readTextFile(filename):
    if (fileExists(filename) == False):
        print "File does not exist:", filename
        return None
    fileHandler = open(filename, "rt")
    text = fileHandler.read()
    fileHandler.close()
    return text

def eliminateSpace(text):
    if (text == None):
        return None
    edited=""
    for i in xrange(0,len(text)):
        #when chr is same as last chr and is space
        if text[i]==text[i-1] and str.isspace(text[i])==True:
            continue
        edited+=text[i]
    return edited

def extractValues(line):
    line=eliminateSpace(line)
    #print "line:",line
    lineNew=line.split("\n")
    coordsList=[]
    hetAtmCoords=[]
    aminoList=[]
    for line in lineNew:
        line= line.split(" ")
        if line[0] == 'ATOM' :
            (px,py,pz)=(float(line[6])/2,float(line[7])/2,
                                 float(line[8])/2)
            coordsList+=[(px,py,pz)]
        
        elif line[0] == 'HETATM':
            (px,py,pz)= (float(line[6]),float(line[7]),
                         float(line[8]))
            hetAtmCoords.append((px,py,pz))
            
    return (coordsList,hetAtmCoords)

def makeAtom(px,py,pz):
    #print "makeAtom"
    colorList=[(1,0,0),(0,1,0),
               (1,0.5,0),(0,0,1),(0,1,1),(1,0,1)]
    index= random.randint(0,5)
    atomColor= colorList[index]
    rad=0.5
    atom = sphere( pos = vector( px,py,pz), radius= rad, color= atomColor
            ,opacity=1)
##    atomName= text (text= atomName, align= 'center',
##                   pos= vector( px,py,pz), depth=0.1,
##                   color= (1,1,0), height= rad)


##def connectAtoms(coordsList):
##    for i in xrange(len(coordsList)):
        
def makeHetAtom(px,py,pz):
    #print "makeAtom"
    rad=0.5
    atom = sphere( pos = vector( px,py,pz), radius= rad, color= (0,0,0)
            ,opacity=1)
    
def makeMolecule(line):
    coordsList,hetAtmCoords=extractValues(line)
    #print "21",coordsList
    emptyList=[]
    for coords in coordsList:
        makeAtom(coords[0],coords[1],coords[2]) 
    for coords in hetAtmCoords:
        makeHetAtom(coords[0],coords[1],coords[2])

        
  
##########################################################    
def redrawAll():
    canvas.delete(ALL)
    boxHeight=30
    # GUI Header--TITLE    
    canvas.create_text(200,30,text='viewMOL', fill='black',
                        font='Times 30 italic bold')
    # non polar amino acid
    canvas.create_rectangle(20, 80 ,320,110, fill= 'grey', width= 2)
    canvas.create_text(30,87,text="Non polar amino acids", fill='black',
                       font='Times 14', anchor=NW)
    # polar amino acid box
    canvas.create_rectangle(20, 140 ,320,170, fill= 'grey', width= 2)
    canvas.create_text(30,147,text="Polar amino acids", fill='black',
                       font='Times 14', anchor=NW)
    # Electrically charged amino acids    
    canvas.create_rectangle(20, 200 ,320,230, fill= 'grey', width= 2)
    canvas.create_text(30,207,text="Electrically charged amino acids",
                       fill='black',font='Times 14', anchor=NW)
    
    # file name input box
    width=canvas.data.width
    height=canvas.data.height
    margin=5
    canvas.create_rectangle(width*1/4,height*3/4,width*3/4,
                            (height*3/4)+boxHeight
                            , fill= 'grey',width=2)
    canvas.create_text((width*1/4)+ margin ,height*3/4+margin,
                       text=" Load PDB file to View"
                       ,fill= 'black',font= 'Times 14', anchor= NW)
    # MAKE pop-up List
    if canvas.data.popupList1 == True:
        nonPolarList(20,110,300,30)
    if canvas.data.popupList2  == True:
        polarList(20,170,300,30)   
    if canvas.data.popupList3  == True:
        electricAminoList(20,230,300,30)   
#########################################################
#Stuff in init()
        ################

def aminoVisibility():
    canvas.data.vGly= False
    canvas.data.vAla= False
    canvas.data.vVal= False
    canvas.data.vLeu= False
    canvas.data.vIle= False
    canvas.data.vMet= False
    canvas.data.vPhe= False
    canvas.data.vTrp= False
    canvas.data.vPro= False
    canvas.data.vSer= False
    canvas.data.vThr= False
    canvas.data.vCys= False
    canvas.data.vTyr= False
    canvas.data.vAsn= False
    canvas.data.vGln= False
    canvas.data.vAsp= False
    canvas.data.vGlu= False
    canvas.data.vLys= False
    canvas.data.vHis= False
    canvas.data.vArg= False
   

def aminoAcid():
    glycineVisibility()
    alanineVisibility()
    valineVisibility()
    serineVisibility()
    threonineVisibility()
    cysteineVisibility()
    leucineVisibility()
    isoLeucineVisibility()
    aspargineVisibility()
    glutamineVisibility()
    asparticAcidVisibility()
    glutamicAcidVisibility()
    phenylAlanineVisibility()
    histidineVisibility()
    

#####################################################
def init():
    # Pop up list initialization
    canvas.data.splashScreen=False
    canvas.data.popupList1 = False
    canvas.data.popupList2 = False
    canvas.data.popupList3 = False    
    # window opening for amino acids
    aminoVisibility()
    aminoAcid()
    redrawAll()
    
def run():
    # create the root and the canvas
    global canvas
    
    # To place the window at the right side of the
    # screen for better GUI.
    def place_window(w=200, h=200):
    # get screen width and height
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
    # calculate position x, y
        x = (ws/2) + (w/2) 
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root = Tk()
    place_window(400,600)
    canvas = Canvas(root, width=400, height=600)
    
    # Set up canvas data and call init
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width= 400
    canvas.data.height= 600
    init()
    aminoVisibility()
    canvas.data.message = "none"
    canvas.pack()
    # set up events
   
    root.bind("<Button-1>", mousePressed)
    #root.bind("<Key>", keyPressed)
    timerFired()
    # and launch the app
    root.mainloop()  
run()
