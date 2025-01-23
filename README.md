# Mouse Tickler Script

This Python script automatically moves the mouse pointer at a specified interval to prevent screensavers or idle states.

## Features

- **Customizable Interval**: Enter a positive number of seconds for the interval between mouse moves.  
- **Countdown Timer**: Displays how long until the next mouse move.  
- **Stopwatch**: Displays the elapsed time since the script was started.  
- **Start/Stop Control**: Easily start or stop the script.

## How It Works

- When you click **Start**, the script:
  1. Reads your desired time interval.
  2. Moves the mouse slightly whenever the countdown reaches zero.
  3. Resets the countdown and repeats.

- The **Stop** button stops the mouse movement, resets the countdown, and clears the stopwatch display.

## Requirements

- Python 3.x
- See [requirements.txt](requirements.txt) for a list of Python modules needed.

## Usage

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Script**:
   ```bash
   python mouse_mover.py
   ```

3. **Set an Interval**:
   - Enter a positive integer (e.g., 30) in the Interval text box.
   - Click Start to begin moving the mouse periodically.
   - Click Stop to halt mouse movements.


## Troubleshooting
    
- If you receive an error about missing dependencies, make sure you have successfully installed all required modules from the requirements.txt file.
- On some platforms (e.g., macOS), pyautogui may require additional libraries for accessibility. Follow any prompts or consult the PyAutoGUI documentation for more details.
