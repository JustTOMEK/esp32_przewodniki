# import subprocess
from jinja2 import Environment, FileSystemLoader, select_autoescape
from tqdm import tqdm
import pandas as pd
import subprocess
import os

__temp_dir = "tmp_sketches"

__esp32_port = input("Podaj nazwę portu płtki: ")

env = Environment(
    loader=FileSystemLoader("."),
    autoescape=select_autoescape()
)

while True:
    template_location = input(
        "Lokalizacja wzorca szkicu (auto: streamer/streamer_template.ino): "
        )
    if not template_location:
        template_location = "streamer/streamer_template.ino"

    try:
        template = env.get_template(template_location)
    except FileNotFoundError:
        print("Podany plik nie istnieje")
        continue
    break

while True:
    input_data = input(
        "Lokalizacja danych czujników (.csv): "
        )
    try:
        test_locations = pd.read_csv(input_data)
    except FileNotFoundError:
        print("Podany plik nie istnieje")
        continue
    break


print("Tworzenie katalogu na szkice")
try:
    os.mkdir(__temp_dir)
except FileExistsError:
    pass

sketch_generate_progress_bar = tqdm(zip(test_locations.ID,
                                        test_locations.X,
                                        test_locations.Y))
# Generowanie sketchy dla każdego czujnika
for ID, X, Y in sketch_generate_progress_bar:
    sketch_generate_progress_bar.set_description(
        f"Generowanie szkiców ({__temp_dir})"
        )
    render = template.render(X=X, Y=Y)
    try:
        os.mkdir(f"{__temp_dir}/{ID}")
    except FileExistsError:
        pass
    with open(f"{__temp_dir}/{ID}/{ID}.ino", "w") as f:
        f.write(render)


sketch_compile_progress_bar = tqdm(test_locations.ID)
# Kompilacja sketchy
for ID in sketch_compile_progress_bar:
    sketch_compile_progress_bar.set_description(
        f"Kompilowanie szkiców ({__temp_dir}/{ID})"
        )
    subprocess.call([
        "arduino-cli",
        "compile",
        "--fqbn",
        "esp32:esp32:esp32",
        f"{__temp_dir}/{ID}",
        ]
    )

sketch_upload_progress_bar = tqdm(test_locations.ID)
# Ładowanie szkiców do pamięci czujników
for ID in sketch_upload_progress_bar:
    sketch_upload_progress_bar.set_description(
        f"Ładowanie szkicu do pamięci płytki ({__temp_dir}/{ID})"
        )
    subprocess.call([
        "arduino-cli",
        "upload",
        "--port",
        __esp32_port,
        "--fqbn",
        "esp32:esp32:esp32",
        f"{__temp_dir}/{ID}",
        ]
    )
    input("Przełącz płytkę i kliknij enter\n")
