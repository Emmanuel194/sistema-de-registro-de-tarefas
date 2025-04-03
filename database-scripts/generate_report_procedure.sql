CREATE PROCEDURE GerarRelatorio
AS
BEGIN
    SELECT 
        SUM(CASE WHEN Status = 'concluída' THEN 1 ELSE 0 END) AS TarefasConcluidas,
        SUM(CASE WHEN Status = 'pendente' THEN 1 ELSE 0 END) AS TarefasPendentes
    FROM Tarefas;
END;
