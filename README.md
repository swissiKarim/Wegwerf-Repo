# Wegwerf-Repo (Lab)

Dieses Repository ist ein **Wegwerf**-Seed fuer einen lokalen AgentForge-E2E-Lauf
(Szenarien cli+api, Verify mit Process-Dienst). Kein Produktionscode.

## Ziel der Story (spaeter)

Auszahlung **brutto → netto** als:

1. CLI (`payout_cli.py`)
2. HTTP `POST /payout` (Prozessdienst im Verify)

`GET /health` muss gruen bleiben.

## Lokal (nur Stdlib + pytest im Polyglot-Image)

```bash
python3 -m compileall -q .
python3 -m pytest --junitxml=.agentsphere/reports/junit.xml
```

Dienst:

```bash
./scripts/start-web.sh
# GET http://127.0.0.1:8080/health
```

## Project contract

Der Vertrag liegt unter `.agentsphere/project.yaml` (schemaVersion 4, inkl. `services.web`).
Nicht mehr im Repo-Root als `project.yaml`.

