#!/usr/bin/python3
#$ {TIME} - 当前系统时间。
# @Author  : Charlie
# @Email   : li-3221039@163.com

import os,csv
#import json
#import yaml
#import traceback
def zhuanhuan(row,str_name ):
    if str_name  in row :
        countername = row[str_name]
    else:
        countername = 'None'
    return countername



def ENBFUN_parser(para_path,datatime,paraname):
    # 参数文件路径
    para_path = os.path.join(para_path, datatime)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    enbfun_dict = {}
    for file in filelist:
        if '-ENBFUNCTION' in str(file)  and 'omc7' in str(file) :
            with open(para_path + '/' + str(file), 'r') as f: #, encoding='utf-8'
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    #print(row)
                    enbid = row['ManagedElement'].replace('MRBTS-', '')
                    paravalue = zhuanhuan(row,paraname)
                    if enbid in enbfun_dict:
                        pass
                    else:
                        enbfun_dict[enbid] = {paraname:paravalue}
    return enbfun_dict

def lnbts_parser(para_path,datatime,paraname):
    # 参数文件路径
    para_path = os.path.join(para_path, datatime)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(para_path)
    enbfun_dict = {}
    for file in filelist:
        if '-ENB-LNBTS_' in str(file)  and 'omc7' in str(file) :
            with open(para_path + '/' + str(file), 'r') as f: #, encoding='utf-8'
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    # print(row)
                    enbid = row['ManagedElement'].replace('MRBTS-', '')
                    paravalue = row[paraname]  #zhuanhuan(row,paraname)
                    if enbid in enbfun_dict:
                        pass
                    else:
                        enbfun_dict[enbid] = {paraname:paravalue}
    return enbfun_dict
def eutracell_parser(para_path,datatime,paraname):
    # 参数文件路径
    parapath = os.path.join(para_path, datatime)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(parapath)
    eutracell_dict = {}
    for file in filelist:
        if 'CM-ENB-EUTRANCELL' in str(file) and  'omc7' in str(file)  :
            #print(file)
            with open(parapath + '/' + str(file), 'r') as f: #, encoding='utf-8'
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    #print(row)
                    lnbtsid = row['ManagedElement'].replace('MRBTS-', '')
                    lcrid = row['Id'].replace('LNCEL-', '')
                    #UserLabel = zhuanhuan(row, 'UserLabel')  # row['MaximumTransmissionPower']
                    paravalue = row[paraname]  #zhuanhuan(row,paraname) #row['MaximumTransmissionPower']
                    cgi = '460-00-' + lnbtsid + '-' + lcrid
                    if  cgi in eutracell_dict  :
                        pass
                    else:
                        eutracell_dict[cgi] = {paraname:paravalue}
                    #print(cgi,prachCS)
    return eutracell_dict
def lncell_parser(para_path,datatime,paraname):
    # 参数文件路径
    parapath = os.path.join(para_path, datatime)  # 'd:\python_project/x2_linkcheck' + '/' + timeStamp
    filelist = os.listdir(parapath)
    eutracell_dict = {}
    for file in filelist:
        if 'CM-ENB-LNCEL_' in str(file) and  'omc7' in str(file)  :
            #print(file)
            with open(parapath + '/' + str(file), 'r') as f: #, encoding='utf-8'
                reader = csv.reader(f)
                filednames = next(reader)
                csv_reader = csv.DictReader(f, fieldnames=filednames)
                for row in csv_reader:
                    #print(row)
                    lnbtsid = row['ManagedElement'].replace('MRBTS-', '')
                    lcrid = row['Id'].replace('LNCEL-', '')
                    #UserLabel = zhuanhuan(row, 'UserLabel')  # row['MaximumTransmissionPower']
                    paravalue = row[paraname]  #zhuanhuan(row,paraname) #row['MaximumTransmissionPower']
                    cgi = '460-00-' + lnbtsid + '-' + lcrid
                    if  cgi in eutracell_dict  :
                        pass
                    else:
                        eutracell_dict[cgi] = {paraname:paravalue}
                    #print(cgi,prachCS)
    return eutracell_dict

# parapath = 'D:\python\关键参数核查\parapath'
# enbfun_dict = eutracell_parser(parapath, '20210408','cellBarred')
#
# print(enbfun_dict)
# for item in enbfun_dict :
#     print(item,enbfun_dict[item])