from flask import Flask, jsonify
from flask import request
app = Flask(__name__)
todos = [
    { "label": "My first task", "done": False },
    
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    #return "<h1>Hello!</h1>"
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("todos antes de la actualizacion", todos)
    todos.append(request_body)
    print("todos despues de la actualizacion", todos)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    """
    Elimina la tarea en la posición especificada de la lista de tareas.

    Args:
        position: La posición de la tarea a eliminar.

    Returns:
        El jsonify de la lista de tareas actualizada.
    """

    # Elimina la tarea de la lista.
    todos.pop(position)

    # Retorna el jsonify de la lista de tareas actualizada.
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)