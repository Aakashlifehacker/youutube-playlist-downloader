from pytube import Playlist
import os

# Get the playlist URL and download path from the user
playlist_url = input("Enter YouTube Playlist URL: ")
download_path = input("Enter download path: ")

# Load the playlist and create a directory for it
playlist = Playlist(playlist_url)
playlist_dir = os.path.join(download_path, playlist.title)
os.makedirs(playlist_dir, exist_ok=True)

# Open a file to store the video titles
titles_file = open(os.path.join(playlist_dir, "titles.txt"), "w", encoding="utf-8")

# Download each video and save its title
for video in playlist.videos:
    try:
        # Download the video to the playlist directory
        filename = video.streams.get_lowest_resolution().download(output_path=playlist_dir)

        # Replace any slashes in the title with dashes
        title = video.title.replace("/", "-")

        # Save the video title to the titles file
        titles_file.write(f"{title}\n")

        print(f"Downloaded '{title}' to '{playlist_dir}'.")
    except Exception as e:
        print(f"Error downloading '{video.title}': {e}")

# Close the titles file
titles_file.close()

print("All videos downloaded.")
