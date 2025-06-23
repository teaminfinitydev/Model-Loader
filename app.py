import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
import json
from pathlib import Path
import os
from datetime import datetime

class DarkModeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Model Training GUI")
        
        self.colors = {
            'bg': '#2B2B2B',
            'fg': '#FFFFFF',
            'button': '#404040',
            'entry': '#333333',
            'console_bg': '#1E1E1E',
            'success': '#50FA7B',
            'error': '#FF5555',
            'info': '#BD93F9'
        }

        self.root.configure(bg=self.colors['bg'])
        self.root.geometry('1000x800')
        
        self.settings = {
            'model_save_path': '',
            'model_name': '',
            'hf_token': '',
            'finetune': False,
            'device': 'cpu',
            'dataset_path': '',
            'trust_remote_code': False,
            'low_cpu_mem_usage': True
        }
        
        self.create_gui()
        self.load_settings()

    def create_gui(self):
        # Create main frames
        self.settings_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.settings_frame.pack(fill='x', padx=10, pady=5)
        
        self.console_frame = tk.Frame(self.root, bg=self.colors['bg'])
        self.console_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Settings Section
        self.create_settings_section()
        
        # Console Section
        self.create_console_section()
        
        # Control Buttons
        self.create_control_buttons()

    def create_settings_section(self):
        # Style configuration
        style = ttk.Style()
        style.configure('Dark.TLabel', background=self.colors['bg'], foreground=self.colors['fg'])
        style.configure('Dark.TEntry', fieldbackground=self.colors['entry'], foreground=self.colors['fg'])
        style.configure('Dark.TCheckbutton', background=self.colors['bg'], foreground=self.colors['fg'])
        
        # Model Settings
        settings_label = ttk.Label(self.settings_frame, text="Settings", style='Dark.TLabel', font=('Arial', 12, 'bold'))
        settings_label.pack(anchor='w', pady=(0, 10))
        
        # Create settings fields
        self.create_path_setting("Model Save Path:", 'model_save_path')
        self.create_entry_setting("Model Name:", 'model_name')
        self.create_entry_setting("Hugging Face Token:", 'hf_token')
        self.create_path_setting("Dataset Path:", 'dataset_path')
        
        # Checkboxes and Radio buttons
        self.create_checkbox_setting("Finetune Model", 'finetune')
        self.create_checkbox_setting("Trust Remote Code", 'trust_remote_code')
        self.create_checkbox_setting("Low CPU Memory Usage", 'low_cpu_mem_usage')
        
        # Device selection
        device_frame = tk.Frame(self.settings_frame, bg=self.colors['bg'])
        device_frame.pack(fill='x', pady=5)
        
        device_label = ttk.Label(device_frame, text="Device:", style='Dark.TLabel')
        device_label.pack(side='left')
        
        self.device_var = tk.StringVar(value=self.settings['device'])
        cpu_radio = tk.Radiobutton(device_frame, text="CPU", variable=self.device_var, value="cpu",
                                  bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['button'])
        gpu_radio = tk.Radiobutton(device_frame, text="GPU", variable=self.device_var, value="gpu",
                                  bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['button'])
        
        cpu_radio.pack(side='left', padx=10)
        gpu_radio.pack(side='left')

    def create_path_setting(self, label_text, setting_key):
        frame = tk.Frame(self.settings_frame, bg=self.colors['bg'])
        frame.pack(fill='x', pady=5)
        
        label = ttk.Label(frame, text=label_text, style='Dark.TLabel')
        label.pack(side='left')
        
        entry = tk.Entry(frame, bg=self.colors['entry'], fg=self.colors['fg'])
        entry.pack(side='left', fill='x', expand=True, padx=(5, 5))
        
        browse_btn = tk.Button(frame, text="Browse", bg=self.colors['button'], fg=self.colors['fg'],
                             command=lambda: self.browse_path(entry, setting_key))
        browse_btn.pack(side='right')
        
        setattr(self, f"{setting_key}_entry", entry)

    def create_entry_setting(self, label_text, setting_key):
        frame = tk.Frame(self.settings_frame, bg=self.colors['bg'])
        frame.pack(fill='x', pady=5)
        
        label = ttk.Label(frame, text=label_text, style='Dark.TLabel')
        label.pack(side='left')
        
        entry = tk.Entry(frame, bg=self.colors['entry'], fg=self.colors['fg'])
        entry.pack(side='left', fill='x', expand=True, padx=5)
        
        setattr(self, f"{setting_key}_entry", entry)

    def create_checkbox_setting(self, label_text, setting_key):
        var = tk.BooleanVar(value=self.settings[setting_key])
        checkbox = tk.Checkbutton(self.settings_frame, text=label_text, variable=var,
                                bg=self.colors['bg'], fg=self.colors['fg'], selectcolor=self.colors['button'])
        checkbox.pack(anchor='w', pady=2)
        setattr(self, f"{setting_key}_var", var)

    def create_console_section(self):
        console_label = ttk.Label(self.console_frame, text="Console Output", style='Dark.TLabel', font=('Arial', 12, 'bold'))
        console_label.pack(anchor='w', pady=(0, 5))
        
        self.console = scrolledtext.ScrolledText(self.console_frame, height=15, 
                                               bg=self.colors['console_bg'], fg=self.colors['fg'],
                                               font=('Courier', 10))
        self.console.pack(fill='both', expand=True)

    def create_control_buttons(self):
        button_frame = tk.Frame(self.root, bg=self.colors['bg'])
        button_frame.pack(fill='x', padx=10, pady=10)
        
        save_btn = tk.Button(button_frame, text="Save Settings", command=self.save_settings,
                           bg=self.colors['button'], fg=self.colors['fg'])
        save_btn.pack(side='left', padx=5)
        
        start_btn = tk.Button(button_frame, text="Start Training", command=self.start_training,
                            bg=self.colors['button'], fg=self.colors['fg'])
        start_btn.pack(side='left', padx=5)
        
        clear_btn = tk.Button(button_frame, text="Clear Console", command=self.clear_console,
                            bg=self.colors['button'], fg=self.colors['fg'])
        clear_btn.pack(side='right', padx=5)

    def browse_path(self, entry_widget, setting_key):
        if 'dataset' in setting_key:
            path = filedialog.askdirectory(title=f"Select {setting_key.replace('_', ' ').title()}")
        else:
            path = filedialog.askdirectory(title=f"Select {setting_key.replace('_', ' ').title()}")
        
        if path:
            entry_widget.delete(0, tk.END)
            entry_widget.insert(0, path)

    def save_settings(self):
        # Update settings from GUI
        self.settings.update({
            'model_save_path': self.model_save_path_entry.get(),
            'model_name': self.model_name_entry.get(),
            'hf_token': self.hf_token_entry.get(),
            'dataset_path': self.dataset_path_entry.get(),
            'finetune': self.finetune_var.get(),
            'trust_remote_code': self.trust_remote_code_var.get(),
            'low_cpu_mem_usage': self.low_cpu_mem_usage_var.get(),
            'device': self.device_var.get()
        })
        
        # Save to JSON file
        settings_path = Path('settings.json')
        with open(settings_path, 'w') as f:
            json.dump(self.settings, f, indent=4)
        
        self.log_message("Settings saved successfully!", 'success')

    def load_settings(self):
        settings_path = Path('settings.json')
        if settings_path.exists():
            try:
                with open(settings_path, 'r') as f:
                    saved_settings = json.load(f)
                    self.settings.update(saved_settings)
                    
                # Update GUI with loaded settings
                self.model_save_path_entry.insert(0, self.settings['model_save_path'])
                self.model_name_entry.insert(0, self.settings['model_name'])
                self.hf_token_entry.insert(0, self.settings['hf_token'])
                self.dataset_path_entry.insert(0, self.settings['dataset_path'])
                self.finetune_var.set(self.settings['finetune'])
                self.trust_remote_code_var.set(self.settings['trust_remote_code'])
                self.low_cpu_mem_usage_var.set(self.settings['low_cpu_mem_usage'])
                self.device_var.set(self.settings['device'])
                
                self.log_message("Settings loaded successfully!", 'success')
            except Exception as e:
                self.log_message(f"Error loading settings: {str(e)}", 'error')

    def log_message(self, message, level='info'):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        color = {
            'success': self.colors['success'],
            'error': self.colors['error'],
            'info': self.colors['info']
        }.get(level, self.colors['fg'])
        
        self.console.tag_config(level, foreground=color)
        self.console.insert(tk.END, f"[{timestamp}] {message}\n", level)
        self.console.see(tk.END)

    def clear_console(self):
        self.console.delete(1.0, tk.END)
        self.log_message("Console cleared", 'info')

    def start_training(self):
        # Validate settings
        required_fields = ['model_save_path', 'model_name', 'dataset_path']
        missing_fields = [field for field in required_fields if not self.settings[field]]
        
        if missing_fields:
            self.log_message(f"Missing required fields: {', '.join(missing_fields)}", 'error')
            return
        
        # Log training configuration
        self.log_message("Starting training with configuration:", 'info')
        for key, value in self.settings.items():
            self.log_message(f"{key}: {value}", 'info')
        
        self.log_message("Training started...", 'success')

if __name__ == "__main__":
    root = tk.Tk()
    app = DarkModeApp(root)
    root.mainloop()
