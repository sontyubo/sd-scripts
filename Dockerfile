FROM nvidia/cuda:12.1.1-cudnn8-runtime-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive

# システムパッケージと Python 3.10
RUN apt-get update && apt-get install -y \
    git python3.10 python3.10-venv python3.10-dev \
    wget curl build-essential libgl1 libglib2.0-0 \
    && apt-get clean

RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.10 1

WORKDIR /workspace

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

COPY . .

# コンテナのbuild中に.venvを作成できない
RUN uv venv /opt/venv
# Use the virtual environment automatically
ENV VIRTUAL_ENV=/opt/venv
# Place entry points in the environment at the front of the path
ENV PATH="/opt/venv/bin:$PATH"

RUN uv pip install --upgrade pip && \
    uv pip install torch==2.1.2 torchvision==0.16.2 --index-url https://download.pytorch.org/whl/cu121 && \
    uv pip install xformers==0.0.23.post1 --index-url https://download.pytorch.org/whl/cu121 && \
    uv pip install -r requirements.txt

RUN uv sync && \
    uv pip install -e .

CMD [ "bash" ]