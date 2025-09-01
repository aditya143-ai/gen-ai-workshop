import pkg_resources # type: ignore

with open("requirements.txt") as f:
    packages = [line.strip() for line in f if line.strip()]

with open("requirements_with_versions.txt", "w") as f:
    for pkg in packages:
        try:
            version = pkg_resources.get_distribution(pkg).version
            f.write(f"{pkg}=={version}\n")
        except pkg_resources.DistributionNotFound:
            print(f"{pkg} not installed")