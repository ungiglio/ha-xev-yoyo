# Security Policy

## Supported Versions

We currently provide security updates for the following versions of this integration:

| Version | Supported           |
| ------- | ------------------- |
| 26.2.x  | :white_check_mark:  |
| 26.1.x  | :white_check_mark:  |
<!--| < 26.2  | :x:                 |-->

We strongly recommend always using the latest version available via HACS to ensure maximum protection and compatibility with XEV APIs.

## Reporting a Vulnerability

If you discover a security vulnerability, please **do not** open a public Issue. Instead, report vulnerabilities directly via [GitHub Private Vulnerability Reporting](https://github.com/ungiglio/ha-xev-yoyo/security/advisories/new).

## Scope and Limitations

This integration is an unofficial project based on reverse engineering of the official XEV APIs. 

Please note the following regarding security:
- **Third-Party APIs**: Security issues directly related to XEV's servers or their authentication protocols (e.g., the required use of MD5) are not under our direct control.
- **Credentials**: The integration stores credentials locally within your Home Assistant configuration. The security of this data depends on the protection of your Home Assistant instance.

## Acknowledgments

We appreciate the work of security researchers who help us keep the XEV Yoyo user community safe.
