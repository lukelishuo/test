# This file contains paras which for negative testing
objects1 = 'xxxx'
objects2 = 'ssss'

ZHCS = {
            'empty':[],
            'integer': [10, 23, 44, 88, 99],
            'float': [1.11, 2.342, -1.03],
            'string': ['aaaa', 'bbbb', 'cccc','dddd'],
            'object': [objects1, objects2],
            'short': ['1', '0'],
            'long': ['11111111111111111111111111111111111111111111111'],
            'sql_injection': [';and 1=1 ;and 1=2', ";and (select count(*) from sysobjects)>0 mssql", ";and 1=(select IS_SRVROLEMEMBER('sysadmin'));--"],
         }

