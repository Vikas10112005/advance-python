from marksheetmodel import MarksheetModel

def test_nextPK():
    model = MarksheetModel()
    pk = model.nextPK()
    assert isinstance(pk, int)
    assert pk > 0
    print(f"Next PK: {pk}")


def test_add():
    model = MarksheetModel()
    data = {
         'name': 'dhurv',
        'rollNo': 14,
        'physics': 90,
        'chemistry': 80,
        'maths': 97
    }
    model.add(data)
    print("Data added successfully")

def testupdate():
      model = MarksheetModel
      data={
          'id':3,
          'rollNo': 12,
          'name': 'kabir bas',
          'physics': 88,
          'chemistry': 92,
          'maths': 96
       }
      model.update(model,data)
      print("data update successfully")

def testDelete():
    model = MarksheetModel()
    model.delete(4)


def  testget():
    marksheet = MarksheetModel()
    marksheet.get(1)

def testfindByRoll():
    model = MarksheetModel()
    model.findByRoll('14')


def testSearch():
    params = {}
    params['name'] = 'amit'
   # params['rollNo'] = 10
    params['pageNo'] = 1
    params['pageSize'] = 0
    model = MarksheetModel()
    model.search(params)


#test_nextPK()
#test_add()
#testupdate()
#testDelete()
#testget()
#testfindByRoll()
testSearch()