import json
import os


DATA_ROOT = "data"
PERSONALIZATION_ROOT = "personalization"


def main():
    data_file_name = "data_2019-11-27_pkg.json"
    pkgstats_file = os.path.join(DATA_ROOT, "pkgstats_" + data_file_name)
    data_file = os.path.join(DATA_ROOT, data_file_name)
    signed_check_file = os.path.join(DATA_ROOT, "package-signed-check_2019-11-26.json")

    personalization_file = os.path.join(PERSONALIZATION_ROOT, "personalization_" + data_file_name)

    try:
        with open(personalization_file) as fp:
            personalization = json.load(fp)
    except:
        personalization = {}

    with open(pkgstats_file) as fp:
        pkgstats = json.load(fp)

    with open(data_file) as fp:
        data = json.load(fp)

    with open(signed_check_file) as fp:
        signed_check = json.load(fp)

    i = 0

    for package in data:
        i += 1
        if package in personalization:
            continue
        popularity = pkgstats.get(package)
        if popularity is None:
            popularity = 0.001

        package_signed = signed_check.get(package)
        if package_signed is True:
            package_signed = 0.0
        elif package_signed is False:
            package_signed = 100.0
        else:
            package_signed = 50.0

        score = (popularity + package_signed) / 2

        personalization[package] = score

        if i % 50 == 0:
            with open(personalization_file, "w+") as fp:
                json.dump(personalization, fp)

    with open(personalization_file, "w+") as fp:
        json.dump(personalization, fp)


if __name__ == "__main__":
    main()