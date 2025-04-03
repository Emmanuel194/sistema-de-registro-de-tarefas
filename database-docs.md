# Documentação do Banco de Dados


Tabela: Tarefas

A tabela Tarefas é responsável por armazenar todas as informações relacionadas às tarefas do sistema.


### Estrutura da Tabela: `Tarefas`
| Nome da Coluna    | Tipo de Dados      | Descrição                                   |
|--------------------|--------------------|-------------------------------------------|
| **TarefaID**       | `INT`             | Identificador único da tarefa (chave primária). |
| **Descricao**      | `NVARCHAR(255)`   | Descrição detalhada da tarefa.             |
| **Status**         | `NVARCHAR(50)`    | Status da tarefa (`pendente` ou `concluida`). |
| **DataCriacao**    | `DATETIME`        | Data em que a tarefa foi criada.           |
| **DataConclusao**  | `DATETIME`        | Data de conclusão da tarefa (nulo para tarefas pendentes). |

1. Adicionar Nova Tarefa
Nome do Procedimento: AdicionarTarefa

Parâmetros de Entrada:
@Descricao (NVARCHAR(255)) - Descrição da tarefa.
@Status (NVARCHAR(50)) - Status inicial da tarefa

SQL do Procedimento:

``CREATE PROCEDURE AdicionarTarefa
    @Descricao NVARCHAR(255),
    @Status NVARCHAR(50)
AS
BEGIN
    INSERT INTO Tarefas (Descricao, Status, DataCriacao)
    VALUES (@Descricao, @Status, GETDATE());
END;``

2. Atualizar Status de Tarefa:

Parâmetros de Entrada:
@TarefaID (INT) - Identificador único da tarefa.
@Status (NVARCHAR(50)) - Novo status da tarefa.

SQL do Procedimento:

``CREATE PROCEDURE AtualizarStatusTarefa
    @TarefaID INT,
    @Status NVARCHAR(50)
AS
BEGIN
    UPDATE Tarefas
    SET Status = @Status, 
        DataConclusao = CASE WHEN @Status = 'concluida' THEN GETDATE() ELSE NULL END
    WHERE TarefaID = @TarefaID;
END;``


3. Gerar Relatório de Tarefas
descrição: este procedimento gera um relatório contendo todas as tarefas, separando-as por status (pendente ou concluida).
Parâmetros de Entrada: Nenhum.

SQL do Procedimento:

``CREATE PROCEDURE GerarRelatorio
AS
BEGIN
    SELECT 
        SUM(CASE WHEN Status = 'concluída' THEN 1 ELSE 0 END) AS TarefasConcluidas,
        SUM(CASE WHEN Status = 'pendente' THEN 1 ELSE 0 END) AS TarefasPendentes
    FROM Tarefas;
END;``

Como Usar os Scripts SQL
Localização dos Arquivos:

Os scripts SQL necessários para criar a tabela e os procedimentos armazenados estão localizados na pasta database-scripts do projeto localizada na raiz do projeto.

Execução dos Scripts:
1-Abra o SQL Server Management Studio (SSMS).
2-Conecte-se ao seu servidor SQL.
3-Execute os scripts na seguinte ordem:
4-Criar tabela: create_table.sql
5-Adicionar Procedimento: add_task_procedure.sql
6-Atualizar Procedimento: update_task_procedure.sql
7-Gerar Relatório: generate_report_procedure.sql


