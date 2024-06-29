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
    params['id'] = 4
    params['firstName'] = 'Shruti'
    params['lastName'] = 'Sisodiya'
    params['loginId'] = '104Shruti'
    params['password'] = 'abc'
    params['dob'] = datetime.date(2003, 3, 3)  # datetime.date(2021, 6, 1) for custom date
    params['address'] = 'Dewas'

    model = UserModel()
    model.update(params)


def testDelete():
    model = UserModel()
    model.delete(7)


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
# testUpdate()
# testRead()
# testGet()
# testfindbylogin()
# testSearch()
