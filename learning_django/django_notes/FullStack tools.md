**Leaked credentials scanner**
https://github.com/trufflesecurity/trufflehog
Should include in CI/CD, fail if anything comes up.
False positives are a potential issue.

**Vulnerability scanners** (was thinking of dependency vuln scanning): 
- https://snyk.io/ - has free plan, 100 scans per month.
- https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide - GitHub's Dependabot
Should find open source alternative.
For JS, including npm audit in CI/CD should be ok for small projects.
Could add further vuln DBs to npm audit?
For Python - not exactly sure yet.
- https://github.com/github/codeql-action = static analysis, can include as an action;

