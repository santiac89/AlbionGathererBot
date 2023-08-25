# Albion Gathering Bot with YOLOv7 Object Recognition

### Note

This is not a fully functional product and is only being developed for research purposes. Don't expect anything from it :).

## Description

This is a Python-based Albion gathering bot that utilizes YOLOv7 object recognition to identify resources in the game world. The bot allows players to automate the resource gathering process, making it easier and more efficient.

## Requirements

Before running the bot, make sure you have the following requirements installed. You can install them using the provided `requirements.txt` file and `pip`.

```bash
pip install -r requirements.txt
```

## Usage

1. **Download YOLOv7 model**: Unzip [model.rar](https://drive.google.com/file/d/1q-mnNTfcaQPozw-5yn0wIwZ4LJbBw-vc/view?usp=sharing) inside the `model` folder

2. **Run the Main Bot Process**: Launch the main bot process using the following command:

```bash
python main.py
```

Once the bot is running, it will wait for user input. The following commands are available:

- Press **S**: The bot starts looking for resources and initiates the gathering process.
- Press **S** again: The bot stops the gathering process.
- Press **Q**: The bot exits the process.

2. **Run the Object Recognition Model Debugger**: To debug the object recognition model, execute the following command:

```bash
python debug_model.py
```

Running this command will open a window that displays the YOLOv7 object recognition model's output, allowing you to visualize and fine-tune its performance.

## Important Notes

1. This bot is intended for educational and personal use only. The usage of bots in online games may violate the game's terms of service, leading to potential consequences like bans or suspensions. Use at your own risk.

2. The object recognition model might require periodic updates based on game updates or changes in resource appearances. Make sure to keep your model up-to-date for accurate resource identification.

3. Please ensure you are not disrupting other players' experiences or engaging in any unfair practices while using this bot.

4. This bot is compatible with the specific version of YOLOv7 and Albion Online available at the time of creation. Be cautious about potential compatibility issues with newer versions.

## Disclaimer

The Albion Gathering Bot is provided as-is without any warranty. The developers are not responsible for any actions taken by this bot or the consequences of using it. Use the bot responsibly and at your own risk.

