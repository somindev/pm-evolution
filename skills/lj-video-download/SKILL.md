---
name: lj-video-download
description: Download videos from any URL using yt-dlp. Supports Xiaohongshu, Bilibili, YouTube, Douyin, Twitter/X, Weibo, and 1000+ other platforms.
---

# Video Download Skill

Download videos from any platform supported by yt-dlp.

## When to Use

Trigger when the user:
- Provides a video URL and asks to download it
- Says "下载视频", "保存视频", "download video", "save video"
- Asks to extract audio from a video URL
- Mentions getting video content from a link

## Prerequisites

**yt-dlp** must be installed. Check with `yt-dlp --version`. If not installed, guide the user:
```bash
brew install yt-dlp
```

## Workflow

### Step 1: Validate the URL

Confirm the user provided a valid URL. Common supported platforms:
- **小红书**: `xiaohongshu.com/explore/...`
- **B站**: `bilibili.com/video/...` or `b23.tv/...`
- **YouTube**: `youtube.com/watch?v=...` or `youtu.be/...`
- **抖音**: `douyin.com/video/...`
- **Twitter/X**: `x.com/.../status/...` or `twitter.com/.../status/...`
- **微博**: `weibo.com/...`

### Step 2: Get Video Info

Before downloading, fetch video metadata to confirm it's the right content:

```bash
yt-dlp --dump-json --no-playlist "<URL>"
```

From the JSON output, extract and present to the user:
- `title` - Video title
- `duration` - Duration in seconds (convert to mm:ss)
- `uploader` - Channel/author name
- `description` - First 100 chars of description (optional)
- `thumbnail` - Thumbnail URL

Show this info and ask the user to confirm before downloading.

### Step 3: Download

Use these default options:

```bash
yt-dlp \
  --no-playlist \
  --concurrent-fragments 4 \
  --newline \
  -o "%(title).80s.%(ext)s" \
  "<URL>"
```

**Option explanations:**
| Option | Purpose |
|--------|---------|
| `--no-playlist` | Only download the single video, not an entire playlist |
| `--concurrent-fragments 4` | Speed up download with parallel fragment downloads |
| `--newline` | Better progress output formatting |
| `%(title).80s.%(ext)s` | Truncate title to 80 chars to avoid path length issues |

### Step 4: Report Result

After download, report:
- File name and full path
- File size (use `ls -lh` on the downloaded file)
- Duration of the video

## Special Cases

### Audio Only

If the user asks for audio/music/MP3:
```bash
yt-dlp \
  --no-playlist \
  -x --audio-format mp3 --audio-quality 0 \
  --newline \
  -o "%(title).80s.%(ext)s" \
  "<URL>"
```

### Specify Quality

If the user wants a specific quality:
- Highest quality: add `-f bestvideo+bestaudio/best`
- Smallest file: add `-f worst`
- Specific resolution: add `-f "bestvideo[height<=?720]+bestaudio/best[height<=?720]/worst"`

### Custom Output Path

If the user specifies a save location, use `-o "<path>/%(title).80s.%(ext)s"`.

### Subtitles

If the user asks for subtitles:
```bash
yt-dlp --write-subs --sub-langs "zh-Hans,zh,en" --embed-subs --no-playlist -o "%(title).80s.%(ext)s" "<URL>"
```

### Playlist Download

If the user explicitly wants to download a playlist, remove `--no-playlist` and use:
```bash
yt-dlp \
  --concurrent-fragments 4 \
  --newline \
  -o "%(playlist_title)s/%(playlist_index)03d - %(title).80s.%(ext)s" \
  "<URL>"
```

## Error Handling

- **403/Authentication error**: Some platforms require cookies. Suggest `yt-dlp --cookies-from-browser chrome` or `--cookies-from-browser safari`
- **Geo-restriction**: Suggest using a proxy: `yt-dlp --proxy socks5://127.0.0.1:1080`
- **Rate limiting**: Add `--sleep-requests 1 --sleep-interval 5` to slow down requests
- **yt-dlp needs update**: Suggest `brew upgrade yt-dlp` or `pip3 install -U yt-dlp`
- **Video not found**: The URL may be private, deleted, or region-locked

## Notes

- Videos are saved to the **current working directory** by default
- If the download takes more than 2 minutes, use the background run feature
- For very large files (>500MB), consider warning the user about file size before downloading
