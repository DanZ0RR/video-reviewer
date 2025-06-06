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


## Usage
1. Run the script:

```bash
python video_reviewer_modern.py

2. Select the folder containing your video files.
3. Use the GUI to review, tag, and manage your videos.

Output Files
- reviewed.json: Tracks what you’ve already reviewed

- trash/: Contains all videos marked as trash

## License
This project is licensed under the MIT License.

## 🤝 Contributions
Feel free to submit issues or pull requests to improve the UI, performance, or features!
