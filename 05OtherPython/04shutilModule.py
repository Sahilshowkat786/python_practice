import shutil
total,used,free=shutil.disk_usage("C:/")
print(f"Total: {total/1024**3}")
print(f"used: {used/1024**3}")
print(f"free: {free/1024**3}")



import shutil
import os

# ============================================================
# SHUTIL MODULE - IMPORTANT COMMANDS
# ============================================================

# 1. COPY FILE
# ------------------------------------------------------------
# shutil.copy(source, destination)

shutil.copy("file.txt", "backup.txt")


# 2. COPY FILE + METADATA
# ------------------------------------------------------------
# shutil.copy2(source, destination)

shutil.copy2("file.txt", "backup2.txt")


# 3. COPY FILE CONTENTS
# ------------------------------------------------------------
# shutil.copyfile(source, destination)

shutil.copyfile("file.txt", "copy.txt")


# 4. COPY PERMISSIONS
# ------------------------------------------------------------
# shutil.copymode(source, destination)

shutil.copymode("file.txt", "copy.txt")


# 5. COPY FILE + PERMISSIONS + METADATA
# ------------------------------------------------------------
# shutil.copystat(source, destination)

shutil.copystat("file.txt", "copy.txt")


# 6. COPY ENTIRE FOLDER
# ------------------------------------------------------------
# shutil.copytree(source_folder, destination_folder)

shutil.copytree("my_folder", "backup_folder")


# 7. MOVE FILE OR FOLDER
# ------------------------------------------------------------
# shutil.move(source, destination)

shutil.move("file.txt", "my_folder/file.txt")


# 8. DELETE ENTIRE FOLDER
# ------------------------------------------------------------
# ⚠️ DANGEROUS - permanently deletes folder and contents

# shutil.rmtree("my_folder")


# 9. GET DISK USAGE
# ------------------------------------------------------------

total, used, free = shutil.disk_usage("C:/")

print("Total:", total)
print("Used :", used)
print("Free :", free)


# 10. FIND EXECUTABLE
# ------------------------------------------------------------
# Finds the location of a program

python_path = shutil.which("python")

print("Python location:", python_path)


# 11. GET TERMINAL SIZE
# ------------------------------------------------------------

columns, lines = shutil.get_terminal_size()

print("Terminal columns:", columns)
print("Terminal lines:", lines)


# ============================================================
# ADVANCED SHUTIL FUNCTIONS
# ============================================================

# 12. MAKE ARCHIVE
# ------------------------------------------------------------
# Creates ZIP/TAR archive

# shutil.make_archive(
#     "backup",
#     "zip",
#     "my_folder"
# )


# 13. UNPACK ARCHIVE
# ------------------------------------------------------------
# Extract ZIP/TAR archive

# shutil.unpack_archive(
#     "backup.zip",
#     "extracted_folder"
# )


# 14. GET ARCHIVE FORMATS
# ------------------------------------------------------------

formats = shutil.get_archive_formats()

print("Supported archive formats:")
print(formats)


# 15. GET UNPACK FORMATS
# ------------------------------------------------------------

formats = shutil.get_unpack_formats()

print("Supported unpack formats:")
print(formats)


# ============================================================
# COPYTREE WITH EXISTING DIRECTORY
# ============================================================

# Python 3.8+
# dirs_exist_ok=True allows destination folder to already exist.

# shutil.copytree(
#     "my_folder",
#     "backup_folder",
#     dirs_exist_ok=True
# )


print("\nShutil examples completed!")