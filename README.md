# Model Training GUI

A dark-themed GUI application built with Python Tkinter for managing machine learning model training configurations and monitoring training progress.

## Features

- **Dark Theme Interface**: Modern dark theme for comfortable extended use
- **Configuration Management**: Easy-to-use settings panel for all training parameters
- **Real-time Console**: Live output console with color-coded messages
- **Settings Persistence**: Automatically saves and loads your configuration settings
- **File Browser Integration**: Built-in file/folder browser for selecting paths
- **Device Selection**: Choose between CPU and GPU training
- **Validation**: Input validation for required fields

## Screenshots

The application features a clean, dark interface with:
- Settings panel for model configuration
- Real-time console output with timestamps
- Intuitive controls for starting training and managing settings

## Requirements

- Python 3.6 or higher
- tkinter (usually included with Python)
- No additional dependencies required

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/model-training-gui.git
cd model-training-gui
```

2. Run the application:
```bash
python main.py
```

## Usage

### Configuration Settings

The GUI provides the following configuration options:

- **Model Save Path**: Directory where trained models will be saved
- **Model Name**: Name for your model
- **Hugging Face Token**: Your HF token for accessing private models/datasets
- **Dataset Path**: Path to your training dataset
- **Finetune Model**: Enable/disable finetuning mode
- **Trust Remote Code**: Allow execution of remote code (use with caution)
- **Low CPU Memory Usage**: Optimize for systems with limited RAM
- **Device**: Choose between CPU or GPU training

### Getting Started

1. **Set Required Paths**: Use the Browse buttons to select your model save directory and dataset path
2. **Configure Model**: Enter your model name and any required tokens
3. **Adjust Settings**: Configure checkboxes and device selection as needed
4. **Save Settings**: Click "Save Settings" to persist your configuration
5. **Start Training**: Click "Start Training" to begin (implement your training logic)

### Settings Persistence

Settings are automatically saved to `settings.json` in the application directory and will be restored when you restart the application.

## Customization

### Adding Training Logic

The `start_training()` method in the `DarkModeApp` class is where you should implement your actual model training code. Currently, it validates the configuration and logs the start of training.

### Modifying the Interface

- **Colors**: Modify the `self.colors` dictionary to change the theme colors
- **Layout**: Adjust the GUI layout in the `create_gui()` method
- **Settings**: Add new configuration options by extending the `self.settings` dictionary and creating corresponding UI elements

### Color Scheme

The application uses the following color palette:
- Background: `#2B2B2B`
- Text: `#FFFFFF`
- Buttons: `#404040`
- Input Fields: `#333333`
- Console: `#1E1E1E`
- Success Messages: `#50FA7B`
- Error Messages: `#FF5555`
- Info Messages: `#BD93F9`

## File Structure

```
model-training-gui/
├── main.py              # Main application file
├── settings.json        # Auto-generated settings file
└── README.md           # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions:

1. Check the console output for error messages
2. Ensure all required fields are filled
3. Verify file paths exist and are accessible
4. Open an issue on GitHub with details about your problem

## Future Enhancements

- [ ] Progress bar for training status
- [ ] Model validation metrics display
- [ ] Export/import configuration presets
- [ ] Integration with popular ML frameworks
- [ ] Training history and logs viewer
- [ ] Real-time training metrics visualization

## Acknowledgments

- Built with Python Tkinter for cross-platform compatibility
- Inspired by modern dark theme design principles
- Designed for machine learning practitioners and researchers
