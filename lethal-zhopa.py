import os, sys, io, shutil, hashlib, zipfile, urllib.request, tempfile

mods = {
    "engine": {
        "name": "BepInEx",
        "url": "https://gcdn.thunderstore.io/live/repository/packages/BepInEx-BepInExPack-5.4.2100.zip",
        "file": "BepInEx-BepInExPack-5.4.2100.zip",
        "hash": "a6d473510fa87652f1e9e5d87c4b4c103ea2cdd7e8ecb2c0b20fdbfcc2935698"
    },

    "extensions": {
        "engine": {
            "name": "Engine",
            "description": "Just install the mods engine to the game",
            "hidden": False,
            "require": [],
            "mods": []
        },

        "foundation": {
            "name": "Foundation",
            "description": "Basic mods setup",
            "hidden": False,
            "require": [],
            "mods": [
                {
                    "name": "MoreCompany",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/notnotnotswipez-MoreCompany-1.9.1.zip",
                    "file": "notnotnotswipez-MoreCompany-1.9.1.zip",
                    "hash": "8f90716a51671fa0e2e57df51dec4faf04ae967346c33f16c069f63dc7f80281"
                },
                {
                    "name": "LateCompany",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/anormaltwig-LateCompany-1.0.13.zip",
                    "file": "anormaltwig-LateCompany-1.0.13.zip",
                    "hash": "fa4b7e09797ecfdce21429d577f7bf9a9b4e472fd8deb3d19fad8b8f2e329149"
                },
                {
                    "name": "MoreItems",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Drakorle-MoreItems-1.0.2.zip",
                    "file": "Drakorle-MoreItems-1.0.2.zip",
                    "hash": "69bdfbc748ea6d2b1320fb1c4636c5b9936308cbdbaf423dcb82116d1f33d952"
                },
                {
                    "name": "LethalConfig",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/AinaVT-LethalConfig-1.4.2.zip",
                    "file": "AinaVT-LethalConfig-1.4.2.zip",
                    "hash": "8428de265fed698c11c36916da9971043af1fcfa307b3478ddd838fc4ca6306c"
                }
            ]
        },

        "fixes": {
            "name": "Fixes",
            "description": "Mods that fix the game",
            "hidden": False,
            "require": [
                "foundation"
            ],
            "mods": [
                {
                    "name": "PathfindingLagFix",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Zaggy1024-PathfindingLagFix-1.2.1.zip",
                    "file": "Zaggy1024-PathfindingLagFix-1.2.1.zip",
                    "hash": "862babc450d94c125ba7f678d0dcf5e545e09194c6d3f17cb3f4a14008b03e12"
                },
                {
                    "name": "DissonanceLagFix",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/linkoid-DissonanceLagFix-1.0.0.zip",
                    "file": "linkoid-DissonanceLagFix-1.0.0.zip",
                    "hash": "b6ae0efed7f5e78cd2d8564ed13a39b8c6ad4407b769e1f216b19bcb27b6e8a8"
                }
            ]
        },

        "qol": {
            "name": "Quality of Life",
            "description": "Mods that improve the quality of the game",
            "hidden": False,
            "require": [
                "foundation"
            ],
            "mods": [
                {
                    "name": "ShipLoot",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/tinyhoot-ShipLoot-1.1.0.zip",
                    "file": "tinyhoot-ShipLoot-1.1.0.zip",
                    "hash": "3f5306dc714dd710d8f394f4b5f75cdee2cc811780ae48fe7f23c9d301acc3c1"
                },
                {
                    "name": "DynamicDeadline",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Krayken-DynamicDeadline-1.2.2.zip",
                    "file": "Krayken-DynamicDeadline-1.2.2.zip",
                    "hash": "2b80716c40e33c3de2321f994ec420691691773630c92821580832217ad395a8"
                },
                {
                    "name": "WeatherMultipliers",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Blorb-WeatherMultipliers-1.1.0.zip",
                    "file": "Blorb-WeatherMultipliers-1.1.0.zip",
                    "hash": "82c13f9328854debbabb18dd620f2c05749e36526d66242c5690a6c2d9d25963"
                },
                {
                    "name": "ReservedFlashlightSlot",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedFlashlightSlot-2.0.3.zip",
                    "file": "FlipMods-ReservedFlashlightSlot-2.0.3.zip",
                    "hash": "f1ad73b63748a0f95b0eb88cce737b302b0532b646deee82c6dc0df51f815a7f"
                },
                {
                    "name": "ReservedWalkieSlot",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedWalkieSlot-2.0.5.zip",
                    "file": "FlipMods-ReservedWalkieSlot-2.0.5.zip",
                    "hash": "c55e720ca8cd5a599ccff2c9a3610e8a4b91cb04d26a3acd93cb97df0179ca79"
                },
                {
                    "name": "ReservedItemSlotCore",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedItemSlotCore-2.0.25.zip",
                    "file": "FlipMods-ReservedItemSlotCore-2.0.25.zip",
                    "hash": "7145ba3a39cceddd3119156851bdbb321a8d3b7b24b231c91d2eae8b0101219e"
                },
                {
                    "name": "EladsHUD",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/EladNLG-EladsHUD-1.2.1.zip",
                    "file": "EladNLG-EladsHUD-1.2.1.zip",
                    "hash": "3ce4bfb60bcc682596986b7b86c357e3e8d480bbb87302d16bec3b0febb1d349"
                },
                {
                    "name": "OpenBodyCams",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Zaggy1024-OpenBodyCams-1.3.0.zip",
                    "file": "Zaggy1024-OpenBodyCams-1.3.0.zip",
                    "hash": "c62737de859f09f7eca4ac33d5522e66eaf07c4d59696c3baba963940f106df5"
                },
                {
                    "name": "BetterTeleporter",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/SirTyler-BetterTeleporter-1.2.2.zip",
                    "file": "SirTyler-BetterTeleporter-1.2.2.zip",
                    "hash": "b8ba2e768c08cf679636d80314af958600c7706313ee32f0955e510ccb8eddb8"
                }
            ]
        },

        "admin": {
            "name": "Admin",
            "description": "Mods that add admin tools to the game",
            "hidden": False,
            "require": [
                "foundation"
            ],
            "mods": [
                {
                    "name": "ChatCommands",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/CTMods-ChatCommands-1.1.92.zip",
                    "file": "CTMods-ChatCommands-1.1.92.zip",
                    "hash": "6ae829a2d65660ba8091d3f11895663e48f9727821e05828f82d7993dafbe031"
                }
            ]
        },

        "emotes": {
            "name": "Emotes",
            "description": "Mods that add emotes to the game",
            "hidden": False,
            "require": [
                "foundation"
            ],
            "mods": [
                {
                    "name": "TooManyEmotes",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-TooManyEmotes-2.1.15.zip",
                    "file": "FlipMods-TooManyEmotes-2.1.15.zip",
                    "hash": "7008778dcd0fe4613c7d68bfdd90d861ed3c21fed2eef8324584ad6f5bf9eaa2"
                }
            ]
        },

        "suits-foundation": {
            "name": "Suits Foundation",
            "description": "Libraries for adding suits to the game",
            "hidden": True,
            "require": [],
            "mods": [
                {
                    "name": "More Suits",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/x753-More_Suits-1.4.3.zip",
                    "file": "x753-More_Suits-1.4.3.zip",
                    "hash": "50f26a2ceb4e6427d4261aca84732c4e3bf51d1b1460cc733a7f5f163f49832b"
                },
                {
                    "name": "ModelReplacementAPI",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/BunyaPineTree-ModelReplacementAPI-2.4.4.zip",
                    "file": "BunyaPineTree-ModelReplacementAPI-2.4.4.zip",
                    "hash": "dfdec37cd3e35ee58b31ab8fe41aa2f35131663597549bebd986f0173dc5c269"
                }
            ]
        },

        "anime-suits": {
            "name": "Anime Suits",
            "description": "Mods that add suits from the Blue Archive to the game",
            "hidden": False,
            "require": [
                "foundation",
                "suits-foundation"
            ],
            "mods": [
                {
                    "name": "Blue Archive Playermodels",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/JerryOnStreak-Blue_Archive_Playermodels-2.0.2.zip",
                    "file": "JerryOnStreak-Blue_Archive_Playermodels-2.0.2.zip",
                    "hash": "8adf89d99275497859c417e604359fe5c03c14155ef33eb0fc38a6b1b604121a"
                }
            ]
        },

        "fumos": {
            "name": "Fumos",
            "description": "Mods that add fumos to the game",
            "hidden": False,
            "require": [
                "foundation"
            ],
            "mods": [
                {
                    "name": "FumoCompany",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/silhygames-FumoCompany-1.2.4.zip",
                    "file": "silhygames-FumoCompany-1.2.4.zip",
                    "hash": "4ab44efc701f20b16dbc2fbfc74f95a5d1df103d9070bae26f9b7631c5607920"
                },
                {
                    "name": "LethalExpansion",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/HolographicWings-LethalExpansion-1.2.16.zip",
                    "file": "HolographicWings-LethalExpansion-1.2.16.zip",
                    "hash": "ca6194ce3e17063d3f749068d256617958594ae2ed9598493627e29530939741"
                }
            ]
        },

        "full": {
            "name": "Full",
            "description": "Install all available mods",
            "hidden": False,
            "require": [
                "foundation",
                "fixes",
                "qol",
                "admin",
                "emotes",
                "anime-suits",
                "fumos"
            ],
            "mods": []
        }
    }
}

