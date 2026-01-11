from pathlib import Path


def clean_pyc_and_cache(root: Path) -> int:
    """
    Remove all .pyc files and __pycache__ directories recursively.

    Parameters
    ----------
    root : Path
        Root directory of the project.

    Returns
    -------
    int
        Number of deleted .pyc files.
    """
    deleted_pyc = 0

    # Remove .pyc files
    for pyc_file in root.rglob("*.pyc"):
        try:
            pyc_file.unlink()
            deleted_pyc += 1
        except Exception as exc:
            print(f"Failed to delete {pyc_file}: {exc}")

    # Remove __pycache__ directories
    for cache_dir in root.rglob("__pycache__"):
        try:
            cache_dir.rmdir()  # works only if empty
        except OSError:
            pass

    return deleted_pyc


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parent
    deleted = clean_pyc_and_cache(project_root)

    print(f"✔ Deleted {deleted} .pyc file(s)")