from MarksheetModel import MarksheetModel


def testAdd():
    params = {}
    params["name"] = "kkk"
    params["rollNo"] = 101
    params["physics"] = 78
    params["chemistry"] = 67
    params["maths"] = 89

    model = MarksheetModel()
    model.add(params)


def testUpdate():
    params = {}
    params["id"] = 2
    params["name"] = "hhh"
    params["rollNo"] = 102
    params["physics"] = 71
    params["chemistry"] = 90
    params["maths"] = 99

    model = MarksheetModel()
    model.update(params)


def testDelete():
    model = MarksheetModel()
    model.delete(1)


def testSearch():
    params = {}
    params["name"] = "k"
    params["rollNo"] = 101
    params["pageNo"] = 1
    params["pageSize"] = 5
    model = MarksheetModel()
    model.search(params)


def testGet():
    model = MarksheetModel()
    model.get(1)


# testAdd()
# testUpdate()
# testDelete()
testSearch()
# testGet()
