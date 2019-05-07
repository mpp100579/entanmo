
from time import sleep
import random
import unittest
import json
import requests
import accounts,blocks,delegates,lockvote,signatures,transactions
import time
import newAccount


class ETest(unittest.TestCase):
    # _genesisSecret = 'fluid bracket forum either face bird toy april boss stamp february pencil'
    # _genesisPublicKey = '220ca36be9d82e9b88abf25d2bdf8de9fd858f381a3cbd5a01d20a1637f28835'
    # _genesisAddress = 'AKEfwcTExJ4NZZ9C5o3P7q5mQcrvuL9vAi'
    def setUp(self):
        self.nodeServer='http://39.105.210.35:4096'
        self.genesisSecret = 'fluid bracket forum either face bird toy april boss stamp february pencil'
        self.genesisPublicKey = '220ca36be9d82e9b88abf25d2bdf8de9fd858f381a3cbd5a01d20a1637f28835'
        self.genesisAddress = 'AKEfwcTExJ4NZZ9C5o3P7q5mQcrvuL9vAi'
        self.genesisTrId = '289c0738ee485ba6f289f015fd2ae7b632e8c1167c40e5a55d663c32ad05b67d'
        self.secondSecret='123456'
        self.secret = 'race forget pause shoe trick first abuse insane hope budget river enough'
        self.recipientId = 'AMFcPgkRndYVgjMs9gKTKMEwW72yGivw3z'
        #A4MFB3MaPd355ug19GYPMSakCAWKbLjDTb
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('teardown')
    @classmethod
    def setUpClass(self):
        # 必须使用@classmethod 装饰器,所有test运行前运行一次
        print('begin')

    @classmethod
    def tearDownClass(self):
        # 必须使用 @ classmethod装饰器, 所有test运行完后运行一次
        print('close')
    def test_addTransactions(self):
        newAccount.AddTransactions()

    def test_addDelegate(self):
        newAccount.AddDelegate()