# Get list of mods from enabled extensions names
def get_mods_list(enabled_extensions):
    mods_list = {}

    while len(enabled_extensions) > 0:
        extension = enabled_extensions.pop()

        if extension in mods["extensions"].keys():
            enabled_extensions.extend(mods["extensions"][extension]["require"])

            for mod in mods["extensions"][extension]["mods"]:
                mods_list[mod["hash"]] = mod

    return mods_list.values()

# Check if the given path is a correct game folder
def is_game_folder(game_path):
    return os.path.exists(f"{game_path}/Lethal Company.exe")

# Check if the mods engine is installed
def is_engine_installed(game_path):
    return os.path.exists(f"{game_path}/BepInEx/core/BepInEx.dll")

# Verify the hash of the downloaded file
def verify_hash(path, file_hash):
    with open(path, "rb") as file:
        digest = hashlib.file_digest(file, "blake2s")

    if file_hash == "?":
        print(f"[debug] '{path}' hash is '{digest.hexdigest()}'")

        return True

    return digest.hexdigest() == file_hash

# Download the component, returning path to the downloaded file
def download(component, cache_folder):
    print(f"[*] Downloading {component["name"]}...")

    cache_folder = f"{cache_folder}/{component["hash"]}"
    cache_path = f"{cache_folder}/{component["file"]}"

    if os.path.exists(cache_path) and verify_hash(cache_path, component["hash"]):
        print("    - Skipping, already downloaded")

        return cache_path

    else:
        os.makedirs(cache_folder, exist_ok = True)

        with urllib.request.urlopen(component["url"]) as response:
            output = open(cache_path, "wb")
            output.write(response.read())
            output.close()

        return cache_path

