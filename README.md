Před spuštěním je nutné změnit cestu k adresářům v každém ansible playbook na řádcích:
path
volumes
stejně tak v adresáři daemon_servis v Dockerfile pro správné kopírování souborů.
podle umístění souborů projektu na vašem počítači.

Pro spuštění projektu je třeba přejít do adresáře ansible a spustit ho následujícím způsobem:
sudo ansible-playbook -i hosts.ini master_playbook.yaml