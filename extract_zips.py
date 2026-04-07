# # import os
# # import zipfile
# # import logging
# # import argparse
# # import shutil
# # from pathlib import Path

# # def setup_logging(log_file="extraction.log"):
# #     """Set up logging to both console and file."""
# #     logging.basicConfig(
# #         level=logging.INFO,
# #         format='%(asctime)s - %(levelname)s - %(message)s',
# #         handlers=[
# #             logging.FileHandler(log_file, encoding='utf-8'),
# #             logging.StreamHandler()
# #         ]
# #     )

# # def extract_zip(zip_path: Path, output_base_dir: Path = None, delete_after: bool = False):
# #     """
# #     Extracts a zip file to a folder with the same name.
    
# #     Args:
# #         zip_path: Path to the zip file.
# #         output_base_dir: Optional base directory to put the extracted folder.
# #                          If None, extracts in the same folder as the zip.
# #         delete_after: If True, deletes the zip file after successful extraction.
# #     """
# #     # Name of the folder will be the zip file's name without extension
# #     folder_name = zip_path.stem
    
# #     # Determine the parent directory for extraction
# #     if output_base_dir:
# #         extract_dir = output_base_dir / folder_name
# #     else:
# #         extract_dir = zip_path.parent / folder_name

# #     # Skip if the directory already exists and has content
# #     if extract_dir.exists() and any(extract_dir.iterdir()):
# #         logging.info(f"⏭️ SKIPPED: '{zip_path.name}' (Directory '{extract_dir}' already exists and is not empty)")
# #         return

# #     logging.info(f"⏳ EXTRACTING: '{zip_path.name}' -> '{extract_dir}'")

# #     try:
# #         # Create output directory if it doesn't exist
# #         extract_dir.mkdir(parents=True, exist_ok=True)

# #         with zipfile.ZipFile(zip_path, 'r') as zip_ref:
# #             zip_ref.extractall(extract_dir)
            
# #         logging.info(f"✅ SUCCESS: Extracted '{zip_path.name}'")

# #         if delete_after:
# #             try:
# #                 zip_path.unlink()
# #                 logging.info(f"🗑️ DELETED: '{zip_path.name}'")
# #             except OSError as e:
# #                 logging.error(f"❌ FAILED TO DELETE: '{zip_path.name}'. Error: {e}")

# #     except zipfile.BadZipFile:
# #         logging.error(f"❌ CORRUPTED: '{zip_path.name}' is not a valid zip file or is corrupted.")
# #         # Cleanup partially extracted empty dir if it was just created
# #         if extract_dir.exists() and not any(extract_dir.iterdir()):
# #             extract_dir.rmdir()
# #     except PermissionError:
# #         logging.error(f"❌ PERMISSION DENIED: Cannot read '{zip_path.name}' or write to '{extract_dir}'.")
# #     except Exception as e:
# #         logging.error(f"❌ UNEXPECTED ERROR with '{zip_path.name}': {e}")


# # def process_directory(target_dir: str, output_dir: str = None, delete_after: bool = False):
# #     """
# #     Recursively scans the target directory for zip files and extracts them.
# #     """
# #     target_path = Path(target_dir).resolve()
    
# #     if not target_path.exists() or not target_path.is_dir():
# #         logging.error(f"The directory '{target_path}' does not exist or is not a folder.")
# #         return

# #     output_path = Path(output_dir).resolve() if output_dir else None
# #     if output_path:
# #         output_path.mkdir(parents=True, exist_ok=True)

# #     logging.info(f"🔍 Scanning directory: {target_path}")
# #     if output_path:
# #         logging.info(f"📂 Output directory: {output_path}")
# #     if delete_after:
# #         logging.info("🗑️ Delete after extraction is ENABLED.")
        
# #     zip_files = list(target_path.rglob("*.zip"))
    
# #     if not zip_files:
# #         logging.info("No ZIP files found.")
# #         return
        
# #     logging.info(f"Found {len(zip_files)} ZIP file(s).")
    
# #     for zip_file in zip_files:
# #         extract_zip(zip_file, output_path, delete_after)

# #     logging.info("🏁 Extraction process completed.")