# Install mods engine to the game folder
def install_engine(game_path, engine_path):
    print(f"[*] Installing mods engine...")

    if not is_game_folder(game_path):
        print("[!] GIVEN GAME FOLDER PATH IS INVALID. SKIPPING")

    elif is_engine_installed(game_path):
        print("    - Skipping, already installed")

    elif not verify_hash(engine_path, mods["engine"]["hash"]):
        print("[!] MOD HAS INVALID HASH. SKIPPING")

    else:
        with tempfile.TemporaryDirectory(dir = game_path) as temp:
            with zipfile.ZipFile(engine_path, 'r') as file:
                file.extractall(temp)

            shutil.move(f"{temp}/BepInExPack/BepInEx", f"{game_path}/BepInEx")

            os.replace(f"{temp}/BepInExPack/doorstop_config.ini", f"{game_path}/doorstop_config.ini")
            os.replace(f"{temp}/BepInExPack/winhttp.dll", f"{game_path}/winhttp.dll")

# Uninstall mods engine from the game folder
def uninstall_engine(game_path):
    print(f"[*] Uninstalling mods engine...")

    if not is_game_folder(game_path):
        print("[!] GIVEN GAME FOLDER PATH IS INVALID. SKIPPING")

    else:
        shutil.rmtree(f"{game_path}/BepInEx")

        os.remove(f"{game_path}/doorstop_config.ini")
        os.remove(f"{game_path}/winhttp.dll")

