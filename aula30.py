"""
 CONSTANTE = "Variáveis" que não vão mudar
 Muitas condições no mesmo if (ruim)
     <- Contagem de complexidade (ruim)
 """
velocidade = 40  # velocidade atual do carro
km_carro = 100  # local em que o carro está na estrada
 
RADAR_1 = 60  # velocidade máxima do radar 1
KM_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega


# velocidade maior que a permitida #
velocidade_carro_passou_radar_1 = velocidade > RADAR_1 
# velocidade menor que a permitida #
velocidade_nao_passou_radar_1 = velocidade < RADAR_1


# velocidade de entrada no raio do radar #
velocidade_entrada = km_carro >= (KM_1 - RADAR_RANGE)
# velocidade de saida no raio do radar #
velocidade_saida = km_carro <= (KM_1 + RADAR_RANGE)


# calculo de entrada e saida do raio do radar #
passou_velocidade_radar_1 = velocidade_entrada and velocidade_saida


# carro pasou da velocidade permitida no raio do radar #
carro_multado_radar_1 = passou_velocidade_radar_1 and velocidade_carro_passou_radar_1 
# carro não pasou da velocidade permitida no raio do radar #
carro_nao_multado_radar_1 = passou_velocidade_radar_1 and velocidade_nao_passou_radar_1 


if velocidade_carro_passou_radar_1 :
    print('A velocidade do carro passou do radar 1')

if carro_nao_multado_radar_1 :
     print('Carro passou radar 1')
     print('Carro não foi multado')

if carro_multado_radar_1 :
     print('Carro multado no radar 1')