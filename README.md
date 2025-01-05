# talk-to-sql
Talk to a SQLite database using your voice.

## Setup
I've only tested this on a MacBook Pro with an M4 Pro Chip (48 GB). I'm using Conda with Python 3.12.2.
It's surprisingly annoying to install whisper and have it run on an M4 (M-series) chip. [This comment](https://github.com/openai/whisper/pull/382#issuecomment-1501027398) saved the day.

```bash
conda create -n talk_to_sql_env python=3.12 -y
conda activate talk_to_sql_env 
pip install git+https://github.com/openai/whisper.git@51c785f7c91b8c032a1fa79c0e8f862dea81b860
pip install --pre --force-reinstall torch --index-url https://download.pytorch.org/whl/nightly/cpu
conda install -c conda-forge ffmpeg
```
