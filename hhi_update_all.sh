#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "🤖 HHI Update Robot Starting..."
echo ""

git config --global push.autoSetupRemote true

GH_ORG="hollowhouseinstitute"

# Repos that should NEVER be overwritten
CANONICAL_REPOS=(
  "HHI_GOV_01"
  "HHI_LUL_01"
  "Hollow_House_Standards_Library"
)

# All repos to process
REPOS=(
  "Hollow_House_Standards_Library"
  "HHI_GOV_01"
  "HHI_Interaction_Controls"
  "HHI_Governance_Portfolio"
  "Master_License_Suite"
  "ai_governance_reference"
  "Longitudinal_AI_Governance_Whitepaper"
  "Longitudinal_Behavioral_Governance"
  "Research_Papers"
  "Datasets_Core"
  "Ai_Human_Relations_Datasets"
  "Hollow_House_Academy"
  "Hollow_House_Institute-site"
)

README_BLOCK=$(cat << 'EOF'
## Governance Alignment
This repository is governed under the Hollow House Institute Master License Suite (HHI-MLS).
All terminology is normative and bound to the HHI Governance Glossary (v1.1.0).

## Standards Referenced
- HHI Governance Glossary (v1.1.0)
- HHI_SPEC_002 — Terminology Governance
- HHI_SPEC_003 — Repository Governance
- AINS — Artificial Intelligence Navigation & Stewardship Framework
- CCS-444A — Continuity Compliance Standard
- RCS-444A — Research Continuity Standard
- HHI-MLS — Master License Suite

## Governance Diagram
```mermaid
flowchart TD
  A[Hollow House Institute Doctrine] --> B[Hollow House Standards Library]
  B --> C[HHI_GOV_01 - Execution Governance]
  B --> D[HHI_LUL_01 - Language Licensing]
  D --> E[Master License Suite - Legal Enforcement]
  C --> F[Datasets & Systems]
  C --> G[Audits & Oversight]
  C --> H[Academy & Site]
