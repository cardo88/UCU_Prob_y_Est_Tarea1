import random

def monty_hall_simulacion(cambiar_puerta=True):
    # Escoger una puerta aleatoria que tenga el premio
    puerta_con_auto = random.randint(1, 3)

    # Escoger una puerta aleatoria como elección inicial del jugador
    puerta_elegida_por_jugador = random.randint(1, 3)

    # Determinar qué puerta abrirá el presentador (que no sea la elegida por el jugador ni la ganadora)
    puertas = [1, 2, 3]    
    puertas.remove(puerta_con_auto)
    if puerta_elegida_por_jugador in puertas:
        puertas.remove(puerta_elegida_por_jugador)
    puerta_abierta_por_presentador = random.choice(puertas)
    
    # Si el jugador decide cambiar de puerta, cambiamos su elección
    if cambiar_puerta:
        puertas = [1, 2, 3]
        puertas.remove(puerta_elegida_por_jugador)
        puertas.remove(puerta_abierta_por_presentador)
        puerta_elegida_por_jugador = puertas[0]

    # Retoranar si el jugador ha ganado o no.
    if puerta_elegida_por_jugador == puerta_con_auto:
        return 1
    else:
        return 0

def simular_monty_hall(num_simulaciones, cambiar_puerta):    
    total_ganados = 0
    for i in range(num_simulaciones):
        total_ganados += monty_hall_simulacion(cambiar_puerta)
    return total_ganados

# Simulaciones para la estrategia de cambio de puerta
print("Estrategia de cambio de puerta:")
for num_simulaciones in [1000, 10000, 100000]:
    ganados = simular_monty_hall(num_simulaciones,True)
    frecuencia_relativa = ganados / num_simulaciones
    print(f"Simulaciones: {num_simulaciones}, Ganados: {ganados}, Frecuencia Relativa: {frecuencia_relativa:.4f}")

# Simulaciones para la estrategia sin cambio de puerta
print("\nEstrategia sin cambio de puerta:")
for num_simulaciones in [1000, 10000, 100000]:
    ganados = simular_monty_hall(num_simulaciones,False)
    frecuencia_relativa = ganados / num_simulaciones
    print(f"Simulaciones: {num_simulaciones}, Ganados: {ganados}, Frecuencia Relativa: {frecuencia_relativa:.4f}")
