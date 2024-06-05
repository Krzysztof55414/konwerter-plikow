import sys
import os

def main():
    if len(sys.argv) == 3:
        sciezka_wejsciowa = sys.argv[1]
        sciezka_wyjsciowa = sys.argv[2]

        if not os.path.isfile(sciezka_wejsciowa):
            print(f"Plik {sciezka_wejsciowa} nie istnieje.")
            sys.exit(1)
        
        print(f"Parsowanie argumentów zakończone sukcesem: {sciezka_wejsciowa}, {sciezka_wyjsciowa}")
    else:
        print("Użycie: program.py <ścieżka wejściowa> <ścieżka wyjściowa>")
        sys.exit(1)

if __name__ == "__main__":
    main()
