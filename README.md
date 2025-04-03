# Documentação

Instruções para Configurar o Ambiente de Desenvolvimento.

 1- Clone o Repositório utilizando o comando : 

 `` git clone https://github.com/Emmanuel194/sistema-de-registro-de-tarefas.git ``
 Após clonar o repositório entre no direito com comando abaixo:
 
  `` cd sistema-registro-tarefas ``

 2- Logo após o clone crie e ative o Ambiente Virtual com o comando:

 `` python -m venv venv ``
        &&
 `` venv\Scripts\activate ``
 
 3- Com ambiente virtual ativado agora instale as dependências usando:

  ``pip install -r requirements.txt ``

 4- Agora configure o banco de dados:

 Execute os scripts SQL fornecidos na pasta database-scripts para criar a tabela Tarefas e os procedimentos armazenados.

 caso queria acessar a documentação e verificar a estrutura apenas verifique o link data-base-docs.md

 [Documentação do Banco de Dados](database-docs.md)

 5- E por fim configure o Arquivo .env utilizando o modelo .envexemple fixado na pasta raiz do projeto:

 * basta renomear o exemple do arquivo e usar a estrutura ja fixada com suas configurações do seu banco de dados.

# Descrição dos Endpoints da API:

Para a disponibilização dos Endpoints, disponibilizei um workdspace no posteman onde você pode copiar esse link e colar em um navegador e vai ter acessos as API ja configuradas para teste.

`` https://app.getpostman.com/join-team?invite_code=f9b5fb38b6957f33bb933d824d009e94a63b90f05cca5e7b6dcdf0cfec023718&target_code=f4a52e8e41bb182e836ff3a932dd01d5 ``

Mas também irei deixar detalhado aqui embaixo cada API:

API Para Adicionar Nova Tarefa:

Método: POST
URL: `` http://127.0.0.1:5000/tarefas ``
BODY:  {
  "id": 1,
  "descricao": "teste1",
  "status": "pendente",
  "data_criacao": "2025-04-02"
}

API Para listar Tarefas:

Método: GET
URL: `` http://127.0.0.1:5000/tarefas ``

API Para Editar Tarefas:

Método: PUT
URL: `` http://127.0.0.1:5000/tarefas/{ID} ``
BODY: {
  "status": "concluída"
}

API Para Deletar Tarefas:

Método: DELETE
URL: `` http://127.0.0.1:5000/tarefas/{ID} ``

API Para Listar Relatorios de tarefas concluídas e pendentes:

Método: GET
URL: `` http://127.0.0.1:5000/tarefas/relatorios ``


