-- Gerado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   em:        2024-03-16 16:11:43 BRT
--   site:      Oracle Database 21c
--   tipo:      Oracle Database 21c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE classificacao (
    idclassificacao NUMBER NOT NULL,
    dsclassificacao VARCHAR2(100) NOT NULL
);

ALTER TABLE classificacao ADD CONSTRAINT classificacao_pk PRIMARY KEY ( idclassificacao );

CREATE TABLE ctengate (
    id                NUMBER NOT NULL,
    dtengate          DATE NOT NULL,
    dtdesengate       DATE,
    veiculo_idveiculo NUMBER NOT NULL,
    nrfrota           NUMBER(5) NOT NULL,
    nrconjunto        NUMBER(5) NOT NULL
);

ALTER TABLE ctengate ADD CONSTRAINT ctengate_pk PRIMARY KEY ( id );

CREATE TABLE ctvinculo (
    id                    NUMBER NOT NULL,
    dtvinculo             DATE NOT NULL,
    dtdesvinculo          DATE,
    motorista_idmotorista NUMBER NOT NULL,
    veiculo_idveiculo     NUMBER NOT NULL,
    nrfrota               NUMBER(5) NOT NULL
);

ALTER TABLE ctvinculo ADD CONSTRAINT ctvinculo_pk PRIMARY KEY ( id );

CREATE TABLE endereco (
    idendereco            NUMBER NOT NULL,
    dslogradouro          VARCHAR2(200) NOT NULL,
    nrcasa                NUMBER NOT NULL,
    nmbairro              VARCHAR2(100) NOT NULL,
    nrcep                 NUMBER(8) NOT NULL,
    municipio_cdmunicipio NUMBER NOT NULL,
    pessoa_idpessoa       NUMBER NOT NULL
);

ALTER TABLE endereco ADD CONSTRAINT endereco_pk PRIMARY KEY ( idendereco );

CREATE TABLE funcionario (
    nrmatricula     NUMBER NOT NULL,
    nmfuncionario   VARCHAR2(100) NOT NULL,
    dsfuncao        VARCHAR2(100) NOT NULL,
    dtadmissao      DATE NOT NULL,
    pessoa_idpessoa NUMBER NOT NULL
);

ALTER TABLE funcionario ADD CONSTRAINT funcionario_pk PRIMARY KEY ( nrmatricula );

CREATE TABLE motorista (
    idmotorista             NUMBER NOT NULL,
    nmmotorista             VARCHAR2(100) NOT NULL,
    funcionario_nrmatricula NUMBER NOT NULL
);

ALTER TABLE motorista ADD CONSTRAINT motorista_pk PRIMARY KEY ( idmotorista );

CREATE TABLE municipio (
    cdmunicipio NUMBER NOT NULL,
    nmmunicipio VARCHAR2(100) NOT NULL,
    uf_cduf     NUMBER NOT NULL
);

ALTER TABLE municipio ADD CONSTRAINT municipio_pk PRIMARY KEY ( cdmunicipio );

CREATE TABLE operador (
    idoperador              NUMBER NOT NULL,
    nmoperador              VARCHAR2(100) NOT NULL,
    funcionario_nrmatricula NUMBER NOT NULL
);

ALTER TABLE operador ADD CONSTRAINT operador_pk PRIMARY KEY ( idoperador );

CREATE TABLE pessoa (
    idpessoa     NUMBER NOT NULL,
    nmpessoa     VARCHAR2(100) NOT NULL,
    nrcpf        NUMBER(11) NOT NULL,
    dtnascimento DATE NOT NULL
);

ALTER TABLE pessoa ADD CONSTRAINT pessoa_pk PRIMARY KEY ( idpessoa );

CREATE TABLE tpveiculo (
    idtpveiculo NUMBER NOT NULL,
    dstpveiculo VARCHAR2(100) NOT NULL
);

