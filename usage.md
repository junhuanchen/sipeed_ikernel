## local debug

- sudo pip install ./

- sipeed_ikernel manage --add     --kernel_cmd="ipython kernel -f {connection_file}"     --name="Remote Python" --interface=ssh     --host=ubuntu@172.20.10.227 --pswd root

- ipython kernelspec list

```shell
  python3                                      /home/juwan/.local/share/jupyter/kernels/python3
  rik_ssh_ubuntu_172_20_10_227_remotepython    /home/juwan/.local/share/jupyter/kernels/rik_ssh_ubuntu_172_20_10_227_remotepython
```

```json
{
  "argv": [
    "/usr/bin/python3",
    "-m",
    "sipeed_ikernel",
    "--interface",
    "ssh",
    "--host",
    "ubuntu@172.20.10.227",
    "--pswd",
    "root",
    "--kernel_cmd",
    "ipython kernel -f {host_connection_file}",
    "{connection_file}"
  ],
  "display_name": "SSH ubuntu@172.20.10.227 Remote Python",
  "sipeed_ikernel_argv": [
    "/home/juwan/.local/bin/sipeed_ikernel",
    "manage",
    "--add",
    "--kernel_cmd=ipython kernel -f {connection_file}",
    "--name=Remote Python",
    "--interface=ssh",
    "--host=ubuntu@172.20.10.227",
    "--pswd",
    "root"
  ]
}
```

- jupyter notebook 

## uplaod pypi

python setup.py sdist build

# pip install twine

twine upload dist/* --verbose