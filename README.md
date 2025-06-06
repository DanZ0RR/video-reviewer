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

## 🚀 Usage

Run the script:

```bash
python video_reviewer_modern.py
```

Then:

- Select the folder containing your video files.
- Use the GUI to review, tag, and manage your videos.
- Press `Save and Next` to go to the next video.
- Use keyboard shortcuts for speed (`K`, `T`, `S`, `Space`, `Enter`).


## 📁 Output Files

```text
reviewed.json     # Tracks which videos have been reviewed
trash/            # Contains videos marked as 'trash'
```

---

## 🛠 Project Structure

```text
video-reviewer/
├── video_reviewer_modern.py     # Main script
├── reviewed.json                # Created automatically
├── trash/                       # Contains trashed videos
├── LICENSE
└── README.md
```

---

## License

This project is licensed under the [MIT License](LICENSE).

You can use, modify, and share it freely — just include attribution.

---

## Contributions

Contributions are welcome!

- Open an [issue](https://github.com/DanZ0RR/video-reviewer/issues) for bugs or suggestions
- Fork the repo and submit a pull request with improvements
- You can help improve UI, add features, or write docs

---

## Acknowledgments

- [ffpyplayer](https://github.com/matham/ffpyplayer) for media decoding
- The open-source Python and Tkinter community

---

> ⭐ Star this repo if you find it useful — it helps more people discover it!
