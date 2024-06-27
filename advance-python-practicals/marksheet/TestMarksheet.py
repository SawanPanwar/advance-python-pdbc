from MarksheetModel import MarksheetModel


def testAdd():
    params = {}
    # params['id'] = 8
    params['rollNo'] = 108
    params['name'] = 'abc'
    params['physics'] = 70
    params['chemistry'] = 67
    params['maths'] = 79

    model = MarksheetModel()
    model.add(params)


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
    model.get(2)


def testFindByRollNo():
    model = MarksheetModel()
    model.findByRoll(103)


def testSearch():
    params = {}
    # params['name'] = 'abc'
    # params['rollNo'] = 101
    params['pageNo'] = 1
    params['pageSize'] = 0
    model = MarksheetModel()
    model.search(params)


# testAdd()
# testUpdate()
# testRead()
# testGet()
# testFindByRollNo()
testSearch()
