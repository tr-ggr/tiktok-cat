
# Cat Compilation TikTok Creator Bot  

This is a semi-automatic bot designed to create TikTok videos featuring cute cat compilations. The script selects short video clips, applies effects, concatenates them, and overlays a background audio track. The output is a ready-to-upload TikTok video.  

---

## Features  

1. **Dynamic Video Selection**: Automatically selects a subset of raw videos from the `raw_videos` directory based on the duration of the background audio track.  
2. **TikTok-Optimized Format**: Processes videos to fit TikTok's resolution (1080x1920) and formats them into short clips.  
3. **Speed Effects**: Speeds up the video clips by 2x for a dynamic, engaging effect.  
4. **Audio Integration**: Merges the video compilation with a selected background audio track (`myloveisallmine_spedup.mp3`).  
5. **Automatic Filename Management**: Ensures generated video filenames are unique (e.g., `part1.mp4`, `part2.mp4`, etc.).  
6. **Optional Cleanup**: Deletes the raw video files after processing to save space.  

---

## Requirements  

### Install Dependencies  

Make sure you have Python installed. Install the required library:  

```bash
pip install moviepy
```  

### Folder Structure  

Ensure the following directory structure:  

```
project/
├── raw_videos/
│   ├── (all raw video files here)
├── audios/
│   ├── myloveisallmine_spedup.mp3
├── script.py
```

---

## How It Works  

1. **Setup**:  
   Place your raw cat video clips in the `raw_videos` folder.  
   Place the audio file (`myloveisallmine_spedup.mp3`) in the `audios` folder.  

2. **Run the Script**:  
   Execute the script with:  
   ```bash
   python script.py
   ```  

3. **Output**:  
   - The script will generate a TikTok-ready video (e.g., `part1.mp4`) in the root directory.  
   - Raw video files will be deleted after the compilation is created.  

---

## Code Workflow  

### Main Steps  

1. **File Selection**:  
   - Scans the `raw_videos` directory.  
   - Selects clips based on the audio duration (3 seconds per clip).  

2. **Video Editing**:  
   - Speeds up each video clip by 2x.  
   - Trims clips to a maximum duration of 3 seconds.  
   - Resizes videos to 1080x1920 for TikTok.  

3. **Filename Management**:  
   - Automatically assigns a unique name to the output video (`part1.mp4`, `part2.mp4`, etc.).  

4. **Audio Synchronization**:  
   - Combines the processed video with the background audio.  

5. **Cleanup**:  
   - Deletes the processed raw video files after the final video is created.  

---

## Notes  

1. **Audio File**:  
   Ensure `myloveisallmine_spedup.mp3` exists in the `audios` folder. You can replace it with any other audio file as long as the filename is updated in the script.  

2. **Raw Video Files**:  
   Place only the raw video files you want to process in the `raw_videos` directory.  

3. **Error Handling**:  
   If the script encounters an error or doesn't generate the output, check the following:  
   - Ensure the `raw_videos` directory contains valid video files.  
   - Verify that `myloveisallmine_spedup.mp3` exists and is accessible.  
   - Check for any permission issues when accessing files.  

---

## Example Output  

- Input:  
  - Raw video files in `raw_videos/`.  
  - Background audio (`myloveisallmine_spedup.mp3`).  

- Output:  
  - Compiled video file (e.g., `part1.mp4`) ready for TikTok.  

Happy TikTok creation!