# Install mod to the game folder
def install_mod(game_path, mod_path, mod_info):
    print(f"[*] Installing {mod_info["name"]}...")

    if not is_game_folder(game_path):
        print("[!] GIVEN GAME FOLDER PATH IS INVALID. SKIPPING")

    elif os.path.exists(f"{game_path}/BepInEx/plugins/{mod_info["name"]}"):
        print("    - Skipping, already installed")

    elif not verify_hash(mod_path, mod_info["hash"]):
        print("[!] MOD HAS INVALID HASH. SKIPPING")

    else:
        with zipfile.ZipFile(mod_path, 'r') as file:
            file.extractall(f"{game_path}/BepInEx/plugins/{mod_info["name"]}")

# Print help message
def print_help(message = False):
    if message:
        print(message)
        print()

    print("Lethal Zhopa 2024-05-04.3 (year-month-day.edition)")
    print()
    print("Use `python3 lethal-zhopa.py setup <game path> <extensions>` to setup the mods to the game")
    print("Example: `python3 lethal-zhopa.py setup \"C:\\Games\\Lethal Company\" full`")
    print()
    print("Available commands:")
    print("  help - print this help message")
    print("  list - list available mods extensions")
    print("  setup <game path> <extensions> - setup the mods to the game")
    print("  remove <game path> - remove the mods from the game")

if len(sys.argv) < 2:
    print_help("No command passed")

else:
    match sys.argv[1]:
        case "help":
            print_help()

        case "list":
            print("Available extensions:")

            for name in mods["extensions"]:
                extension = mods["extensions"][name]

                if not extension["hidden"]:
                    print(f"  {extension["name"]} [{name}]")
                    print(f"    Description: {extension["description"]}")

                    if len(extension["mods"]) > 0:
                        print( "    Mods:")

                        for mod in extension["mods"]:
                            print(f"      - {mod["name"]}")

                    print()

        case "setup":
            if len(sys.argv) < 4:
                print_help("Too few arguments passed")

            elif not is_game_folder(sys.argv[2]):
                print_help("The given path is not a valid game folder")

            else:
                cache_folder = f"{sys.argv[2]}/lethal-zhopa-cache"

                if not is_engine_installed(sys.argv[2]):
                    engine = download(mods["engine"], cache_folder)

                    install_engine(sys.argv[2], engine)

                for mod in get_mods_list(sys.argv[3:]):
                    downloaded_file = download(mod, cache_folder)

                    install_mod(sys.argv[2], downloaded_file, mod)

                print()
                print("Installation completed")

        case "remove":
            if len(sys.argv) < 3:
                print_help("Too few arguments passed")

            elif not is_game_folder(sys.argv[2]):
                print_help("The given path is not a valid game folder")

            else:
                uninstall_engine(sys.argv[2])

                print()
                print("Uninstallation completed")

        case _:
            print_help("Invalid command")
