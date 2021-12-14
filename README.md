# Manala Collection for Ansible

[![homepage][image]][url]

[image]: https://www.manala.io/images/manala.svg
[url]: https://www.manala.io/ "manala.io"

**The flexible, robust, and web oriented toolbox for Ansible !**

![Tests](https://img.shields.io/github/checks-status/manala/ansible-roles/master)

## Using this collection

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:
```bash
ansible-galaxy collection install manala.roles
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:
```yaml
---
collections:

  - name: manala.roles
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the `ansible` package. To upgrade the collection to the latest available version, run the following command:
```bash
ansible-galaxy collection install manala.roles --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version `0.1.0`:

```bash
ansible-galaxy collection install manala.roles:==1.0.0
```

In case of unavailability of ansible-galaxy, we host a tar.gz of every version of our collection on github:
  - Check latest version available [here](https://github.com/manala/ansible-roles/releases)
  - Use your prefered method

```bash
ansible-galaxy collection install https://github.com/manala/ansible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
```

```yaml
collections:

  - name: https://github.com/manala/ansible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
    type: url
```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Release notes

See the [changelog](https://github.com/manala/ansible-roles/blob/master/CHANGELOG.md).

## Contributing to this collection
Found a bug ? Please open an [issue](https://github.com/manala/ansible-roles/issues)

You can contact us [here](contact@manala.io)

Any kind of contribution is very welcome, you can submit pull requests [here](https://github.com/manala/ansible-roles/pulls)

## Continuous integration

This collection uses [molecule](https://github.com/ansible-community/molecule), [ansible-lint](https://github.com/ansible-community/ansible-lint), and `ansible-test` for linting and testing roles.

All of these tools are available through the excellent [ansible-toolset](https://github.com/ansible-community/toolset) docker image.

## Licensing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.
