from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    users = [
        {
            "id": 1,
            "name": "Leanne Graham",
            "email": "Sincere@april.biz",
            "company_name": "Romaguera-Crona"
        },
        {
            "id": 2,
            "name": "Ervin Howell",
            "email": "Shanna@melissa.tv",
            "company_name": "Deckow-Crist"
        },
        {
            "id": 3,
            "name": "Clementine Bauch",
            "email": "Nathan@yesenia.net",
            "company_name": "Romaguera-Jacobson"
        }
    ]
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
