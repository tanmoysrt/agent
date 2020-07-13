import os
import requests
import tempfile
from urllib.parse import urlparse


def download_file(url):
    filename = urlparse(url).path.split("/")[-1]
    tempdir = tempfile.mkdtemp(prefix="agent-upload-", suffix=f"-{filename}")
    local_filename = os.path.join(tempdir, filename)

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                f.write(chunk)

    return local_filename
