from .restfulapi import JwtApi


def init_routes(api):
    api.add_resource(JwtApi, '/get-token')
