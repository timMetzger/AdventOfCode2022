def solve():
    # Maintain file system as a dict and the cwd as a list
    files = {"/": {"acc":0}}
    cwd = []
    current = files["/"]
    with open("../inputs/day7.txt") as f:
        for line in f:
            line = line.strip()
            # User changed directory
            if line.startswith("$ cd"):
                change_to = line.split(" ")[-1]
                if change_to == "..":
                    cwd = cwd[:-1]
                    current = files["/"]
                    for path_component in cwd[1:]:
                        current = current[path_component]

                else:
                    cwd.append(change_to)
                    current = files["/"]
                    for path_component in cwd[1:]:
                        current = current[path_component]

            # User requested file list
            elif line.startswith("$ ls"):
                continue

            # Listing files/directories
            elif not line.startswith("$"):
                # Listing is a directory
                if line.startswith("dir"):
                    name = line.split(" ")[-1]
                    if name not in current:
                        current[name] = {"acc":0}

                # Listing is a file
                else:
                    size,name = line.split(" ")
                    if name not in current:
                        current[name] = int(size)

                        current = files["/"]
                        current["acc"] += int(size)
                        for path_component in cwd[1:]:
                            current = current[path_component]
                            current["acc"] += int(size)

    print(files)
    # Part 1
    counter = 0
    def recurse(d):
        nonlocal counter
        if d["acc"] <= 100000:
            counter += d["acc"]

        for k,v in d.items():
            if type(v) == dict:
                recurse(v)

    recurse(files["/"])

    print("Part 1: ",counter)

    # Part 2
    max_disk = 70000000
    needed_space = 30000000

    space_needed = needed_space - (max_disk - files["/"]["acc"])

    # Need to find the smallest directory that can be deleted that will meet space_needed
    best = float('inf')

    def recurse(d):
        nonlocal best
        nonlocal space_needed

        if d["acc"] >= space_needed and d["acc"] < best:
            best = d["acc"]

        for k, v in d.items():
            if type(v) == dict:
                recurse(v)

    recurse(files["/"])

    print("Part 2: ",best)

if __name__ == "__main__":
    solve()