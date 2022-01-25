from flask import Blueprint, request, jsonify
from sqlalchemy import func
from app.models import Session
from app.models.reaction import Reaction

api = Blueprint('api', __name__)


def reactions(device):
    with Session() as session:
        rows = session.query(func.count(Reaction.id).label('total_reactions'), Reaction.project_id) \
            .filter(Reaction.deleted_at == None) \
            .group_by(Reaction.project_id) \
            .all()

        if device is None:
            return [dict(row) for row in rows]

        reacted_projects = session.query(Reaction.project_id) \
            .filter(Reaction.deleted_at == None, Reaction.device_id == device).all()

        results = []
        for row in rows:
            reacted = any(row.project_id in r1 for r1 in reacted_projects)
            results.append(dict(row, **{'reacted': reacted}))
        return results


@api.get('/reactions')
def all_reactions():
    """ Get all reactions grouped by project
    """
    return {"reactions": reactions(None)}


@api.get('/reactions/<device>')
def fetch_reactions(device):
    """ Get reactions and status of device reaction on each project
    """
    return {'reactions': reactions(device)}


@api.post('/reactions/<project>')
def save_reaction(project):
    """ Store device reaction
    """
    if request.form.get('device_id') is None and request.json.get('device_id') is None:
        return {'error': 'Device identifier missing'}, 400

    device_id = request.form.get('device_id') or request.json.get('device_id')

    exists = Reaction.first(deleted_at=None, device_id=device_id)
    if exists is not None:
        return {'error': 'Reaction already exists'}, 422

    reaction = Reaction()
    reaction.device_id = device_id
    reaction.project_id = project
    reaction.save()
    return {'reactions': reactions(device_id)}


@api.delete('/reactions/<project>')
def destroy_reaction(project):
    """Soft delete reaction
    """
    if request.form.get('device_id') is None and request.json.get('device_id') is None:
        return {'error': 'Device identifier missing'}, 400

    device_id = request.form.get('device_id') or request.json.get('device_id')

    reaction = Reaction.first(device_id=device_id, project_id=project, deleted_at=None)
    if reaction is None:
        return {'error': 'Not found'}, 404

    reaction.deleted_at = func.now()
    reaction.update()
    return {'reactions': reactions(device_id)}
