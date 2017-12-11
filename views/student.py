from sanic.response import json
from sanic.views import HTTPMethodView
import uuid

# Key Value Store / In Memory DB
in_memory_db = {}


def create_kv(key, value):
    global in_memory_db
    in_memory_db[key] = value
    return in_memory_db[key]


def update_kv(key, value):
    global in_memory_db
    if key in in_memory_db:
        in_memory_db[key] = value
        return in_memory_db[key]
    else:
        return {"error": "key not found"}

def delete_kv(key):
    global in_memory_db
    if key in in_memory_db:
        in_memory_db[key] = None
        return {'id': key, 'status': 'deleted'}
    else:
        return {}

def get_kv(key):
    global in_memory_db
    if (key in in_memory_db) and in_memory_db[key]:
        return in_memory_db[key]
    else:
        return {"error": "key not found"}

def list_kv():
    result = [val for key, val in in_memory_db.items() if val]
    return result

def filter_kv(filter):
    global in_memory_db
    result = []
    for db_key, db_value in in_memory_db.items():
        for fkey, fvalue in filter.items():
            if (fkey in db_value):
                for val in fvalue:
                    if val == db_value[fkey]:
                        result.append(db_value)
    return result


# UUID Generation
def generate_uuid():
    return str(uuid.uuid4())

'''
Students
-------
  GET
   - all students
   - single student
  POST
    - create a new student
  PUT
    - update a student
  DELETE
    - remove a student
'''
class StudentsView(HTTPMethodView):

    # return list of all students
    async def get(self, request):
        if request.args:
            data = filter_kv(request.args)
        else:
            data = list_kv()
        return json(data, status=200)

    # create a new student
    async def post(self, request):
        content = request.json
        content["id"] = generate_uuid()
        headers = {"location": "student/"+content["id"]}
        return(json(create_kv(content["id"], content),
                              headers=headers,
                              status=201))

class SingleStudentView(HTTPMethodView):

    # return single student
    async def get(self, request, id):
        data = get_kv(id)
        if 'error' in data.keys():
            status = 404
        else:
            status = 200
        return json(data, status=status)

    # update details of a student
    async def put(self, request, id):
        content = request.json
        content["id"] = id
        data = update_kv(id, content)
        if 'error' in data.keys():
            status = 404
        else:
            status = 200
        return json(update_kv(id, content))

    # delete a student
    async def delete(self, request, id):
        message = delete_kv(id)
        if message:
            status = 200
        else:
            status = 204
        return json(message, status=status)
