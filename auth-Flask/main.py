from flask import Flask , request, jsonify
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    create_refresh_token
)
USERENAME = "admin"
PASSWORD = "1234"
app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = "abrar1245"
jwt = JWTManager(app)
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username == USERENAME and password == PASSWORD:
        access_token = create_access_token(identity=username)
        refresh_token = create_refresh_token(identity=username)
        return jsonify({
            'status': 'success' ,
            'data': {
                'access_token': access_token,
                'refresh_token': refresh_token

            }
        })
    return jsonify({
        'satatus':'fail',
        'msg': 'invalid username or password'
    })
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    username = get_jwt_identity()
    return jsonify({
            'status': 'success',
            'msg': f"welcome {username}"
        })
@app.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh():
    username = get_jwt_identity()
    access_token = create_access_token(identity=username)

    return jsonify({
        'access_token': access_token
    })










@app.route('/')
def hello_world():
    return 'Hello World!'