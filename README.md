# 🧾 Gerador de Nota Fiscal em Python

Este projeto tem como objetivo criar uma aplicação simples em Python que simule a emissão de uma nota fiscal, com entrada de dados do cliente e dos produtos, cálculos automáticos e exibição formatada no terminal.

---

## 📝 Objetivo do Projeto

### 📥 Entrada de Dados
- Nome do cliente  
- CPF ou CNPJ  
- Nome dos produtos comprados  
- Quantidade de cada produto  
- Preço unitário de cada produto  

### ⚙️ Processamento
- Calcular o subtotal de cada item (`quantidade × valor unitário`)  
- Calcular o total geral da compra  
- Calcular o imposto (ICMS fictício de 10%)  

### 📤 Saída
- Exibir um recibo/nota fiscal formatado no terminal, com as informações do cliente, lista de produtos, totais e impostos.

---

## 💡 Possíveis Melhorias Futuras
- Validação de CPF/CNPJ  
- Geração de arquivo `.txt` da nota fiscal  
- Inclusão de data e hora da emissão  
- Interface gráfica (GUI) com Tkinter ou PyQt  
