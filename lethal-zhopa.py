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
                    "description": "A stable lobby player count expansion mod. With cosmetics!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/notnotnotswipez-MoreCompany-1.10.1.zip",
                    "file": "notnotnotswipez-MoreCompany-1.10.1.zip",
                    "hash": "2561942fa6ec6f2fc0e9c6eee5fdc659f40c9bcfb7e9df74db30daf3cb6fe0cf"
                },
                {
                    "name": "LateCompany",
                    "description": "A mod to allow players to join after the game starts",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/anormaltwig-LateCompany-1.0.18.zip",
                    "file": "anormaltwig-LateCompany-1.0.18.zip",
                    "hash": "16d4ba28e4ae233141e59c9fcf78471120e38f01f1fa23745df9f6e033aed91a"
                },
                {
                    "name": "MoreItems",
                    "description": "Changes the max amount of items that the game saves from 45 to 999",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Drakorle-MoreItems-1.0.2.zip",
                    "file": "Drakorle-MoreItems-1.0.2.zip",
                    "hash": "69bdfbc748ea6d2b1320fb1c4636c5b9936308cbdbaf423dcb82116d1f33d952"
                },
                {
                    "name": "LethalConfig",
                    "description": "Provides an in-game config menu for players to edit their configs",
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
                    "description": "Lethal Company mod to fix stutters caused by the AI of Brackens, Spore Lizards, and Snare Fleas",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Zaggy1024-PathfindingLagFix-1.4.0.zip",
                    "file": "Zaggy1024-PathfindingLagFix-1.4.0.zip",
                    "hash": "0e2a6db6e60f8f94e3c87a35800f5ec52dcc7bc28aaa6eca6f8f6fc51e029e47"
                },
                {
                    "name": "DissonanceLagFix",
                    "description": "This plugin significantly reduces the duration of lag spikes simply by changing the log level of DissonanceVoip",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/linkoid-DissonanceLagFix-1.0.0.zip",
                    "file": "linkoid-DissonanceLagFix-1.0.0.zip",
                    "hash": "b6ae0efed7f5e78cd2d8564ed13a39b8c6ad4407b769e1f216b19bcb27b6e8a8"
                },
                {
                    "name": "LCMaxSoundsFix",
                    "description": "Simple mod that increase max number of simultaneous playing sounds, hopefully fixing missing sound problems",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Hardy-LCMaxSoundsFix-1.2.0.zip",
                    "file": "Hardy-LCMaxSoundsFix-1.2.0.zip",
                    "hash": "53d988a154449f6bd8d4f655d14bbb6740af2ff926563d640d817889b7c84de3"
                },
                {
                    "name": "Boombox Sync Fix",
                    "description": "This mod fixes a base game bug where an already spawned boombox does not play the same song between the client and host",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FutureSavior-Boombox_Sync_Fix-1.1.3.zip",
                    "file": "FutureSavior-Boombox_Sync_Fix-1.1.3.zip",
                    "hash": "908c6e465d9a28af8a932bb4d43543f97961ebd3216b5c07eaec480623e4b106"
                },
                {
                    "name": "DoorFix",
                    "description": "Fixes the hitbox of doors so items can be picked up through open doors more easily",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/itsmeowdev-DoorFix-1.0.0.zip",
                    "file": "itsmeowdev-DoorFix-1.0.0.zip",
                    "hash": "6ce41e432d49c02c34a184e28ee800a0b5e5fe18a08a3ec2416c8450864c950f"
                },
                {
                    "name": "FixResolution",
                    "description": "Changes the render resolution to your screens resolution rather than 520p",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/nodelll-kruumys_FixResolution-1.0.0.zip",
                    "file": "nodelll-kruumys_FixResolution-1.0.0.zip",
                    "hash": "fd983a6a0e72a2823e5349d0fa19a99c269d58497f266cceff4936d6abdbf621"
                },
                {
                    "name": "CullFactory",
                    "description": "Stops rendering interior rooms that aren't visible. Helps with performance without affecting visuals",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/fumiko-CullFactory-1.3.2.zip",
                    "file": "fumiko-CullFactory-1.3.2.zip",
                    "hash": "0fc927bf65b760dad6e5de81b9273f46cd447215ee649f5d207d8b4a2387c0cd"
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
                    "description": "Reliably shows the total value of all scrap in your ship",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/tinyhoot-ShipLoot-1.1.0.zip",
                    "file": "tinyhoot-ShipLoot-1.1.0.zip",
                    "hash": "3f5306dc714dd710d8f394f4b5f75cdee2cc811780ae48fe7f23c9d301acc3c1"
                },
                {
                    "name": "DynamicDeadline",
                    "description": "Just a simple mod to have the deadline increase with the quota",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Krayken-DynamicDeadline-1.2.2.zip",
                    "file": "Krayken-DynamicDeadline-1.2.2.zip",
                    "hash": "2b80716c40e33c3de2321f994ec420691691773630c92821580832217ad395a8"
                },
                {
                    "name": "MeteoMultiplier",
                    "description": "Multiplies scrap value and/or amount by current weather",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Fredolx-MeteoMultiplier-1.1.3.zip",
                    "file": "Fredolx-MeteoMultiplier-1.1.3.zip",
                    "hash": "4e1a78dcab1e237ec8281ae7e1a91d2ab111944b290539e9361442596890f290"
                },
                {
                    "name": "ReservedFlashlightSlot",
                    "description": "Gives a dedicated Flashlight slot on the right side of your screen. Activates with [F]",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedFlashlightSlot-2.0.7.zip",
                    "file": "FlipMods-ReservedFlashlightSlot-2.0.7.zip",
                    "hash": "59b52bcdee64662f1078ad608eddf7bdc2554a764e680479d34ad92c9f80db54"
                },
                {
                    "name": "ReservedWalkieSlot",
                    "description": "Gives a dedicated Walkie slot on the right side of your screen. Activates with [X]",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedWalkieSlot-2.0.6.zip",
                    "file": "FlipMods-ReservedWalkieSlot-2.0.6.zip",
                    "hash": "75b362aa3bcbd991e0e3ea2fc61bfdc6b635ca3a28925b520263e5e85432e5a2"
                },
                {
                    "name": "ReservedItemSlotCore",
                    "description": "The core mod for all ReservedItemSlot mods",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedItemSlotCore-2.0.35.zip",
                    "file": "FlipMods-ReservedItemSlotCore-2.0.35.zip",
                    "hash": "cf710feb8c1cb3de708c7747e062c59a06ab950246f422b323995b51dd8477e8"
                },
                {
                    "name": "EladsHUD",
                    "description": "A nice HUD menu",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/EladNLG-EladsHUD-1.3.0.zip",
                    "file": "EladNLG-EladsHUD-1.3.0.zip",
                    "hash": "772ecfd42629d3b18a49174f233418ff4612d81500865c60ad15cc4048d6ddec"
                },
                {
                    "name": "OpenBodyCams",
                    "description": "An implementation of a body camera that is displayed on the bottom right monitor in the ship",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Zaggy1024-OpenBodyCams-2.2.4.zip",
                    "file": "Zaggy1024-OpenBodyCams-2.2.4.zip",
                    "hash": "f76eb7a906cb5c6234dd8eceb7dc5bd6ba470c887560104980a41e741b61c4f1"
                },
                {
                    "name": "BetterTeleporter",
                    "description": "Better Teleporters for Lethal Company",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/SirTyler-BetterTeleporter-1.2.2.zip",
                    "file": "SirTyler-BetterTeleporter-1.2.2.zip",
                    "hash": "b8ba2e768c08cf679636d80314af958600c7706313ee32f0955e510ccb8eddb8"
                },
                {
                    "name": "FairAI",
                    "description": "Everyone that can die will die by stepping on land mines or by facing turrets",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/TheFluff-FairAI-1.3.9.zip",
                    "file": "TheFluff-FairAI-1.3.9.zip",
                    "hash": "727b191701fcaa46e30421146c58f89e6c49a337b8cfe99c54635385d9321ebb"
                },
                {
                    "name": "NoJumpDelay",
                    "description": "Removes the delay when jumping",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/DaXcess-NoJumpDelay-1.0.0.zip",
                    "file": "DaXcess-NoJumpDelay-1.0.0.zip",
                    "hash": "49ee2c2dafe1fc8f50093ef5b3d181c3322edd93769d5a758152b10a9762452c"
                },
                {
                    "name": "ViewExtension",
                    "description": "Increases the view distance",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/sfDesat-ViewExtension-1.3.0.zip",
                    "file": "sfDesat-ViewExtension-1.3.0.zip",
                    "hash": "52d7c06df5ba2f960930aa531262d8d1f7410a92edf3e9dd9e5745c8b13450b9"
                },
                {
                    "name": "ObjectVolumeController",
                    "description": "Allows adjusting the volume on the media objects, such as television and boombox",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ObjectVolumeController-1.1.1.zip",
                    "file": "FlipMods-ObjectVolumeController-1.1.1.zip",
                    "hash": "0711be67758e977cf42e404ff2d649c9a7571326c524be5c388620eb2c63231c"
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
                    "description": "Adds a lot of usable (admin) commands in the chat",
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
                    "description": "Adds over 200 new emotes!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-TooManyEmotes-2.2.4.zip",
                    "file": "FlipMods-TooManyEmotes-2.2.4.zip",
                    "hash": "ad28c32db8ca890323b01c02220bb0f9409e0d9b698fabe389ffdb1262be0175"
                },
                {
                    "name": "TooManyEmotesScrap",
                    "description": "Adds grabbable emote props as scrap to moons!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-TooManyEmotesScrap-1.0.7.zip",
                    "file": "FlipMods-TooManyEmotesScrap-1.0.7.zip",
                    "hash": "d0e8c622c5f12b0afb9570a8ce49302639560c44e4b53d31f1dc2d6d2e059eac"
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
                    "description": "Adds more suits to choose from, and can be used as a library to load your own suits!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/x753-More_Suits-1.4.3.zip",
                    "file": "x753-More_Suits-1.4.3.zip",
                    "hash": "50f26a2ceb4e6427d4261aca84732c4e3bf51d1b1460cc733a7f5f163f49832b"
                },
                {
                    "name": "ModelReplacementAPI",
                    "description": "API to simplify model replacement",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/BunyaPineTree-ModelReplacementAPI-2.4.8.zip",
                    "file": "BunyaPineTree-ModelReplacementAPI-2.4.8.zip",
                    "hash": "6fd35d4582646656f4438b217947dc8b1d5e46c7de92785ce1ff766c776adbae"
                },
                {
                    "name": "TooManySuits",
                    "description": "More Suits Addon which adds pages to the suit rack",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Verity-TooManySuits-1.1.0.zip",
                    "file": "Verity-TooManySuits-1.1.0.zip",
                    "hash": "cb5591c6307246549d2ed482d19bae406fc27294813523ffbda22cf450f68ea8"
                }
            ]
        },

        "anime-suits": {
            "name": "Anime Suits",
            "description": "Mod that adds suits from the Blue Archive to the game",
            "hidden": False,
            "require": [
                "foundation",
                "suits-foundation"
            ],
            "mods": [
                {
                    "name": "Blue Archive Playermodels",
                    "description": "New hires from Kivotos",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/JerryOnStreak-Blue_Archive_Playermodels-2.0.2.zip",
                    "file": "JerryOnStreak-Blue_Archive_Playermodels-2.0.2.zip",
                    "hash": "8adf89d99275497859c417e604359fe5c03c14155ef33eb0fc38a6b1b604121a"
                }
            ]
        },

        "scrap": {
            "name": "Scrap",
            "description": "Mods with additional scrap and items",
            "hidden": False,
            "require": [
                "foundation"
            ],
            "mods": [
                {
                    "name": "MinecraftScraps",
                    "description": "Adds More Minecraft Scraps!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/rainbow137-MinecraftScraps-1.4.3.zip",
                    "file": "rainbow137-MinecraftScraps-1.4.3.zip",
                    "hash": "d7778aa1ac5d4bfa6d5cde7cb2f86ce19f2df4162dac442924c1c40f30bc45b0"
                },
                {
                    "name": "AlltheScrapsMod",
                    "description": "Bunch of new scrap!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/czech_lethal-AlltheScrapsMod-1.1.7.zip",
                    "file": "czech_lethal-AlltheScrapsMod-1.1.7.zip",
                    "hash": "483569604074fa98a1131f5a113fea451361cc5eea579d4439d27995ba6a68cb"
                },
                {
                    "name": "LethalExpansionCore",
                    "description": "De-bloated LethalExpansion fork with only the LethalSDK module support",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/jockie-LethalExpansionCore-1.3.15.zip",
                    "file": "jockie-LethalExpansionCore-1.3.15.zip",
                    "hash": "3cd7f4d6ca58f1fab5678005a249bea9f586df9b66efd3e5939c0bf8eb431c05"
                },
                {
                    "name": "Maxwell ScrapItem",
                    "description": "Adds Maxwell the Cat as a scrap item that you can collect",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Kittenji-Maxwell_ScrapItem-1.0.1.zip",
                    "file": "Kittenji-Maxwell_ScrapItem-1.0.1.zip",
                    "hash": "9b1cbe521145d781763edf9bcc963ee42700ceca1d1bee91eebeb341410b9f63"
                }
            ]
        },

        "new-features": {
            "name": "New Features",
            "description": "Mods that add new game mechanics",
            "hidden": False,
            "require": [
                "foundation"
            ],
            "mods": [
                {
                    "name": "MobDrops",
                    "description": "All killable mobs drop VALUABLE SCRAP! (even mod included)!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/MamboDancer-MobDrops-1.3.0.zip",
                    "file": "MamboDancer-MobDrops-1.3.0.zip",
                    "hash": "afee0e70674b35a38c404dbcdd409f9bc33a7230be587a053fce1b1e09ffe004"
                },
                {
                    "name": "LethalProgression",
                    "description": "Leveling and skillpoints!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Stoneman-LethalProgression-1.3.2.zip",
                    "file": "Stoneman-LethalProgression-1.3.2.zip",
                    "hash": "d23605235d73ea0c8b4dffb54ebfdf0a09cdcaea0045b623269894f39525b534"
                }
            ]
        },

        "lite": {
            "name": "Lite",
            "description": "Install QoL and bug fixes mods",
            "hidden": False,
            "require": [
                "foundation",
                "fixes",
                "qol"
            ],
            "mods": []
        },

        "vanilla+": {
            "name": "Vanilla+",
            "description": "Install QoL, bug fixes, emotes and new features mods",
            "hidden": False,
            "require": [
                "foundation",
                "fixes",
                "qol",
                "admin",
                "emotes",
                "new-features"
            ],
            "mods": []
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
                "scrap",
                "new-features"
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
    print(f"[*] Downloading {component['name']}...")

    cache_folder = f"{cache_folder}/{component['hash']}"
    cache_path = f"{cache_folder}/{component['file']}"

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
    print(f"[*] Installing {mod_info['name']}...")

    if not is_game_folder(game_path):
        print("[!] GIVEN GAME FOLDER PATH IS INVALID. SKIPPING")

    elif os.path.exists(f"{game_path}/BepInEx/plugins/{mod_info['name']}"):
        print("    - Skipping, already installed")

    elif not verify_hash(mod_path, mod_info["hash"]):
        print("[!] MOD HAS INVALID HASH. SKIPPING")

    else:
        with zipfile.ZipFile(mod_path, 'r') as file:
            file.extractall(f"{game_path}/BepInEx/plugins/{mod_info['name']}")

# Print help message
def print_help(message = False):
    if message:
        print(message)
        print()

    print("Lethal Zhopa 2024-08-27.2 (year-month-day.edition)")
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
                    print(f"  {extension['name']} [{name}]")
                    print(f"    Description: {extension['description']}")

                    if len(extension["mods"]) > 0:
                        print(f"    Mods ({len(extension['mods'])}):")

                        for mod in extension["mods"]:
                            print(f"      - [{mod['name']}]: {mod['description']}")

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
