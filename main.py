import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# Initialize translator
translator = Translator()

# Language choices mapping names to standard ISO language codes
LANGUAGES = {
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Kannada": "kn",
    "Bengali": "bn"
}

def handle_translation():
    input_text = entry_text.get("1.0", tk.END).strip()
    target_lang_name = combo_language.get()
    
    if not input_text:
        messagebox.showwarning("Empty Input", "Please enter some English text to translate!")
        return
        
    try:
        lang_code = LANGUAGES[target_lang_name]
        translated = translator.translate(input_text, dest=lang_code)
        
        # Display the result in the output box
        text_output.config(state=tk.NORMAL)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated.text)
        text_output.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")

# --- UI Setup ---
root = tk.Tk()
root.title("Bhasha Bridge App 🚀")
root.geometry("500x450")
root.configure(padx=20, pady=20)

# Input section label
label_input = tk.Label(root, text="Enter English Text:", font=("Arial", 11, "bold"))
label_input.pack(anchor="w", pady=(0,5))

entry_text = tk.Text(root, height=4, width=55, font=("Arial", 10))
entry_text.pack(fill="x", pady=(0,15))

# Dropdown language selector section
label_lang = tk.Label(root, text="Select Target Language:", font=("Arial", 11, "bold"))
label_lang.pack(anchor="w", pady=(0,5))

combo_language = ttk.Combobox(root, values=list(LANGUAGES.keys()), state="readonly", font=("Arial", 10))
combo_language.set("Hindi")  # default choice value
combo_language.pack(fill="x", pady=(0,15))

# Action Button
btn_translate = tk.Button(root, text="Translate Now", bg="#007ACC", fg="white", 
                          font=("Arial", 11, "bold"), command=handle_translation)
btn_translate.pack(fill="x", height=2, pady=(0,15))

# Output section display
label_output = tk.Label(root, text="Translated Output:", font=("Arial", 11, "bold"))
label_output.pack(anchor="w", pady=(0,5))

text_output = tk.Text(root, height=4, width=55, font=("Arial", 11), bg="#F0F0F0", state=tk.DISABLED)
text_output.pack(fill="x")

# Fire up the application loop window
root.mainloop()
