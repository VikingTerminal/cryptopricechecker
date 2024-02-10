import requests
import time

def green_text(text):
    return f"\033[32m{text}\033[0m"  

def yellow_text(text):
    return f"\033[33m{text}\033[0m"  

def cyan_text(text):
    return f"\033[36m{text}\033[0m"  

def red_text(text):
    return f"\033[31m{text}\033[0m"  

def light_blue_text(text):
    return f"\033[94m{text}\033[0m"  

def get_crypto_price(coin_identifier):
    api_url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_identifier}&vs_currencies=usd'
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()
        return data[coin_identifier]['usd']
    except requests.exceptions.RequestException as e:
        return red_text(f"Errore nella richiesta HTTP: {e}")
    except KeyError:
        return red_text(f"La criptovaluta con identificatore {coin_identifier} non è stata trovata.")

def print_crypto_list():
    print(yellow_text("Scegli una criptovaluta:\n"))
    print(yellow_text("1. Bitcoin (BTC)"))
    print(yellow_text("2. Ethereum (ETH)"))
    print(yellow_text("3. Litecoin (LTC)"))
    print(yellow_text("4. Monero (XMR)"))
    print(yellow_text("5. Ripple (XRP)"))
    print(yellow_text("6. Tether (USDT)"))
    print(yellow_text("7. Solana (SOL)"))
    print(yellow_text("8. USD Coin (USDC)"))
    print(yellow_text("9. Cardano (ADA)"))
    print(yellow_text("10.Dogecoin (DOGE)"))
    

def print_with_typing_effect(text, color_fn=cyan_text):
    for char in text:
        print(color_fn(char), end='', flush=True)
        time.sleep(0.05)
    print()

def print_welcome_message():
    print_with_typing_effect("Benvenuto in questo tool Crypto Price Checker!", cyan_text)
    print_with_typing_effect("Ricevi i valori aggiornati delle principali criptovalute.", cyan_text)
    print_with_typing_effect("Segui @VikingTerminal su Telegram per altre informazioni.\n", cyan_text)

def print_farewell_message():
    print_with_typing_effect("Grazie per aver utilizzato Crypto Price Checker!", cyan_text)
    print_with_typing_effect("Torna presto. Segui @VikingTerminal su Telegram per aggiornamenti.", cyan_text)

def main():
    print_welcome_message()

    while True:
        print_crypto_list()
        
        crypto_choice = input(light_blue_text("Inserisci il numero corrispondente alla criptovaluta desiderata (o scrivi 'exit' per uscire): "))

        if crypto_choice.lower() == "exit":
            break

        coin_identifier = None
        if crypto_choice == "1":
            coin_identifier = "bitcoin"
        elif crypto_choice == "2":
            coin_identifier = "ethereum"
        elif crypto_choice == "3":
            coin_identifier = "litecoin"
        elif crypto_choice == "4":
            coin_identifier = "monero"
        elif crypto_choice == "5":
            coin_identifier = "ripple"
        elif crypto_choice == "6":
            coin_identifier = "tether"
        elif crypto_choice == "7":
            coin_identifier = "solana"
        elif crypto_choice == "8":
            coin_identifier = "usd-coin"
        elif crypto_choice == "9":
            coin_identifier = "cardano"
        elif crypto_choice == "10":
            coin_identifier = "dogecoin"
        

        if coin_identifier:
            print_with_typing_effect(f"Ricerca del valore attuale di {coin_identifier.capitalize()}...", yellow_text)

            price = get_crypto_price(coin_identifier)

            if price is not None:
                print_with_typing_effect(f"Il valore attuale è: ${price}", yellow_text)
            else:
                print_with_typing_effect(f"Impossibile ottenere il valore della criptovaluta. Verifica la tua selezione.", red_text)

    print_farewell_message()

if __name__ == "__main__":
    main()