# # if __name__ == "__main__":
# #     parser = argparse.ArgumentParser(description="Recursively extract ZIP files from a directory.")
# #     parser.add_argument("target_dir", help="Directory to scan for ZIP files (e.g., . for current directory).")
# #     parser.add_argument("-o", "--output_dir", help="Optional separate directory to extract contents into.", default=None)
# #     parser.add_argument("-d", "--delete", action="store_true", help="Delete ZIP files after successful extraction.")
# #     parser.add_argument("-l", "--log", default="extraction.log", help="Log file path (default: extraction.log)")
    
# #     args = parser.parse_args()
    
# #     setup_logging(args.log)
# #     process_directory(args.target_dir, args.output_dir, args.delete)

# import zipfile
# import logging
# from pathlib import Path

# # ================== CONFIG ==================
# BASE_DIR = r"D:\SOFTCORE PART-B"   # Your folder
# OUTPUT_DIR = None                  # Set like r"D:\OUTPUT" if needed
# DELETE_AFTER = False               # True = delete zip after extract
# LOG_FILE = "extraction.log"
# # ============================================


# def setup_logging():
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s - %(message)s",
#         handlers=[
#             logging.FileHandler(LOG_FILE, encoding='utf-8'),
#             logging.StreamHandler()
#         ]
#     )


# def extract_zip(zip_path: Path, output_base_dir: Path = None):
#     folder_name = zip_path.stem

#     # Decide extraction location
#     if output_base_dir:
#         extract_dir = output_base_dir / folder_name
#     else:
#         extract_dir = zip_path.parent / folder_name

#     # Skip if already extracted
#     if extract_dir.exists() and any(extract_dir.iterdir()):
#         logging.info(f"⏭️ Skipped: {zip_path}")
#         return

#     try:
#         extract_dir.mkdir(parents=True, exist_ok=True)

#         with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#             zip_ref.extractall(extract_dir)

#         logging.info(f"✅ Extracted: {zip_path}")

#         # Delete zip if enabled
#         if DELETE_AFTER:
#             zip_path.unlink()
#             logging.info(f"🗑 Deleted: {zip_path}")

#     except zipfile.BadZipFile:
#         logging.error(f"❌ Corrupted ZIP: {zip_path}")
#     except Exception as e:
#         logging.error(f"⚠️ Error: {zip_path} -> {e}")


# def process_all():
#     base_path = Path(BASE_DIR)

#     if not base_path.exists():
#         logging.error("❌ Folder not found!")
#         return

#     output_path = Path(OUTPUT_DIR) if OUTPUT_DIR else None

#     logging.info(f"🔍 Scanning: {base_path}")

#     zip_files = list(base_path.rglob("*.zip"))

#     if not zip_files:
#         logging.info("No ZIP files found.")
#         return

#     logging.info(f"📦 Found {len(zip_files)} ZIP files")

#     for zip_file in zip_files:
#         extract_zip(zip_file, output_path)

#     logging.info("🏁 Done!")


# if __name__ == "__main__":
#     setup_logging()
#     process_all()


# import zipfile
# import logging
# from pathlib import Path

# # ================== CONFIG ==================
# BASE_DIR = r"D:\SOFTCORE PART-B"   # Your folder path
# OUTPUT_DIR = None                  # Example: r"D:\OUTPUT" (or keep None)
# DELETE_AFTER = True                # ✅ True = delete zip after extraction
# LOG_FILE = "extraction.log"
# # ============================================


# def setup_logging():
#     logging.basicConfig(
#         level=logging.INFO,
#         format="%(asctime)s - %(levelname)s - %(message)s",
#         handlers=[
#             logging.FileHandler(LOG_FILE, encoding='utf-8'),
#             logging.StreamHandler()
#         ]
#     )


# def extract_zip(zip_path: Path, output_base_dir: Path = None):
#     folder_name = zip_path.stem

#     # Decide extraction location
#     if output_base_dir:
#         extract_dir = output_base_dir / folder_name
#     else:
#         extract_dir = zip_path.parent / folder_name

#     # Skip if already extracted
#     if extract_dir.exists() and any(extract_dir.iterdir()):
#         logging.info(f"⏭️ Skipped: {zip_path}")
#         return

#     try:
#         extract_dir.mkdir(parents=True, exist_ok=True)

#         with zipfile.ZipFile(zip_path, 'r') as zip_ref:
#             zip_ref.extractall(extract_dir)

#         logging.info(f"✅ Extracted: {zip_path}")

#         # 🗑 DELETE ZIP AFTER SUCCESS
#         if DELETE_AFTER:
#             try:
#                 zip_path.unlink()
#                 logging.info(f"🗑 Deleted ZIP: {zip_path}")
#             except Exception as e:
#                 logging.error(f"❌ Failed to delete ZIP: {zip_path} -> {e}")

