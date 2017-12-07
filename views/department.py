from sanic.response import json
from sanic.views import HTTPMethodView

'''
Department
-----
  GET
   - all departments
   - single department
  POST
    - create a new department
  PUT
    - update a department
  DELETE
    - remove a department

'''
class DepartmentsView(HTTPMethodView):

    # return list of all departments
    async def get(self, request):
        return json({'hello': 'departments'})


class SingleDepartmentView(HTTPMethodView):

    # return single department
    async def get(self, request, name):
        return json({'method': request.method, 'name': name})

    # create a new department
    async def post(self, request, name):
        return json({'method': request.method, 'name': name})

    # update details of a department
    async def put(self, request, name):
        return json({'method': request.method, 'name': name})

    # delete a department
    async def delete(self, request, name):
        return json({'method': request.method, 'name': name})

