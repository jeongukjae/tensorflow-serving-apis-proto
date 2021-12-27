import base64
import os
import shutil

import httpx
from absl import logging, flags, app

TFS_API_PATH = "tensorflow_serving/apis"

FLAGS = flags.FLAGS
flags.DEFINE_string("tfs_version", "2.6.2", "Target TensorFlow Serving version")


def main(argv):
    logging.info("Remove api path")
    if os.path.exists(TFS_API_PATH):
        shutil.rmtree(TFS_API_PATH)

    target_url = f"https://api.github.com/repos/tensorflow/serving/git/trees/{FLAGS.tfs_version}?recursive=1"
    logging.info(f"target url: {target_url}")

    response = httpx.get(target_url).json()
    items = [item for item in response["tree"] if _is_api_file(item)]

    logging.info("Download all required files")
    os.makedirs(TFS_API_PATH, exist_ok=True)
    for item in items:
        directory = os.path.dirname(item["path"])
        if TFS_API_PATH != directory:
            os.makedirs(directory, exist_ok=True)

        try:
            with open(item["path"], "wb") as f:
                content = httpx.get(item["url"]).json()
                content = base64.b64decode(content["content"])
                f.write(content)
        except:
            print(item)


def _is_api_file(item: dict) -> bool:
    if not item["path"].startswith(TFS_API_PATH):
        return False

    if not item["path"].endswith(".proto"):
        return False

    if item["type"] != "blob":
        return False

    return True


if __name__ == "__main__":
    app.run(main)
