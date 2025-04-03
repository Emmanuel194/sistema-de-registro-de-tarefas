from flask import Blueprint, request, jsonify
from db import get_connection



routes = Blueprint("routes", __name__)


tarefas = []


@routes.route("/tarefas", methods=["POST"])
def adicionar_tarefa():
    nova_tarefa = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC AdicionarTarefa ?, ?", nova_tarefa['descricao'], nova_tarefa['status'])
    conn.commit()
    conn.close()
    return jsonify({"message": "Tarefa adicionada com sucesso!", "tarefa": nova_tarefa}), 201



@routes.route("/tarefas", methods=["GET"])
def listar_tarefas():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    tarefas_formatadas = [
        {
            "id": tarefa.TarefaID,
            "descricao": tarefa.Descricao,
            "status": tarefa.Status,
            "data_criacao": tarefa.DataCriacao,
            "data_conclusao": tarefa.DataConclusao,
        }
        for tarefa in tarefas
    ]
    return jsonify(tarefas_formatadas), 200



@routes.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefa(tarefa_id):
    dados = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC AtualizarStatusTarefa ?, ?", tarefa_id, dados["status"])
    conn.commit()
    conn.close()
    return jsonify({"message": "Tarefa atualizada com sucesso!"}), 200



@routes.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def deletar_tarefa(tarefa_id):
    conn = get_connection()  
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Tarefas WHERE TarefaID = ?", tarefa_id)  
    conn.close()
    return jsonify({"message": "Tarefa deletada com sucesso!"}), 200



@routes.route("/tarefas/relatorios", methods=["GET"])
def gerar_relatorio():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC GerarRelatorio")
    relatorio = cursor.fetchone()
    conn.close()
    return jsonify({
        "tarefas_concluidas": relatorio[0],
        "tarefas_pendentes": relatorio[1]
    }), 200