'''

#生成新账号
    def test_newAccount(self):
        r = accounts.new(self.nodeServer, ent=128)
        print('new', r)
        s=r['data']['secret']
        p=r['data']['publicKey']
        a=r['data']['address']
        return s,p,a
    


        # 转账
    def test_addTransactions(self):
        t=time.time()
        a = random.randint(1, 1000)
        accounts=int(t)+a
        transactions.add(self.nodeServer, self.secret, self.recipientId, accounts)
        print('addTransactions', transactions.add(self.nodeServer, self.secret, self.recipientId, accounts))

    def test_Account(self):
        resp = accounts.new(self.nodeServer, ent=128)
        print('new', resp)
        if resp['done'] == True:  # 如果返回结果为true,
            _newSecret = resp['data']['secret']  # 获取新建账号返回结果中的地址和公钥
            _newPublicKey = resp['data']['publicKey']
            _newAddress = resp['data']['address']
            print('open', accounts.open(self.nodeServer, _newSecret))
            print('open2', accounts.open2(self.nodeServer, _newPublicKey))
            print('getBalance', accounts.getBalance(self.nodeServer, _newAddress))
            print('getPublicKey', accounts.getPublicKey(self.nodeServer, _newAddress))
            print('generatePublicKey', accounts.generatePublicKey(self.nodeServer, self.genesisSecret))
            print('getDelegates', accounts.getDelegates(self.nodeServer, _newAddress))
            print('getAccount', accounts.getAccount(self.nodeServer, _newAddress))
            print('accountOnChain', accounts.accountOnChain(self.nodeServer, _newAddress))
            print('delayOrders', accounts.delayOrders(self.nodeServer, _newAddress))
            print('delayOrders', accounts.delayOrders(self.nodeServer, _newAddress, 1))

#对指定代理进行投票或取消投票
    def test_addDelegates(self):
        accounts.addDelegates(self.nodeServer, self.genesisSecret,
                              remove='a08dc0d7b170a0e12caff0a7faaef952741e65f3585905a5847e4d877d650f07', secondSecret='123456')
        print('addDelegates', accounts.addDelegates(self.nodeServer, self.genesisSecret,
                              remove='a08dc0d7b170a0e12caff0a7faaef952741e65f3585905a5847e4d877d650f07'))

#获取指定账号的余额
    def test_getBalance(self):
        accounts.getBalance(self.nodeServer, self.genesisAddress)
        print('getBalance', accounts.getBalance(self.nodeServer, self.genesisAddress))

#获取账号详细信息
    def test_getAccount(self):
        resp = accounts.getAccount(self.nodeServer, self.genesisAddress)
        # print('getAccount', accounts.getAccount(self.nodeServer, self.genesisAddress))
        print('getAccount', accounts.getAccount(self.nodeServer, self.genesisAddress))

#检测指定地址是否在链上
    def test_accountOnBlockchain(self):
        accounts.accountOnChain(self.nodeServer, self.genesisAddress)
        print('accountOnChain', accounts.accountOnChain(self.nodeServer, self.genesisAddress))

#获取链交易费
    def test_getFee(self):
        blocks.getFee(self.nodeServer, timeout=4000)

    def test_blocks(self):
        print('getFee', blocks.getFee(self.nodeServer))
        print('getHeight', blocks.getHeight(self.nodeServer))
        print('getMilestone', blocks.getMilestone(self.nodeServer))
        print('getSupply', blocks.getSupply(self.nodeServer))
        print('getReward', blocks.getReward(self.nodeServer))
        print('getStatus', blocks.getStatus(self.nodeServer))
        print('getBlock', blocks.getBlock(self.nodeServer, height=2))
        print('getBlock',
              blocks.getBlock(self.nodeServer, blockid='b8f0e9310ede1fc64fbbcdc7dee0edebdd74490017e5b4261573c14c80de591a'))
        print('getFullBlock', blocks.getFullBlock(self.nodeServer, height=2))
        print('getFullBlock', blocks.getFullBlock(self.nodeServer,
                                                  blockid='b8f0e9310ede1fc64fbbcdc7dee0edebdd74490017e5b4261573c14c80de591a'))
        print('getBlocks', blocks.getBlocks(self.nodeServer,
                                            previousBlock='b8f0e9310ede1fc64fbbcdc7dee0edebdd74490017e5b4261573c14c80de591a'))
        print('getBlocks', blocks.getBlocks(self.nodeServer, orderBy='height:desc', limit=2))
        print('getBlocks', blocks.getBlocks(self.nodeServer,
                                            generatorPublicKey='220ca36be9d82e9b88abf25d2bdf8de9fd858f381a3cbd5a01d20a1637f28835',
                                            limit=1))
#获取当前链高度
    def test_getHeight(self):
        blocks.getHeight(self.nodeServer)
        print('getHeight', blocks.getHeight(self.nodeServer))

#获取链当前区块奖励
    def test_getReward(self):
        blocks.getReward(self.nodeServer)
        print('getReward', blocks.getReward(self.nodeServer))

#获取指定区块信息
    def test_getBlock(self):
        blocks.getBlock(self.nodeServer, blockid='b8f0e9310ede1fc64fbbcdc7dee0edebdd74490017e5b4261573c14c80de591a')
        blocks.getBlock(self.nodeServer, height=2)

#获取链当前已发行的Token总量
    def test_getSupply(self):
        blocks.getSupply(self.nodeServer, timeout=4000)
        print('getSupply', blocks.getSupply(self.nodeServer, timeout=4000))

#获取指定区块的详细信息(包含区块中打包的交易信息)
    def test_getFullBlock(self):
        blocks.getFullBlock(self.nodeServer,height=200)
        print('getFullBlock', blocks.getFullBlock(self.nodeServer,height=200))

    def test_delegates(self):
        print('count', delegates.count(self.nodeServer))
        print('getDelegate', delegates.getDelegate(self.nodeServer, publicKey=self.genesisPublicKey))
        print('getDelegate', delegates.getDelegate(self.nodeServer, username='etm_001'))
        print('getVoters', delegates.getVoters(self.nodeServer, publicKey=self.genesisPublicKey))
        print('getFee', delegates.getFee(self.nodeServer))
        print('getForgedByAccount', delegates.getForgedByAccount(self.nodeServer, generatorPublicKey=self.genesisPublicKey))
        print('getDelegates', delegates.getDelegates(self.nodeServer, address=self.genesisAddress, limit=2))
        print('getDelegates', delegates.getDelegates(self.nodeServer, limit=3))
        print('getDelegates', delegates.getDelegates(self.nodeServer, offset=1, limit=2))
        print('getDelegates', delegates.getDelegates(self.nodeServer, limit=3, orderBy='username:desc'))

#获取当前代理人总数量
    def test_count(self):
        delegates.count(self.nodeServer)
        print('count', delegates.count(self.nodeServer))

#获取满足条件的代理人详细信息
    def test_getDelegate(self):
        delegates.getDelegate(self.nodeServer, publicKey=self.genesisPublicKey)
        delegates.getDelegate(self.nodeServer, username='etm_001')

#获取指定代理人的投票人列表
    def test_getVoters(self):
        delegates.getVoters(self.nodeServer, publicKey=self.genesisPublicKey)

#获取代理人相关操作交易费
    def test_delegateFee(self):
        delegates.getFee(self.nodeServer)

#获取满足条件的代理人集
    def test_getDelegates(self):
        delegates.getDelegates(self.nodeServer, address=self.genesisAddress, limit=2)
        delegates.getDelegates(self.nodeServer, limit=3)
        delegates.getDelegates(self.nodeServer, offset=1, limit=2)
        delegates.getDelegates(self.nodeServer, limit=3, orderBy='username:desc')

#获取指定代理人出块收益信息
    def test_getForgedByAccount(self):
        delegates.getForgedByAccount(self.nodeServer, generatorPublicKey=self.genesisPublicKey)

#注册代理人
    def test_addDelegate(self):
        delegates.addDelegate(self.nodeServer, secret=self.genesisSecret, username='mpp3', publicKey=self.genesisPublicKey,secondSecret=self.secondSecret)
        print('addDelegate',delegates.addDelegate(self.nodeServer, secret=self.genesisSecret, username='mpp3', publicKey=self.genesisPublicKey,secondSecret=self.secondSecret))

#注销代理人
    def test_delDelegate(self):
        delegates.delDelegate(self.nodeServer, secret=self.genesisSecret)
        print('delDelegate',delegates.delDelegate(self.nodeServer, secret=self.genesisSecret))


#获取锁仓交易信息
    def test_getLockVote(self):
        lockvote.getLockVote(self.nodeServer, self.genesisTrId)

#获取满足条件的锁仓交易列表
    def test_getAllLockVotes(self):
        lockvote.getAllLockVotes(self.nodeServer, self.genesisAddress)

#添加锁仓
    def test_addLockvote(self):
        lockvote.add(self.nodeServer, secret=self.genesisSecret, amount='1000',secondSecret=self.secondSecret)
        print('addLockVote', lockvote.add(self.nodeServer, secret=self.genesisSecret, amount='1000',secondSecret=self.secondSecret))

#解除锁仓
    def test_remove(self):
        lockvote.remove(self.nodeServer, secret=self.genesisSecret, trids=[159],secondSecret=self.secondSecret)
        print('remove', lockvote.remove(self.nodeServer, secret=self.genesisSecret, trids=[159],secondSecret=self.secondSecret))

#设置二级密码
    def test_signatures(self):
        signatures.getFee(self.nodeServer)
        signatures.add(self.nodeServer,self.genesisSecret,self.secondSecret)

#获取满足条件的交易集
    def test_transactions(self):
        transactions.getTransactions(self.nodeServer, limit=1)
        transactions.getTransactions(self.nodeServer, limit=2, orderBy='blockHeight:desc')
        transactions.getTransaction(self.nodeServer,
                                    trid='f0af7052a760edb104c118d1f6950f597f50a314b872508d9bc7e16f7062219c')
#获取满足条件的未确认交易集
    def test_getUnconfirmedTransactions(self):
        transactions.getUnconfirmedTransactions(self.nodeServer, senderPublicKey='', address='')



#延时转账
    def test_addDelayTransactions(self):
        transactions.addDelay(self.nodeServer, self.secret, self.recipientId, 10000, '1800')
        print('addDelayTransactions', transactions.addDelay(self.nodeServer, self.secret, self.recipientId,10000,'1800'))














# 如果想临时跳过某个case：skip装饰器
#     @unittest.skip("i don't want to run this case. ")



'''

if __name__ == '__main__':
    # 在main()中加verbosity参数，可以控制输出的错误报告的详细程度
    # verbosity=*：默认是1；设为0，则不输出每一个用例的执行结果；2-输出详细的执行结果
    unittest.main(verbosity=2)
