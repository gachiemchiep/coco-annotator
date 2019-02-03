from flask_restplus import Namespace, Resource, reqparse
from flask_login import login_required, current_user

from ..config import Config
from ..models import TaskModel


api = Namespace('tasks', description='Task related operations')


@api.route('/')
class Info(Resource):
    @login_required
    def get(self):
        """ Returns all tasks """
        return {}
        