ALTER TABLE tpveiculo ADD CONSTRAINT tpveiculo_pk PRIMARY KEY ( idtpveiculo );

CREATE TABLE uf (
    cduf    NUMBER NOT NULL,
    nmuf    VARCHAR2(100) NOT NULL,
    dssigla CHAR(2) NOT NULL
);

ALTER TABLE uf ADD CONSTRAINT uf_pk PRIMARY KEY ( cduf );

CREATE TABLE veiculo (
    idveiculo                     NUMBER NOT NULL,
    nrplaca                       CHAR(7) NOT NULL,
    dsmodelo                      VARCHAR2(100) NOT NULL,
    tptracao                      VARCHAR2(40) NOT NULL,
    nrrenavam                     NUMBER(11) NOT NULL,
    dtaquisicao                   DATE NOT NULL,
    nrfrota                       NUMBER(5),
    nrconjunto                    NUMBER(5),
    nrchassi                      VARCHAR2(17) NOT NULL,
    tpcombustivel                 VARCHAR2(100),
    anoveic                       DATE NOT NULL,
    dsmarca                       VARCHAR2(100) NOT NULL,
    qteixo                        NUMBER NOT NULL,
    tpveiculo_idtpveiculo         NUMBER NOT NULL,
    classificacao_idclassificacao NUMBER NOT NULL,
    veiculo_idveiculo             NUMBER
);

ALTER TABLE veiculo ADD CONSTRAINT veiculo_pk PRIMARY KEY ( idveiculo );

ALTER TABLE ctengate
    ADD CONSTRAINT ctengate_veiculo_fk FOREIGN KEY ( veiculo_idveiculo )
        REFERENCES veiculo ( idveiculo );

ALTER TABLE ctvinculo
    ADD CONSTRAINT ctvinculo_motorista_fk FOREIGN KEY ( motorista_idmotorista )
        REFERENCES motorista ( idmotorista );

ALTER TABLE ctvinculo
    ADD CONSTRAINT ctvinculo_veiculo_fk FOREIGN KEY ( veiculo_idveiculo )
        REFERENCES veiculo ( idveiculo );

ALTER TABLE endereco
    ADD CONSTRAINT endereco_municipio_fk FOREIGN KEY ( municipio_cdmunicipio )
        REFERENCES municipio ( cdmunicipio );

ALTER TABLE endereco
    ADD CONSTRAINT endereco_pessoa_fk FOREIGN KEY ( pessoa_idpessoa )
        REFERENCES pessoa ( idpessoa );

ALTER TABLE funcionario
    ADD CONSTRAINT funcionario_pessoa_fk FOREIGN KEY ( pessoa_idpessoa )
        REFERENCES pessoa ( idpessoa );

ALTER TABLE motorista
    ADD CONSTRAINT motorista_funcionario_fk FOREIGN KEY ( funcionario_nrmatricula )
        REFERENCES funcionario ( nrmatricula );

ALTER TABLE municipio
    ADD CONSTRAINT municipio_uf_fk FOREIGN KEY ( uf_cduf )
        REFERENCES uf ( cduf );

ALTER TABLE operador
    ADD CONSTRAINT operador_funcionario_fk FOREIGN KEY ( funcionario_nrmatricula )
        REFERENCES funcionario ( nrmatricula );

ALTER TABLE veiculo
    ADD CONSTRAINT veiculo_classificacao_fk FOREIGN KEY ( classificacao_idclassificacao )
        REFERENCES classificacao ( idclassificacao );

ALTER TABLE veiculo
    ADD CONSTRAINT veiculo_tpveiculo_fk FOREIGN KEY ( tpveiculo_idtpveiculo )
        REFERENCES tpveiculo ( idtpveiculo );

ALTER TABLE veiculo
    ADD CONSTRAINT veiculo_veiculo_fk FOREIGN KEY ( veiculo_idveiculo )
        REFERENCES veiculo ( idveiculo );

