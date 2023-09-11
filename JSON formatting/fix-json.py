import sys
import re
import os

regexJsonForgotComma = re.compile(r"\]\s*\n\s*\[", re.MULTILINE)


def FixJsonComma(jsonFilePath):
    if not os.path.isfile(jsonFilePath):
        sys.stderr.write("Not a valid file path: %s" % (jsonFilePath))
        return
    json_text = ""
    with open(jsonFilePath, "r", encoding="utf8") as file:
        json_text = file.read()

    commaFaultMatches = re.findall(regexJsonForgotComma, json_text)
    textFixed = re.sub(regexJsonForgotComma, r"],\n\t[", json_text)

    sys.stderr.write("\nFound %d json faults of type:\n" %
                     len(commaFaultMatches))
    sys.stderr.write("]\n[\n")
    sys.stderr.write("Replaced with correct:\n")
    sys.stderr.write("],\n[\n")
    sys.stderr.write("\n")

    with open(jsonFilePath + "_fixed", "w", encoding="utf8") as fileOut:
        fileOut.write("".join(textFixed))


if __name__ == "__main__":
    try:
        jsonFilePath = sys.argv[1]
    except IndexError:
        sys.stderr.write("No path to .json file provided :(\n")

    if "jsonFilePath" in locals():
        FixJsonComma(jsonFilePath)
        sys.stderr.write("Done! See output file %s_fixed\n" % jsonFilePath)
