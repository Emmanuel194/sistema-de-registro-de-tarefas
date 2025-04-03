CREATE PROCEDURE AdicionarTarefa
    @Descricao NVARCHAR(255),
    @Status NVARCHAR(50)
AS
BEGIN
    INSERT INTO Tarefas (Descricao, Status, DataCriacao)
    VALUES (@Descricao, @Status, GETDATE());
END;
