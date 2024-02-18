import photoscript
import os

photoslib = photoscript.PhotosLibrary()

photoslib.activate()
print(f"Running Photos version: {photoslib.version}")

album = photoslib.album("_iPhone")
photos = album.photos()

for photo in photos:
    if 'synced' not in photo.keywords:
        photo.keywords = photo.keywords + ['synced']
        dest = f"/Users/tball/Sync/photos/{photo.date.strftime('%Y/%Y-%m-%B')}/iPhone"
        os.makedirs(dest, exist_ok=True)
        print(f"Exporting {photo.filename} to {dest}")
        photo.export(dest, original=True)

photoslib.quit()
