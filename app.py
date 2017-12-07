from sanic import Sanic
from views.student import StudentsView, SingleStudentView
from views.department import DepartmentsView, SingleDepartmentView

app = Sanic()

if __name__ == "__main__":

    # API routing for students
    app.add_route(StudentsView.as_view(), '/students')
    app.add_route(SingleStudentView.as_view(), '/student/<name>')

    # API routing for departments
    app.add_route(DepartmentsView.as_view(), '/departments')
    app.add_route(SingleDepartmentView.as_view(), '/department/<name>')
 
    app.run(host='0.0.0.0', port=8000)
