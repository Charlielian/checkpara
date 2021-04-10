




def btspara():
    btspara_dict = [
    'actCSFBRedir|LNBTS|1'
  , 'actConvVoice|LNBTS|1'
, 'acteNACCtoGSM|LNBTS|0'
, 'actRedirect|LNBTS|1'
, 'actSrvccToGsm|LNBTS|0'
, 'pdcpProf101snSize|LNBTS|1'
    ,'pdcpProf102snSize|LNBTS|1'
    ,'rlcProf101snFieldLengthDL|LNBTS|1'
    ,'rlcProf101snFieldLengthUL|LNBTS|1'
    ,'rlcProf102snFieldLengthDL|LNBTS|1'
    ,'rlcProf102snFieldLengthUL|LNBTS|1'
    ]
#acteNACCtoGSM
# actRedirect
# actSrvccToGsm
#     'pdcpProf101snSize|LNBTS|1'
#     'pdcpProf102snSize|LNBTS|1'
#     'rlcProf101snFieldLengthDL|LNBTS|1'
#     'rlcProf101snFieldLengthUL|LNBTS|1'
#     'rlcProf102snFieldLengthDL|LNBTS|1'
#     'rlcProf102snFieldLengthUL|LNBTS|1'

    return btspara_dict

def cellpara():
    cellpara_dict = [
    'Enable64Qam|EUTRANCELL|TRUE'
        #,'t300|LNCELL|TRUE'
        #, 't301|LNCELL|TRUE'
        , 't302|EUTRANCELL|2000'
        , 't304IntraLte|EUTRANCELL|4'
        #, 't310|LNCELL|TRUE'
        #, 't311|LNCELL|TRUE'
   # ,'cellBarred|LNCELL|NOTBARRED'
    #,'dlRsBoost|LNCELL|TRUE'

    ]
    return cellpara_dict
def lncelpara():
    cellpara_dict = [
             't300|LNCELL|TRUE'
            , 't301|LNCELL|TRUE'
            , 't310|LNCELL|TRUE'
            , 't311|LNCELL|TRUE'
            # ,'cellBarred|LNCELL|NOTBARRED'
            # ,'dlRsBoost|LNCELL|TRUE'

        ]

    return cellpara_dict










def para_compare(today,para_data,para_dict,record_list):

    paraname = para_dict['paraname']
    paravlue = para_dict['paravlue']
    class_type = para_dict['class_type']
    for item in para_data :
        cur_para_value = para_data[item][paraname]
        #print(item,enbfun_dict[item]['actCSFBRedir'])
        if paravlue != cur_para_value and paravlue != 'None' :
            #print(today,item,paraname,cur_para_value,paravlue)
            record_list.append(
                {'sdate':today
                ,'DN':item
                 ,'userlaber':None
                ,'paraname':paraname
                ,'class':class_type
                ,'cur_value':cur_para_value
                ,'para_value':paravlue
                 ,'remark':None
                 ,'sum_pdcp':None})

    return record_list