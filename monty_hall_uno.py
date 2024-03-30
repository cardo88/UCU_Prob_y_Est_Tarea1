import random

def monty_hall_simulacion(cambiar_puerta=True):
    # Escoger una puerta aleatoria que tenga el premio
    puerta_con_auto = random.randint(1, 3)
    
    # Escoger una puerta aleatoria como elección inicial del jugador
    puerta_inicial_elegida_por_jugador = random.randint(1, 3)
    puerta_final_elegida_por_jugador = puerta_inicial_elegida_por_jugador

    # Determinar qué puerta abrirá el presentador (que no sea la elegida por el jugador ni la ganadora)
    puertas = [1, 2, 3]
    puertas.remove(puerta_con_auto)
    if puerta_inicial_elegida_por_jugador in puertas:
        puertas.remove(puerta_inicial_elegida_por_jugador)
    puerta_abierta_por_presentador = random.choice(puertas)
    
    # Si el jugador decide cambiar de puerta, cambiamos su elección
    if cambiar_puerta:
        puertas = [1, 2, 3]
        puertas.remove(puerta_inicial_elegida_por_jugador)
        puertas.remove(puerta_abierta_por_presentador)
        puerta_final_elegida_por_jugador = puertas[0]

    # Verificar si el jugador ha ganado
    resultado = "No ganó el auto"
    if puerta_final_elegida_por_jugador == puerta_con_auto:
        resultado = "¡Ganó el auto!"

    # Imprimir los resultados de la simulación
    print("Puerta elegida por el participante:", puerta_inicial_elegida_por_jugador)
    print("Puerta donde está el auto:", puerta_con_auto)
    print("Puerta abierta por el presentador:", puerta_abierta_por_presentador)
    if cambiar_puerta:
        print("El participante cambió de puerta y eligió la puerta:", puerta_final_elegida_por_jugador)
    print("Resultado del concurso:", resultado)

# Ejemplo de uso:
print("Simulación sin cambiar de puerta:")
monty_hall_simulacion(cambiar_puerta=False)

print("\nSimulación cambiando de puerta:")
monty_hall_simulacion(cambiar_puerta=True)
