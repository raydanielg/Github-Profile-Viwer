import webbrowser
import time
from tqdm import tqdm

def open_profile(url):
    webbrowser.open_new_tab(url)

def main():
    github_username = input("👤 Ingiza GitHub username (mfano: raydanielg): ").strip()
    times = int(input("🔢 Ingiza idadi ya mara za kufungua (mfano: 500): "))

    url = f"https://github.com/{github_username}"

    pbar = tqdm(total=times, desc="🚀 Inafungua profile", ncols=100)

    for _ in range(times):
        open_profile(url)
        pbar.update(1)
        time.sleep(0.1)  # Delay kidogo kuzuia overload

    pbar.close()
    print("✅ Kazi imekamilika kabisa!")

if __name__ == "__main__":
    main()
