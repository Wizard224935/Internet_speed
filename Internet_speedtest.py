#pip install speedtest-cli

import speedtest

st = speedtest.Speedtest()
download_speed = st.download() / 1000000  # convert to megabits
upload_speed = st.upload() / 1000000     # convert to megabits

print(f"Download speed: {download_speed:.2f} Mbps")
print(f"Upload speed: {upload_speed:.2f} Mbps")
