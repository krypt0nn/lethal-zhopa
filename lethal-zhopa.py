import os, sys, shutil, hashlib, zipfile, urllib.request, tempfile

def FixPluginTypesSerializationHook(game_path: str, mod_info):
    # Unfortunately VR mod (or some another mod) can't see this plugin
    # in the plugins directory of BepInEx, so we have to copy its files
    # into special BepInEx folders manually

    shutil.copy(
        f"{game_path}/BepInEx/plugins/{mod_info["name"]}/BepInEx/config/FixPluginTypesSerialization.cfg",
        f"{game_path}/BepInEx/config"
    )

    shutil.copytree(
        f"{game_path}/BepInEx/plugins/{mod_info["name"]}/BepInEx/patchers/FixPluginTypesSerialization",
        f"{game_path}/BepInEx/patchers/FixPluginTypesSerialization",
        dirs_exist_ok = True
    )

    return True

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
                    "hash": "71721743d8d0352262cf836a16ca4302f397ce9ac84c47fb89cabdc68e0fffa3",
                    "hook": None
                },
                {
                    "name": "MoreCompany",
                    "description": "A stable lobby player count expansion mod. With cosmetics!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/notnotnotswipez-MoreCompany-1.12.0.zip",
                    "file": "notnotnotswipez-MoreCompany-1.12.0.zip",
                    "hash": "581b3c732c015f19b4ab5015f2111a8891350c09faf5f2a2a7e1b4c3aaaa3806",
                    "hook": None
                },
                {
                    "name": "ExtendedLateCompany",
                    "description": "A mod to allow players to join after the game starts",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Happyness-ExtendedLateCompany-1.1.1.zip",
                    "file": "Happyness-ExtendedLateCompany-1.1.1.zip",
                    "hash": "f4c595ddbc4695f7374e1b935da2a68865135c3c088effe6d782a0f05dd5986a",
                    "hook": None
                },
                {
                    "name": "MoreItems",
                    "description": "Changes the max amount of items that the game saves from 45 to 999",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Drakorle-MoreItems-1.0.2.zip",
                    "file": "Drakorle-MoreItems-1.0.2.zip",
                    "hash": "69bdfbc748ea6d2b1320fb1c4636c5b9936308cbdbaf423dcb82116d1f33d952",
                    "hook": None
                },
                {
                    "name": "LethalConfig",
                    "description": "Provides an in-game config menu for players to edit their configs",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/AinaVT-LethalConfig-1.4.6.zip",
                    "file": "AinaVT-LethalConfig-1.4.6.zip",
                    "hash": "c9b20858915430da5edc8737d0818201df8eb68a55aef4675addd685af853fc2",
                    "hook": None
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
                    "hash": "a36c00a2a794c34325b5163f8ddbb474a192e7bc571719f1208039df895a20c9",
                    "hook": None
                },
                {
                    "name": "PathfindingLib",
                    "description": "Provides functionality for mod authors to run pathfinding off of the main thread",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Zaggy1024-PathfindingLib-2.4.1.zip",
                    "file": "Zaggy1024-PathfindingLib-2.4.1.zip",
                    "hash": "971db624546f41683f8b27e0a3f12c1b547679590b396d6c0e8cea28e191f59e",
                    "hook": None
                },
                {
                    "name": "DissonanceLagFix",
                    "description": "This plugin significantly reduces the duration of lag spikes simply by changing the log level of DissonanceVoip",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/linkoid-DissonanceLagFix-1.0.0.zip",
                    "file": "linkoid-DissonanceLagFix-1.0.0.zip",
                    "hash": "b6ae0efed7f5e78cd2d8564ed13a39b8c6ad4407b769e1f216b19bcb27b6e8a8",
                    "hook": None
                },
                {
                    "name": "LCMaxSoundsFix",
                    "description": "Simple mod that increase max number of simultaneous playing sounds, hopefully fixing missing sound problems",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Hardy-LCMaxSoundsFix-1.2.0.zip",
                    "file": "Hardy-LCMaxSoundsFix-1.2.0.zip",
                    "hash": "53d988a154449f6bd8d4f655d14bbb6740af2ff926563d640d817889b7c84de3",
                    "hook": None
                },
                {
                    "name": "EnemySoundFixes",
                    "description": "Fixes numerous issues with missing sound effects, or SFX playing when they shouldn't",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/ButteryStancakes-EnemySoundFixes-1.8.8.zip",
                    "file": "ButteryStancakes-EnemySoundFixes-1.8.8.zip",
                    "hash": "c58d17d55bd0861f9117893930bf8b6bb99639a939ccb071ffe6de0adba897d8",
                    "hook": None
                },
                {
                    "name": "Boombox Sync Fix",
                    "description": "This mod fixes a base game bug where an already spawned boombox does not play the same song between the client and host",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FutureSavior-Boombox_Sync_Fix-1.1.3.zip",
                    "file": "FutureSavior-Boombox_Sync_Fix-1.1.3.zip",
                    "hash": "908c6e465d9a28af8a932bb4d43543f97961ebd3216b5c07eaec480623e4b106",
                    "hook": None
                },
                {
                    "name": "FixResolution",
                    "description": "Changes the render resolution to your screens resolution rather than 520p",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/nodelll-kruumys_FixResolution-1.0.0.zip",
                    "file": "nodelll-kruumys_FixResolution-1.0.0.zip",
                    "hash": "fd983a6a0e72a2823e5349d0fa19a99c269d58497f266cceff4936d6abdbf621",
                    "hook": None
                },
                {
                    "name": "CullFactory",
                    "description": "Stops rendering interior rooms that aren't visible - Helps with performance without affecting visuals",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/fumiko-CullFactory-2.0.4.zip",
                    "file": "fumiko-CullFactory-2.0.4.zip",
                    "hash": "d648925cc4b7e790b3f23d46eabe37106f403d1aa214adbb4c9542c9310ac529",
                    "hook": None
                },
                {
                    "name": "MaskFixes",
                    "description": "Fixes several problems with mask items and masked enemies",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/ButteryStancakes-MaskFixes-1.5.2.zip",
                    "file": "ButteryStancakes-MaskFixes-1.5.2.zip",
                    "hash": "11b4ad250c47b0988f442ca808f10edb97b77ce46c28d468403e7be4d3e40ce3",
                    "hook": None
                },
                {
                    "name": "MaskedInvisFix",
                    "description": "Fixes bugs where masked are invisible",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/VirusTLNR-MaskedInvisFix-0.0.2.zip",
                    "file": "VirusTLNR-MaskedInvisFix-0.0.2.zip",
                    "hash": "3b844de3554e142fc3477ce97fbb47f81f5ea02cbc9ec1ab954385321871019f",
                    "hook": None
                },
                {
                    "name": "DetourContext Dispose Fix",
                    "description": "A BepInEx patcher to fix MonoMod.RuntimeDetour's DetourContext.Dispose not working",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Hamunii-DetourContext_Dispose_Fix-1.0.7.zip",
                    "file": "Hamunii-DetourContext_Dispose_Fix-1.0.7.zip",
                    "hash": "61c485f23fa99970d2944cea5c662f53fb2cc51d5b3179a9266af07b97d0926a",
                    "hook": None
                },
                {
                    "name": "StarlancerAIFix",
                    "description": "Automatically assigns interior/exterior AI for enemies based on their spawn location",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/AudioKnight-StarlancerAIFix-3.11.1.zip",
                    "file": "AudioKnight-StarlancerAIFix-3.11.1.zip",
                    "hash": "e9a1f28ed8f2e10e651bbd1880acac3dc3f64a8f0cac2ba1baac5e13dbc7362f",
                    "hook": None
                },
                {
                    "name": "BarberFixes",
                    "description": "Fixes several issues with Barbers",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/ButteryStancakes-BarberFixes-1.3.0.zip",
                    "file": "ButteryStancakes-BarberFixes-1.3.0.zip",
                    "hash": "3fb2b3419a670e9ccb98677e0b2b95619a393c9af17fd0b4d421f168fcc6ab58",
                    "hook": None
                }
            ]
        },

        "qol": {
            "name": "Quality of Life",
            "description": "Mods that improve the gaming experience without changing UI",
            "hidden": False,
            "require": [
                "foundation"
            ],
            "mods": [
                {
                    "name": "BiggerShip",
                    "description": "It's just a bigger ship",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/mrov-BiggerShip-1.0.12.zip",
                    "file": "mrov-BiggerShip-1.0.12.zip",
                    "hash": "e8fd54f8a9a9cc32465f1fdb3e2eaa3eb8f09f1c0e5577a97c7ff10f6d023be4",
                    "hook": None
                },
                {
                    "name": "MrovLib",
                    "description": "Common methods for mrov mods",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/mrov-MrovLib-0.4.2.zip",
                    "file": "mrov-MrovLib-0.4.2.zip",
                    "hash": "17cb5dcb36460dcd56e288649a92ed654b30e7bade1b0b6ecc9e748694be9592",
                    "hook": None
                },
                {
                    "name": "DynamicDeadline",
                    "description": "Just a simple mod to have the deadline increase with the quota",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Krayken-DynamicDeadline-1.2.2.zip",
                    "file": "Krayken-DynamicDeadline-1.2.2.zip",
                    "hash": "2b80716c40e33c3de2321f994ec420691691773630c92821580832217ad395a8",
                    "hook": None
                },
                {
                    "name": "QuotaRollover",
                    "description": "Anti-hoarding technology that only removes required credits for the quota instead of setting progress to 0",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/boxofbiscuits97-QuotaRollover-2.5.0.zip",
                    "file": "boxofbiscuits97-QuotaRollover-2.5.0.zip",
                    "hash": "5a02ce2245640b0d962ff029571e540ddca47ba76b9379165243e61c84837184",
                    "hook": None
                },
                {
                    "name": "ReservedFlashlightSlot",
                    "description": "Gives a dedicated Flashlight slot on the right side of your screen. Activates with [F]",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedFlashlightSlot-2.0.10.zip",
                    "file": "FlipMods-ReservedFlashlightSlot-2.0.10.zip",
                    "hash": "8372ce5686cbdf4bd75b55ae7f40cfd9587f23ab2857c0a8b4c112d86cc4497f",
                    "hook": None
                },
                {
                    "name": "ReservedWalkieSlot",
                    "description": "Gives a dedicated Walkie slot on the right side of your screen. Activates with [X]",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedWalkieSlot-2.0.7.zip",
                    "file": "FlipMods-ReservedWalkieSlot-2.0.7.zip",
                    "hash": "d4832985cf064f72a33be957d6da1ac4585c549e1d36bb8b4a7ef5f94fae597b",
                    "hook": None
                },
                {
                    "name": "ReservedSprayPaintSlot",
                    "description": "Gives a dedicated SprayPaint slot on the right side of your screen",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedSprayPaintSlot-1.1.3.zip",
                    "file": "FlipMods-ReservedSprayPaintSlot-1.1.3.zip",
                    "hash": "bee25665c0f14e57ec4f4ac46ed7d1e326777dd4f23541f97d30d2a1cb525bf1",
                    "hook": None
                },
                {
                    "name": "ReservedItemSlotCore",
                    "description": "The core mod for all ReservedItemSlot mods",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ReservedItemSlotCore-2.0.54.zip",
                    "file": "FlipMods-ReservedItemSlotCore-2.0.54.zip",
                    "hash": "cd3240a84922fe6f493d6b2e25655d7ad5ac24ba6963365b7e022e4e0baae0d9",
                    "hook": None
                },
                {
                    "name": "NiceChat",
                    "description": "Better text chat",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/taffyko-NiceChat-1.2.7.zip",
                    "file": "taffyko-NiceChat-1.2.7.zip",
                    "hash": "8fc91af7f5763218f6320c40259d6a15374310ff6316c563cb0e82c9f43a49c4",
                    "hook": None
                },
                {
                    "name": "OpenBodyCams",
                    "description": "An implementation of a body camera that is displayed on the bottom right monitor in the ship",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Zaggy1024-OpenBodyCams-3.0.11.zip",
                    "file": "Zaggy1024-OpenBodyCams-3.0.11.zip",
                    "hash": "f91f69dbede44905a187ac4a503769f238c57b83f11923b37af6a352a0ad39ab",
                    "hook": None
                },
                {
                    "name": "BetterBetterTeleporter",
                    "description": "A fully configurable Teleporter and Inverse Teleporter mod with advanced item filtering",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/jaramp-BetterBetterTeleporter-1.2.3.zip",
                    "file": "jaramp-BetterBetterTeleporter-1.2.3.zip",
                    "hash": "9baa69fd0e38ce88e904c7fe18e480cd5e5126b333ec8129a6b1dac24223e1fc",
                    "hook": None
                },
                {
                    "name": "FairAI",
                    "description": "Everyone that can die will die by stepping on land mines or by facing turrets",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/TheFluff-FairAI-1.5.6.zip",
                    "file": "TheFluff-FairAI-1.5.6.zip",
                    "hash": "608bf43318069733dc6bf3f404ff09ef78ef478eeb821bdc4f466404642550c4",
                    "hook": None
                },
                {
                    "name": "NoJumpDelay",
                    "description": "Removes the delay when jumping",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/DaXcess-NoJumpDelay-1.1.1.zip",
                    "file": "DaXcess-NoJumpDelay-1.1.1.zip",
                    "hash": "ba5e4c7fdfb9a92aed1dd271bbce2b7f762cabb3f5e4488bf59ccc81d3a80284",
                    "hook": None
                },
                {
                    "name": "ViewExtension",
                    "description": "Increases the view distance",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/sfDesat-ViewExtension-1.3.0.zip",
                    "file": "sfDesat-ViewExtension-1.3.0.zip",
                    "hash": "52d7c06df5ba2f960930aa531262d8d1f7410a92edf3e9dd9e5745c8b13450b9",
                    "hook": None
                },
                {
                    "name": "ObjectVolumeController",
                    "description": "Allows adjusting the volume on the media objects, such as television and boombox",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-ObjectVolumeController-1.1.3.zip",
                    "file": "FlipMods-ObjectVolumeController-1.1.3.zip",
                    "hash": "9e01849d998f607bc3637905eec830bc189e326306e2f8e2dbc5d21bd16eb952",
                    "hook": None
                },
                {
                    "name": "BetterSprayPaint",
                    "description": "Significantly more responsive and reliable painting, many bug-fixes, infinite spray paint, longer range, quieter sounds.",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/taffyko-BetterSprayPaint-2.1.0.zip",
                    "file": "taffyko-BetterSprayPaint-2.1.0.zip",
                    "hash": "62e27d0fb734f4aef44826cd84daf09f7004e78a20273bdd068c4d9647383e86",
                    "hook": None
                },
                {
                    "name": "LethalCompany InputUtils",
                    "description": "API/Library for creating Unity InputActions with in-game re-binding support",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Rune580-LethalCompany_InputUtils-0.7.12.zip",
                    "file": "Rune580-LethalCompany_InputUtils-0.7.12.zip",
                    "hash": "4e84ba24100b4838007873b7c5082df7995e1d44266568cf3fe6d8277d0b8a6d",
                    "hook": None
                }
            ]
        },

        "hud": {
            "name": "HUD",
            "description": "Mods that change the game UI or add new elements. Incompatible with VR mods!",
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
                    "hash": "efc6186cd4872e0e2386833db254cda298b6427ff2ce1c677a19c2d290dd65e7",
                    "hook": None
                },
                {
                    "name": "EladsHUD",
                    "description": "A nice HUD menu",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/EladNLG-EladsHUD-1.3.0.zip",
                    "file": "EladNLG-EladsHUD-1.3.0.zip",
                    "hash": "772ecfd42629d3b18a49174f233418ff4612d81500865c60ad15cc4048d6ddec",
                    "hook": None
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
                    "hash": "fe262059133ea504201fc7f94f8d9f48eba5d840ab89e2d6e91563552f678384",
                    "hook": None
                },
                {
                    "name": "TooManyEmotesScrap",
                    "description": "Adds grabbable emote props as scrap to moons!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/FlipMods-TooManyEmotesScrap-1.0.9.zip",
                    "file": "FlipMods-TooManyEmotesScrap-1.0.9.zip",
                    "hash": "8361f71141189b3d5b59d8eeb1b7869d34287591a7f29cfdc95f4ad1e64fc1db",
                    "hook": None
                },
                {
                    "name": "LethalCompany InputUtils",
                    "description": "API/Library for creating Unity InputActions with in-game re-binding support",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Rune580-LethalCompany_InputUtils-0.7.12.zip",
                    "file": "Rune580-LethalCompany_InputUtils-0.7.12.zip",
                    "hash": "4e84ba24100b4838007873b7c5082df7995e1d44266568cf3fe6d8277d0b8a6d",
                    "hook": None
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
                    "hash": "3eeaccbefbe2a62097ecc79ab4d3e93e18ba4f99a83e230231f673818942ac6e",
                    "hook": None
                },
                {
                    "name": "More Suits",
                    "description": "Adds more suits to choose from, and can be used as a library to load your own suits!",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/x753-More_Suits-1.5.2.zip",
                    "file": "x753-More_Suits-1.5.2.zip",
                    "hash": "3172978c5aa30c580be81263e3fb89b4f545f9be4686c9d72b6242b82d55f4bd",
                    "hook": None
                },
                {
                    "name": "SCP Foundation Suit",
                    "description": "Adds an SCP Facility Guard suit to the game",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/TeamClark-SCP_Foundation_Suit-1.1.0.zip",
                    "file": "TeamClark-SCP_Foundation_Suit-1.1.0.zip",
                    "hash": "6f91cfa18c47e6ec185360711725b975c6592ea9622c43526510027f3ebbb2fb",
                    "hook": None
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
                    "hash": "483569604074fa98a1131f5a113fea451361cc5eea579d4439d27995ba6a68cb",
                    "hook": None
                },
                {
                    "name": "LethalExpansionCore",
                    "description": "De-bloated LethalExpansion fork with only the LethalSDK module support",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/jockie-LethalExpansionCore-1.3.15.zip",
                    "file": "jockie-LethalExpansionCore-1.3.15.zip",
                    "hash": "3cd7f4d6ca58f1fab5678005a249bea9f586df9b66efd3e5939c0bf8eb431c05",
                    "hook": None
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
                    "hash": "29bb03d609380ce0e7faf231140c9343fa033a883b839ca0221344aa1325713e",
                    "hook": None
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
                    "hash": "a0d5e20e9e0a2d4ab0ecc23142995a191e0e5dcb3c807c8b9d2f56c058151051",
                    "hook": None
                },
                {
                    "name": "TypeLoadExceptionFixer",
                    "description": "Fixes issues caused by unloadable types",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Hamunii-TypeLoadExceptionFixer-1.0.4.zip",
                    "file": "Hamunii-TypeLoadExceptionFixer-1.0.4.zip",
                    "hash": "e3e09775e0a60b4ab0340ba6b2bc787858a5fe2f907ba4c589a815f308aee0de",
                    "hook": None
                },
                {
                    "name": "MonoDetour BepInEx 5",
                    "description": "HarmonyX interop & BepInEx 5 logger integration for MonoDetour",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/MonoDetour-MonoDetour_BepInEx_5-0.7.13.zip",
                    "file": "MonoDetour-MonoDetour_BepInEx_5-0.7.13.zip",
                    "hash": "7e41518b8b8c14580fde9ff53ff903b4f33c3eec93a18b3174b9bb41f5f41213",
                    "hook": None
                },
                {
                    "name": "MonoDetour",
                    "description": "Easy and convenient .NET detouring library, powered by MonoMod.RuntimeDetour",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/MonoDetour-MonoDetour-0.7.13.zip",
                    "file": "MonoDetour-MonoDetour-0.7.13.zip",
                    "hash": "5eb52722c60c9f960a371e18e9cdf33566a4c330b7fcd0c9a79a7ed7ff4eae5b",
                    "hook": None
                },
                {
                    "name": "FixPluginTypesSerialization",
                    "description": "Fix custom Serializable structs and such not properly getting deserialized by Unity",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/Evaisa-FixPluginTypesSerialization-1.1.4.zip",
                    "file": "Evaisa-FixPluginTypesSerialization-1.1.4.zip",
                    "hash": "debe47f4f2a24ff7387d88d55e89b9a7184e75af74c3bb751bf3093d7b2d5b35",
                    "hook": FixPluginTypesSerializationHook
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
                    "hash": "3b007a926c9e16be0c9c4a4b56d047d412f818c8e8977c725a0c9b2976e8867e",
                    "hook": None
                },
                {
                    "name": "NiceChat",
                    "description": "Better text chat",
                    "url": "https://gcdn.thunderstore.io/live/repository/packages/taffyko-NiceChat-1.2.7.zip",
                    "file": "taffyko-NiceChat-1.2.7.zip",
                    "hash": "8fc91af7f5763218f6320c40259d6a15374310ff6316c563cb0e82c9f43a49c4",
                    "hook": None
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
                "qol",
                "hud"
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
                "hud",
                "emotes",
                "suits"
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
                "hud",
                "emotes",
                "suits",
                "scrap",
                "enemies",
                "admin"
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
def is_game_folder(game_path: str) -> bool:
    return os.path.exists(f"{game_path}/Lethal Company.exe")

# Check if the mods engine is installed
def is_engine_installed(game_path: str) -> bool:
    return os.path.exists(f"{game_path}/BepInEx/core/BepInEx.dll")

# Verify the hash of the downloaded file
def verify_hash(path: str, file_hash: str):
    with open(path, "rb") as file:
        digest = hashlib.file_digest(file, "blake2s")

    if not file_hash:
        print(f"[debug] '{path}' hash is '{digest.hexdigest()}'")

        return True

    return digest.hexdigest() == file_hash

# Download the component, returning path to the downloaded file
def download(component, cache_folder: str):
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
def install_engine(game_path: str, engine_path: str) -> bool:
    print("[*] Installing mods engine...")

    if not is_game_folder(game_path):
        print("[!] GIVEN GAME FOLDER PATH IS INVALID")

        return False

    elif is_engine_installed(game_path):
        print("    - Skipping, already installed")

        return True

    elif not verify_hash(engine_path, mods["engine"]["hash"]):
        print("[!] Mod engine hash mismatched")

        return True

    else:
        with tempfile.TemporaryDirectory(dir = game_path) as temp:
            with zipfile.ZipFile(engine_path, 'r') as file:
                file.extractall(temp)

            shutil.move(f"{temp}/BepInExPack/BepInEx", f"{game_path}/BepInEx")

            os.replace(f"{temp}/BepInExPack/doorstop_config.ini", f"{game_path}/doorstop_config.ini")
            os.replace(f"{temp}/BepInExPack/winhttp.dll", f"{game_path}/winhttp.dll")

        return True

# Uninstall mods engine from the game folder
def uninstall_engine(game_path: str) -> bool:
    print("[*] Uninstalling mods engine...")

    if not is_game_folder(game_path):
        print("[!] GIVEN GAME FOLDER PATH IS INVALID")

        return False

    else:
        shutil.rmtree(f"{game_path}/BepInEx")

        os.remove(f"{game_path}/doorstop_config.ini")
        os.remove(f"{game_path}/winhttp.dll")

        return True

# Install mod to the game folder
def install_mod(game_path: str, mod_path: str, mod_info) -> bool:
    print(f"[*] Installing {mod_info["name"]}...")

    if not is_game_folder(game_path):
        print("[!] GIVEN GAME FOLDER PATH IS INVALID")

        return False

    elif os.path.exists(f"{game_path}/BepInEx/plugins/{mod_info["name"]}"):
        print("    - Skipping, already installed")

        return True

    elif not verify_hash(mod_path, mod_info["hash"]):
        print(f"[!] {mod_info["name"]} hash mismatched")

        return False

    else:
        with zipfile.ZipFile(mod_path, 'r') as file:
            file.extractall(f"{game_path}/BepInEx/plugins/{mod_info["name"]}")

        if mod_info["hook"]:
            print(f"[*] Running {mod_info["name"]} post-install hook...")

            if not mod_info["hook"](game_path, mod_info):
                print(f"[!] Failed to run {mod_info["name"]} post-install hook")

                return False

        return True

# Print help message
def print_help(message: str = ""):
    if message:
        print(message)
        print()

    print("Lethal Zhopa 2026-03-30.2 (year-month-day.edition)")
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
                        print(f"    Mods ({len(extension["mods"])}):")

                        for mod in extension["mods"]:
                            print(f"      - [{mod["name"]}]: {mod["description"]}")

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

                    if not install_engine(sys.argv[2], engine):
                        print()
                        print("[!] Failed to install mod engine")

                        exit(1)

                for mod_info in get_mods_list(sys.argv[3:]):
                    downloaded_file = download(mod_info, cache_folder)

                    if not install_mod(sys.argv[2], downloaded_file, mod_info):
                        print()
                        print(f"[!] Failed to install {mod_info["name"]}")

                        exit(1)

                print()
                print("Installation completed")

        case "remove":
            if len(sys.argv) < 3:
                print_help("Too few arguments passed")

            elif not is_game_folder(sys.argv[2]):
                print_help("The given path is not a valid game folder")

            else:
                if not uninstall_engine(sys.argv[2]):
                    print()
                    print("[!] Failed to uninstall mod engine")

                    exit(1)

                print()
                print("Uninstallation completed")

        case _:
            print_help("Invalid command")