CREATE SEQUENCE classificacao_idclassificacao START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER classificacao_idclassificacao BEFORE
    INSERT ON classificacao
    FOR EACH ROW
    WHEN ( new.idclassificacao IS NULL )
BEGIN
    :new.idclassificacao := classificacao_idclassificacao.nextval;
END;
/

CREATE SEQUENCE ctengate_id_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctengate_id_trg BEFORE
    INSERT ON ctengate
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := ctengate_id_seq.nextval;
END;
/

CREATE SEQUENCE ctvinculo_id_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER ctvinculo_id_trg BEFORE
    INSERT ON ctvinculo
    FOR EACH ROW
    WHEN ( new.id IS NULL )
BEGIN
    :new.id := ctvinculo_id_seq.nextval;
END;
/

CREATE SEQUENCE endereco_idendereco_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER endereco_idendereco_trg BEFORE
    INSERT ON endereco
    FOR EACH ROW
    WHEN ( new.idendereco IS NULL )
BEGIN
    :new.idendereco := endereco_idendereco_seq.nextval;
END;
/

CREATE SEQUENCE funcionario_nrmatricula_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER funcionario_nrmatricula_trg BEFORE
    INSERT ON funcionario
    FOR EACH ROW
    WHEN ( new.nrmatricula IS NULL )
BEGIN
    :new.nrmatricula := funcionario_nrmatricula_seq.nextval;
END;
/

CREATE SEQUENCE motorista_idmotorista_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER motorista_idmotorista_trg BEFORE
    INSERT ON motorista
    FOR EACH ROW
    WHEN ( new.idmotorista IS NULL )
BEGIN
    :new.idmotorista := motorista_idmotorista_seq.nextval;
END;
/

CREATE SEQUENCE municipio_cdmunicipio_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER municipio_cdmunicipio_trg BEFORE
    INSERT ON municipio
    FOR EACH ROW
    WHEN ( new.cdmunicipio IS NULL )
BEGIN
    :new.cdmunicipio := municipio_cdmunicipio_seq.nextval;
END;
/

CREATE SEQUENCE operador_idoperador_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER operador_idoperador_trg BEFORE
    INSERT ON operador
    FOR EACH ROW
    WHEN ( new.idoperador IS NULL )
BEGIN
    :new.idoperador := operador_idoperador_seq.nextval;
END;
/

CREATE SEQUENCE pessoa_idpessoa_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER pessoa_idpessoa_trg BEFORE
    INSERT ON pessoa
    FOR EACH ROW
    WHEN ( new.idpessoa IS NULL )
BEGIN
    :new.idpessoa := pessoa_idpessoa_seq.nextval;
END;
/

CREATE SEQUENCE tpveiculo_idtpveiculo_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER tpveiculo_idtpveiculo_trg BEFORE
    INSERT ON tpveiculo
    FOR EACH ROW
    WHEN ( new.idtpveiculo IS NULL )
BEGIN
    :new.idtpveiculo := tpveiculo_idtpveiculo_seq.nextval;
END;
/

CREATE SEQUENCE uf_cduf_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER uf_cduf_trg BEFORE
    INSERT ON uf
    FOR EACH ROW
    WHEN ( new.cduf IS NULL )
BEGIN
    :new.cduf := uf_cduf_seq.nextval;
END;
/

CREATE SEQUENCE veiculo_idveiculo_seq START WITH 1 NOCACHE ORDER;

CREATE OR REPLACE TRIGGER veiculo_idveiculo_trg BEFORE
    INSERT ON veiculo
    FOR EACH ROW
    WHEN ( new.idveiculo IS NULL )
BEGIN
    :new.idveiculo := veiculo_idveiculo_seq.nextval;
END;
/



-- Relat�rio do Resumo do Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            12
-- CREATE INDEX                             0
-- ALTER TABLE                             24
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                          12
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                         12
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
