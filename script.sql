-- criar detabase `escola_db`
create DATABASE 'escola_db';

-- criar tabela `tb_alunos`
create table 'tb_alunos' (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(150) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    senha VARCHAR(19) NOT NULL,
    telefone VARCHAR(14);
    data_nasc DATETIME
);