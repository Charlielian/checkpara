#!/usr/bin/python3
#$ {TIME} - 当前系统时间。
# @Author  : Charlie
# @Email   : li-3221039@163.com

import os,csv
import json
#import yaml
import traceback
def zhuanhuan(row,str_name ):
    if str_name  in row :
        countername = row[str_name]
    else:
        countername = 'None'
    return countername



def rdcell_parser(patn, timeStamp):
    # 参数文件路径
    para_path = os.path.join(patn, timeStamp)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    eutracell_dict = {}
    for file in filelist:
        if 'CM-ENB-ITRAN-EUTRANCELLTDD' in file:
            with open(para_path + '/' + str(file), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    lnbtsid = row['EnbFunction'].replace('MRBTS-', '')
                    lcrid = row['EutranCellTdd'].replace('LNCEL-', '')


                    Maxpw = row['MaximumTransmissionPower']
                    crs = row['ReferenceSignalPower']
                    OperationalState = row['OperationalState']
                    Tac = row['Tac']
                    Pci= row['Pci']
                    RootSequenceIndex = row['RootSequenceIndex']
                    if  'Earfcn' in row :
                        earfcn = row['Earfcn']
                    else:
                        earfcn =row['EarfcnDl']

                    cgi = '460-00-' + lnbtsid + '-' + lcrid
                    if  cgi in eutracell_dict :
                        pass
                    else:
                        eutracell_dict[cgi] = {'Maxpw':Maxpw,'earfcn':earfcn,'crs':crs,'OperationalState':OperationalState,'Tac':Tac,'Pci':Pci,'RootSequenceIndex':RootSequenceIndex}
    return eutracell_dict
def lncel_parser(patn, timeStamp):
    # 参数文件路径
    para_path = os.path.join(patn, timeStamp)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    eutracell_dict = {}
    for file in filelist:
        if 'CM-ENB-LNCEL_' in file:
            print(file)
            with open(para_path + '/' + str(file), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    try:
                        lnbtsid = row['EnbFunction'].replace('LNBTS-', '')
                        if  'EutranCellFdd' in row :
                            lcrid = row['EutranCellFdd'].replace('LNCEL-', '')
                        if 'EutranCellTdd' in row:
                            lcrid = row['EutranCellTdd'].replace('LNCEL-', '')
                        cgi ='460-00-' +str(lnbtsid) +'-'+ str(lcrid)
                        PrachConfigIndex = zhuanhuan(row, 'PrachConfigIndex')
                        ulRsCs = zhuanhuan(row, 'ulRsCs')
                        prachCS = zhuanhuan(row, 'prachCS')
                        if  cgi in eutracell_dict  :
                            pass
                        else:
                            eutracell_dict[cgi] = {'PrachConfigIndex':PrachConfigIndex,'ulRsCs':ulRsCs,'prachCS':prachCS           }
                    except Exception as e:
                        print(e)
    return eutracell_dict

def EUTRANRELATION_parser(patn, timeStamp):
    # 参数文件路径
    para_path = os.path.join(patn, timeStamp)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    eutracell_dict = {}
    for file in filelist:
        if '-EUTRANRELATION-' in file:
            print(file)
            with open(para_path + '/' + str(file), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    try:
                        lnbtsid = row['EnbFunction'].replace('LNBTS-', '')
                        if  'EutranCellFdd' in row :
                            lcrid = row['EutranCellFdd'].replace('LNCEL-', '')
                        if 'EutranCellTdd' in row:
                            lcrid = row['EutranCellTdd'].replace('LNCEL-', '')
                        cgi ='460-00-' +str(lnbtsid) +'-'+ str(lcrid)
                        #print(cgi,row)
                        adjeci = row['EutranRelation']
                        if  'ECI-' in adjeci :
                            adj_eci = adjeci.replace("ECI-","")
                        else:
                            #list_tmp = adjeci.split(":")
                            adj_eci =str(int(adjeci.split(":")[3])*256+int(adjeci.split(":")[4]))
                        #adj_eci = row['Tci'].split("-")[2] +'_' +row['Tci'].split("-")[3]
                        #print("当前eci:",adj_eci)
                        Pci = row['Pci']
                        Earfcn= row['Earfcn']
                        CellIndividualOffset= row['CellIndividualOffset']
                        QOffsetCell= row['QOffsetCell']

                        if  cgi in eutracell_dict :
                            if adj_eci in eutracell_dict[cgi]:
                                pass
                            else:
                                eutracell_dict[cgi][adj_eci] = {'Pci':Pci,'Earfcn':Earfcn,'CellIndividualOffset':CellIndividualOffset,'QOffsetCell':QOffsetCell}
                        else:
                            eutracell_dict[cgi] = {}
                            eutracell_dict[cgi][adj_eci]= {}
                            eutracell_dict[cgi][adj_eci] = {'Pci':Pci,'Earfcn':Earfcn,'CellIndividualOffset':CellIndividualOffset,'QOffsetCell':QOffsetCell}
                    except Exception as e:
                        traceback.print_exc()

    return eutracell_dict



def eutracell_parser(patn, timeStamp):
    # 参数文件路径
    para_path = os.path.join(patn, timeStamp)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    eutracell_dict = {}
    for file in filelist:
        if 'CM-ENB-EUTRANCELLTDD' in file or 'CM-ENB-EUTRANCELLFDD' in file or  'CM-ENB-ITRAN-EUTRANCELLTDD'  in file :
            print(file)
            with open(para_path + '/' + str(file), 'r') as f: #, encoding='utf-8'
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    lnbtsid = row['ManagedElement'].replace('MRBTS-', '')
                    lcrid = row['Id'].replace('LNCEL-', '')
                    UserLabel = zhuanhuan(row, 'UserLabel')  # row['MaximumTransmissionPower']
                    pmax = zhuanhuan(row,'MaximumTransmissionPower' ) #row['MaximumTransmissionPower']
                    crs = zhuanhuan(row,'ReferenceSignalPower' ) #rrow['ReferenceSignalPower']
                    OperationalState = zhuanhuan(row,'OperationalState' ) #  row['OperationalState']
                    Tac = zhuanhuan(row,'Tac' ) #row['Tac']
                    phyCellId = zhuanhuan(row,'Pci' ) #row['Pci']
                    rootSeqIndex = zhuanhuan(row,'RootSequenceIndex' ) # row['RootSequenceIndex']
                    dlRsBoost = zhuanhuan(row,'Pa' )
                    QRxLevMin = zhuanhuan(row,'QRxLevMin' )
                    PrachConfigIndex = zhuanhuan(row,'PrachConfigIndex')
                    ulRsCs = zhuanhuan(row,'ulRsCs')
                    BandIndicator = zhuanhuan(row, 'BandIndicator')
                    prachCS = zhuanhuan(row, 'prachCS')
                    band = 'D'
                    if BandIndicator == '3':
                        band = 'FDD1800'
                    if BandIndicator == '8':
                        band = 'FDD900'
                    if BandIndicator == '38':
                        band = 'D'
                    if BandIndicator == '40':
                        band = 'E'
                    if BandIndicator == '39':
                        band = 'F'
                    if BandIndicator == '34':
                        band = 'A'
                    if BandIndicator == '41':
                        band = 'D'
                    if  QRxLevMin == 'None' or  len(QRxLevMin) == 0:
                        pass
                    else:
                        #print(QRxLevMin)
                        QRxLevMin = str(int(float(QRxLevMin) *2))

                    if  dlRsBoost == 'None':
                        pass
                    else:
                        dlRsBoost=  dlRsBoost.replace("DB-","").replace("DB0","0")  +str('DB')
                    if  'Earfcn' in row :
                        earfcn = row['Earfcn']
                    else:
                        earfcn =row['EarfcnDl']
                    cgi = '460-00-' + lnbtsid + '-' + lcrid
                    if  cgi in eutracell_dict  :
                        pass
                    else:
                        if  '阳江' in  UserLabel or 'YJ-' in  UserLabel or  'omc7' in file :
                            eutracell_dict[cgi] = {'pmax':pmax,'PrachConfigIndex':PrachConfigIndex,'ulRsCs':ulRsCs,'earfcn':earfcn,'crs':crs,'OperationalState':OperationalState
                                ,'Band':band,'prachCS':prachCS
                                ,'Tac':Tac,'phyCellId':phyCellId,'rootSeqIndex':rootSeqIndex,'dlRsBoost':dlRsBoost,'QRxLevMin':QRxLevMin}
                    #print(cgi,prachCS)
    return eutracell_dict

def lnhoif_parser(patn,timeStamp):
    # 读取lnadj
    # 参数文件路径
    para_path = os.path.join(patn,timeStamp)#'d:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    lnhoif_dict = {}
    for file in filelist:
        if 'CM-ENB-LNHOIF-' in file:
            with open(para_path + '/' + str(file), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    lnbtsid = row['ManagedElement'].replace('MRBTS-', '')
                    if  len(row['EutranCellTdd']) >0 :
                        lcrid = row['EutranCellTdd'].replace('LNCEL-', '')
                    else:
                        lcrid = row['EutranCellFdd'].replace('LNCEL-', '')
                    id = row['Id'].replace('IRFIM-', '')
                    a3OffsetRsrpInterFreq = row['a3OffsetRsrpInterFreq']
                    eutraCarrierInfo = row['eutraCarrierInfo']
                    hysA3OffsetRsrpInterFreq = row['hysA3OffsetRsrpInterFreq']
                    offsetFreqInter = row['offsetFreqInter']
                    threshold3InterFreq = row['threshold3InterFreq']
                    threshold3InterFreqQci1 = row['threshold3InterFreqQci1']
                    threshold3aInterFreq = row['threshold3aInterFreq']
                    threshold3aInterFreqQci1 = row['threshold3aInterFreqQci1']
                    thresholdRsrpEndcFilt = row['thresholdRsrpEndcFilt']
                    thresholdRsrpIFLBFilter = row['thresholdRsrpIFLBFilter']
                    thresholdRsrpIFSBFilter = row['thresholdRsrpIFSBFilter']
                    thresholdRsrqIFSBFilter = row['thresholdRsrqIFSBFilter']
                    cgi = '460-00-' + lnbtsid + '-' + lcrid
                    # interFrqThrH	interFrqThrL interTResEut	pMaxInterF	qOffFrq	qQualMinR9	qRxLevMinInterF
                    if cgi in lnhoif_dict:
                        if id in lnhoif_dict[cgi]:
                            pass
                        else:
                            lnhoif_dict[cgi][id] = {'a3OffsetRsrpInterFreq': a3OffsetRsrpInterFreq, 'eutraCarrierInfo': eutraCarrierInfo,
                                                   'hysA3OffsetRsrpInterFreq': hysA3OffsetRsrpInterFreq, 'thresholdRsrpEndcFilt': thresholdRsrpEndcFilt, 'thresholdRsrpIFLBFilter': thresholdRsrpIFLBFilter
                                , 'offsetFreqInter': offsetFreqInter, 'threshold3InterFreq': threshold3InterFreq, 'threshold3InterFreqQci1': threshold3InterFreqQci1,
                                'threshold3aInterFreq': threshold3aInterFreq, 'threshold3aInterFreqQci1': threshold3aInterFreqQci1
                                ,'thresholdRsrpIFSBFilter': thresholdRsrpIFSBFilter, 'thresholdRsrqIFSBFilter': thresholdRsrqIFSBFilter}
                    else:
                        # print(lnadj_list)
                        lnhoif_dict[cgi] = {}
                        lnhoif_dict[cgi][id] = {}
                        lnhoif_dict[cgi][id] = {'a3OffsetRsrpInterFreq': a3OffsetRsrpInterFreq, 'eutraCarrierInfo': eutraCarrierInfo,
                                                   'hysA3OffsetRsrpInterFreq': hysA3OffsetRsrpInterFreq, 'thresholdRsrpEndcFilt': thresholdRsrpEndcFilt, 'thresholdRsrpIFLBFilter': thresholdRsrpIFLBFilter
                                , 'offsetFreqInter': offsetFreqInter, 'threshold3InterFreq': threshold3InterFreq, 'threshold3InterFreqQci1': threshold3InterFreqQci1,
                                'threshold3aInterFreq': threshold3aInterFreq, 'threshold3aInterFreqQci1': threshold3aInterFreqQci1
                                ,'thresholdRsrpIFSBFilter': thresholdRsrpIFSBFilter, 'thresholdRsrqIFSBFilter': thresholdRsrqIFSBFilter}
    return lnhoif_dict



def irfim_parser(patn,timeStamp):
    # 读取lnadj
    # 参数文件路径
    para_path = os.path.join(patn,timeStamp)#'d:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    irfim_dict = {}
    for file in filelist:
        if 'CM-ENB-IRFIM-' in file:
            with open(para_path + '/' + str(file), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    lnbtsid = row['ManagedElement'].replace('MRBTS-', '')
                    if  len(row['EutranCellTdd']) >0 :
                        lcrid = row['EutranCellTdd'].replace('LNCEL-', '')
                    else:
                        lcrid = row['EutranCellFdd'].replace('LNCEL-', '')
                    id = row['Id'].replace('IRFIM-', '')
                    dlCarFrqEut = row['dlCarFrqEut']
                    eutCelResPrio = row['eutCelResPrio']
                    interFrqThrH = row['interFrqThrH']
                    interFrqThrL = row['interFrqThrL']
                    interTResEut = row['interTResEut']
                    pMaxInterF = row['pMaxInterF']
                    qOffFrq = row['qOffFrq']
                    qRxLevMinInterF = row['qRxLevMinInterF']
                    cgi = '460-00-' + lnbtsid + '-' + lcrid
                    #interFrqThrH	interFrqThrL interTResEut	pMaxInterF	qOffFrq	qQualMinR9	qRxLevMinInterF
                    if cgi in irfim_dict:
                        if id in irfim_dict[cgi]:
                            pass
                        else:
                            irfim_dict[cgi][id] = {'dlCarFrqEut': dlCarFrqEut, 'eutCelResPrio': eutCelResPrio, 'interFrqThrH': interFrqThrH
                                ,'interFrqThrL': interFrqThrL,'interTResEut': interTResEut,'pMaxInterF': pMaxInterF,'qOffFrq': qOffFrq,'qRxLevMinInterF': qRxLevMinInterF}
                    else:
                        # print(lnadj_list)
                        irfim_dict[cgi] = {}
                        irfim_dict[cgi][id] = {}
                        irfim_dict[cgi][id] = {'dlCarFrqEut': dlCarFrqEut, 'eutCelResPrio': eutCelResPrio, 'interFrqThrH': interFrqThrH
                                ,'interFrqThrL': interFrqThrL,'interTResEut': interTResEut,'pMaxInterF': pMaxInterF,'qOffFrq': qOffFrq,'qRxLevMinInterF': qRxLevMinInterF}
    return irfim_dict

def parser_lnadj(patn,timeStamp):
    # 读取lnadj
    # 参数文件路径
    para_path = os.path.join(patn,timeStamp)#'d:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    lnadj_list = {}
    for file in filelist:
        if '-LNADJ-' in file:
            with open(para_path + '/' + str(file), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    lnbtsid = row['EnbFunction'].replace('LNBTS-', '')
                    id = row['Id'].replace('LNADJ-', '')
                    adjenbid = row['adjEnbId']
                    adjip = row['cPlaneIpAddr']
                    targetBtsDn = row['targetBtsDn']
                    x2LinkStatus = row['x2LinkStatus']
                    if lnbtsid in lnadj_list:
                        lnadj_list[lnbtsid][id] = {'adjEnbId': adjenbid, 'adjip': adjip, 'targetBtsDn': targetBtsDn,
                                                    'x2LinkStatus': x2LinkStatus}
                    else:
                        # print(lnadj_list)
                        lnadj_list[lnbtsid] = {}
                        lnadj_list[lnbtsid][id] = {}
                        lnadj_list[lnbtsid][id] = {'adjEnbId': adjenbid, 'adjip': adjip, 'targetBtsDn': targetBtsDn,
                                                   'x2LinkStatus': x2LinkStatus}

    return lnadj_list
def parser_lnadjl(patn,timeStamp):
    # 参数文件路径
    para_path = os.path.join(patn, timeStamp)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    lnadjl_dict = {}
    for file in filelist:
        if '-LNADJL-' in file:
            with open(para_path + '/' + str(file), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    # print(row)
                    lnbtsid = row['EnbFunction'].replace('LNBTS-', '')
                    lnadjid = row['LNADJ'].replace('LNADJ-', '')
                    lnadjlid = row['Id'].replace('LNADJL-', '')
                    ecgiAdjEnbId = row['ecgiAdjEnbId']
                    ecgiLcrId = row['ecgiLcrId']
                    fDlEarfcn = row['fDlEarfcn']
                    phyCellId = row['phyCellId']
                    tac = row['tac']
                    a_cgi = '460-00-' + ecgiAdjEnbId +'-' +ecgiLcrId

                    if  lnbtsid in lnadjl_dict :
                        if lnadjid in lnadjl_dict[lnbtsid] :
                            if lnadjlid in lnadjl_dict[lnbtsid][lnadjid] :
                                pass
                            else:
                                lnadjl_dict[lnbtsid][lnadjid][lnadjlid] = {'a_cgi':a_cgi,'ecgiAdjEnbId':ecgiAdjEnbId,'ecgiLcrId':ecgiLcrId,'fDlEarfcn':fDlEarfcn,'phyCellId':phyCellId,'tac':tac}
                        else:
                            lnadjl_dict[lnbtsid][lnadjid] = {}
                            lnadjl_dict[lnbtsid][lnadjid][lnadjlid] = {'a_cgi': a_cgi, 'ecgiAdjEnbId': ecgiAdjEnbId,
                                                                       'ecgiLcrId': ecgiLcrId, 'fDlEarfcn': fDlEarfcn,
                                                                       'phyCellId': phyCellId, 'tac': tac}

                    else:
                        lnadjl_dict[lnbtsid] = {}
                        lnadjl_dict[lnbtsid][lnadjid] = {}
                        lnadjl_dict[lnbtsid][lnadjid][lnadjlid] =  {'a_cgi':a_cgi,'ecgiAdjEnbId':ecgiAdjEnbId,'ecgiLcrId':ecgiLcrId,'fDlEarfcn':fDlEarfcn,'phyCellId':phyCellId,'tac':tac}
    return lnadjl_dict
def CTRLTS_parser(para_path,datatime):
    # 参数文件路径
    para_path = os.path.join(para_path, datatime)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    ctrlts_dict = {}
    for file in filelist:
        if 'CM-ENB-CTRLTS' in file:
            with open(para_path + '/' + str(file), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    # print(row)
                    enbid = row['ManagedElement'].replace('MRBTS-', '')
                    ctrltsid = row['Id']
                    netActIpAddr = row['netActIpAddr']

                    #cgi = '460-00-' + enbid + '-' + lcrId
                    if enbid in ctrlts_dict:
                        pass
                    else:
                        ctrlts_dict[enbid] = {'ctrltsid': ctrltsid,'netActIpAddr': netActIpAddr}
    return ctrlts_dict
def mtrace_parser(para_path,datatime):
    # 参数文件路径
    para_path = os.path.join(para_path, datatime)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    mrtrace_dict = {}
    for file in filelist:
        if 'CM-ENB-MTRACE' in file:
            with open(para_path + '/' + str(file), 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    # print(row) immedMDTAnonymization	immedMDTForceUEConsent	immedMDTObtainLocation	immedMDTPosMethod	immedMDTSelectOnlyGNSSUes
                    enbid = row['ManagedElement'].replace('MRBTS-', '')
                    lcrId = row['lcrId']
                    mtraceid = row['Id']
                    ifmdtlist = row['iFMDTList.iFFreqEARFCN']
                    tceIpAddress = row['tceIpAddress']
                    maxMDTFreqLayers = row['maxMDTFreqLayers']
                    interfaceSelection = row['interfaceSelection']
                    forceUeIdsRepetition = row['forceUeIdsRepetition']
                    ripTracing = row['ripTracing']
                    immedMDTAnonymization = row['immedMDTAnonymization']
                    immedMDTForceUEConsent = row['immedMDTForceUEConsent']
                    immedMDTObtainLocation = row['immedMDTObtainLocation']
                    immedMDTPosMethod = row['immedMDTPosMethod']
                    immedMDTSelectOnlyGNSSUes = row['immedMDTSelectOnlyGNSSUes']




                    cgi = '460-00-' + enbid + '-' + lcrId
                    if cgi in mrtrace_dict:
                        pass
                    else:
                        mrtrace_dict[cgi] = {'forceUeIdsRepetition':forceUeIdsRepetition,'interfaceSelection':interfaceSelection,'maxMDTFreqLayers':maxMDTFreqLayers
                            ,'mtraceid': mtraceid, 'ifmdtlist': ifmdtlist, 'tceIpAddress': tceIpAddress,'ripTracing':ripTracing,'immedMDTAnonymization':immedMDTAnonymization
                            , 'immedMDTForceUEConsent': immedMDTForceUEConsent,'immedMDTObtainLocation':immedMDTObtainLocation,'immedMDTPosMethod':immedMDTPosMethod,'immedMDTSelectOnlyGNSSUes':immedMDTSelectOnlyGNSSUes}
    return mrtrace_dict

def ENBFUNCTION_parser(para_path,datatime):
    # 参数文件路径
    para_path = os.path.join(para_path, datatime)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    enbfun_dict = {}
    for file in filelist:
        if '-ENBFUNCTION' in file  and 'omc7' in file:
            with open(para_path + '/' + str(file), 'r') as f: #, encoding='utf-8'
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    # print(row)
                    enbid = row['ManagedElement'].replace('MRBTS-', '')
                    actCSFBRedir = zhuanhuan(row,'actCSFBRedir')
                    actConvVoice = zhuanhuan(row,'actConvVoice')
                    X2IpAddressList  = zhuanhuan(row,'X2IpAddressList' ).split("/")[0].replace("{","").replace("}","")
                    actCellTrace = zhuanhuan(row,'actCellTrace' )  #row['actCellTrace']
                    actMDTCellTrace = zhuanhuan(row,'actMDTCellTrace' )  # row['actMDTCellTrace']
                    actVendSpecCellTraceEnh = zhuanhuan(row,'actVendSpecCellTraceEnh' )  # row['actVendSpecCellTraceEnh']
                    actMDTloggedCellTrace = zhuanhuan(row,'actMDTloggedCellTrace' )  # row['actMDTloggedCellTrace']
                    actInterFreqMDTCellTrace =zhuanhuan(row,'actInterFreqMDTCellTrace' )  #  row['actInterFreqMDTCellTrace']
                    #actCellTrace actMDTCellTrace actVendSpecCellTraceEnh actMDTloggedCellTrace actInterFreqMDTCellTrace

                    if enbid in enbfun_dict:
                        pass
                    else:
                        enbfun_dict[enbid] = {'X2IpAddressList':X2IpAddressList,'actCellTrace':actCellTrace,'actMDTCellTrace':actMDTCellTrace,'actVendSpecCellTraceEnh':actVendSpecCellTraceEnh
                            ,'actMDTloggedCellTrace': actMDTloggedCellTrace, 'actInterFreqMDTCellTrace': actInterFreqMDTCellTrace
                            ,'actCSFBRedir':actCSFBRedir,'actConvVoice':actConvVoice}
    return enbfun_dict

def ENBFUN_parser(para_path,datatime,paraname):
    # 参数文件路径
    para_path = os.path.join(para_path, datatime)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    enbfun_dict = {}
    for file in filelist:
        if '-ENBFUNCTION' in file  and 'omc7' in file:
            with open(para_path + '/' + str(file), 'r') as f: #, encoding='utf-8'
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    # print(row)
                    enbid = row['ManagedElement'].replace('MRBTS-', '')
                    paravalue = zhuanhuan(row,paraname)


                    if enbid in enbfun_dict:
                        pass
                    else:
                        enbfun_dict[enbid] = {paraname:paravalue}
    return enbfun_dict
def mro_parser(path,datatime):
    # 参数文件路径
    para_path = os.path.join(path, datatime)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    mro_dict = {}
    for file in filelist:
        if 'mro_rsrp_' in file:
            with open(para_path + '/' + str(file), 'r', encoding='gbk') as f:
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    enbid = row['ENBID']
                    lcrid = row['ENB_CELLID'][7:10]
                    count = row['ALL计数器']
                    cover_rate = row['MR覆盖率（RSRP>=-110)']
                    cgi = '460-00-' + str(enbid) + '-' + str(lcrid)
                    # print(cgi)

                    if cgi in mro_dict:
                        pass
                    else:
                        mro_dict[cgi] = {'count': count, 'cover_rate': cover_rate}
                    # lnbtsid = row['EnbFunction'].replace('LNBTS-', '')
    return mro_dict