-- =======================================================================
-- SCRIPT DE CRIAÇÃO DO BANCO DE DADOS E TABELA - SISTEMA ESTODOLIST
-- Este script cria o banco de dados "estodolist" e a tabela "tarefa"
-- =======================================================================

-- Apaga o banco de dados "estodolist" caso ele já exista
-- Isso evita erro de "banco de dados já existe" ao rodar o script novamente
/* DROP DATABASE IF EXISTS estodolist; */

-- Cria o banco de dados chamado "estodolist"
-- IF NOT EXISTS impede erro caso o banco já tenha sido criado anteriormente
/* CREATE DATABASE IF NOT EXISTS estodolist; */

-- Seleciona o banco de dados "estodolist" para uso nas operações seguintes
-- Todos os comandos CREATE TABLE, INSERT, etc. serão aplicados a este banco
USE estodolist;

-- -----------------------------------------------------------------------
-- Criação da tabela TAREFA
-- Esta tabela armazena todas as informações das tarefas do sistema
-- -----------------------------------------------------------------------
CREATE TABLE tarefa (
    -- Identificador único de cada tarefa (chave primária)
    -- AUTO_INCREMENT faz o MySQL gerar automaticamente o próximo ID (1, 2, 3, ...)
    idTarefa INT PRIMARY KEY AUTO_INCREMENT,

    -- Nome da tarefa (obrigatório, não pode ser nulo)
    -- VARCHAR(30) armazena até 30 caracteres de texto variável
    nomeTarefa VARCHAR(30) NOT NULL,

    -- Descrição detalhada da tarefa (opcional, pode ser nula)
    -- VARCHAR(100) armazena até 100 caracteres
    descricao VARCHAR(100),

    -- Categoria da tarefa (ex: Trabalho, Estudo, Pessoal)
    -- Obrigatório, não pode ser nulo
    categoria VARCHAR(30) NOT NULL,

    -- Data de prazo para conclusão da tarefa
    -- Tipo DATE armazena data no formato AAAA-MM-DD (ano-mês-dia)
    -- Obrigatório, não pode ser nulo
    dataPrazo DATE NOT NULL,

    -- Prioridade da tarefa: ALTA, MEDIA ou BAIXA
    -- ENUM restringe o valor a apenas estas três opções
    -- Obrigatório, não pode ser nulo
    prioridade ENUM('ALTA', 'MEDIA', 'BAIXA') NOT NULL,

    -- Status da tarefa: Pendente, Concluida ou Não Realizada
    -- Valor padrão é 'Pendente' quando uma nova tarefa é inserida
    status ENUM('Pendente', 'Concluida', 'Não Realizada') DEFAULT 'Pendente'
);

-- Fim do script
-- Após executar este script no MySQL, o banco estará pronto para uso pelo app.py
-- =======================================================================