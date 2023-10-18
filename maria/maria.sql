/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE TABLE `cadastro` (
  `idcliente` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `telefone` varchar(45) NOT NULL,
  `tipo` varchar(45) NOT NULL,
  PRIMARY KEY (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `categoria` (
  `idcategoria` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(45) NOT NULL,
  PRIMARY KEY (`idcategoria`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `edereco` (
  `idedereco` int NOT NULL AUTO_INCREMENT,
  `cep` varchar(45) NOT NULL,
  `uf` varchar(45) NOT NULL,
  `cidade` varchar(45) NOT NULL,
  `bairro` varchar(45) NOT NULL,
  `numero` varchar(45) NOT NULL,
  `complemento` varchar(45) NOT NULL,
  `ederecocol` varchar(45) NOT NULL,
  `cliente_idcliente` int NOT NULL,
  PRIMARY KEY (`idedereco`),
  KEY `fk_edereco_cliente1_idx` (`cliente_idcliente`),
  CONSTRAINT `fk_edereco_cliente1` FOREIGN KEY (`cliente_idcliente`) REFERENCES `cadastro` (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3;

CREATE TABLE `produto` (
  `idproduto` int NOT NULL AUTO_INCREMENT,
  `nomeprod` varchar(45) NOT NULL,
  `quantidade` varchar(45) NOT NULL,
  `preco` varchar(45) NOT NULL,
  `lucro` varchar(45) NOT NULL,
  `imposto1` varchar(45) NOT NULL,
  `imposto2` varchar(45) NOT NULL,
  `imposto3` varchar(45) NOT NULL,
  `fabricante_id` int NOT NULL,
  `fornecedor_id` int NOT NULL,
  `categoria_idcategoria` int NOT NULL,
  PRIMARY KEY (`idproduto`),
  KEY `fk_produto_cliente1_idx` (`fabricante_id`),
  KEY `fk_produto_cliente2_idx` (`fornecedor_id`),
  KEY `fk_produto_categoria1_idx` (`categoria_idcategoria`),
  CONSTRAINT `fk_produto_categoria1` FOREIGN KEY (`categoria_idcategoria`) REFERENCES `categoria` (`idcategoria`),
  CONSTRAINT `fk_produto_cliente1` FOREIGN KEY (`fabricante_id`) REFERENCES `cadastro` (`idcliente`),
  CONSTRAINT `fk_produto_cliente2` FOREIGN KEY (`fornecedor_id`) REFERENCES `cadastro` (`idcliente`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;

INSERT INTO `cadastro` (`idcliente`, `nome`, `email`, `telefone`, `tipo`) VALUES
(1, 'gabriel', 'gabriel@gmail.com', '12345678', 'for');
INSERT INTO `cadastro` (`idcliente`, `nome`, `email`, `telefone`, `tipo`) VALUES
(2, 'marina', 'marina@gmail.com', '654321', 'fabr');
INSERT INTO `cadastro` (`idcliente`, `nome`, `email`, `telefone`, `tipo`) VALUES
(3, 'josé', 'jose@gmail.com', '0987654', 'clien');
INSERT INTO `cadastro` (`idcliente`, `nome`, `email`, `telefone`, `tipo`) VALUES
(4, 'maria', 'maria@gmail.com', '4567890', 'clien'),
(5, 'milena', 'milena@gmail.com', '5678900', 'clien'),
(6, 'luiza', 'luiza@gmail', '456790', 'fabri');

INSERT INTO `categoria` (`idcategoria`, `categoria`) VALUES
(1, 'sobremesa');
INSERT INTO `categoria` (`idcategoria`, `categoria`) VALUES
(2, 'salgado');
INSERT INTO `categoria` (`idcategoria`, `categoria`) VALUES
(3, 'exótica');

INSERT INTO `edereco` (`idedereco`, `cep`, `uf`, `cidade`, `bairro`, `numero`, `complemento`, `ederecocol`, `cliente_idcliente`) VALUES
(1, '7777777', 'to', 'palmas', 'papai noel', '30', '35', '2345', 3);
INSERT INTO `edereco` (`idedereco`, `cep`, `uf`, `cidade`, `bairro`, `numero`, `complemento`, `ederecocol`, `cliente_idcliente`) VALUES
(2, '222222', 'to', 'palmas', '40', '66', 'nada', 'nada', 6);
INSERT INTO `edereco` (`idedereco`, `cep`, `uf`, `cidade`, `bairro`, `numero`, `complemento`, `ederecocol`, `cliente_idcliente`) VALUES
(3, '44444', 'to', 'palmas', '20', '23', '12333', '233232', 1);
INSERT INTO `edereco` (`idedereco`, `cep`, `uf`, `cidade`, `bairro`, `numero`, `complemento`, `ederecocol`, `cliente_idcliente`) VALUES
(4, '2222', 'to', 'palmas', '20', '24', '123455', '89-090', 2),
(5, '9999', 'to', 'palmas', '20', '28', '123455', '40-090', 4),
(6, '5555', 'to', 'palmas', '20', '90', '123455', '90-090', 5);

INSERT INTO `produto` (`idproduto`, `nomeprod`, `quantidade`, `preco`, `lucro`, `imposto1`, `imposto2`, `imposto3`, `fabricante_id`, `fornecedor_id`, `categoria_idcategoria`) VALUES
(1, 'pudim', '10', '22,00', '120%', '5', '10', '15', 1, 2, 1);
INSERT INTO `produto` (`idproduto`, `nomeprod`, `quantidade`, `preco`, `lucro`, `imposto1`, `imposto2`, `imposto3`, `fabricante_id`, `fornecedor_id`, `categoria_idcategoria`) VALUES
(2, 'pudim', '10', '22,00', '120%', '5', '10', '15', 1, 2, 1);
INSERT INTO `produto` (`idproduto`, `nomeprod`, `quantidade`, `preco`, `lucro`, `imposto1`, `imposto2`, `imposto3`, `fabricante_id`, `fornecedor_id`, `categoria_idcategoria`) VALUES
(3, 'esfirra', '27', '6,00', '120%', '5', '10', '15', 1, 2, 2);
INSERT INTO `produto` (`idproduto`, `nomeprod`, `quantidade`, `preco`, `lucro`, `imposto1`, `imposto2`, `imposto3`, `fabricante_id`, `fornecedor_id`, `categoria_idcategoria`) VALUES
(4, 'surpresa', '2', '12,00', '120%', '5', '10', '5', 1, 2, 3);


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;