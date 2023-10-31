# zabbix-cups

## Zabbix template for monitoring CUPS servers, printers and queues via Zabbix Agent

Written by andre@schild.ws and changed a bit of stuff by paulopaag. (I'm not not very proud of it, so bear with my mistakes, please)

At the moment we only monitor printers and their queues, but not the classes.

The configuration files and scripts have to be placed in the correct
directories as shown in the repository.

- `Template_App_CUPS.yaml`
    -> Import this template on your Zabbix server and assign it to your monitored CUPS servers

- `/etc/zabbix/zabbix_agentd2.d/plugins.d/cups.conf`
    -> Place in the file on your CUPS serverno modification needed, unless you place the external script in another location.

- `/etc/zabbix/scripts/discover_cups_printers.pl`
    -> The script doing the actual cups printer discovery. If you place this script in another location, you will have to change sudoers.d and the zabbix files accordingly
	
### Stuff I'm not proud of

Changes need to crontab.

Run crontab -e and add the following:
```bash
*/1 * * * * python3 /etc/zabbix/zabbix_agent2.d/plugins.d/count_cups_jobs.py >/dev/null 2>&1
*/1 * * * * python3 /etc/zabbix/zabbix_agent2.d/plugins.d/sum_cups_pages.py >/dev/null 2>&1
```
