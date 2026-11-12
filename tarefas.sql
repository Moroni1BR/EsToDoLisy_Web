/* Script para inserir tarefas no seu banco de dados: */
INSERT INTO tarefa (nomeTarefa, descricao, categoria,
                    dataPrazo, prioridade, status)
VALUES
('Trabalho de História',
'Capítulo 4 e resumo de 2 páginas',
'Escola', '2026-12-10', 'ALTA', 'Pendente'),

('Prova de Matemática',
 'Estudar funções do 1º e 2º grau e resolver exercícios',
 'Escola', '2026-12-15', 'ALTA', 'Pendente'),

('Projeto de Desenvolvimento Web',
 'Finalizar o layout da página inicial e revisar o CSS',
 'Curso', '2026-12-18', 'ALTA', 'Pendente'),

('Leitura de Literatura',
 'Ler os capítulos 5 a 8 e elaborar um fichamento',
 'Escola', '2026-12-20', 'MEDIA', 'Pendente'),

('Organizar materiais de estudo',
 'Separar anotações, revisar conteúdos e organizar arquivos',
 'Pessoal', '2026-12-22', 'BAIXA', 'Pendente');

SELECT * FROM tarefa;