Vagrant.configure("2") do |config|

  # Ubuntu focal vm
  config.vm.define "focal" do |focal|

    # We use docker
    config.vm.provider "docker" do |d|
      d.image = "langouste/vagrant-ready"
      d.has_ssh = true
      d.remains_running = true
      d.create_args = [
      	"--tmpfs", "/tmp",
      	"--tmpfs", "/run",
      	"--tmpfs", "/run/lock",
      	"-v", "/sys/fs/cgroup:/sys/fs/cgroup:ro"
      ]
    end
  end

  # Run playbook
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "site.yml"
  end
end
