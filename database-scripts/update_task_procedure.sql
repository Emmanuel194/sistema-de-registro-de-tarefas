CREATE PROCEDURE AtualizarStatusTarefa
    @TarefaID INT,
    @Status NVARCHAR(50)
AS
BEGIN
    UPDATE Tarefas
    SET Status = @Status, 
        DataConclusao = CASE WHEN @Status = 'concluída' THEN GETDATE() ELSE NULL END
    WHERE TarefaID = @TarefaID;
END;
