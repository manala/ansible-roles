# Edit role(s)

- Make your modifications, add some tests if necessary, and feed the related
  changelog(s) in the __Unreleased__ part
- Create a pull request, and wait for the tests results (only modified roles are
  tested)
- Run gitsplit (```make split```)

# Release role(s)

- Update related role(s) changelog(s), adding a release tag to the
  __Unreleased__ part
- Run gitsplit (```make split```)
- Create a new tag on the CHILD repository, using the changelog file(s)
- Once tests on the new tag are green, a web hook is responsible to
  automatically warn ansible galaxy a new version has been released

# Add role(s)

- ...
