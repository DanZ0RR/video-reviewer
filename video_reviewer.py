import os
import json
import shutil
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
from ffpyplayer.player import MediaPlayer

VIDEO_EXTS = ('.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm')

class ModernVideoReviewer:
    def __init__(self, root):
        self.root = root
        self.root.title("🎥 Video Reviewer")
        self.root.geometry("800x550")
        self.root.configure(bg="#2e2e2e")
        self.frame_loop_id = None  # for managing update loop

        self.folder = filedialog.askdirectory(title="Select folder with videos")
        if not self.folder:
            messagebox.showerror("Error", "No folder selected.")
            root.quit()
            return

        self.trash_folder = os.path.join(self.folder, "trash")
        os.makedirs(self.trash_folder, exist_ok=True)

        self.reviewed_path = os.path.join(self.folder, "reviewed.json")
        self.reviewed = self.load_reviewed()
        self.video_files = [f for f in os.listdir(self.folder)
                            if f.lower().endswith(VIDEO_EXTS) and f not in self.reviewed]

        self.current_index = 0
        self.selected_action = tk.StringVar(value="keep")
        self.playing = True
        self.user_seek = False

        self.setup_ui()
        self.bind_keys()

        if self.video_files:
            self.load_video()
        else:
            messagebox.showinfo("Done", "All videos left reviewed.")
            root.quit()

    def setup_ui(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        style.configure("TRadiobutton", background="#2e2e2e", foreground="white", font=("Segoe UI", 10))
        style.configure("TLabel", background="#2e2e2e", foreground="white", font=("Segoe UI", 10))

        self.canvas = tk.Canvas(self.root, width=640, height=360, bg="black", highlightthickness=0)
        self.canvas.pack(pady=10)

        self.progress_label = ttk.Label(self.root, text="Video 1 of X")
        self.progress_label.pack()

        self.slider = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", length=640, command=self.seek_video)
        self.slider.pack(pady=5)

        self.controls = ttk.Frame(self.root)
        self.controls.pack(pady=10)

        ttk.Label(self.controls, text="Action:").grid(row=0, column=0, padx=10)
        ttk.Radiobutton(self.controls, text="Keep", variable=self.selected_action, value="keep").grid(row=0, column=1)
        ttk.Radiobutton(self.controls, text="Trash", variable=self.selected_action, value="trash").grid(row=0, column=2)

        self.play_pause_btn = ttk.Button(self.controls, text="Pause", command=self.toggle_play)
        self.play_pause_btn.grid(row=0, column=3, padx=10)

        self.skip_btn = ttk.Button(self.controls, text="Skip", command=self.skip_video)
        self.skip_btn.grid(row=0, column=4, padx=5)

        self.save_btn = ttk.Button(self.controls, text="Save and Next ▶", command=self.save_and_next)
        self.save_btn.grid(row=0, column=5, padx=5)

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def bind_keys(self):
        self.root.bind("<space>", lambda e: self.toggle_play())
        self.root.bind("<Return>", lambda e: self.save_and_next())
        self.root.bind("k", lambda e: self.selected_action.set("keep"))
        self.root.bind("t", lambda e: self.selected_action.set("trash"))
        self.root.bind("s", lambda e: self.skip_video())

    def load_reviewed(self):
        if os.path.exists(self.reviewed_path):
            with open(self.reviewed_path, "r") as f:
                return json.load(f)
        return {}

    def save_reviewed(self):
        with open(self.reviewed_path, "w") as f:
            json.dump(self.reviewed, f, indent=2)

    def load_video(self):
        if self.current_index >= len(self.video_files):
            messagebox.showinfo("Done", "All videos reviewed.")
            self.root.quit()
            return

        # Cancel any previous playback loop
        if self.frame_loop_id:
            self.root.after_cancel(self.frame_loop_id)

        self.selected_action.set("keep")
        self.video_name = self.video_files[self.current_index]
        video_path = os.path.join(self.folder, self.video_name)

        self.player = MediaPlayer(video_path)
        self.playing = True
        self.frame_loop_id = self.root.after(0, self.update_video)
        self.progress_label.config(text=f"Video {self.current_index + 1} of {len(self.video_files)}")

    def update_video(self):
        if self.playing and not self.user_seek:
            frame, val = self.player.get_frame()
            if val == 'eof':
                self.playing = False
                return

            if frame is not None:
                img, t = frame
                w, h = img.get_size()
                img_data = img.to_bytearray()[0]
                image = Image.frombytes('RGB', (w, h), bytes(img_data))
                image = image.resize((640, 360))
                photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                self.canvas.image = photo

        self.frame_loop_id = self.root.after(30, self.update_video)

    def seek_video(self, val):
        self.user_seek = True
        was_playing = self.playing
        self.playing = False
        self.player.set_pause(True)

        meta = self.player.get_metadata()
        duration = meta.get('duration', 0)
        if duration == 0:
            self.user_seek = False
            return

        percent = float(val) / 100
        seek_seconds = percent * duration
        self.player.seek(seek_seconds, relative=False)

        for _ in range(10):
            frame, val = self.player.get_frame()
            if frame is not None and val != 'eof':
                img, _ = frame
                w, h = img.get_size()
                img_data = img.to_bytearray()[0]
                image = Image.frombytes('RGB', (w, h), bytes(img_data))
                image = image.resize((640, 360))
                photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
                self.canvas.image = photo
                break
            self.root.update()

        self.user_seek = False
        self.playing = was_playing
        self.player.set_pause(not self.playing)

    def toggle_play(self):
        self.playing = not self.playing
        self.player.set_pause(not self.playing)
        self.play_pause_btn.config(text="Play" if not self.playing else "Pause")

    def save_and_next(self):
        action = self.selected_action.get()
        video_path = os.path.join(self.folder, self.video_name)

        try:
            if hasattr(self, 'player'):
                self.player.close_player()

            if action == "trash":
                os.replace(video_path, os.path.join(self.trash_folder, self.video_name))
                self.reviewed[self.video_name] = "trash"
            else:
                self.reviewed[self.video_name] = "keep"

        except Exception as e:
            messagebox.showerror("Error", f"Could not process file: {e}")
            return

        self.save_reviewed()
        self.current_index += 1
        self.load_video()

    def skip_video(self):
        if hasattr(self, 'player'):
            self.player.close_player()
        self.current_index += 1
        self.load_video()

    def on_close(self):
        if hasattr(self, 'player'):
            self.player.close_player()
        if self.frame_loop_id:
            self.root.after_cancel(self.frame_loop_id)
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernVideoReviewer(root)
    root.mainloop()
