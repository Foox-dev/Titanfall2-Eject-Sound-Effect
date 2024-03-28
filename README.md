# Titan Eject Sound Effect

This project is a standalone executable that enhances your gaming experience. When the player ejects from a titan in the game, it will play the first 10 seconds of "Free Bird" as a sound effect.

## Features

- Standalone executable: No need to install any additional software.
- Custom sound effect: Plays the first 10 seconds of "Free Bird" when ejecting from a titan.

## How to Use

1. Download the executable from the [releases page](<link to your releases page>).
2. Run the executable in the background while playing the game.
3. Enjoy the custom sound effect when you eject from a titan!

## Building from Source

If you want to build the executable from source, you will need Python and PyInstaller. Run the following command to build the executable:

```bash
pyinstaller --onefile --add-data "free-bird.mp3;." main.py
