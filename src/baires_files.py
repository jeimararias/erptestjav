

queries = [
  ["ADD_FILE", "/dir1/dir2/file.txt", "10"],
  ["ADD_FILE", "/dir1/dir2/file.txt", "5"],
  ["GET_FILE_SIZE", "/dir1/dir2/file.txt"],
  ["DELETE_FILE", "/non-existing.file"],
  ["DELETE_FILE", "/dir1/dir2/file.txt"],
  ["GET_FILE_SIZE", "/not-existing.file"]
]

