import threading
import time
import multiprocessing

def worker(thread_id, total_calculos):
    print(f"Thread {thread_id} iniciada.")
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
    
    print(f"Thread {thread_id} finalizada. Total de cálculos: {contagem}.")
    
    # Adicionar a contagem total da thread à contagem global
    with total_calculos.get_lock():
        total_calculos.value += contagem

# Criar um objeto compartilhado para armazenar a contagem total
total_calculos = multiprocessing.Value('i', 0)

# Criar threads
threads = []
for i in range(4):
    thread = threading.Thread(target=worker, args=(i, total_calculos))
    threads.append(thread)

# Iniciar threads
start_time_all = time.time()
for thread in threads:
    thread.start()

# Aguardar todas as threads concluírem
for thread in threads:
    thread.join()
end_time_all = time.time()

# Obter a contagem total final
total_calculos_final = total_calculos.value

print(f"Todas as threads foram finalizadas. Tempo total de execução: {end_time_all - start_time_all:.4f} segundos.")
print(f"Total de cálculos realizados por todas as threads: {total_calculos_final}.")
