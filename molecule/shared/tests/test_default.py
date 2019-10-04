import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_fail2ban_service_is_runnning(host):
    command = host.command('systemctl status fail2ban')
    assert command.stdout.find('running') > -1, "fail2ban not running"


def test_fail2ban_client_status(host):
    command = host.command('sudo fail2ban-client status')
    assert command.stdout.find('sshd') > -1, "jail not enabled"


def test_jail_local_exists(host):
    command = host.command('ls /etc/fail2ban/')
    assert command.stdout.find('jail.local') > -1, "no jail.local file"