#     except zipfile.BadZipFile:
#         logging.error(f"❌ Corrupted ZIP: {zip_path}")

#         # Remove empty folder if created
#         if extract_dir.exists() and not any(extract_dir.iterdir()):
#             extract_dir.rmdir()

#     except Exception as e:
#         logging.error(f"⚠️ Error: {zip_path} -> {e}")


# def process_all():
#     base_path = Path(BASE_DIR)

#     if not base_path.exists():
#         logging.error("❌ Folder not found!")
#         return

#     output_path = Path(OUTPUT_DIR) if OUTPUT_DIR else None

#     logging.info(f"🔍 Scanning: {base_path}")

#     zip_files = list(base_path.rglob("*.zip"))

#     if not zip_files:
#         logging.info("No ZIP files found.")
#         return

#     logging.info(f"📦 Found {len(zip_files)} ZIP files")

#     for zip_file in zip_files:
#         extract_zip(zip_file, output_path)

#     logging.info("🏁 Extraction Completed!")


# if __name__ == "__main__":
#     setup_logging()
#     process_all()


import zipfile
import logging
import time
import os
from pathlib import Path

# ================== CONFIG ==================
BASE_DIR = r"D:\SOFTCORE PART-B"
OUTPUT_DIR = None
DELETE_AFTER = True   # ✅ Enable delete
LOG_FILE = "extraction.log"
# ============================================

# 📊 Counters
total = 0
extracted = 0
skipped = 0
failed = 0
deleted = 0


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8'),
            logging.StreamHandler()
        ]
    )


# 🗑 Safe delete function (FIX for Windows lock issue)
def delete_zip_file(zip_path):
    global deleted

    for i in range(3):  # retry 3 times
        try:
            os.remove(zip_path)
            logging.info(f"🗑 Deleted ZIP: {zip_path}")
            deleted += 1
            return True
        except PermissionError:
            logging.warning(f"🔁 Retry delete (file in use): {zip_path}")
            time.sleep(1)
        except Exception as e:
            logging.error(f"❌ Delete failed: {zip_path} -> {e}")
            return False
    return False


def extract_zip(zip_path: Path, output_base_dir: Path = None):
    global extracted, skipped, failed

    folder_name = zip_path.stem

    # Decide extraction location
    if output_base_dir:
        extract_dir = output_base_dir / folder_name
    else:
        extract_dir = zip_path.parent / folder_name

    # ⏭ Skip if already extracted
    if extract_dir.exists() and any(extract_dir.iterdir()):
        logging.info(f"⏭️ Skipped: {zip_path}")
        skipped += 1
        return

    try:
        extract_dir.mkdir(parents=True, exist_ok=True)

        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)

        logging.info(f"✅ Extracted: {zip_path}")
        extracted += 1

        # 🗑 Delete ZIP safely
        if DELETE_AFTER:
            delete_zip_file(zip_path)

    except zipfile.BadZipFile:
        logging.error(f"❌ Corrupted ZIP: {zip_path}")
        failed += 1

        if extract_dir.exists() and not any(extract_dir.iterdir()):
            extract_dir.rmdir()

    except Exception as e:
        logging.error(f"⚠️ Error: {zip_path} -> {e}")
        failed += 1


def process_all():
    global total

    base_path = Path(BASE_DIR)

    if not base_path.exists():
        logging.error("❌ Folder not found!")
        return

    output_path = Path(OUTPUT_DIR) if OUTPUT_DIR else None

    logging.info(f"🔍 Scanning: {base_path}")

    zip_files = list(base_path.rglob("*.zip"))
    total = len(zip_files)

    if not zip_files:
        logging.info("No ZIP files found.")
        return

    logging.info(f"📦 Found {total} ZIP files")

    for zip_file in zip_files:
        extract_zip(zip_file, output_path)

    # 📊 FINAL SUMMARY
    logging.info("🏁 Extraction Completed!")

    print("\n========= SUMMARY =========")
    print(f"📦 Total ZIP files : {total}")
    print(f"✅ Extracted       : {extracted}")
    print(f"⏭ Skipped         : {skipped}")
    print(f"❌ Failed          : {failed}")
    print(f"🗑 Deleted ZIP     : {deleted}")
    print("===========================\n")


if __name__ == "__main__":
    setup_logging()
    process_all()