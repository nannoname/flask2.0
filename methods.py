from flask import Flask, request, jsonify

app = Flask(__name__)

db_users = []

# http://lockalhost:3005/user
@app.route('/user', methods=['get', 'post'])
def career():
    if request.method == 'GET':
        return db_users, 200
    if request.method == 'POST':
        data = request.json
        if(data==False and []):
            return "Данные не заполнены", 403
        if(data["name"]==''):
            return "Имя не заполнено", 403
        
        db_users.append(data["name"])
        db_users.append(data["email"])
        db_users.append(data["password"])

        return "Пользователь добавлен", 200

    return jsonify(data)

# @app.route('/user/<id>/', methods=['put', 'delite'])
# def career():
#     if request.method == 'PUT':
#         data = request.json()
#     if request.method == 'DELITE':
#         try:
#             db_users.pop(id)
#             return "Пользователь удален", 200
#         except:
#             return "Ошибка операции", 403
    
if __name__ == "__main__":
    app.run()
