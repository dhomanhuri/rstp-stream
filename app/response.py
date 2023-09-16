from flask import jsonify, make_response,render_template


def success(values, message):
    res = {
        'data': values,
        'message': message
    }
    return make_response(jsonify(res)), 200


def badRequest(values, message):
    res = {
        'data': values,
        'message': message
    }
    return make_response(jsonify(res)), 400

# def successPage(values, message):
#     res = {
#         'data': values,
#         'message': message
#     }
#     return render_template("cam1.html", menu='master', submenu='cam1', data=data)

