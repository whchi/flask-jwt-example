from flask import request
from ..database.models import AppAccount
from flask_restful import Resource
import datetime
from flask_jwt_extended import create_access_token


class JwtApi(Resource):

    def post(self):
        """
            get jwt token
        """
        try:
            body = request.get_json()
            app = AppAccount.objects.get(account=body.get('account'))
            authorized = app.check_password(body.get('password'))
            if not authorized:
                return {'error': 'account or password invalid'}, 401

            expires = datetime.timedelta(days=365)
            access_token = create_access_token(identity=str(app.id),
                                               expires_delta=expires)
            return {'token': access_token}, 200
        except Exception as e:
            return {'error': str(e)}, 400
