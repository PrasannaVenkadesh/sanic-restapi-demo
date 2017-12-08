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
        return {"id": key, "status": "deleted"}
    else:
        return {"error": "key not found"}

def get_kv(key):
    global in_memory_db
    if key in in_memory_db and in_memory_db[key]:
        return in_memory_db[key]
    else:
        return {"error": "key not found"}


def list_kv():
    result = []
    for key, val in in_memory_db.items():
        if val:
            result.append(val)
    return result

def filter_kv(filter):
    result = []


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
        print(request.url)
        print(request.query_string)
        print(request.args)
        print(raw.args)        
        return json(list_kv())

    # create a new student
    async def post(self, request):
        content = request.json
        content["id"] = generate_uuid()
        return(json(create_kv(content["id"], content)))

class SingleStudentView(HTTPMethodView):

    # return single student
    async def get(self, request, id):
        return json(get_kv(id))

    # update details of a student
    async def put(self, request, id):
        content = request.json
        content["id"] = id
        return json(update_kv(id, content))

    # delete a student
    async def delete(self, request, id):
        return json(delete_kv(id))