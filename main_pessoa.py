from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

# Criando uma instância da classe Pessoa
pessoa = Pessoa("Joao Rafael", 123456789, "2014-04-14", True)
pessoa.nome = "Jose"
pessoa.imprimir_informacoes()

# Criando uma instância da classe PessoaFisica
pessoa_fisica = PessoaFisica("Ana Lucia", 987654321, "2016-04-17", True, "1990-01-01", "12345678901", "123456789")
pessoa_fisica.nome = "Josiane"
pessoa_fisica.imprimir_informacoes()

# Criando uma instância da classe PessoaJuridica
pessoa_juridica = PessoaJuridica("Silva e Uchoa", 876543210, "2023-01-01", True, "2000-01-01", "12.345.678/0001-99")
pessoa_juridica.nome = "IMAP"
pessoa_juridica.imprimir_informacoes()