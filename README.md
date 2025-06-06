# Video Reviewer App (Python + ffpyplayer)

A lightweight desktop tool to review a folder full of videos and tag each one as **Keep**, **Trash**, or **Skip** — with automatic file management and review tracking.

## Features

- ✅ Watch videos with synchronized **audio & video**
- ✅ Tag each video: Keep / Trash / Skip
- ✅ Automatically move trashed videos to a `trash/` folder
- ✅ Resume where you left off (stored in `reviewed.json`)
- ✅ Modern UI with `tkinter.ttk`
- ✅ Keyboard shortcuts:
  - `K`: Keep
  - `T`: Trash
  - `S`: Skip
  - `Space`: Play/Pause
  - `Enter`: Save and go to next

## 📦 Requirements

- Python 3.7+
- [ffpyplayer](https://github.com/matham/ffpyplayer)
- Pillow

Install dependencies:
```bash
pip install ffpyplayer pillow
