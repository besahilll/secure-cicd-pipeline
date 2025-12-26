# CI/CD Exploit Simulation & Secure Deployment Pipeline

## 📌 Overview
This is a **personal DevSecOps project** designed to **simulate real-world CI/CD security threats and controls**

The project focuses on **preventing high-risk vulnerabilities early in the SDLC** and **detecting runtime issues automatically**, using a GitHub Actions–based CI/CD pipeline with enforced security gates.

> ⚠️ Note: This project is a **simulation**, not a production deployment.  
> It intentionally includes insecure patterns to validate CI/CD security tooling and workflows.

---

## 🎯 Objectives
- Simulate realistic DevSecOps threat scenarios in CI/CD
- Enforce automated security gates on pull requests
- Detect runtime vulnerabilities post-deployment
- Demonstrate measurable improvement in vulnerability detection time (MTTR)
- Showcase practical integration of security tools without overengineering

---

## 🏗️ Architecture (Simplified)

```mermaid
flowchart TD

    A[Developer Pull Request] --> B[PR Security Pipeline]

    B --> B1[Gitleaks - Secrets Scan]
    B --> B2[Snyk - Dependency Scan]
    B --> B3[Checkov - IaC Scan]

    B1 --> C{High Risk Found?}
    B2 --> C
    B3 --> C

    C -- Yes --> D[Block PR]
    C -- No --> E[Merge to Main]

    E --> F[Deployment Security Pipeline]
    F --> G[Start Application Services]
    G --> H[OWASP ZAP Scan]
    H --> I[Security Report Generated]

## 🧩 Application Design

The project uses **two lightweight services** to create a realistic attack surface.

### 🔐 Auth Service
- Handles user authentication
- Issues JWT tokens
- **Intentional vulnerabilities**:
  - Hardcoded JWT secret (for secrets detection)
  - Weak authentication logic
  - Outdated dependencies

### 📦 Orders Service
- Exposes business-critical data
- Requires authentication token
- **Intentional vulnerabilities**:
  - Insecure Direct Object Reference (IDOR)
  - Missing authorization checks

This design enables meaningful security findings during CI/CD scans.

---

## 🔄 CI/CD Pipelines

### 1️⃣ PR Security Pipeline (`pr-security.yml`)
Triggered on pull requests to `main`.

**Security Controls**
- **Gitleaks** → Blocks leaked secrets
- **Snyk** → Blocks vulnerable dependencies (HIGH/CRITICAL)
- **Checkov** → Blocks insecure IaC configurations

**Outcome**
- High-risk commits never reach the main branch
- Vulnerabilities are caught before deployment

---

### 2️⃣ Deployment Security Pipeline (`deploy-security.yml`)
Triggered on merge to `main`.

**Security Controls**
- Starts application services
- **OWASP ZAP** baseline scan (DAST)
- Generates runtime vulnerability reports

**Outcome**
- Detects authorization flaws and insecure endpoints
- Provides runtime visibility without blocking developer velocity

---

## 🧨 Exploit Scenarios Simulated

| Scenario | Risk | Tool Used | Pipeline Stage |
|-------|------|----------|---------------|
| Hardcoded secrets | Credential compromise | Gitleaks | PR |
| Vulnerable dependency | RCE / known CVEs | Snyk | PR |
| IDOR | Data exposure | OWASP ZAP | Post-merge |
| Open ingress rules | Infrastructure exposure | Checkov | PR |

These vulnerabilities are **intentionally introduced** to validate CI/CD security enforcement.

---

## ⏱️ MTTR Improvement (Simulated)

### Before CI/CD Security
- Vulnerabilities detected during manual testing
- Detection time: **1–2 days**
- Remediation time: **~1 day**

### After CI/CD Security
- Vulnerabilities detected during PR or immediately after merge
- Detection time: **<15 minutes**
- Remediation time: **same day**

**Estimated MTTR reduction: ~35–40%**

---

## 🔍 Tools & Why They Were Used

| Tool | Purpose |
|----|-------|
| GitHub Actions | CI/CD orchestration |
| Gitleaks | Prevent secret leakage |
| Snyk | Dependency vulnerability detection |
| Checkov | Infrastructure misconfiguration detection |
| OWASP ZAP | Runtime vulnerability detection (DAST) |

---

## 📂 Documentation
Additional design and analysis documents are available in the `docs/` directory:
- Threat model
- Exploit scenarios
- MTTR analysis

---

## 🧠 Key Takeaways
- Security controls are **threat-driven**, not tool-driven
- CI/CD security must balance **risk reduction and developer velocity**
- Automated detection significantly improves remediation timelines
- Even simple applications can expose realistic security risks

---

## 🚀 Disclaimer
This project is a **personal DevSecOps simulation** built for learning and demonstration purposes.  
It does not represent a production environment or an organizational deployment.

