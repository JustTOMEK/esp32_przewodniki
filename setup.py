import subprocess

_esp32_board_manager_url = "https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json"

# Stworzenie pliku konfiguracyjnego
subprocess.call([
    "arduino-cli",
    "config",
    "init"
    ])

# Dodanie url board managera dla esp32
subprocess.call([
    "arduino-cli",
    "config",
    "add",
    "board_manager.additional_urls",
    _esp32_board_manager_url
    ])


# Aktualizacja indeksu
subprocess.call([
    "arduino-cli",
    "core",
    "update-index"
    ])


# Instalacja oprogramowania płytki
subprocess.call([
    "arduino-cli",
    "core",
    "install",
    "esp32:esp32"
    ])


# Sprawdzenie instalacji
esp32_core_installed = "esp32" in str(
    subprocess.check_output([
        "arduino-cli",
        "core",
        "list"
        ]
    )
)


print("Wszystko gotowe")
