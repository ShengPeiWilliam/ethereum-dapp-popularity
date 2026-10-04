# Ethereum DApp Popularity

We study how Ethereum DApps grow and fade, using public on-chain data.

- What separates DApps that keep growing from those that spike and fade?
- Can the first weeks after launch tell us which DApps will become popular?

Right now the code takes a DApp's contract addresses and measures its first 30 days of activity.

## Run

```bash
conda activate dapp
pip install -r requirements.txt
gcloud auth application-default login
python main.py
```

To change the DApps or the window length, edit `config.py`.

## Shared files

Discussion notes, the Feature Dictionary, and results are in the [shared Google Drive folder](https://drive.google.com/drive/folders/14pnCcbBcztvvUGyhA2NYVJNclz36J0j2).
