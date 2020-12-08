sudo apt-get update
sudo apt install git
sudo add-apt-repository ppa:oibaf/graphics-drivers
sudp apt install libvulkan1 mesa-vulkan-drivers vulkan-utils
apt install autoconf libtool libdrm-dev xorg xorg-dev openbox libx11-dev libgl1-mesa-glx libgl1-mesa-dev
sudo apt-get install autoconf automake autopoint build-essential cmake git libass-dev libbz2-dev libfontconfig1-dev libfreetype6-dev libfribidi-dev libharfbuzz-dev libjansson-dev liblzma-dev libmp3lame-dev libnuma-dev libogg-dev libopus-dev libsamplerate-dev libspeex-dev libtheora-dev libtool libtool-bin libturbojpeg0-dev libvorbis-dev libx264-dev libxml2-dev libvpx-dev m4 make meson nasm ninja-build patch pkg-config python tar zlib1g-dev 
apt install intel-media-va-driver
 
# INtell quick sync for handbrake
sudo apt-get install libva-dev libdrm-dev

# only if we want GUI
sudo apt-get install gstreamer1.0-libav intltool libappindicator-dev libdbus-glib-1-dev libglib2.0-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgtk-3-dev libgudev-1.0-dev libnotify-dev libwebkit2gtk-4.0-dev
sudo apt install autoconf libtool libdrm-dev xorg xorg-dev openbox libx11-dev libgl1-mesa-glx libgl1-mesa-dev

## Intel quicksync HandBrake
#wget https://github.com/Intel-Media-SDK/MediaSDK/releases/download/intel-mediasdk-20.3.0/MediaStack.tar.gz
#tar -xvf MediaStack.tar.gz
#cd MediaStack
#sudo chmod +x install_media.sh
#sudo ./install_media.sh
#cd ..

#Libva driver, not really needed- unless you know you need it 
#wget https://github.com/intel/libva/archive/master.zip
#unzip master.zip
#cd libva-master
#./autogen.sh
#make
#sudo make install

#intel media sdk 
git clone https://github.com/Intel-Media-SDK/MediaSDK msdk
cd msdk
mkdir build && cd build
cmake ..
make
make install

## Handbrake
git clone https://github.com/HandBrake/HandBrake.git && cd HandBrake
./configure --disable-gtk --enable-qsv --enable-vce --launch-jobs=$(nproc) --launch
sudo make --directory=build install
