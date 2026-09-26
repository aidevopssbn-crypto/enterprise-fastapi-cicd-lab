# Enterprise FastAPI CI/CD Lab

This repository is the starting point for a hands-on enterprise-style CI/CD and DevSecOps training lab.

## Primary learning track

1. Jenkins running locally in Docker Desktop
2. SonarQube Community Build running locally with PostgreSQL
3. Docker build and image lifecycle
4. Pytest, Ruff, Bandit and pip-audit
5. Semgrep CE as the open-source substitute for Checkmarx SAST
6. Trivy as the open-source container/repository/IaC/secrets scanner and the practical substitute for an Aqua image-scanning workflow
7. Gitleaks for dedicated secret detection
8. OWASP ZAP for DAST
9. Syft/Grype for SBOM and an additional vulnerability view
10. Cosign/Sigstore for image signing and provenance/attestation concepts
11. GitHub Actions implementation of the same pipeline
12. Azure DevOps YAML implementation of the same pipeline
13. Local Kubernetes deployment and promotion/rollback

## Start the platform

From PowerShell in this directory:

```powershell
./scripts/up.ps1
```

Then open:

- Jenkins: http://localhost:8080
- SonarQube: http://localhost:9000

## Notes

This lab uses Docker-in-Docker because Jenkins needs its own Docker daemon in the local Docker Desktop environment. This is a learning setup, not a production Jenkins topology.

In later lessons we will refactor the pipeline toward ephemeral build agents, immutable images, credentials stored outside source control, pull-request gates, quality gates, SBOMs, image signing, and deployment promotion.
