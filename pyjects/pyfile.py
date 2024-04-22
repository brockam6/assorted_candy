# Use pathlib to read from local files. OS agnostic
from pathlib import Path

path = Path("pyfile_txt.txt")
contents = path.read_text()
print(contents)
lines = contents.splitlines()
print(' '.join(lines))