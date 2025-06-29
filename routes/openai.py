from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import Prompt
from  utils.openai_service import ask_mistralai

prompt_bp = Blueprint('prompt', __name__)

@prompt_bp.route('prompt', methods=['POST'])
@jwt_required()
def create_prompt():
    data = request.get_json()
    user_id = get_jwt_identity()
    response = ask_mistralai(data['prompt'])
    new_prompt = Prompt(user_id=user_id, prompt=data['prompt'], response=response)
    db.session.add(new_prompt)
    db.session.commit()
    return jsonify(id=new_prompt.id, prompt=new_prompt.prompt, response=new_prompt.response)

@prompt_bp.route('/prompt', methods=['GET'])
@jwt_required()
def get_prompt():
    user_id = get_jwt_identity()
    prompts = Prompt.query.filter_by(user_id = user_id).all()
    return jsonify([
        {
            'id':p.id,
            'prompt':p.prompt,
            'response' : p.response
        } for p in prompts
    ])

@prompt_bp.route('/prompt/<int:id>', methods=['PUT'])
@jwt_required()
def update_prompt(id):
    data = request.get_json()
    prompt = Prompt.query.get_or_404(id)
    if prompt.user_id != int(get_jwt_identity()):
        return jsonify(msg='Unauthorized'), 403
    prompt.prompt = data['prompt']
    prompt.response = ask_mistralai(data['prompt'])
    db.session.commit()
    return jsonify(msg='Prompt updated')

@prompt_bp.route('/prompt/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_prompt(id):
    prompt = Prompt.query.get_or_404(id)
    if prompt.user_id != int(get_jwt_identity()):
        return jsonify(msg='Unauthorized'), 403
    db.session.delete(prompt)
    db.session.commit()
    return jsonify(msg='Prompt Deleted')