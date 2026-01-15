import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

df_transacao = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
df_ativo = pd.read_excel('base_invest.xlsx',sheet_name='Ativo')

#------------------------------------------------------------------------pergunta01--------------------------------------------------------------------------------------------------------------
#a variavel compras ta recebendo o valor da df_buyAndSell 
compras = df_transacao[df_transacao['operacao'] == 'compra'] #a coluna operação que está dentro da planilia Transacoes é igual a compra? (true) salva na variavel (false) não salva
vendas = df_transacao[df_transacao['operacao'] == 'venda'] #a coluna operação que está dentro da planilia Transacoes é igual a venda? (true) salva na variavel (false) não salva
#               chama:    tabela       coluna       linha

#aqui ele ta encontrando os valores maximos e minimos da coluna preco e salvando nas seguintes variaveis
maxCompra = compras['preco'].max() #aqui vai chamar o valor da coluna preco só na linha que compra for true, porem só o valor maximo
minCompra = compras['preco'].min() #aqui vai chamar o valor da coluna preco só na linha que compra for true, porem só o valor minimo
   
maxVenda = vendas['preco'].max() #aqui vai chamar o valor da coluna preco só na linha que venda for true, porem só o valor maximo
minVenda = vendas['preco'].min() #aqui vai chamar o valor da coluna preco só na linha que venda for true, porem só o valor minimo

print(f'O máximo e o mínimo de compras foi:\n{maxCompra}\n{minCompra}\n',
        f'\nO máximo e o mínimo de vendas foi:\n{maxVenda}\n{minVenda}')

#------------------------------------------------------------------------pergunta02--------------------------------------------------------------------------------------------------------------
#criando uma coluna nova que multiplica a coluna quantidade pela coluna preco
df_transacao['valorTotal'] = df_transacao['quantidade'] * df_transacao['preco']
valorPorAtivo= df_transacao.groupby('id_ativo')['valorTotal'].sum() #agrupando a coluna valor total por id_ativo(coluna) e somando eles

ativoMaiorValor= valorPorAtivo.idxmax() #mostra qual o maior valor do valorPorAtivo

#a coluna id_ativo que está dentro da planilia Ativo é igual a compra? (true) salva na variavel (false) não salva
cnpjMaiorValor= df_ativo[df_ativo['id_ativo'] == ativoMaiorValor]['cnpj'].iloc[0]# ou loc[id_ativo] (a diferença é q o iloc localiza pelo indice)

print(f'\nO CNPJ para o ativo com o maior valor é: {cnpjMaiorValor}')
#------------------------------------------------------------------------pergunta03--------------------------------------------------------------------------------------------------------------
df_transacao['valorTotal'] = df_transacao['quantidade'] * df_transacao['preco']
valorPorParticipante= df_transacao.groupby('id_participante')['valorTotal'].sum()
print('\n',valorPorParticipante)
#------------------------------------------------------------------------parte da aula02-----------------------------------------------------------------------------------------------------------
# Calcule o Q1, Q2 (Mediana) e Q3 para a coluna 'preco'
q1_preco = df_transacao['preco'].quantile(0.25)
q2_preco = df_transacao['preco'].quantile(0.50)
q3_preco = df_transacao['preco'].quantile(0.75)
media =df_transacao['preco'].mean
print(f"Preço Q1: {q1_preco:.2f}")
print(f"Preço Mediana (Q2): {q2_preco:.2f}")
print(f"Preço Q3: {q3_preco:.2f}")
print(f'Média: {media}')

# Contar a frequência de cada tipo de operação
contagem_operacao = df_transacao['operacao'].value_counts()
# Criar um gráfico de barras
contagem_operacao.plot(kind='bar', title='Tipos de Operação')
# Mostrar o gráfico
plt.show()