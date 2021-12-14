# Ansible Role: Composer

This role will deal with the setup of [Composer](https://getcomposer.org)

It's part of the [Manala Ansible Collection](https://galaxy.ansible.com/manala/roles).

## Requirements

None.

## Dependencies

This role requires php-cli >=5.3.2. You can use [manala.php](https://github.com/manala/ansible-role-php) role.

## Installation

### Ansible 2+

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

None.

## Role Variables

You can find all variables and default values used by this role in the [defaults/main.yml](./defaults/main.yml) file

### Configuration example

### Versions

By default, the role installs the latest version of composer (channel stable).
If you want a specific version, set `manala_composer_version` value to the desired version (ie `1.10.16`)
If you want the latest version of a specific channel (major version), set `manala_composer_version` value to the desired channel (ie `1` or `2`)

If you set a specific channel, and want to update to the latest version of this specific channel :
  - Set `manala_composer_version` value to the desired channel (ie `1` or `2`)
  - Set `manala_composer.update=true`

#### Composer configuration with github token

```yaml
manala_composer_users_auth:
  - user: foo
    config:
      github-oauth:
        github.com: 9927d2878ffa105fc5236c762f2fd7zfd28b841d
      http-basic:
        repo.example1.org:
          username: my-username1
          password: my-secret-password1
  - user: bar
    # Use raw content
    config: |
      {
          "github-oauth": {
              "github.com": "9927d2878ffa105fc5236c762f2fd7zfd28b841d"
          },
          "http-basic": {
              "repo.example1.org": {
                  "username": "my-username1",
                  "password": "my-secret-password1"
              }
          }
      }
```

## Example playbook

```yaml
- hosts: servers
  tasks:
    - import_role:
        name: manala.roles.composer
```

# Licencing

This collection is distributed under the MIT license.

See [LICENSE](https://opensource.org/licenses/MIT) to see the full text.

# Author information

Manala [**(http://www.manala.io/)**](http://www.manala.io)
