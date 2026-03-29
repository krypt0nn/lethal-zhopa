import os, sys, shutil, hashlib, zipfile, urllib.request, tempfile

mods = {
    "engine": {
        "name": "BepInEx",
        "url": "https://gcdn.thunderstore.io/live/repository/packages/BepInEx-BepInExPack-5.4.2305.zip",
        "file": "BepInEx-BepInExPack-5.4.2305.zip",
        "hash": "e00f72a9bc2477d5cd95c716b4787735148ba8b0e3596e8db620537a9d60db53"
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
                    "name": "LCDirectLAN",
                    "description": "Mod that fixes and enhances LAN lobbies without interfering with the Steam-networked lobbies, built around BepInEx",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/TIRTAGT-LCDirectLAN-1.1.3.zip",
                    "file": "TIRTAGT-LCDirectLAN-1.1.3.zip",
                    "hash": "71721743d8d0352262cf836a16ca4302f397ce9ac84c47fb89cabdc68e0fffa3"
                },
                {
                    "name": "MoreCompany",
                    "description": "A stable lobby player count expansion mod. With cosmetics!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/notnotnotswipez-MoreCompany-1.12.0.zip",
                    "file": "notnotnotswipez-MoreCompany-1.12.0.zip",
                    "hash": "581b3c732c015f19b4ab5015f2111a8891350c09faf5f2a2a7e1b4c3aaaa3806"
                },
                {
                    "name": "ExtendedLateCompany",
                    "description": "A mod to allow players to join after the game starts",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Happyness-ExtendedLateCompany-1.1.1.zip",
                    "file": "Happyness-ExtendedLateCompany-1.1.1.zip",
                    "hash": "f4c595ddbc4695f7374e1b935da2a68865135c3c088effe6d782a0f05dd5986a"
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
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/AinaVT-LethalConfig-1.4.6.zip",
                    "file": "AinaVT-LethalConfig-1.4.6.zip",
                    "hash": "c9b20858915430da5edc8737d0818201df8eb68a55aef4675addd685af853fc2"
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
                    "description": "Improves overall performance by threading vanilla AI pathfinding and patching slow methods",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Zaggy1024-PathfindingLagFix-2.2.5.zip",
                    "file": "Zaggy1024-PathfindingLagFix-2.2.5.zip",
                    "hash": "a36c00a2a794c34325b5163f8ddbb474a192e7bc571719f1208039df895a20c9"
                },
                {
                    "name": "PathfindingLib",
                    "description": "Provides functionality for mod authors to run pathfinding off of the main thread",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Zaggy1024-PathfindingLib-2.4.1.zip",
                    "file": "Zaggy1024-PathfindingLib-2.4.1.zip",
                    "hash": "971db624546f41683f8b27e0a3f12c1b547679590b396d6c0e8cea28e191f59e"
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
                    "name": "EnemySoundFixes",
                    "description": "Fixes numerous issues with missing sound effects, or SFX playing when they shouldn't",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/ButteryStancakes-EnemySoundFixes-1.8.8.zip",
                    "file": "ButteryStancakes-EnemySoundFixes-1.8.8.zip",
                    "hash": "c58d17d55bd0861f9117893930bf8b6bb99639a939ccb071ffe6de0adba897d8"
                },
                {
                    "name": "Boombox Sync Fix",
                    "description": "This mod fixes a base game bug where an already spawned boombox does not play the same song between the client and host",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FutureSavior-Boombox_Sync_Fix-1.1.3.zip",
                    "file": "FutureSavior-Boombox_Sync_Fix-1.1.3.zip",
                    "hash": "908c6e465d9a28af8a932bb4d43543f97961ebd3216b5c07eaec480623e4b106"
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
                    "description": "Stops rendering interior rooms that aren't visible - Helps with performance without affecting visuals",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/fumiko-CullFactory-2.0.4.zip",
                    "file": "fumiko-CullFactory-2.0.4.zip",
                    "hash": "d648925cc4b7e790b3f23d46eabe37106f403d1aa214adbb4c9542c9310ac529"
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
                    "name": "ShipLootCruiser",
                    "description": "Reliably shows the total value of all scrap in your ship",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/HQHQTeam-ShipLootCruiser-1.0.3.zip",
                    "file": "HQHQTeam-ShipLootCruiser-1.0.3.zip",
                    "hash": "efc6186cd4872e0e2386833db254cda298b6427ff2ce1c677a19c2d290dd65e7"
                },
                {
                    "name": "BiggerShip",
                    "description": "It's just a bigger ship",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/mrov-BiggerShip-1.0.12.zip",
                    "file": "mrov-BiggerShip-1.0.12.zip",
                    "hash": "e8fd54f8a9a9cc32465f1fdb3e2eaa3eb8f09f1c0e5577a97c7ff10f6d023be4"
                },
                {
                    "name": "MrovLib",
                    "description": "Common methods for mrov mods",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/mrov-MrovLib-0.4.2.zip",
                    "file": "mrov-MrovLib-0.4.2.zip",
                    "hash": "17cb5dcb36460dcd56e288649a92ed654b30e7bade1b0b6ecc9e748694be9592"
                },
                {
                    "name": "DynamicDeadline",
                    "description": "Just a simple mod to have the deadline increase with the quota",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Krayken-DynamicDeadline-1.2.2.zip",
                    "file": "Krayken-DynamicDeadline-1.2.2.zip",
                    "hash": "2b80716c40e33c3de2321f994ec420691691773630c92821580832217ad395a8"
                },
                {
                    "name": "ReservedFlashlightSlot",
                    "description": "Gives a dedicated Flashlight slot on the right side of your screen. Activates with [F]",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedFlashlightSlot-2.0.10.zip",
                    "file": "FlipMods-ReservedFlashlightSlot-2.0.10.zip",
                    "hash": "8372ce5686cbdf4bd75b55ae7f40cfd9587f23ab2857c0a8b4c112d86cc4497f"
                },
                {
                    "name": "ReservedWalkieSlot",
                    "description": "Gives a dedicated Walkie slot on the right side of your screen. Activates with [X]",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedWalkieSlot-2.0.7.zip",
                    "file": "FlipMods-ReservedWalkieSlot-2.0.7.zip",
                    "hash": "d4832985cf064f72a33be957d6da1ac4585c549e1d36bb8b4a7ef5f94fae597b"
                },
                {
                    "name": "ReservedItemSlotCore",
                    "description": "The core mod for all ReservedItemSlot mods",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedItemSlotCore-2.0.54.zip",
                    "file": "FlipMods-ReservedItemSlotCore-2.0.54.zip",
                    "hash": "cd3240a84922fe6f493d6b2e25655d7ad5ac24ba6963365b7e022e4e0baae0d9"
                },
                {
                    "name": "EladsHUD",
                    "description": "A nice HUD menu",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/EladNLG-EladsHUD-1.3.0.zip",
                    "file": "EladNLG-EladsHUD-1.3.0.zip",
                    "hash": "772ecfd42629d3b18a49174f233418ff4612d81500865c60ad15cc4048d6ddec"
                },
                {
                    "name": "NiceChat",
                    "description": "Better text chat",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/taffyko-NiceChat-1.2.7.zip",
                    "file": "taffyko-NiceChat-1.2.7.zip",
                    "hash": "8fc91af7f5763218f6320c40259d6a15374310ff6316c563cb0e82c9f43a49c4"
                },
                {
                    "name": "OpenBodyCams",
                    "description": "An implementation of a body camera that is displayed on the bottom right monitor in the ship",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Zaggy1024-OpenBodyCams-3.0.11.zip",
                    "file": "Zaggy1024-OpenBodyCams-3.0.11.zip",
                    "hash": "f91f69dbede44905a187ac4a503769f238c57b83f11923b37af6a352a0ad39ab"
                },
                {
                    "name": "BetterBetterTeleporter",
                    "description": "A fully configurable Teleporter and Inverse Teleporter mod with advanced item filtering",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/jaramp-BetterBetterTeleporter-1.2.3.zip",
                    "file": "jaramp-BetterBetterTeleporter-1.2.3.zip",
                    "hash": "9baa69fd0e38ce88e904c7fe18e480cd5e5126b333ec8129a6b1dac24223e1fc"
                },
                {
                    "name": "FairAI",
                    "description": "Everyone that can die will die by stepping on land mines or by facing turrets",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/TheFluff-FairAI-1.5.6.zip",
                    "file": "TheFluff-FairAI-1.5.6.zip",
                    "hash": "608bf43318069733dc6bf3f404ff09ef78ef478eeb821bdc4f466404642550c4"
                },
                {
                    "name": "NoJumpDelay",
                    "description": "Removes the delay when jumping",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/DaXcess-NoJumpDelay-1.1.1.zip",
                    "file": "DaXcess-NoJumpDelay-1.1.1.zip",
                    "hash": "ba5e4c7fdfb9a92aed1dd271bbce2b7f762cabb3f5e4488bf59ccc81d3a80284"
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
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ObjectVolumeController-1.1.3.zip",
                    "file": "FlipMods-ObjectVolumeController-1.1.3.zip",
                    "hash": "9e01849d998f607bc3637905eec830bc189e326306e2f8e2dbc5d21bd16eb952"
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
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/CTMods-ChatCommands-2.0.0.zip",
                    "file": "CTMods-ChatCommands-2.0.0.zip",
                    "hash": "3b007a926c9e16be0c9c4a4b56d047d412f818c8e8977c725a0c9b2976e8867e"
                },
                {
                    "name": "NiceChat",
                    "description": "Better text chat",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/taffyko-NiceChat-1.2.7.zip",
                    "file": "taffyko-NiceChat-1.2.7.zip",
                    "hash": "8fc91af7f5763218f6320c40259d6a15374310ff6316c563cb0e82c9f43a49c4"
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
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-TooManyEmotes-2.3.13.zip",
                    "file": "FlipMods-TooManyEmotes-2.3.13.zip",
                    "hash": "fe262059133ea504201fc7f94f8d9f48eba5d840ab89e2d6e91563552f678384"
                },
                {
                    "name": "TooManyEmotesScrap",
                    "description": "Adds grabbable emote props as scrap to moons!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-TooManyEmotesScrap-1.0.9.zip",
                    "file": "FlipMods-TooManyEmotesScrap-1.0.9.zip",
                    "hash": "8361f71141189b3d5b59d8eeb1b7869d34287591a7f29cfdc95f4ad1e64fc1db"
                },
                {
                    "name": "LethalCompany InputUtils",
                    "description": "API/Library for creating Unity InputActions with in-game re-binding support",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Rune580-LethalCompany_InputUtils-0.7.12.zip",
                    "file": "Rune580-LethalCompany_InputUtils-0.7.12.zip",
                    "hash": "4e84ba24100b4838007873b7c5082df7995e1d44266568cf3fe6d8277d0b8a6d"
                }
            ]
        },

        "suits": {
            "name": "Suits",
            "description": "Extra character suits",
            "hidden": True,
            "require": [
                "foundation"
            ],
            "mods": [
                {
                    "name": "TooManySuits",
                    "description": "More Suits Addon which adds pages to the suit rack",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Verity-TooManySuits-2.0.3.zip",
                    "file": "Verity-TooManySuits-2.0.3.zip",
                    "hash": "3eeaccbefbe2a62097ecc79ab4d3e93e18ba4f99a83e230231f673818942ac6e"
                },
                {
                    "name": "More Suits",
                    "description": "Adds more suits to choose from, and can be used as a library to load your own suits!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/x753-More_Suits-1.5.2.zip",
                    "file": "x753-More_Suits-1.5.2.zip",
                    "hash": "3172978c5aa30c580be81263e3fb89b4f545f9be4686c9d72b6242b82d55f4bd"
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
                }
            ]
        },

        "enemies": {
            "name": "Enemies",
            "description": "Mods that add new enemies or update existing ones",
            "hidden": False,
            "require": [
                "foundation"
            ],
            "mods": [
                {
                    "name": "Mimics",
                    "description": "Adds a dangerous new monster to the game. Can you figure out what's real or will you be devoured?",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/x753-Mimics-2.7.2.zip",
                    "file": "x753-Mimics-2.7.2.zip",
                    "hash": "29bb03d609380ce0e7faf231140c9343fa033a883b839ca0221344aa1325713e"
                }
            ]
        },

        "vr": {
            "name": "VR support",
            "description": "Mods that add VR headset support to the game",
            "hidden": False,
            "require": [],
            "mods": [
                {
                    "name": "LethalCompanyVR",
                    "description": "Collecting scrap in VR",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/DaXcess-LethalCompanyVR-1.4.6.zip",
                    "file": "DaXcess-LethalCompanyVR-1.4.6.zip",
                    "hash": "a0d5e20e9e0a2d4ab0ecc23142995a191e0e5dcb3c807c8b9d2f56c058151051"
                },
                {
                    "name": "TypeLoadExceptionFixer",
                    "description": "Fixes issues caused by unloadable types",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Hamunii-TypeLoadExceptionFixer-1.0.4.zip",
                    "file": "Hamunii-TypeLoadExceptionFixer-1.0.4.zip",
                    "hash": "e3e09775e0a60b4ab0340ba6b2bc787858a5fe2f907ba4c589a815f308aee0de"
                },
                {
                    "name": "MonoDetour BepInEx 5",
                    "description": "HarmonyX interop & BepInEx 5 logger integration for MonoDetour",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/MonoDetour-MonoDetour_BepInEx_5-0.7.13.zip",
                    "file": "MonoDetour-MonoDetour_BepInEx_5-0.7.13.zip",
                    "hash": "7e41518b8b8c14580fde9ff53ff903b4f33c3eec93a18b3174b9bb41f5f41213"
                },
                {
                    "name": "MonoDetour",
                    "description": "Easy and convenient .NET detouring library, powered by MonoMod.RuntimeDetour",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/MonoDetour-MonoDetour-0.7.13.zip",
                    "file": "MonoDetour-MonoDetour-0.7.13.zip",
                    "hash": "5eb52722c60c9f960a371e18e9cdf33566a4c330b7fcd0c9a79a7ed7ff4eae5b"
                },
                {
                    "name": "FixPluginTypesSerialization",
                    "description": "Fix custom Serializable structs and such not properly getting deserialized by Unity",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Evaisa-FixPluginTypesSerialization-1.1.4.zip",
                    "file": "Evaisa-FixPluginTypesSerialization-1.1.4.zip",
                    "hash": "debe47f4f2a24ff7387d88d55e89b9a7184e75af74c3bb751bf3093d7b2d5b35"
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
                "emotes"
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
                "suits",
                "scrap",
                "enemies"
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

    if not file_hash:
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
def print_help(message = ""):
    if message:
        print(message)
        print()

    print("Lethal Zhopa 2026-03-29.1 (year-month-day.edition)")
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
