# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.241.1/containers/ubuntu/.devcontainer/base.Dockerfile

# [Choice] Ubuntu version (use ubuntu-22.04 or ubuntu-18.04 on local arm64/Apple Silicon): ubuntu-22.04, ubuntu-20.04, ubuntu-18.04
FROM devkitpro/devkitppc

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

#RUN sudo dpkg --add-architecture i386
RUN sudo apt-get update && sudo apt-get install -y build-essential
RUN sudo apt-get install -y libarchive-tools
RUN sudo apt-get install -y cmake
# RUN sudo apt-get install -y wine64
# RUN sudo apt-get install -y wine
RUN sudo apt-get install -y ninja-build
RUN sudo apt-get upgrade -y
RUN sudo apt-get install -y libtinfo5

# # Install the patchers
# WORKDIR /workspaces/romhack/wii
# RUN curl -L https://github.com/zsrtp/romhack-compiler/releases/download/v0.1.1-r2/romhack-v0.1.1-r2-linux-x64-musl.zip | bsdtar -xvf -
# RUN chmod +x romhack
# WORKDIR /workspaces/romhack/gc
# RUN curl -L https://github.com/zsrtp/romhack-compiler/releases/download/v0.1.1-r2/romhack-v0.1.1-r2-linux-x64-musl-gc.zip | bsdtar -xvf -
# RUN chmod +x romhack
