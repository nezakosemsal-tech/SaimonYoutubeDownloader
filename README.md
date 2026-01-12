# Saimon YouTube Downloader

A simple and efficient YouTube downloader that supports downloading YouTube videos, mixes, and playlists.

## Features

- ✨ Download single YouTube videos
- 🎵 Download YouTube mixes (auto-generated playlists)
- 📝 Download complete playlists
- 🎧 Audio-only download option (MP3 format)
- 📊 Real-time download progress
- 🎯 Quality selection (360p, 480p, 720p, 1080p, or best)
- 📁 Custom output directory support

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nezakosemsal-tech/SaimonYoutubeDownloader.git
cd SaimonYoutubeDownloader
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Download a single video:
```bash
python downloader.py https://www.youtube.com/watch?v=VIDEO_ID
```

### Download YouTube Mixes

YouTube mixes are auto-generated playlists. You can download them by using the mix URL:
```bash
python downloader.py "https://www.youtube.com/watch?v=VIDEO_ID&list=RDVIDEO_ID"
```

### Download Playlists

```bash
python downloader.py https://www.youtube.com/playlist?list=PLAYLIST_ID
```

### Audio Only

Download only the audio track in MP3 format:
```bash
python downloader.py -a https://www.youtube.com/watch?v=VIDEO_ID
```

### Custom Output Directory

Specify where to save downloaded files:
```bash
python downloader.py -o my_music https://www.youtube.com/watch?v=VIDEO_ID
```

### Video Quality

Choose video quality (360p, 480p, 720p, 1080p):
```bash
python downloader.py -q 720 https://www.youtube.com/watch?v=VIDEO_ID
```

## Command Line Options

```
usage: downloader.py [-h] [-a] [-o OUTPUT] [-q {best,worst,360,480,720,1080}] url

positional arguments:
  url                   YouTube URL (video, mix, or playlist)

optional arguments:
  -h, --help            show this help message and exit
  -a, --audio-only      Download audio only (MP3 format)
  -o OUTPUT, --output OUTPUT
                        Output directory for downloads (default: downloads)
  -q QUALITY, --quality QUALITY
                        Video quality (default: best)
```

## Examples

1. **Download a music video:**
   ```bash
   python downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

2. **Download a YouTube mix as audio:**
   ```bash
   python downloader.py -a "https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ"
   ```

3. **Download a playlist in 720p:**
   ```bash
   python downloader.py -q 720 https://www.youtube.com/playlist?list=PLrAXtmErZgOeiKm4sgNOknGvNjby9efdf
   ```

4. **Download to a specific folder:**
   ```bash
   python downloader.py -o ~/Music/YouTube "https://www.youtube.com/watch?v=VIDEO_ID"
   ```

## Requirements

- Python 3.6+
- yt-dlp
- FFmpeg (optional, required only for audio extraction with `-a` flag)

**Note:** If you plan to use the audio-only download feature (`-a` flag), you need to have FFmpeg installed on your system. You can install it via:
- **Ubuntu/Debian:** `sudo apt install ffmpeg`
- **macOS:** `brew install ffmpeg`
- **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## License

This project is provided as-is for educational purposes.

## Notes

- Downloaded files are saved in the `downloads` folder by default
- The downloader respects YouTube's terms of service
- Make sure you have permission to download content
- Some videos may be restricted based on geographic location or copyright