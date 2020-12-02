sudo cp /usr/local/share/motioneye/extra/motioneye.systemd-unit-local /etc/systemd/system/motioneye.service
sudo systemctl daemon-reload
sudo systemctl enable motioneye
sudo systemctl start motioneye
