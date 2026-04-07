import zipfile
import os
import time
from pathlib import Path
import threading
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

# ================= GLOBAL =================
DELETE_AFTER = False

stats = {
    "total": 0,
    "extracted": 0,
    "skipped": 0,
    "failed": 0,
    "deleted": 0
}
# ==========================================


def log(msg):
    log_box.insert(tk.END, msg + "\n")
    log_box.see(tk.END)


def delete_zip(zip_path):
    for _ in range(3):
        try:
            os.remove(zip_path)
            stats["deleted"] += 1
            return
        except PermissionError:
            time.sleep(1)
        except:
            return


def extract_zip(zip_path, output_dir):
    folder_name = zip_path.stem

    if output_dir:
        extract_dir = Path(output_dir) / folder_name
    else:
        extract_dir = zip_path.parent / folder_name

    if extract_dir.exists() and any(extract_dir.iterdir()):
        stats["skipped"] += 1
        log(f"⏭ Skipped: {zip_path.name}")
        return

    try:
        extract_dir.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        stats["extracted"] += 1
        log(f"✅ Extracted: {zip_path.name}")

        if DELETE_AFTER:
            delete_zip(zip_path)

    except:
        stats["failed"] += 1
        log(f"❌ Failed: {zip_path.name}")


def update_stats():
    stats_label.config(
        text=f"Total: {stats['total']} | Extracted: {stats['extracted']} | "
             f"Skipped: {stats['skipped']} | Failed: {stats['failed']} | Deleted: {stats['deleted']}"
    )


def process():
    global DELETE_AFTER
    folder = folder_path.get()
    output = output_path.get()
    DELETE_AFTER = delete_var.get()

    if not folder:
        messagebox.showerror("Error", "Select folder first")
        return

    zip_files = list(Path(folder).rglob("*.zip"))
    stats["total"] = len(zip_files)

    if not zip_files:
        log("No ZIP files found.")
        return

    progress["maximum"] = len(zip_files)

    for i, zip_file in enumerate(zip_files, start=1):
        extract_zip(zip_file, output if output else None)
        progress["value"] = i
        update_stats()
        root.update_idletasks()

    log("\n🏁 Completed!")


def start_thread():
    threading.Thread(target=process, daemon=True).start()


def browse_folder():
    folder_path.set(filedialog.askdirectory())


def browse_output():
    output_path.set(filedialog.askdirectory())


# ================= GUI =================
root = tk.Tk()
root.title("ZIP Extractor PRO 🚀")
root.geometry("800x550")
root.configure(bg="#1e1e1e")

folder_path = tk.StringVar()
output_path = tk.StringVar()
delete_var = tk.BooleanVar()

# Style
style = ttk.Style()
style.theme_use('default')
style.configure("TProgressbar", thickness=20)

# Title
tk.Label(root, text="ZIP Extractor PRO", font=("Arial", 16, "bold"), fg="white", bg="#1e1e1e").pack(pady=10)

# Folder
tk.Label(root, text="Select Folder", fg="white", bg="#1e1e1e").pack()
tk.Entry(root, textvariable=folder_path, width=80).pack()
tk.Button(root, text="Browse", command=browse_folder).pack(pady=5)

# Output
tk.Label(root, text="Output Folder (Optional)", fg="white", bg="#1e1e1e").pack()
tk.Entry(root, textvariable=output_path, width=80).pack()
tk.Button(root, text="Browse Output", command=browse_output).pack(pady=5)

# Delete option
tk.Checkbutton(root, text="Delete ZIP after extraction", variable=delete_var,
               fg="white", bg="#1e1e1e", selectcolor="#1e1e1e").pack(pady=5)

# Start button
tk.Button(root, text="Start 🚀", command=start_thread, bg="green", fg="white", width=20).pack(pady=10)

# Progress bar
progress = ttk.Progressbar(root, orient="horizontal", length=600, mode="determinate")
progress.pack(pady=10)

# Stats
stats_label = tk.Label(root, text="Stats will appear here", fg="white", bg="#1e1e1e")
stats_label.pack()

# Log box
log_box = tk.Text(root, height=15, width=95, bg="black", fg="lime")
log_box.pack(pady=10)

root.mainloop()