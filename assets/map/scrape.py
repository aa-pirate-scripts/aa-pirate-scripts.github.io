import requests
import shutil
from multiprocessing.pool import ThreadPool
import os.path

# Select which zoom level you want to scrape
SELECT = 'Z9'

# Do not change anything below this === XXX
map_img_url_template = 'http://ongab.ru/media/map/19/' + SELECT + '/{}/{}.jpg'

tiles_bounds = {'Z9': [(x, y) for x in range(256, 259) for y in range(256, 259)],
					'Z10': [(x, y) for x in range(512, 518) for y in range(512, 518)],
					'Z11': [(x, y) for x in range(1024, 1036) for y in range(1024, 1036)],
					'Z12': [(x, y) for x in range(2048, 2072) for y in range(2048, 2072)],
					'Z13': [(x, y) for x in range(4096, 4144) for y in range(4096, 4144)],
					'Z14': [(x, y) for x in range(8192, 8288) for y in range(8192, 8288)]}
					
def download_img(tile):
    x, y = tile
    img_url = map_img_url_template.format(y, x)
    filename = SELECT + '/{}-{}.jpg'.format(x, y)
    r = requests.get(img_url, stream=True)

    if os.path.exists(filename):
        return 'skipped ' + filename

    if r.status_code == 200:
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)

        return 'downloaded ' + filename
    else:
        return 'error ' + filename

results = ThreadPool(32).imap_unordered(download_img, tiles_bounds[SELECT])
for result in results:
    print(result)
