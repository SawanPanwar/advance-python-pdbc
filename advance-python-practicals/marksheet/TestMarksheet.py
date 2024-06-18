from MarksheetModel import MarksheetModel


def testAdd():
    params = {}
    params["id"] = 1
    params["name"] = "kkk"
    params["rollNo"] = 101
    params["physics"] = 78
    params["chemistry"] = 67
    params["maths"] = 89

    model = MarksheetModel()
    model.add(params)

def testUpdate():
    params = {}
    params["id"] = 1
    params["name"] = "hhh"
    params["rollNo"] = 101
    params["physics"] = 78
    params["chemistry"] = 67
    params["maths"] = 89

    model = MarksheetModel()
    model.update(params)

def testDelete():
    model = MarksheetModel()
    model.delete(1)

def testRead():
    model = MarksheetModel()
    model.read()

#testAdd()
#testUpdate()
#testDelete()
testRead()
