### Tools
**Leaked credentials scanner**
https://github.com/trufflesecurity/trufflehog
Should include in CI/CD, fail if anything comes up.
False positives are a potential issue.

**Vulnerability scanners** (was thinking of dependency vuln scanning): 
- https://snyk.io/ - has free plan, 100 scans per month.
- https://docs.github.com/en/code-security/getting-started/dependabot-quickstart-guide - GitHub's Dependabot
- If you are suspicious about a package and what connections it makes, run CWE-020-ExternalAPIs with CodeQL https://github.com/github/codeql/blob/main/python/ql/src/Security/CWE-020-ExternalAPIs/UntrustedDataToExternalAPI.ql
Should find open source alternative.
For JS, including npm audit in CI/CD should be ok for small projects.
Could add further vuln DBs to npm audit?
For Python - not exactly sure yet.
- https://github.com/github/codeql-action = static analysis, can include as an action;


### Considerations
- If using 3rd party Github actions, best practice should be to mention the hash of the specific version of the action you're using and maybe mark a time every x months to update those versions.
  
  If you keep the @v4 thing, your actions update to the newest version as soon as the 3rd party devs push a change => if compromised = not good.