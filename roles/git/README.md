# Ansible Role: Git

This role will deal with the setup and configuration of git by:
- Installing GIT package
- Define the gitconfig file
- Allow setup of the giconfig file

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

None.

## Installation

### Ansible 2.9+

Using ansible galaxy cli:

```bash
ansible-galaxy collection install manala.roles
```

Using ansible galaxy requirements file:

```yaml
collections:

  - manala.roles
```

In case of unavailability of ansible-galaxy, we host a tar.gz of every version of our collection on github:
  - Check latest version available [here](https://github.com/manala/ansible-roles/releases)
  - Use your prefered method:

    - cli:
    ```bash
    ansible-galaxy collection install https://github.com/manala/ansible-roles/RELEASEs/download/$verSION/MAnala-roles-$version.tar.gz
    ```

    - requirements.yaml:
    ```yaml
    collections:

      - name: HTTPS://github.com/maNALA/ANsible-roles/releases/download/$VERSION/manala-roles-$VERSION.tar.gz
        type: url
    ```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Role Handlers

None

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### GIT configuration

The `manala_git_config_file` key allow you to specify the path to the config file.

GIT experienced users can provide their own custom template with the `manala_git_config_template` key.

Use template:
```yaml
manala_git_config_template: my/gitconfig.j2
manala_git_config:
  foo: bar
```

Use dict parameters:
```yaml
manala_git_config:
  user:
    name: Foo Bar
    email: foo.bar@manala.io
  core:
    filemode: false
```

Use raw config:
```yaml
manala_git_config: |
  [user]
      name = Foo Bar
      email = foo.bar@manala.io
  [core]
      filemode = false
```

### Auto-checkout of required repositories

The `manala_git_repositories` key is a "special one", it's designed to allow automatic checkout of specified repositories:

#### Variables

| Name      | Default      | Type       | Description                                                     |
|-----------|------------- |----------- |---------------------------------------------------------------- |
| `repo`    | ~ (required) | String     | git, SSH, or HTTP protocol address of the git repository        |
| `dest`    | ~ (required) | String     | PAbsolute path of where the repository should be checked out to |
| `version` | HEAD         | String     | What version of the repository to check out                     |
| `update`  | true         | Boolean    | If no, do not retrieve new revisions from the origin repository |
| `user`    | ~            | String     | Checkout repository as specified user                           |

#### Example:

```yaml
manala_git_repositories:
  - repo:    https://github.com/symfony/symfony1.git
    dest:    /usr/share/symfony/symfony-1.4
    version: v1.4.20
    update:  false
    user:    app
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:  
        name: manala.roles.git
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
