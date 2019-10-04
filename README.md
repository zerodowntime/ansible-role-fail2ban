# fail2ban

Role to install and configure fail2ban package.

## Requirements

- Ansible >= 2.7

### Supported platforms

- EL
  - 7
- Ubuntu
  - xenial

## Default role variables

| Name | Description | Type | Default | Required |
| -----| ----------- | :--: | :------:| :------: |
| fail2ban__package_name | Package name to be installed. | string | `fail2ban` | True |
| fail2ban__package_state | Whether to install the package or not. | string | `present` | True |
| fail2ban__service_name | Name of the service. | string | `fail2ban` | True |
| fail2ban__service_state | Service state. | string | `started` | True |
| fail2ban__service_enable | Whether the service should start on boot. | bool | `True` | True |
| fail2ban__blacklisted_files | Default installation files to be removed. | list | `['jail.d/defaults-debian.conf', 'jail.d/00-firewalld.conf']` | True |
| fail2ban__jail_defaults_disabled | Whether to disable all the enabled services in jail.conf by default. | bool | `False` | True |
| fail2ban__fail2ban_local | Custom configuration for fail2ban.local file. | dict | `{}` | False |
| fail2ban__jail_defaults | Default configuration for jails, written to /etc/fail2ban/jail.local custom file. | dict | `{}` | False |
| fail2ban__jail_services | Configuration/creation of jails for a single services. | list | `[]` | False |
| fail2ban__custom_filter | Settings for a custom filter. | list | `[]` | False |
| fail2ban__custom_action | Settings for a custom action. | list | `[]` | True |

**All default variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

This section describes static variables implemented in the role.

### Main variables

| Name | Description | Type | Default |
| -----| ----------- | :--: | :-----: |
| fail2ban__config_directory | Path to the main config directory. | string | `/etc/fail2ban` |
| fail2ban__custom_config_file | Path to the file for fail2ban custom configuration. | string | `{{ fail2ban__config_directory }}/fail2ban.local` |
| fail2ban__path_jail_conf | Path to the main default jail.conf file. | string | `/etc/fail2ban/jail.conf` |
| fail2ban__path_jail_local | Path to the custom jail.local file. | string | `/etc/fail2ban/jail.local` |
| fail2ban__jail_local_file_backup | Whether to make a jail.local file backup or not. | bool | `False` |
| fail2ban__fail2ban_local_file_backup | Whether to make a fail2ban.local file backup or not. | bool | `False` |

**All static main variables are described in [vars/main.yml](vars/main.yml) file.**

## Example Playbook

```yaml

  - hosts: all
    become: true
    roles:
      - role: zerodowntime.fail2ban
```

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit <https://www.zdt.io/building-blocks/>.
