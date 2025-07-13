from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import Prompt
from  utils.groqai_service import askGroqAI

prompt_groqai_bp = Blueprint('prompt_groq', __name__)

@prompt_groqai_bp.route('prompt', methods=['POST'])
@jwt_required()
def create_prompt():
    data = request.get_json()
    user_id = get_jwt_identity()
    response = askGroqAI(data['prompt'])
    new_prompt = Prompt(user_id=user_id, prompt=data['prompt'], response=response)
    db.session.add(new_prompt)
    db.session.commit()
    return jsonify(id=new_prompt.id, prompt=new_prompt.prompt, response=new_prompt.response)



@prompt_groqai_bp.route('/prompt/<int:id>', methods=['PUT'])
@jwt_required()
def update_prompt(id):
    data = request.get_json()
    prompt = Prompt.query.get_or_404(id)
    if prompt.user_id != int(get_jwt_identity()):
        return jsonify(msg='Unauthorized'), 403
    prompt.prompt = data['prompt']
    prompt.response = askGroqAI(data['prompt'])
    db.session.commit()
    return jsonify(msg='Prompt updated')

