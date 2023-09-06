# C:\Users\User\OneDrive\Documents\maya\2022\scripts\quickHairGuideGen\quickHairGuide.py
import maya.cmds as cmds
import maya.mel as mel
from pprint import pprint

def quickHairUIWindow():
    if cmds.window('quickHairUIWindow',q=True,ex=True):
        cmds.deleteUI('quickHairUIWindow',window = True)
    cmds.window('quickHairUIWindow',t='QUICK HAIR GUIDE TOOL')
    
    cmds.columnLayout(adj=True)
    cmds.frameLayout('Select Single Edge')

    cmds.rowLayout(numberOfColumns = 1)
    cmds.text('edgeLoopText',l='')
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 3)
    cmds.text('\t\t     ')
    cmds.button('Select Edge Loop',w=200,c=selectEdgeLoop)
    cmds.setParent('..')

    cmds.frameLayout('Create Guide')
    
    cmds.rowLayout(numberOfColumns = 1)
    cmds.text('hairIDText',l='')
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 3)
    cmds.text('\t\t     ')
    cmds.button('Create',w=200,c=quickGuideGenerator)
    cmds.setParent('..')

    cmds.frameLayout('Match All Curve Direction')

    cmds.rowLayout(numberOfColumns = 1)
    cmds.text('\t\t\t*Ensure that all guides follow the same direction!*')
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 4)
    cmds.text('Show Selected Curve CV:    ')
    cmds.button('Display',c=cmds.ToggleCVs)
    cmds.text('    Reverse Selected Curve CV:    ')
    cmds.button('Reverse',c=reverseCurveDirection)
    cmds.setParent('..')

    cmds.frameLayout('Rename and Group the Hair')
    
    cmds.rowLayout(numberOfColumns = 1)
    cmds.text('NOTE: {num}: serial number i.e. 1, 2, 3, ..., n')
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 2)
    cmds.text('Name:\t')
    cmds.textField('nameTextField',text='hairStrand{num}_crv',w = 340)
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 2)
    cmds.text('Group:\t')
    cmds.textField('groupTextField',text='hairStrand_hairGrp',w = 340)
    cmds.setParent('..')

    cmds.rowLayout(numberOfColumns = 3)
    cmds.text('\t\t     ')
    cmds.button('Rename and Group',w=200,c=renameHairCrv)
    cmds.setParent('..')

    cmds.showWindow()
    cmds.window('quickHairUIWindow',e=True,wh=[410,380])

def selectEdgeLoop(*args):  
    sel = cmds.ls(sl=True)[0]

    #todo ensure that the selected data is an edge
    if 'e[' in sel.split('.')[-1] and 'vtxFace' not in sel.split('.')[-1]:
        cmds.pickWalk(d='down', type='edgering')
        
        edgeringSel = cmds.ls(sl=True,fl=True)  #list of all the hair base edge
        edgeLoopLst = []                        #list of all the edge loops        
        
        #todo get all the edge loops as raw text data
        for i in range(len(edgeringSel)):
            cmds.pickWalk(d='left',type = 'edgeLoop')
            edgeLoopLst.append(cmds.ls(sl=True,fl=True))
        
        #//pprint(edgeLoopLst)
        cmds.text('edgeLoopText',e=True,l = str(edgeLoopLst))

def quickGuideGenerator(*args):
    #todo convert the raw text data to list
    rawTextData = cmds.text('edgeLoopText',q=True,l=True)
    edgeLoopLst = eval(rawTextData)
    hairGrpLst = []
    #//pprint(edgeLoopLst)

    #todo creating each curve from individual edges
    for currentEdgeLoop in edgeLoopLst:
        duplicateCurveLst = []
        
        #! storing each edge created in a list
        for edge in currentEdgeLoop:
            hairCurve = cmds.duplicateCurve(edge,ch=True,rn=False,local=False)
            duplicateCurveLst.append(hairCurve[0])

        #todo attach the curve and delete the component edges curve
        hair = cmds.attachCurve(duplicateCurveLst,ch=False,rpo = 0,kmk = 1,m = 1,bb = 0.5,bki = 0,p = 0.1) 
        
        hairGrpLst.append(hair[0])
        cmds.CenterPivot(hair)
        cmds.delete(duplicateCurveLst)

    cmds.text('hairIDText',e=True,l=str(hairGrpLst))

def renameHairCrv(*args):
    rawTextData = cmds.text('hairIDText',q=True,l=True)
    hairGrpLst = eval(rawTextData)
    newNamePrompt = cmds.textField('nameTextField',q=True,text=True)
    newHairNameGrp = []
    
    for i in range(len(hairGrpLst)):
        num = i+1

        newHairNameGrp.append(newNamePrompt.format(num = num))
        cmds.rename(hairGrpLst[i],newHairNameGrp[i])

    groupName = cmds.textField('groupTextField',q=True,text=True)
    cmds.group(newHairNameGrp,n=groupName)

def reverseCurveDirection(*args):
    selCurve = cmds.ls(sl=True)
    for i in selCurve:
        cmds.reverseCurve(i,rpo=1)      

    
quickHairUIWindow()