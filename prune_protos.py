import os
import glob

TFS_PATH = "tensorflow_serving"

def main():
    deps = _get_all_deps()
    _remove_tf_core_protos_except(deps)


def _get_all_deps():
    files = (
        [os.path.join(TFS_PATH, "apis", item) for item in os.listdir(os.path.join(TFS_PATH, "apis"))]
        + [os.path.join(TFS_PATH, "config", item) for item in os.listdir(os.path.join(TFS_PATH, "config"))]
    )

    required_tf_protos = set()
    for filename in files:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line.startswith("import \"tensorflow/"):
                    required_tf_protos.add(line.split("\"")[1])

    while True:
        added = 0
        for proto in list(required_tf_protos):
            with open(proto) as f:
                for line in f:
                    line = line.strip()
                    if line.startswith("import \"tensorflow/"):
                        target_file = line.split("\"")[1]
                        if target_file not in required_tf_protos:
                            required_tf_protos.add(target_file)
                            added += 1
        if added == 0:
            break

    return required_tf_protos


def _remove_tf_core_protos_except(deps):
    files = set(glob.glob("tensorflow/**/*.proto", recursive=True))
    files_to_remove = files - deps
    print(*sorted(list(files_to_remove)), sep='\n')
    c = input("want to remove above files? [y/n]")
    if c != 'y':
        return
    for filename in files_to_remove:
        os.remove(filename)


if __name__ == "__main__":
    main()
