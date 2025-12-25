## Threat Model – CI/CD Exploit Simulation

### Assets
- JWT signing secrets
- User authentication tokens
- Order data
- Infrastructure configuration

### Threat Actors
- Malicious external attacker
- Insider developer
- Compromised dependency / supply chain

### Key Threat Scenarios
1. Hardcoded secrets committed to repository
2. Vulnerable dependencies introduced via PR
3. Unauthorized access to another user's order (IDOR)
4. Insecure infrastructure configuration

### Security Controls
- Gitleaks for secrets detection at PR stage
- Snyk for dependency vulnerability scanning
- Checkov for IaC misconfiguration detection
- OWASP ZAP for runtime vulnerability detection

### Design Choice
This project intentionally simulates insecure patterns to validate CI/CD security controls.
