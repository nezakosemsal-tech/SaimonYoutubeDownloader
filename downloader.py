#!/usr/bin/env python3
"""
Saimon YouTube Downloader
A simple YouTube downloader that supports downloading YouTube mixes and playlists.
"""

import argparse
import sys
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("Error: yt-dlp is not installed.")
    print("Please install it using: pip install yt-dlp")
    sys.exit(1)


class YouTubeDownloader:
    """Simple YouTube downloader for videos and mixes."""
    
    def __init__(self, output_dir="downloads"):
        """
        Initialize the YouTube downloader.
        
        Args:
            output_dir: Directory where downloaded files will be saved
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def download(self, url, audio_only=False, quality="best"):
        """
        Download a YouTube video, mix, or playlist.
        
        Args:
            url: YouTube URL (video, mix, or playlist)
            audio_only: If True, download only audio
            quality: Video quality (best, worst, or specific resolution)
        """
        ydl_opts = {
            'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
            'progress_hooks': [self._progress_hook],
        }
        
        if audio_only:
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        else:
            if quality == "best":
                ydl_opts['format'] = 'bestvideo+bestaudio/best'
            elif quality == "worst":
                ydl_opts['format'] = 'worst'
            else:
                # Remove 'p' suffix if present (e.g., '720p' -> '720')
                quality_num = quality[:-1] if quality.endswith('p') else quality
                ydl_opts['format'] = f'bestvideo[height<={quality_num}]+bestaudio/best[height<={quality_num}]'
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\nFetching video information from: {url}")
                info = ydl.extract_info(url, download=False)
                
                if 'entries' in info:
                    print(f"\nFound playlist/mix with {len(info['entries'])} videos")
                    print("Starting download...\n")
                else:
                    print(f"\nDownloading: {info.get('title', 'Unknown')}")
                    duration = info.get('duration') or 0
                    print(f"Duration: {duration // 60} minutes\n")
                
                ydl.download([url])
                print("\n✓ Download completed successfully!")
                print(f"Files saved to: {self.output_dir.absolute()}")
                
        except yt_dlp.utils.DownloadError as e:
            print(f"\n✗ Download error: {str(e)}", file=sys.stderr)
            sys.exit(1)
        except yt_dlp.utils.ExtractorError as e:
            print(f"\n✗ Error extracting video information: {str(e)}", file=sys.stderr)
            sys.exit(1)
        except KeyboardInterrupt:
            print("\n\n✗ Download cancelled by user", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"\n✗ Unexpected error: {str(e)}", file=sys.stderr)
            sys.exit(1)
    
    def _progress_hook(self, d):
        """Hook to display download progress."""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0%')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"\rDownloading: {percent} at {speed} (ETA: {eta})", end='', flush=True)
        elif d['status'] == 'finished':
            print(f"\r✓ Download finished, processing...", flush=True)


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='Saimon YouTube Downloader - Download YouTube videos, mixes, and playlists',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Download a single video
  python downloader.py https://www.youtube.com/watch?v=VIDEO_ID
  
  # Download a YouTube mix
  python downloader.py https://www.youtube.com/watch?v=VIDEO_ID&list=RDVIDEO_ID
  
  # Download a playlist
  python downloader.py https://www.youtube.com/playlist?list=PLAYLIST_ID
  
  # Download audio only
  python downloader.py -a https://www.youtube.com/watch?v=VIDEO_ID
  
  # Specify output directory
  python downloader.py -o my_videos https://www.youtube.com/watch?v=VIDEO_ID
        """
    )
    
    parser.add_argument(
        'url',
        help='YouTube URL (video, mix, or playlist)'
    )
    
    parser.add_argument(
        '-a', '--audio-only',
        action='store_true',
        help='Download audio only (MP3 format)'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='downloads',
        help='Output directory for downloads (default: downloads)'
    )
    
    parser.add_argument(
        '-q', '--quality',
        default='best',
        choices=['best', 'worst', '360', '480', '720', '1080'],
        help='Video quality (default: best)'
    )
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("Saimon YouTube Downloader")
    print("=" * 60)
    
    downloader = YouTubeDownloader(output_dir=args.output)
    downloader.download(
        url=args.url,
        audio_only=args.audio_only,
        quality=args.quality
    )


if __name__ == '__main__':
    main()
