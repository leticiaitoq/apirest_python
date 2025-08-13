from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados de exemplo (pode ser substituído por um banco de dados)
items = [
        {"id": 1, "name": "Item A", "description": "Descrição do Item A"},
        {"id": 2, "name": "Item B", "description": "Descrição do Item B"},
]

# Rota para obter todos os itens
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Rota para obter um item específico por ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para adicionar um novo item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    if not new_item or 'name' not in new_item:
        return jsonify({"message": "Dados inválidos"}), 400
        
    # Atribui um novo ID (simples, para exemplo)
    new_item['id'] = len(items) + 1 
    items.append(new_item)
    return jsonify(new_item), 201

# Rota para atualizar um item existente
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item_data = request.json
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item.update(item_data)
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para deletar um item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items # Permite modificar a lista global
    original_len = len(items)
    items = [item for item in items if item['id'] != item_id]
    if len(items) < original_len:
        return jsonify({"message": "Item deletado com sucesso"}), 200
    return jsonify({"message": "Item não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True) # debug=True para desenvolvimento
 \