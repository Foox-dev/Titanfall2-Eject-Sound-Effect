# Titan Eject Sound Effect

This project is a standalone executable that enhances your gaming experience. When the player ejects from a titan in the game, it will play the first 10 seconds of "Free Bird" as a sound effect.

## Features

- Standalone executable: No need to install any additional software.
- Custom sound effect: Plays the first 10 seconds of "Free Bird" when ejecting from a titan.
- Volume Customizer which is used with: "Volume 50%".

## How to Use

1. Download the executable from the [releases page](https://github.com/Foox-dev/freebird-titanfall2/releases).
2. Run the executable in the background while playing the game.
3. Enjoy the custom sound effect when you eject from a titan!

## Dependencies

This project requires the following Python libraries:

- keyboard
- pygame

You can install these libraries using pip:

## Compiling the Source Code

To compile the source code into an executable file, you'll need Python and either PyInstaller or its graphical alternative, auto-py-to-exe. Here are the steps for both methods:

```bash
pip install keyboard pygame
```

### Using PyInstaller

1. Open your terminal or command prompt.
2. Navigate to the directory containing the source code.
3. Run the following command:

```bash
pyinstaller --onefile --add-data "free-bird.mp3;." main.py
```

### Using auto-py-to-exe

1. Install auto-py-to-exe by running the following command in your terminal or command prompt:
  ```bash
  pip install auto-py-to-exe
  ```

2. Launch auto-py-to-exe by running:
  ```bash
  auto-py-to-exe
  ```

3. In the auto-py-to-exe interface, do the following:
   - Select `main.py` as the script to be converted into an executable.
   - Add "free-bird.mp3" to the additional files.
   - Select "icon.ico" as the icon for the executable.

4. Click on the "Convert .py to .exe" button.