from urllib.parse import urlparse
import tldextract


def main():
    result = set()
    data = "data/all-package-urls"
    with open(data) as fp:
        all_lines = fp.readlines()
    for line in all_lines:
        line = line.strip("\n")

        scheme = urlparse(line).scheme
        extract = tldextract.extract(line)
        host = extract.domain + "." + extract.suffix

        result.add((scheme, host))

    output = "data/unique-schemes-hosts"

    result = "\n".join(sorted([str(x) for x in list(result)]))

    with open(output, "w+") as fp:
        fp.write(result)


if __name__ == "__main__":
    main()
