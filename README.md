Projeto de sistemas de gestão de hotel
Autor: Gabriel Gomes


Descrição do Projeto
O HotelGest é uma aplicação de consola desenvolvida em Python, focada na automatização de processos fundamentais de uma unidade hoteleira. O sistema utiliza os princípios de Programação Orientada a Objetos (POO) para gerir de forma eficiente a interação entre clientes, quartos e o registo de estadias.

Este projeto foi desenhado para ser modular, facilitando a manutenção e a escalabilidade, permitindo que cada componente (Cliente, Quarto e Reserva) funcione de forma independente mas integrada.

Funções Principais
O sistema está dividido em quatro módulos principais, cada um com as seguintes responsabilidades:

1. Gestão de Clientes (clientes.py)
Registo de Clientes: Permite armazenar a informação básica de cada hóspede (ID, Nome e Email).

Identificação Única: Garante que cada cliente está associado a um identificador para evitar duplicações em reservas.

2. Gestão de Inventário de Quartos (quartos.py)
Categorização: Suporta diferentes tipos de alojamento (Single, Double, Suite) com preços diferenciados.

Controlo de Estado: Monitoriza em tempo real se um quarto está Disponível ou Ocupado.

Listagem Dinâmica: Permite visualizar rapidamente todos os quartos do hotel e o seu estado atual.

3. Motor de Reservas (reservas.py)
Cálculo Automático de Custos: Calcula o valor total da estadia multiplicando o preço da noite pelo número de noites selecionado.

Vinculação de Dados: Associa um objeto Cliente a um objeto Quarto específico.

Atualização Automática de Disponibilidade: No momento em que uma reserva é efetuada, o sistema altera automaticamente o estado do quarto para "Ocupado".

4. Interface e Fluxo de Trabalho (app.py)
Menu Interativo: Interface de linha de comandos simples e intuitiva para o utilizador.

Validação de Regras: Impede a reserva de quartos que já estão ocupados ou a criação de reservas sem clientes registados.

Histórico de Reservas: Permite consultar todas as transações e estadias efetuadas durante a execução do programa.