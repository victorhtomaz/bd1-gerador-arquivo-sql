CREATE DATABASE IF NOT EXISTS Loja; 
USE Loja; 

CREATE TABLE IF NOT EXISTS Clientes(
    Cliente_id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(80) NOT NULL,
    Email VARCHAR(150) NOT NULL,
    Telefone VARCHAR(50) NOT NULL,
    Endereco TEXT NOT NULL
);
INSERT INTO Clientes (Nome, Email, Telefone, Endereco) VALUES
	('William Bishop', 'urogers@example.net', '+1-534-945-1544', '458 Woods Fields, Hunterstad, CA 97369'),
	('Kimberly Richmond', 'ricky71@example.net', '600-720-6295', '21512 Allen Flat, West Blake, KS 08302'),
	('Amber Watson', 'lewismelissa@example.net', '(257)439-0122x2281', 'PSC 0999, Box 9206, APO AE 55962'),
	('Nicholas Leonard', 'brandonfisher@example.org', '9886005718', '01303 Michelle Green, North Jose, FL 13224');

CREATE TABLE IF NOT EXISTS Produtos(
    Produto_id INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Descricao TEXT NOT NULL,
    Preco FLOAT NOT NULL,
    Estoque INT NOT NULL
);
INSERT INTO Produtos (Nome, Descricao, Preco, Estoque) VALUES
	('See', 'Town can father act state while.', 252.82, 69),
	('Check', 'Suffer rest little church.', 31.07, 57),
	('Treat', 'International long detail explain available continue over.', 468.48, 55),
	('Develop', 'Ten today be middle north thing prove.', 311.55, 92);

CREATE TABLE IF NOT EXISTS Pedidos(
    Pedido_id INT AUTO_INCREMENT PRIMARY KEY,
    Cliente_id INT NOT NULL,
    Data_pedido DATETIME NOT NULL,
    Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (Cliente_id) REFERENCES Clientes(Cliente_id)
);
INSERT INTO Pedidos (Cliente_id, Data_pedido, Status) VALUES
	(2, '2025-03-07 22:35:11.539854', 'Pendente'),
	(1, '2025-01-20 08:30:08.080866', 'Pendente'),
	(2, '2025-03-24 00:59:43.778200', 'Cancelado'),
	(3, '2025-02-24 20:15:19.120196', 'Entregue');

CREATE TABLE IF NOT EXISTS Itens_Pedidos(
    Item_id INT AUTO_INCREMENT PRIMARY KEY,
    Pedido_id INT NOT NULL,
    Produto_id INT NOT NULL,
    Quantidade SMALLINT NOT NULL,
    Preco_unitario FLOAT NOT NULL,
    FOREIGN KEY (Pedido_id) REFERENCES Pedidos(Pedido_id),
    FOREIGN KEY (Produto_id) REFERENCES Produtos(Produto_id)
);
INSERT INTO Itens_Pedidos (Pedido_id, Produto_id, Quantidade, Preco_unitario) VALUES
	(1, 1, 3, 133.75),
	(2, 1, 2, 32.28),
	(3, 4, 5, 439.36),
	(3, 4, 4, 149.07);

