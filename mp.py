import multiprocessing
import os
import time

def worker(process_id, total_calculos):
    print(f"Processo {process_id} iniciado.")
    tempo_inicial = time.time()
    tempo_atual = tempo_inicial
    contagem = 0

    while tempo_atual - tempo_inicial < 10:
        # Executar algum cálculo intensivo
        resultado = 1 + 1

        # Incrementar a contagem
        contagem += 1

        # Atualizar o tempo atual
        tempo_atual = time.time()
    
    print(f"Processo {process_id} finalizado. Total de cálculos: {contagem}.")
    
    # Adicionar a contagem total do processo à contagem global
    with total_calculos.get_lock():
        total_calculos.value += contagem

# Criar um objeto compartilhado para armazenar a contagem total
total_calculos = multiprocessing.Value('i', 0)

# Criar processos
processes = []
cpu = os.cpu_count()
for i in range(4):
    process = multiprocessing.Process(target=worker, args=(i, total_calculos))
    processes.append(process)

# Iniciar processos
start_time_all = time.time()
for process in processes:
    process.start()

# Aguardar todos os processos concluírem
for process in processes:
    process.join()
end_time_all = time.time()

# Obter a contagem total final
total_calculos_final = total_calculos.value

print(f"Todos os processos foram finalizados. Tempo total de execução: {end_time_all - start_time_all:.4f} segundos.")
print(f"Total de cálculos realizados por todos os processos: {total_calculos_final}.")
