from UserModel import UserModel
import datetime


def testadd():
    params = {}
    params['firstName'] = 'Sneha'
    params['lastName'] = 'Kushwah'
    params['loginId'] = '105Sneha'
    params['password'] = 'abc'
    params['dob'] = datetime.date(2003, 12, 27)  # datetime.date(2021, 6, 1) for custom date
    params['address'] = 'Indore'

    model = UserModel()
    model.add(params)


def testUpdate():
    params = {}
    params['id'] = 5
    params['firstName'] = 'Snehaa'
    params['lastName'] = 'Kushwah'
    params['loginId'] = '105Sneha'
    params['password'] = 'abc'
    params['dob'] = datetime.date(2003, 12, 27)  # datetime.date(2021, 6, 1) for custom date
    params['address'] = 'Indore'

    model = UserModel()
    model.update(params)


def testDelete():
    model = UserModel()
    model.delete(1)


def testRead():
    model = UserModel()
    model.read()

def testGet():
    model = UserModel()
    model.get(5)

def testfindbylogin():
    model = UserModel()
    model.findbylogin(103)

def testSearch():
    params = {}
    params['pageNo'] = 1
    params['pageSize'] = 4
    model = UserModel()
    model.search(params)
# testDelete()
# testadd()
#testUpdate()
#testRead()
#testGet()
#testfindbylogin()
testSearch()