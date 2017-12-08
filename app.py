from sanic import Sanic
from views.student import StudentsView, SingleStudentView

app = Sanic()

if __name__ == "__main__":

    # API routing for students
    app.add_route(StudentsView.as_view(), '/students')
    app.add_route(SingleStudentView.as_view(), '/students/<id>')

    app.run(host='0.0.0.0', port=8000)
