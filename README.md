# ESP32 Location Streamer #

Skrypt na płytkę ESP32, który pozwala zaprogramować na niej lokalizację i udostępniać ją połączonym urządzeniom poprzez BLE

## Konfiguracja

Projekt używa package managera `apm`

1. [Zainstaluj APM](https://github.com/ksrichard/apm)
2. Wywołaj `apm install`

Do komunikacji z płytką przyda się `arduino-cli`.

1. [Zainstaluj Arduino CLI](https://arduino.github.io/arduino-cli/0.29/installation/)

Skrypt programujący płytki wymaga odpowiedniego środowiska w `pythonie3`.

1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt`

Konfiguracja płytki

1. Sprawdź port płytki
2. Uruchom `python3 setup.py`
3. Podążaj za instrukcjami


## Używanie skryptu programującego płytki