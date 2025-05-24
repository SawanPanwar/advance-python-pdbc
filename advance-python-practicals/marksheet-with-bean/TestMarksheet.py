from MarksheetModel import MarksheetModel
from MarksheetBean import MarksheetBean


def testAdd():

    bean = MarksheetBean()
    bean.set_rollNo(108)
    bean.set_name('abc')
    bean.set_physics(70)
    bean.set_chemistry(70)
    bean.set_maths(70)

    model = MarksheetModel()
    model.add(bean)


def testUpdate():
    params = {}
    params['id'] = 8
    params['rollNo'] = 108
    params['name'] = 'ooo'
    params['physics'] = 70
    params['chemistry'] = 67
    params['maths'] = 79

    model = MarksheetModel()
    model.update(params)


def testDelete():
    model = MarksheetModel()
    model.delete(8)


def testRead():
    model = MarksheetModel()
    model.read()


def testGet():
    model = MarksheetModel()
    list = model.get(1)
    for data in list:
        print(data['id'], '\t', data['rollNo'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


def testFindByRollNo():
    model = MarksheetModel()
    list = model.findByRoll(103)
    for data in list:
        print(data['id'], '\t', data['rollNo'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


def testSearch():
    params = {}
    # params['name'] = 'abc'
    # params['rollNo'] = 101
    params['pageNo'] = 1
    params['pageSize'] = 0
    model = MarksheetModel()
    list = model.search(params)
    for data in list:
        print(data['id'], '\t', data['rollNo'], '\t', data['name'], '\t', data['physics'], '\t', data['chemistry'],
              '\t',
              data['maths'], )


# testAdd()
# testUpdate()
# testRead()
testGet()
# testFindByRollNo()
# testSearch()
