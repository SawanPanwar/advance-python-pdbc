from studentModel import studentModel


def testAdd():
    x = {}
    x['emp_id'] = 108
    x['name'] = 'Vinay'
    x['salary'] = 30000

    model = studentModel()
    model.add(x)


def testUpdate():
    x = {}
    x['id'] = 7
    x['emp_id'] = 107
    x['name'] = 'Tarun'
    x['salary'] = 20000

    model = studentModel()
    model.update(x)


def testDelete():
    model = studentModel()
    model.delete(9)


def testRead():
    model = studentModel()
    model.read()


def testGet():
    model = studentModel()
    model.get(5)


def testfindbyempId():
    model = studentModel()
    model.findbyempId(103)


def testSearch():
    x = {}
    x['pageNo'] = 1
    x['pageSize'] = 4
    model = studentModel()
    model.search(x)
# testAdd()
# testUpdate()
# testDelete()
# testRead()
# testfindbyempId()
# testSearch()
# testGet()
