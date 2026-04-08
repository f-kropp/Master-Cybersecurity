import socket
import ipaddress
import random  # Modulo aggiunto per la generazione casuale dei byte

def genera_payload(dimensione_kb):
    """Genera un pacchetto di byte casuali in base ai KB richiesti."""
    dimensione_byte = dimensione_kb * 1024
    # Genera una lista di byte casuali utilizzando il modulo random
    return bytes([random.randint(0, 255) for _ in range(dimensione_byte)])

def simula_traffico_udp(ip_target, porta_target, numero_pacchetti):
    """Gestisce la creazione del socket e l'invio dei pacchetti."""
    # Creazione del socket UDP (AF_INET = IPv4, SOCK_DGRAM = UDP)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Richiamiamo la funzione per creare il pacchetto da 1 KB (come richiesto)
    dati_pacchetto = genera_payload(1)
    
    print(f"\n[+] Inizio invio traffico verso {ip_target}:{porta_target}...")
    
    pacchetti_inviati = 0
    try:
        # Ciclo di invio per il numero di pacchetti specificato
        for _ in range(numero_pacchetti):
            sock.sendto(dati_pacchetto, (ip_target, porta_target))
            pacchetti_inviati += 1
            
        print(f"[+] Trasmissione completata con successo! Inviati {pacchetti_inviati} pacchetti.")
        
    except Exception as errore:
        # Gestione di eventuali errori di rete durante l'invio
        print(f"[-] Si è verificato un errore di rete: {errore}")
        
    finally:
        # Chiusura sicura del socket per liberare le risorse
        sock.close()

def main():
    print("""
     _   _  ____   ____    _____           _   
    | | | ||  _ \ |  _ \  |_   _| ___  ___| |_ 
    | | | || | | || |_) |   | |  / _ \/ __| __|
    | |_| || |_| ||  __/    | | |  __/\__ \ |_ 
     \___/ |____/ |_|       |_|  \___||___/\__|
    """)
    print("[*] Inizializzazione modulo di invio...")
    
    # 1. Input e validazione continua dell'IP Target
    while True:
        ip = input("Inserisci l'IP della macchina target: ")
        try:
            ipaddress.ip_address(ip)
            break  # L'IP è valido, esce dal ciclo
        except ValueError:
            print("[-] Errore: Indirizzo IP non valido. Riprova.")

    # 2. Input e validazione continua della Porta Target
    while True:
        try:
            porta = int(input("Inserisci la porta UDP target (1-65535): "))
            if 1 <= porta <= 65535:
                break  # La porta è valida, esce dal ciclo
            else:
                print("[-] Errore: La porta deve essere compresa tra 1 e 65535.")
        except ValueError:
            print("[-] Errore: Devi inserire un numero intero per la porta.")

    # 3. Input e validazione del numero di pacchetti da inviare
    while True:
        try:
            pacchetti = int(input("Quanti pacchetti da 1 KB vuoi inviare? "))
            if pacchetti > 0:
                break  # Il numero è valido, esce dal ciclo
            else:
                print("[-] Errore: Il numero di pacchetti deve essere maggiore di zero.")
        except ValueError:
            print("[-] Errore: Devi inserire un numero intero.")

    # Avvio della funzione principale passando i parametri raccolti
    simula_traffico_udp(ip, porta, pacchetti)

# Punto di ingresso standard degli script Python
if __name__ == "__main__":
    main()