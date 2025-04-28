# Constante = variaveis que não mudam
# Muitas condições em um único if = ruim
# Quanto mais o código esta afastado da margem = contagem de complexidade (ruim)

velocidade = 62 # velocidade do carro
local_carro = 99 # local em que o carro esta na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar esta
RADAR_RANGE = 1 # distância onde o radar pega

velocidade_acima_radar_1 = velocidade > RADAR_1
carro_sob_radar_range = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if carro_sob_radar_range and velocidade_acima_radar_1:
    print('Carro foi multado no radar 1')


# if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
#        local_carro <= (LOCAL_1 + RADAR_RANGE) and \
#            velocidade > RADAR_1:
#    print('Carro foi multado no radar 1')
