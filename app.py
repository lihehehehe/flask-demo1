from flask import Flask, jsonify, make_response, app, request
from flask_restful import abort, Resource, Api

app = Flask(__name__)
api = Api(app)
app.config["testcase"] = []


class TestCaseServer(Resource):

    #按照用例名称读取用例
    def get(self):
        name = request.args["name"]
        testcase = app.config["testcase"]
        for case in testcase:
            if case['name'] == name:
                return {"result": "ok", "errcode": 0, "data": case}
        return {"result": "ok", "errcode": 0}

    #上传测试用例
    def post(self):
        testcase = app.config["testcase"]
        testcase.append(request.json)
        return {"result": "ok", "errcode": 0}


api.add_resource(TestCaseServer, "/testcase")


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
