# YouTube-2-MP3-Converter
This is a minimal web interface written in Flask for the youtube-dl script.

## Requirements
* ffmpeg for converting mp4 fiels to mp3 fiels
* The youtube-dl Python script, which is available at https://github.com/rg3/youtube-dl
* python3

## Usage

### Docker
```
docker build -t ydl:latest .
```

```
docker run -d -p 5000:5000 ydl
```
### Without Docker
```
flask db init
```
```
flask db migrate
```
```
flask db upgrade
```