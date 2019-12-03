"""
This file checks if packages are signed and dumps it to data/
"""

import os
import sys
import datetime
import json


DATA_ROOT = "data"


def main():
    pkgbuild_root = os.path.abspath(sys.argv[1])
    packages_root = os.path.join(pkgbuild_root, "packages")
    community_root = os.path.join(pkgbuild_root, "community")
    check_roots = [packages_root, community_root]

    now = datetime.datetime.now()
    today = "-".join([str(now.year), str(now.month), str(now.day)])
    output_file_name = "package-signed-check_" + today + ".json"

    try:
        with open(os.path.join(DATA_ROOT, output_file_name)) as fp:
            package_status = json.load(fp)
    except:
        package_status = {}

    i = 0

    for root in check_roots:
        i += 1
        for package_name in os.listdir(root):
            print(f"Checking {package_name}...")
            if not os.path.isdir(os.path.join(root, package_name)):
                continue
            pkgbuild_path = os.path.join(root,
                                         package_name,
                                         "trunk",
                                         "PKGBUILD")
            if not os.path.exists(pkgbuild_path):
                package_status[package_name] = "PKGBUILD NOT FOUND"
                continue
            with open(pkgbuild_path, encoding="ISO-8859-1") as fp:
                pkgbuild = fp.read()
            # with open(pkgbuild_path) as fp:
            #     pkgbuild_lines = fp.readlines()

            if "validpgpkeys" in pkgbuild:
                if ".sig" in pkgbuild or ".asc" in pkgbuild or "sign" in pkgbuild:
                    # FIXME: makes a massive assumption that the strings can only occur for signatures
                    # example: "ascii" will trigger this but hopefully we don't have a bunch of
                    # validpgpkeys without actually having signatures :/
                    package_status[package_name] = True
                else:
                    package_status[package_name] = False
                    # for line in pkgbuild_lines:
                    #     if line.startswith("source") and "signed" in line:
                    #         package_status[package_name] = True
                    #         break
            else:
                package_status[package_name] = False

        if i % 50 == 0:
            with open(os.path.join(DATA_ROOT, output_file_name), "w+") as fp:
                json.dump(package_status, fp)

    with open(os.path.join(DATA_ROOT, output_file_name), "w+") as fp:
        json.dump(package_status, fp)


if __name__ == "__main__":
    main()
