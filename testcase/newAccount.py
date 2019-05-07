import accounts,transactions  #引入模块
import time,random,delegates
import json,string,lockvote,accounts,transactions

#生成新账号
def set_newAccount():
    url='http://39.105.210.35:5000'
    r = accounts.new(url, ent=128)
    r['url']=url
    r['suppersecret'] = 'race forget pause shoe trick first abuse insane hope budget river enough'
    r['superpublickey'] = 'bd93add22ab931a279f0ef741b768796afc3756ec697f76bef4e2f634969294d'
    r['reciptionid']='AMFcPgkRndYVgjMs9gKTKMEwW72yGivw3z'
    print('new', r)
    account=json.dumps(r)      #把返回的json对象转成字符串用dumps()保存写入txt，先转字符串后写
    f=open('./account.txt', 'w',encoding='utf-8')
    # account=str(r)
    f.write(account)
    return account

set_newAccount()

#把新建账号的信息缓存到本地，然后所有的信息都从本地取
def get_account():
    r2=open('./account.txt', 'r',encoding='utf-8')
    js=r2.read()
    r2.close()
    dic = json.loads(js)      #JSON编码的字符串转换回一个Python数据结构字典用loads(),读取txt中的字典，先读后转Python对象
    return dic
get_account()

#给新用户转账
def AddTransactions1():
    list_account=get_account()
    url=list_account['url']
    secret=list_account['secret']
    address=list_account['address']  #获取字典的key对应value值
    suppersecret=list_account['suppersecret']
    superpublickey=list_account['superpublickey']
    t = time.time()
    print(t)
    a = random.randint(1, 100)
    amounts = (int(t) + a)*20000
    transactions.add(nodeServer=url, secret=suppersecret, recipientId=address, amount=amounts)
    print('addTransactions给新用户转账', transactions.add(url, suppersecret, address, amounts+1))
    print('addTransactions给新用户转账','Address:'+address,amounts)
    time.sleep(5)
AddTransactions1()

#获取指定账号的余额,交易能在链上查得到，再查余额才是准确的
def GetBalance():
    time.sleep(3)
    list_account = get_account()
    url = list_account['url']
    secret = list_account['secret']
    address = list_account['address']  # 获取字典的key对应value值
    accounts.getBalance(nodeServer=url, address=address)
    print('获取新建账号的余额：','secret:'+secret,'addrss:',address,accounts.getBalance(nodeServer=url, address=address))
GetBalance()

#给其他用户转账
def AddTransactions2():
    list_account = get_account()
    url = list_account['url']
    secret = list_account['secret']
    address = list_account['address']  # 获取字典的key对应value值
    reciptionid = list_account['reciptionid']
    a = random.randint(10, 2000)
    transactions.add(nodeServer=url, secret=secret, recipientId=reciptionid, amount=a)
    print('给其他用户转账:','RecipientId:'+reciptionid,transactions.add(nodeServer=url, secret=secret, recipientId=reciptionid, amount=a+1))
    address = list_account['address']  # 获取字典的key对应value值
    resp = accounts.getAccount(nodeServer=url, address=address)
    print('getAccount获取新建账户信息还没有生成publickey', 'Secret:'+secret,'address:'+address,resp)

AddTransactions2()

# def main():#控制函数执行顺序
#     AddTransactions2()
#     if True:
#         GetAccount()
#     else:
#         print('fail')


#获取账号公钥
def GetPublicKey():
    time.sleep(5)
    list_account = get_account()
    url = list_account['url']
    address = list_account['address']  # 获取字典的key对应value值
    secret = list_account['secret']
    result= accounts.getPublicKey(nodeServer=url, address=address)
    # print('result:',result,'address:'+address)
    publicKey=result['publicKey']
    list_account['publickey']=publicKey
    print('获取账户公钥Getpublickey:', publicKey)
    print('list_account[publickey]:',list_account['publickey'],'Secret:'+secret,'address:'+address)

GetPublicKey()


#注册代理人
def AddDelegate():
    list_account = get_account()
    url = list_account['url']
    secret = list_account['secret']
    address = list_account['address']  # 获取字典的key对应value值
    publickey = list_account['publicKey']
    # print('Url:'+url,'Secret:'+secret,'Address:'+address,'Publickey:'+publickey)
    username= ''.join(random.sample(string.ascii_letters + string.digits, 8))
    r=delegates.addDelegate(nodeServer=url, secret=secret, username=username, publicKey=publickey)
    print(u'addDelegate注册代理人:',r)
    print(u'addDelegate注册代理人:','secret:'+secret,'publickey:'+publickey)

AddDelegate()



# 注销代理人
# def DelDelegate():
#     time.sleep(2)
#     list_account = get_account()
#     url = list_account['url']
#     secret = list_account['secret']
#     delegates.delDelegate(nodeServer=url, secret=secret)
#     print(u'delDelegate注销代理人',delegates.delDelegate(url, secret=secret)
#
# DelDelegate()

#添加锁仓
def AddLockvote():
    GetPublicKey()
    time.sleep(5)
    list_account = get_account()
    url = list_account['url']
    secret = list_account['secret']
    publickey = list_account['publicKey']
    amount='100000000'
    result=lockvote.add(nodeServer=url, secret=secret,amount=amount,publicKey=publickey)
    print('addLockVote添加锁仓:',result)
    print('addLockVote添加锁仓', 'url:'+url,'secret:'+secret,amount,'publickey:'+publickey)
    return result

AddLockvote()
#解除锁仓
# def RemoveLockVote():
#     list_account = get_account()
#     url = list_account['url']
#     secret = list_account['secret']
#     lockvote.remove(nodeServer=url, secret=secret, trids=[159])
#     print('remove', lockvote.remove(nodeServer=url, secret=secret, trids=[159]))
#
# RemoveLockVote()

# 对指定代理进行投票或取消投票,被投票的人必须是矿工
def AddDelegates():
    time.sleep(2)
    list_account = get_account()
    url = list_account['url']
    secret = list_account['secret']
    publickey=list_account['publicKey']
    AddLockvote()  # 对指定代理进行投票或取消投票,被投票的人必须是矿工
    result=accounts.addDelegates(nodeServer=url, secret=secret,add=publickey)
    print('addDelegates对指定代理投票：','secret:'+secret, 'delegates:'+publickey)
    print('addDelegates对指定代理投票：',result)
AddDelegates()