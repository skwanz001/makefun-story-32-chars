"""Tell a Whole Story in 32 Characters.

Writes a single Wi-Fi network name of at most 32 characters to
/output/entry.txt. Standard library only.
"""

import os

WIFI_NAME = "Ex took router, I kept the dog"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-32 chars, not only whitespace.
    if not 1 <= len(WIFI_NAME) <= 32:
        raise ValueError(f"Wi-Fi name is {len(WIFI_NAME)} chars, must be 1-32")
    if not WIFI_NAME.strip():
        raise ValueError("Wi-Fi name must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WIFI_NAME)
    print(f"Wrote {len(WIFI_NAME)} chars to {OUTPUT_PATH}: {WIFI_NAME!r}")


if __name__ == "__main__":
    main()
