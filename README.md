# app-convert-network-netstats

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Converts a network datatype (JSON graph without node measurements) into a CSV table of connectivity matrices with pybrainlife, a format conversion utility.**

Loads the compressed JSON graph with jgf/igraph and uses pybrainlife to extract its connectivity matrix as conmats.csv tagged with the subject and session. Use it for networks that have no measurements; use the full variant to also export global and local network statistics.

Run it on brainlife.io: [https://doi.org/10.25663/brainlife.app.796](https://doi.org/10.25663/brainlife.app.796)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `network` | `generic/network` (!measurements) | yes | Network datatype (compressed JSON graph) without measurements. |

| Output | Datatype | Description |
|---|---|---|
| `net-stats` | `neuro/net-stats` | CSV table conmats.csv with the connectivity matrix. |

Runtime: container `brainlife/ga-python:lab328-dipy141-pybrainlife-1.0`; 2 CPUs; 0.33 h walltime.

<!-- brainlife-app:end -->

