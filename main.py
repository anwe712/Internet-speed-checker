import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 1024 / 1024  # Convert to Mbps
    upload_speed = st.upload() / 1024 / 1024  # Convert to Mbps

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    print("Checking Internet Speed...")
    check_internet_speed()
