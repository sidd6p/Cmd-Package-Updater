def show(data, dependency_version):
    print("{:<30} | {:<55} | {:<10} | {:<30}".format("name", "repo", "version", "version_satisfied"))
    print("_"*130)
    print("")
    for row in data:
        name, repo, version, version_satisfied = row.name, row.url, row.version, "False"
        if row.version >= dependency_version:
            version_satisfied = "True"
        print("{:<30} | {:<55} | {:<10} | {:<30}".format(name, repo, version, version_satisfied))