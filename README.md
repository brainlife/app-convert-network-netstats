<h1 align="center">Extract connectivity matrices and network statistics</h1>

<p align="center">
  CSV tables of connectivity matrices, and of global and per-node network measures, from a brainlife.io network dataset.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.787"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.787-blue.svg" alt="Run on brainlife.io"></a>
  <a href="https://github.com/brainlife/app-convert-network-netstats/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

> **This branch, `v1.0`, is the brainlife.io App Extract network statistics and connectivity matrices from network datatype** ([doi:10.25663/brainlife.app.787](https://doi.org/10.25663/brainlife.app.787)). The other Apps in this repository are listed under **Versions on brainlife.io** below.

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Converts a network datatype (JSON graph with node measurements) into CSV tables of connectivity matrices and global and local network statistics with pybrainlife, a format conversion utility.**

Loads the compressed JSON graph with jgf/igraph and uses pybrainlife to extract its connectivity matrices and global and local (per-node) measures, writing conmats.csv, global_measures.csv and local_measures.csv tagged with the subject and session. Use it to prepare network outputs for group analysis; for networks without measurements use the no-measures variant.

| | |
|---|---|
| **Inputs** | `generic/network` |
| **Outputs** | `neuro/net-stats` |
| **Container** | `brainlife/ga-python:lab328-dipy141-pybrainlife-1.0` |
| **Resources** | 2 CPUs · 0.33 h walltime |
| **Run it** | [doi.org/10.25663/brainlife.app.787](https://doi.org/10.25663/brainlife.app.787) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `network` | `generic/network` (measurements) | yes | Network datatype (compressed JSON graph) that includes network measurements. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `net-stats` | `neuro/net-stats` | CSV tables: conmats.csv (connectivity matrices), global_measures.csv and local_measures.csv. |

<!-- brainlife-app:end -->

## Versions on brainlife.io

This repository hosts two Apps, each built from its own branch. Pick the one that matches your network dataset.

| App | Input network | Branch | Run it | Status |
|---|---|---|---|---|
| Extract connectivity matrices from network datatype | without measurements | [`no-measures-v1.0`](https://github.com/brainlife/app-convert-network-netstats/tree/no-measures-v1.0) | [doi:10.25663/brainlife.app.796](https://doi.org/10.25663/brainlife.app.796) | current |
| **Extract network statistics and connectivity matrices from network datatype** (this branch) | with measurements | [`v1.0`](https://github.com/brainlife/app-convert-network-netstats/tree/v1.0) | [doi:10.25663/brainlife.app.787](https://doi.org/10.25663/brainlife.app.787) | current |

## Running the App

### On brainlife.io

Open the App that matches your data and choose a `generic/network` dataset (a compressed JSON graph):

- networks **tagged `measurements`** go to [Extract network statistics and connectivity matrices](https://doi.org/10.25663/brainlife.app.787), which exports the connectivity matrices and the global and local network measures;
- networks **without measurements** go to [Extract connectivity matrices](https://doi.org/10.25663/brainlife.app.796), which exports the connectivity matrices only.

Press **Execute**. The Apps have no options. The tables are archived to your project as a `neuro/net-stats` dataset, labelled with the subject and session of the input, ready to be combined across subjects for group analysis.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/); pybrainlife, python-igraph and jgf come from the `brainlife/ga-python:lab328-dipy141-pybrainlife-1.0` container.

1. Clone this repository and check out the App branch (`git checkout v1.0` or `git checkout no-measures-v1.0`).
2. Create `config.json` with the path to the network file and the subject (and optionally session) that brainlife.io would pass in `_inputs`:

   ```json
   {
       "network": "/input/network/network.json.gz",
       "_inputs": [ { "meta": { "subject": "sub-01", "session": "1" } } ]
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

If no session is given, the App uses `1`.

## Outputs

```text
net-stats/
└── net-stats/
    ├── conmats.csv           connectivity matrices
    ├── global_measures.csv   whole-network measures (v1.0 only)
    └── local_measures.csv    per-node measures (v1.0 only)
```

Each table carries `subjectID` and `sessionID` columns taken from the input's metadata.

## Troubleshooting

- **Global and local measures are missing**: the network has no measurements. Use the `v1.0` App only on networks tagged `measurements`; for other networks use the `no-measures-v1.0` App, which writes `conmats.csv` alone.

## Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Extract network statistics and connectivity matrices from network datatype. brainlife.io App. [doi:10.25663/brainlife.app.787](https://doi.org/10.25663/brainlife.app.787)
- Garyfallidis et al. Dipy, a library for the analysis of diffusion MRI data. *Frontiers in Neuroinformatics* 8 (2014). [doi:10.3389/fninf.2014.00008](https://doi.org/10.3389/fninf.2014.00008)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Brad Caron

**Project director:** Franco Pestilli

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## License

[MIT](https://github.com/brainlife/app-convert-network-netstats/blob/main/LICENSE).
