
#!/usr/bin/python3
#$ {TIME} - 当前系统时间。
# @Author  : Charlie
# @Email   : li-3221039@163.com

import parser_class
import configparser
import os,sys,datetime
import check_modular
from pathlib import Path




if __name__ == '__main__':
    exe_path = os.path.split(os.path.abspath(sys.argv[0]))[0]
    config = configparser.ConfigParser()
    config.read(exe_path + "/" + "conf.ini", encoding="utf-8-sig")
    parapath = config.get("main","parapath")
    time_cur = datetime.datetime.now()
    today = '20210408'  #time_cur.strftime('%Y%m%d')
#actCSFBRedir 1
    ##################判断目录是否存在#########################33
    my_file = Path(parapath+"/"+today)
    if my_file.exists():
        record_list = []
        ######################基站侧参数核查 para_path,datatime,paraname
        #enbfun_dict = parser_class.ENBFUN_parser(parapath, today)
        btspara = check_modular.btspara()
        for  item in btspara :
            try:
                paraname= item.split('|')[0]
                class_type = item.split('|')[1]
                paravlue = item.split('|')[2]
                enbfun_dict = parser_class.ENBFUN_parser(parapath, today,paraname)
                para_dict ={'paraname':paraname,'class_type':class_type,'paravlue':paravlue}
                record_list = check_modular.para_compare(today,enbfun_dict,para_dict,record_list)
            except Exception as e:
                print(e)
        #####################小区侧参数核查
        cellpara = check_modular.cellpara()
        for item in cellpara :
            try:
                paraname = item.split('|')[0]
                class_type = item.split('|')[1]
                paravlue = item.split('|')[2]
                cell_dict = parser_class.eutracell_parser(parapath, today, paraname)
                para_dict = {'paraname': paraname, 'class_type': class_type, 'paravlue': paravlue}
                record_list = check_modular.para_compare(today, cell_dict, para_dict, record_list)
            except Exception as e:
                print(e)
        ########################lncel参数核查###############
        lncellpara = check_modular.lncelpara()
        for item in lncellpara:
            try:
                paraname = item.split('|')[0]
                class_type = item.split('|')[1]
                paravlue = item.split('|')[2]
                cell_dict = parser_class.lncell_parser(parapath, today, paraname)
                para_dict = {'paraname': paraname, 'class_type': class_type, 'paravlue': paravlue}
                record_list = check_modular.para_compare(today, cell_dict, para_dict, record_list)
            except Exception as e:
                print(e)
        for item in record_list :
             print(item)


    #files =os.listdir(os.path.join(parapath,today))

    #print(files,today)






