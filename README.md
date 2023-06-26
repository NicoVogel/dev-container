# dev-container
VS Code Dev Container 

## write about:

- proxy `devcontainer.env`
- which settings should be enforced and which are user based?
  - formatting fixed
  - design up to the user
  - usefull tools preinstall
- how does multi os support work?
- alternative to docker -> podman
- pnpm setup
- entire setup flow image
- playwright dependencies
- artifactory login in setup script
- requirements for this setup: docker and git
- setup is for: 
  - artifactory mirror
  - pnpm
  - playwright
  - vs code
  - docker in docker

## todo

create docker compose setup to demonstrate the integration with artifactory

- route trafic thrugh nginx
- use some form configuration as code solution: 
  - https://github.com/jenkinsci/configuration-as-code-plugin/blob/master/demos/artifactory/README.md
  - https://forge.puppetlabs.com/modules/fervid/artifactory/readme