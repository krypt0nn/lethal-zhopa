# Lethal Zhopa

Lethal company mods installation script.

Mods and BepInEx will be cached in the game folder under the `lethal-zhopa-cache` directory to speed up the commands.

Do not use this software if you don't know what are you doing. I will not explain any details or how to run it for you.

All the mods will also be available on the releases page so you could just download the archive from there and extract it to the game folder instead of using this script.

## List available mods extensions

Mods extension is a group of theme related mods and their libraries.

```bash
python3 lethal-zhopa.py list
```

## Setup mods extensions to the game

To install emotes and anime suits extensions:

```bash
python3 lethal-zhopa.py setup 'C:\Games\Lethal Company' emotes anime-suits
```

To install all the available mods from the Lethal Zhopa modpack:

```bash
python3 lethal-zhopa.py setup 'C:\Games\Lethal Company' full
```

This command will automatically install BepInEx modloader as well.

## Remove all the mods from the game

```bash
python3 lethal-zhopa.py remove 'C:\Games\Lethal Company'
```

Author: [Nikita Podvirnyi](https://github.com/krypt0nn)\
Licensed under [Unlicense](LICENSE)
