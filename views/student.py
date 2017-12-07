from sanic.response import json
from sanic.views import HTTPMethodView

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
        return json({'hello': 'students'})


class SingleStudentView(HTTPMethodView):

    # return single student
    async def get(self, request, name):
        return json({'method': request.method, 'name': name})

    # create a new student
    async def post(self, request, name):
        return json({'method': request.method, 'name': name})

    # update details of a student
    async def put(self, request, name):
        return json({'method': request.method, 'name': name})

    # delete a student
    async def delete(self, request, name):
        return json({'method': request.method, 'name': name})

